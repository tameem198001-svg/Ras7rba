"""03_build_db.py
Placeholder to build SQLite FTS5 DB from source texts.
"""

import sqlite3
import os

DB_PATH = "data/algo_faqih.db"

def build_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE VIRTUAL TABLE IF NOT EXISTS texts USING fts5(title, body)''')
    conn.commit()
    conn.close()
    print("DB built at", DB_PATH)

if __name__ == "__main__":
    build_db()
