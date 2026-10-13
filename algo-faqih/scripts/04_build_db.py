"""04_build_db.py
Build a minimal SQLite FTS5 database for text search.
"""

import os
import sqlite3

DB_PATH = "data/algo_faqih.db"


def build_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("CREATE VIRTUAL TABLE IF NOT EXISTS texts USING fts5(title, body, source, source_ref, tags)")
    cursor.execute(
        "INSERT INTO texts(title, body, source, source_ref, tags) VALUES (?, ?, ?, ?, ?)",
        ("placeholder_quran", "نص تجريبي للقرآن - placeholder", "quran", "quran:placeholder", "quran,placeholder"),
    )
    cursor.execute(
        "INSERT INTO texts(title, body, source, source_ref, tags) VALUES (?, ?, ?, ?, ?)",
        ("placeholder_hadith", "نص تجريبي للحديث - placeholder", "hadith", "hadith:placeholder", "hadith,placeholder"),
    )
    conn.commit()
    conn.close()
    print(f"Built FTS database at: {DB_PATH}")


if __name__ == "__main__":
    build_db()
