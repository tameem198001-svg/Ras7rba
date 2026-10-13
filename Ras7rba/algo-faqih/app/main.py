import streamlit as st
import sqlite3
from pathlib import Path

st.set_page_config(page_title="algo-faqih", layout="centered")

st.title("algo-faqih — محرك بحث شرعي (تجريبي)")
st.write("التزام: هذه أداة بحثية فقط — ليست للفتوى. راجع CHARTER.md للضوابط.")

DB = Path("data/algo_faqih.db")

if not DB.exists():
    st.warning("قاعدة البيانات غير موجودة. شغّل scripts/03_build_db.py لتجهيزها.")
else:
    q = st.text_input("بحث")
    if q:
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute("SELECT rowid, title, body FROM texts WHERE texts MATCH ? LIMIT 20", (q,))
        rows = cur.fetchall()
        if not rows:
            st.info("لا نتائج.")
        else:
            for rid, title, body in rows:
                st.subheader(title or "(بدون عنوان)")
                st.write(body[:1000])
        conn.close()
