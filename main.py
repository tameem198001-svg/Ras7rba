#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Shamsi v4.0 + Astrolabe v2 - يا حق 55055
import os, time, logging, threading, queue, hmac, hashlib
import numpy as np
from datetime import datetime
from prometheus_client import Gauge, Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse, JSONResponse
try:
 from kubernetes import client, config
 try: config.load_incluster_config()
 except: config.load_kube_config()
 k8s_apps = client.AppsV1Api()
except Exception as e:
 k8s_apps = None

TARGET_DEPLOYMENT=os.getenv("TARGET_DEPLOYMENT","my-app")
TARGET_NAMESPACE=os.getenv("TARGET_NAMESPACE","production")
MIN_REPLICAS=int(os.getenv("MIN_REPLICAS",1))
MAX_REPLICAS=int(os.getenv("MAX_REPLICAS",20))
KP_BASE=float(os.getenv("KP_BASE",5.0)); KI=float(os.getenv("KI",0.5))
MAX_STEP=int(os.getenv("MAX_STEP",2)); INTERVAL=float(os.getenv("INTERVAL",2))
DEADBAND=float(os.getenv("DEADBAND",0.02))
INGEST_SECRET=os.getenv("INGEST_SECRET",")
COST_PER_REPLICA=float(os.getenv("COST_PER_REPLICA",0.05))

g_desired=Gauge("shamsi_desired_replicas","Desired"); g_signal=Gauge("shamsi_signal","Signal")
g_m=Gauge("shamsi_m","m"); g_v=Gauge("shamsi_volatility","vol")
g_error=Gauge("shamsi_control_error","error")
g_consciousness=Gauge("shamsi_consciousness_state","0=observer,1=balanced,2=leader")
g_threat=Gauge("shamsi_astrolabe_threat","threat")
g_zakat=Gauge("shamsi_ethical_zakat_usd","zakat/hour")
g_season=Gauge("shamsi_season_code","season")

state={"m":0.5,"v":0.0,"current_replicas":5,"error_i":0.0}
ingest_q=queue.Queue(maxsize=100); history=[]

class CompleteAstrolabe:
 def get_season(self):
 m=datetime.now().month
 return {1:"winter",2:"winter",3:"spring",4:"spring",5:"spring",6:"summer",7:"summer",8:"summer",9:"autumn",10:"autumn",11:"autumn",12:"winter"}[m]
 def scan_threat(self,h):
 if len(h)<10: return 0.0,"peace"
 vol=float(np.std(h[-20:])); threat=float(np.clip(vol*3,0,1))
 mode="war" if threat>0.7 else "alert" if threat>0.35 else "peace"
 return threat,mode

astrolabe=CompleteAstrolabe()

def compute(demand,m_prev,v_prev):
 v=0.9*v_prev+0.1*abs(demand-state["m"]); kp=KP_BASE*(1+v)
 m_pred=state["m"]+0.8*(state["m"]-m_prev); m_eff=0.7*state["m"]+0.3*m_pred
 if abs(m_eff-0.35)<DEADBAND: return 0.5,m_eff,0,v,kp
 err=m_eff-0.35
 if MIN_REPLICAS<state["current_replicas"]<MAX_REPLICAS: state["error_i"]+=err*0.1
 else: state["error_i"]*=0.9
 delta=int(np.clip(kp*err+KI*state["error_i"],-MAX_STEP,MAX_STEP))
 return 0.5+delta/10.0,m_eff,delta,v,kp

def apply_k8s(desired):
 if not k8s_apps: return False
 try:
 k8s_apps.patch_namespaced_deployment_scale(TARGET_DEPLOYMENT,TARGET_NAMESPACE,body={"spec":{"replicas":desired}})
 return True
 except Exception as e: logging.error(e); return False

def loop():
 while True:
 try: demand=ingest_q.get_nowait()
 except: demand=state["m"]
 m_prev=state["m"]; lam=np.clip(0.2+0.8*state["v"],0.05,0.9)
 state["m"]=float(np.clip((1-lam)*state["m"]+lam*demand+np.random.normal(0,0.01),0,1))
 history.append(state["m"]); threat,mode=astrolabe.scan_threat(history)
 signal,m_eff,delta_r,v_val,kp=compute(demand,m_prev,state["v"]); state["v"]=v_val
 g_m.set(state["m"]); g_v.set(v_val); g_error.set(abs(m_eff-0.35)); g_threat.set(threat)
 g_consciousness.set(0 if m_eff<0.3 else 2 if m_eff>0.7 else 1)
 g_season.set({"winter":0,"spring":1,"summer":2,"autumn":3}[astrolabe.get_season()])
 prev=state["current_replicas"]; new=int(np.clip(prev-delta_r,MIN_REPLICAS,MAX_REPLICAS))
 if mode=="war": new=max(MIN_REPLICAS,prev-1)
 state["current_replicas"]=new; g_desired.set(new); g_signal.set(signal)
 saved=MAX_REPLICAS-new; g_zakat.set(saved*COST_PER_REPLICA*55/115)
 if new!=prev: apply_k8s(new)
 time.sleep(INTERVAL)

app=FastAPI(title="Shamsi Sovereignty v4.0",version="4.0")
@app.get("/metrics")
async def metrics(): return PlainTextResponse(generate_latest(),media_type=CONTENT_TYPE_LATEST)
@app.post("/ingest")
async def ingest(req: Request):
 p=await req.json(); d=float(p.get("demand",0.5))
 ts=int(p.get("timestamp",int(time.time()))); proof=p.get("proof","")
 if INGEST_SECRET:
 exp=hmac.new(INGEST_SECRET.encode(),f"{d:.5f}|{ts}".encode(),hashlib.sha256).hexdigest()
 if not hmac.compare_digest(proof,exp): return JSONResponse(status_code=403,content={"error":"invalid proof"})
 try: ingest_q.put_nowait(d)
 except: return JSONResponse(status_code=429,content={"error":"queue full"})
 return {"status":"accepted","season":astrolabe.get_season(),"threat":float(g_threat._value.get())}
@app.get("/status")
async def status(): return {**state,"season":astrolabe.get_season(),"threat":float(g_threat._value.get()),"zakat":float(g_zakat._value.get())}
@app.on_event("startup")
def start(): threading.Thread(target=loop,daemon=True).start()
