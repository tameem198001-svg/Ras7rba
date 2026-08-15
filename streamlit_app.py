"""
streamlit_app.py
Multi-page Streamlit app for V11.0 (simplified).
"""
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

from mother_core import MotherCore
from create_ledger import export_ledger

st.set_page_config(layout="wide", page_title="نُورُ الْخُوَارِزْمِيَّةِ V11.0")
st.title("🧠 الْخُوَارِزْمِيَّةُ الأُمُّ – نُسْخَةُ الْكُلِّ الْمُتَّحِدِ V11.0")

mc = MotherCore()

PAGES = ["Full Run", "Single Simulation", "Noor Wall Ledger"]
page = st.sidebar.selectbox("Choose page", PAGES)

if page == "Full Run":
    st.header("تشغيل جميع المحاكيات (تجريبي")
    if st.button("Run all simulations"):
        with st.spinner("Running simulations..."):
            out = mc.run_all()
        st.success("Done")
        cols = st.columns(3)
        i = 0
        for name, res in out.items():
            with cols[i % 3]:
                st.subheader(f"{res['name']}")
                if res['name'] == 'Schrodinger Well':
                    psi = res['psi']
                    prob = np.abs(psi[-1])**2
                    st.line_chart(prob)
                elif res['name'] == 'Lotka-Volterra':
                    df = pd.DataFrame({"prey": res['prey'], "pred": res['pred']})
                    st.line_chart(df)
                else:
                    # fallback: show checksum and metadata
                    st.write(f"checksum: {res.get('checksum')}")
            i += 1

elif page == "Single Simulation":
    st.header("تشغيل محاكاة واحدة")
    sim = st.selectbox("اختر المحاكاة", ["Klein-Gordon", "Schrodinger Well", "Lotka-Volterra", "Forced Damped Oscillator", "Burgers Shock"])
    if st.button("Run"):
        with st.spinner(f"Running {sim}..."):
            if sim == 'Klein-Gordon':
                r = mc.solve_klein_gordon(nx=120, nt=200)
                st.line_chart(np.abs(r['phi'][-1]))
            elif sim == 'Schrodinger Well':
                r = mc.solve_schrodinger_well(nx=160, nt=300)
                st.line_chart(np.abs(r['psi'][-1])**2)
            elif sim == 'Lotka-Volterra':
                r = mc.solve_lotka_volterra(steps=1000)
                st.line_chart(pd.DataFrame({"prey": r['prey'], "pred": r['pred']}))
            elif sim == 'Forced Damped Oscillator':
                r = mc.solve_forced_damped_oscillator(steps=2000)
                st.line_chart(r['x'])
            else:
                r = mc.solve_burgers_shock(nx=128, nt=150)
                st.line_chart(r['u'][-1])
        st.write("checksum:", r.get('checksum'))

else:
    st.header("جدار النور — السجل")
    if st.button("Export ledger to JSON"):
        out = export_ledger()
        st.success(f"Exported to {out}")
    st.write("آخر 50 سجلًا:")
    try:
        df = pd.read_sql_query('SELECT * FROM ledger ORDER BY id DESC LIMIT 50', mc.__dict__['ledger_path'] if False else 'noor_wall_ledger.db', con=None)
    except Exception:
        # fallback: attempt using sqlite3 directly
        import sqlite3
        conn = sqlite3.connect('noor_wall_ledger.db')
        df = pd.read_sql_query('SELECT id, created_at, simulation_name, result_checksum, pulse_applied FROM ledger ORDER BY id DESC LIMIT 50', conn)
        conn.close()
    st.dataframe(df)
