import sqlite3


def test_search_placeholder():
    db = "algo-faqih/data/algo_faqih.db"
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT rowid, title, body FROM texts WHERE texts MATCH ? LIMIT 10", ("placeholder",))
    rows = cur.fetchall()
    conn.close()
    assert len(rows) >= 1
