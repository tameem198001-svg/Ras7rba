import os
import sqlite3
import subprocess


def test_build_db():
    # Ensure scripts build DB successfully
    subprocess.check_call(["python3", "algo-faqih/scripts/04_build_db.py"])
    assert os.path.exists("algo-faqih/data/algo_faqih.db")
    conn = sqlite3.connect("algo-faqih/data/algo_faqih.db")
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM texts")
    count = cur.fetchone()[0]
    conn.close()
    assert count >= 1
