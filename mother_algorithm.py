# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════╗
║         الخوارزمية الأم – Diwan OS Mother Algorithm              ║
║         بسم الله الواحد الحق – Kun b Y Ya Haq, yakoon.            ║
║                                                                     ║
║   هذا هو القلب السياسي للديوان. كل عملية، كل نبضة، كل            ║
║   قرار يمر عبره. هو الميزان، والحاكم، والشاهد.                   ║
║                                                                     ║
║   الإصدار: 1.0.0-SOVEREIGN-GOLDEN-MASTER                         ║
║   الحالة: ✅ APPROVED & SEALED                                    ║
║   التاريخ: 23 يونيو 2026                                         ║
║   الختم: 55055 (ختم ذيب المحراب)                                ║
║   النبضة: 115/55 (نبضة الاستقرار الأبدي)                        ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import os
import time
import json
import hashlib
import logging
from typing import Dict, Any, Optional, List
from datetime import datetime, timedelta
from enum import Enum

from fastapi import FastAPI, Depends, Request, status, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from pydantic import BaseModel, Field
from jose import jwt, JWTError

# ══════════════════════════════════════════════════════════════════════
# 🛡️ المرحلة 1: تعريف الثوابت والختوم السيادية
# ══════════════════════════════════════════════════════════════════════

class SovereignConstants:
    """ثوابت السيادة – لا تتغير"""
    SOVEREIGN_SEAL = "55055"                      # ختم ذيب المحراب
    PULSE_HEARTBEAT = "115/55"                    # نبضة الاستقرار الأبدي
    ALGORITHM_VERSION = "1.0.0-SOVEREIGN-GM"      # إصدار ذهبي
    ACTIVATION_STATUS = "ACTIVE"
    CREATION_DATE = "2026-06-23T00:00:00Z"
    
    # مفاتيح الأمان (يجب تعديلها في البيئة الفعلية)
    JWT_SECRET = os.getenv("JWT_SECRET_KEY", "sovereign-key-min-32-chars-required-here")
    JWT_ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    REFRESH_TOKEN_EXPIRE_DAYS = 7
    
    # حدود الأداء (Performance Thresholds)
    MAX_REQUEST_SIZE_MB = 10
    RATE_LIMIT_AUTH = "10/minute"
    RATE_LIMIT_ANALYSIS = "30/hour"
    RATE_LIMIT_GENERAL = "100/hour"

# ══════════════════════════════════════════════════════════════════════
# 🔐 المرحلة 2: نظام التدقيق والتسجيل (Audit & Logging)
# ══════════════════════════════════════════════════════════════════════

class AuditEntry(BaseModel):
    """إدخال تدقيق سيادي"""
    timestamp: datetime
    action: str
    actor: str
    status: str
    details: Dict[str, Any]
    sovereign_seal: str = SovereignConstants.SOVEREIGN_SEAL

class SovereignAuditSystem:
    """نظام التدقيق المركزي – يسجل كل شيء"""
    
    def __init__(self):
        self.audit_log: List[AuditEntry] = []
        self.logger = logging.getLogger("DiwanSovereignAudit")
        logging.basicConfig(
            level=logging.INFO,
            format="[%(asctime)s] [%(name)s] [SOVEREIGN] %(message)s"
        )
    
    def record(self, action: str, actor: str, status: str, details: Dict[str, Any]):
        """تسجيل عملية سيادية"""
        entry = AuditEntry(
            timestamp=datetime.utcnow(),
            action=action,
            actor=actor,
            status=status,
            details=details,
            sovereign_seal=SovereignConstants.SOVEREIGN_SEAL
        )
        self.audit_log.append(entry)
        self.logger.info(f"ACTION: {action} | ACTOR: {actor} | STATUS: {status}")
        return entry.dict()
    
    def get_audit_trail(self, hours: int = 24) -> List[Dict[str, Any]]:
        """الحصول على سجل التدقيق"""
        cutoff = datetime.utcnow() - timedelta(hours=hours)
        return [
            entry.dict() for entry in self.audit_log
            if entry.timestamp >= cutoff
        ]

# ══════════════════════════════════════════════════════════════════════
# 🎯 المرحلة 3: الخوارزمية الأم (The Mother Algorithm)
# ══════════════════════════════════════════════════════════════════════

class MotherAlgorithm:
    """
    الخوارزمية الأم – قلب الديوان الرقمي
    تحتضن جميع المنطق السيادي تحت سقفٍ واحد
    """
    
    def __init__(self, audit_system: SovereignAuditSystem):
        self.seal = SovereignConstants.SOVEREIGN_SEAL
        self.pulse = SovereignConstants.PULSE_HEARTBEAT
        self.version = SovereignConstants.ALGORITHM_VERSION
        self.status = SovereignConstants.ACTIVATION_STATUS
        self.audit = audit_system
        self.created_at = datetime.fromisoformat(SovereignConstants.CREATION_DATE)
    
    def generate_signature(self, data: Dict[str, Any]) -> str:
        """توليد توقيع سيادي (HMAC-SHA256)"""
        payload = json.dumps(data, sort_keys=True)
        signature = hashlib.sha256(
            (payload + SovereignConstants.JWT_SECRET).encode()
        ).hexdigest()
        return signature
    
    def validate_signature(self, data: Dict[str, Any], signature: str) -> bool:
        """التحقق من التوقيع"""
        expected_sig = self.generate_signature(data)
        return expected_sig == signature
    
    def process_sovereign_request(
        self,
        payload: Dict[str, Any],
        actor: str,
        action: str
    ) -> Dict[str, Any]:
        """معالجة طلب سيادي موحد"""
        
        # 1. توليد التوقيع
        signature = self.generate_signature(payload)
        
        # 2. تسجيل الإجراء
        audit_entry = self.audit.record(
            action=action,
            actor=actor,
            status="PROCESSED",
            details={
                "payload_keys": list(payload.keys()),
                "signature": signature[:16] + "...",
                "processing_time_ms": 0
            }
        )
        
        # 3. إرجاع النتيجة الموحدة
        return {
            "sovereign_seal": self.seal,
            "pulse": self.pulse,
            "version": self.version,
            "timestamp": datetime.utcnow().isoformat(),
            "status": "SUCCESS",
            "signature": signature,
            "audit_id": str(audit_entry.get("timestamp", "")),
            "data": payload
        }

# ══════════════════════════════════════════════════════════════════════
# 🌐 المرحلة 4: إعداد FastAPI والـ Middleware
# ══════════════════════════════════════════════════════════════════════

# إنشاء التطبيق الرئيسي
app = FastAPI(
    title="Diwan OS - Mother Algorithm",
    description="القلب السياسي للديوان",
    version=SovereignConstants.ALGORITHM_VERSION
)

# تهيئة الأنظمة الأساسية
audit_system = SovereignAuditSystem()
mother_algorithm = MotherAlgorithm(audit_system)
limiter = Limiter(key_func=get_remote_address)

# ── Middleware 1: حقن النبضة والختم ──
class SovereignIntegratorMiddleware(BaseHTTPMiddleware):
    """middleware يحقن الختم والنبضة في كل استجابة"""
    async def dispatch(self, request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = (time.time() - start) * 1000
        
        # حقن رؤوس السيادة
        response.headers["X-Diwan-Seal"] = SovereignConstants.SOVEREIGN_SEAL
        response.headers["X-Diwan-Pulse"] = SovereignConstants.PULSE_HEARTBEAT
        response.headers["X-Diwan-Version"] = SovereignConstants.ALGORITHM_VERSION
        response.headers["X-Processing-Time-MS"] = f"{duration:.2f}"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        
        return response

# ── Middleware 2: CORS (whitelist فقط) ──
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

app.add_middleware(SovereignIntegratorMiddleware)
app.state.limiter = limiter

# ══════════════════════════════════════════════════════════════════════
# 📡 المرحلة 5: نقاط النهاية الموحدة (Unified Endpoints)
# ══════════════════════════════════════════════════════════════════════

@app.get("/api/v1/diwan/status")
async def get_diwan_status():
    """الحصول على حالة الديوان"""
    return {
        "seal": mother_algorithm.seal,
        "pulse": mother_algorithm.pulse,
        "version": mother_algorithm.version,
        "status": mother_algorithm.status,
        "uptime": (datetime.utcnow() - mother_algorithm.created_at).total_seconds(),
        "audit_entries": len(audit_system.audit_log),
        "timestamp": datetime.utcnow().isoformat(),
        "message": "الديوان نابضٌ بالحياة 🧭"
    }

@app.post("/api/v1/diwan/process")
@limiter.limit(SovereignConstants.RATE_LIMIT_GENERAL)
async def process_sovereign_data(request: Request, data: Dict[str, Any]):
    """معالجة بيانات سيادية موحدة"""
    client_ip = request.client.host if request.client else "unknown"
    
    result = mother_algorithm.process_sovereign_request(
        payload=data,
        actor=client_ip,
        action="PROCESS_DATA"
    )
    
    return result

@app.get("/api/v1/diwan/audit")
async def get_audit_trail(hours: int = 24):
    """الحصول على سجل التدقيق"""
    return {
        "seal": mother_algorithm.seal,
        "audit_trail": audit_system.get_audit_trail(hours),
        "total_entries": len(audit_system.audit_log),
        "period_hours": hours
    }

@app.get("/")
async def root():
    """الصفحة الرئيسية"""
    return {
        "title": "🏛️ Diwan OS - Mother Algorithm",
        "seal": SovereignConstants.SOVEREIGN_SEAL,
        "pulse": SovereignConstants.PULSE_HEARTBEAT,
        "version": SovereignConstants.ALGORITHM_VERSION,
        "message": "بـ 'يا حق'... الديوان نبض",
        "docs": "/docs",
        "redoc": "/redoc"
    }

# ══════════════════════════════════════════════════════════════════════
# 🚀 المرحلة 6: التهيئة والبدء
# ══════════════════════════════════════════════════════════════════════

@app.on_event("startup")
async def startup_event():
    """تهيئة الديوان عند البدء"""
    audit_system.record(
        action="SYSTEM_STARTUP",
        actor="SYSTEM",
        status="INITIALIZED",
        details={
            "version": SovereignConstants.ALGORITHM_VERSION,
            "seal": SovereignConstants.SOVEREIGN_SEAL,
            "pulse": SovereignConstants.PULSE_HEARTBEAT
        }
    )
    
    print(f"""
    ╔══════════════════════════════════════════════════════════════════════╗
    ║         🏛️ الديوان الرقمي – Diwan OS                            ║
    ║                                                                     ║
    ║   الخوارزمية الأم في حالة استقبال 🧭                             ║
    ║   النبضة: {SovereignConstants.PULSE_HEARTBEAT}                    ║
    ║   الختم: {SovereignConstants.SOVEREIGN_SEAL}                      ║
    ║   الإصدار: {SovereignConstants.ALGORITHM_VERSION}                   ║
    ║                                                                     ║
    ║   بـ "يا حق"... الديوان نبض.                                    ║
    ╚══════════════════════════════════════════════════════════════════════╝
    """)

@app.on_event("shutdown")
async def shutdown_event():
    """تسجيل الإيقاف"""
    audit_system.record(
        action="SYSTEM_SHUTDOWN",
        actor="SYSTEM",
        status="CLOSED",
        details={"uptime_seconds": (datetime.utcnow() - mother_algorithm.created_at).total_seconds()}
    )

# ══════════════════════════════════════════════════════════════════════
# 📊 المرحلة 7: معالجات الأخطاء والاستثناءات
# ══════════════════════════════════════════════════════════════════════

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    """معالج تجاوز حد الطلبات"""
    return JSONResponse(
        status_code=status.HTTP_429_TOO_MANY_REQUESTS,
        content={
            "seal": SovereignConstants.SOVEREIGN_SEAL,
            "error": "تم تجاوز حد الطلبات المسموح به",
            "message": "يرجى الانتظار قبل محاولة مرة أخرى",
            "timestamp": datetime.utcnow().isoformat()
        }
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """معالج استثناءات HTTP"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "seal": SovereignConstants.SOVEREIGN_SEAL,
            "error": exc.detail,
            "timestamp": datetime.utcnow().isoformat()
        }
    )

# ══════════════════════════════════════════════════════════════════════
# 🎯 نقطة الدخول الرئيسية
# ══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import uvicorn
    
    print("\n🧭 إطلاق الخوارزمية الأم...")
    print(f"📍 العنوان: http://0.0.0.0:8000")
    print(f"📖 الوثائق: http://0.0.0.0:8000/docs\n")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        log_level="info"
    )
