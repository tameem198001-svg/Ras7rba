import streamlit as st
import sqlite3
from pathlib import Path
import json

st.set_page_config(page_title="algo-faqih", layout="centered")

st.title("algo-faqih — محرك بحث نصّي شرعي (تجريبي)")
st.warning("تحذير: هذه أداة بحثية فقط — ليست للفتوى. راجع CHARTER.md للضوابط.")

DB = Path("algo-faqih/data/faqih_search.db")

def get_sources(conn):
    cur = conn.cursor()
    cur.execute("SELECT source_id, name, category FROM sources")
    return cur.fetchall()

if not DB.exists():
    st.error("قاعدة البيانات غير موجودة. شغّل: python3 algo-faqih/src/etl_quran.py و python3 algo-faqih/src/etl_hadith.py أو سكربت البناء.")
else:
    conn = sqlite3.connect(DB)
    sources = get_sources(conn)
    source_options = ["ALL"] + [f"{s[0]}|{s[1]}" for s in sources]
    selected = st.selectbox("اختر المصدر (أو ALL)", source_options)

    query = st.text_input("بحث")
    limit = st.number_input("عدد النتائج", min_value=1, max_value=100, value=20)

    if st.button("بحث"):
        q = query.strip()
        if not q:
            st.info("أدخل نص البحث.")
        else:
            cur = conn.cursor()
            if selected == "ALL":
                cur.execute(
                    "SELECT t.text_id, t.reference_key, t.full_text, t.provenance_note, s.name FROM texts t JOIN sources s ON t.source_id=s.source_id JOIN texts_fts fts ON fts.rowid=t.text_id WHERE texts_fts MATCH ? LIMIT ?",
                    (q, limit),
                )
            else:
                sid = int(selected.split('|',1)[0])
                cur.execute(
                    "SELECT t.text_id, t.reference_key, t.full_text, t.provenance_note, s.name FROM texts t JOIN sources s ON t.source_id=s.source_id JOIN texts_fts fts ON fts.rowid=t.text_id WHERE texts_fts MATCH ? AND t.source_id = ? LIMIT ?",
                    (q, sid, limit),
                )
            rows = cur.fetchall()
            if not rows:
                st.info("لا نتائج.")
            else:
                for text_id, ref, full_text, provenance_note, source_name in rows:
                    st.subheader(f"{source_name} — {ref}")
                    st.write(full_text)
                    try:
                        prov = json.loads(provenance_note)
                        st.markdown(f"**Provenance:** `{prov}`")
                    except Exception:
                        st.markdown(f"**Provenance:** {provenance_note}")
                    st.write('---')
    conn.close()
