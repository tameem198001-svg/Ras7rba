import json
import re
import sqlite3
from pathlib import Path
from typing import Optional

DEFAULT_DB = "algo-faqih/data/faqih_search.db"


def normalize_arabic(text: str) -> str:
    """Normalization for Arabic text without losing original source text."""
    if not text:
        return ""
    tashkeel = re.compile(r"[\u0610-\u061A\u064B-\u065F\u06D6-\u06ED]")
    t = tashkeel.sub("", text)
    t = re.sub(r"[\u0622\u0623\u0625]", "\u0627", t)
    t = re.sub(r"\u0649", "\u064A", t)
    t = re.sub(r"\u0629", "\u0647", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


class Database:
    def __init__(self, path: Optional[str] = None):
        self.path = path or DEFAULT_DB
        Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.path)
        self.conn.execute("PRAGMA journal_mode=WAL;")
        self._ensure_schema()

    def _ensure_schema(self):
        cur = self.conn.cursor()

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS sources (
                source_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                reliability_score REAL DEFAULT 1.0,
                metadata TEXT
            )
            """
        )

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS texts (
                text_id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_id INTEGER NOT NULL,
                reference_key TEXT NOT NULL,
                full_text TEXT NOT NULL,
                normalized_text TEXT,
                tags TEXT,
                provenance_note TEXT NOT NULL,
                FOREIGN KEY (source_id) REFERENCES sources(source_id)
            )
            """
        )

        cur.execute(
            """
            CREATE VIRTUAL TABLE IF NOT EXISTS texts_fts USING fts5(
                full_text,
                normalized_text,
                reference_key,
                content='texts',
                content_rowid='text_id'
            )
            """
        )

        cur.execute(
            """
            CREATE TRIGGER IF NOT EXISTS texts_ai AFTER INSERT ON texts BEGIN
                INSERT INTO texts_fts(rowid, full_text, normalized_text, reference_key)
                VALUES (new.text_id, new.full_text, new.normalized_text, new.reference_key);
            END;
            """
        )

        cur.execute(
            """
            CREATE TRIGGER IF NOT EXISTS texts_ad AFTER DELETE ON texts BEGIN
                INSERT INTO texts_fts(texts_fts, rowid, full_text, normalized_text, reference_key)
                VALUES('delete', old.text_id, old.full_text, old.normalized_text, old.reference_key);
            END;
            """
        )

        cur.execute(
            """
            CREATE TRIGGER IF NOT EXISTS texts_au AFTER UPDATE ON texts BEGIN
                INSERT INTO texts_fts(texts_fts, rowid, full_text, normalized_text, reference_key)
                VALUES('delete', old.text_id, old.full_text, old.normalized_text, old.reference_key);
                INSERT INTO texts_fts(rowid, full_text, normalized_text, reference_key)
                VALUES (new.text_id, new.full_text, new.normalized_text, new.reference_key);
            END;
            """
        )

        self.conn.commit()

    def add_source(self, name: str, category: str, reliability_score: float = 1.0, metadata: Optional[dict] = None) -> int:
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO sources(name, category, reliability_score, metadata) VALUES (?, ?, ?, ?)",
            (name, category, reliability_score, json.dumps(metadata or {}, ensure_ascii=False)),
        )
        self.conn.commit()
        return cur.lastrowid

    def get_source_by_name(self, name: str):
        cur = self.conn.cursor()
        cur.execute(
            "SELECT source_id, name, category, reliability_score, metadata FROM sources WHERE name = ?",
            (name,),
        )
        return cur.fetchone()

    def add_text(self, source_id: int, reference_key: str, full_text: str, normalized_text: Optional[str], tags: Optional[str], provenance_note: str) -> int:
        assert source_id is not None, "source_id is required"
        assert provenance_note is not None and provenance_note.strip(), "provenance_note is required"
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO texts(source_id, reference_key, full_text, normalized_text, tags, provenance_note) VALUES (?, ?, ?, ?, ?, ?)",
            (source_id, reference_key, full_text, normalized_text, tags, provenance_note),
        )
        self.conn.commit()
        return cur.lastrowid

    def search(self, q: str, limit: int = 20):
        cur = self.conn.cursor()
        cur.execute(
            "SELECT t.text_id, t.reference_key, t.full_text, t.provenance_note, s.name FROM texts t "
            "JOIN sources s ON t.source_id = s.source_id "
            "JOIN texts_fts fts ON fts.rowid = t.text_id "
            "WHERE texts_fts MATCH ? LIMIT ?",
            (q, limit),
        )
        return cur.fetchall()

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    db = Database(DEFAULT_DB)
    source = db.get_source_by_name('القرآن الكريم')
    if not source:
        sid = db.add_source('القرآن الكريم', 'quran', 1.0, {'lang': 'ar'})
    else:
        sid = source[0]

    sample_text = 'الله لا إله إلا هو الحي القيوم'
    db.add_text(
        sid,
        '2:255',
        sample_text,
        normalize_arabic(sample_text),
        'aya',
        json.dumps({'source': 'quran', 'ref': '2:255'}, ensure_ascii=False),
    )
    print('Database initialized and sample row inserted.')
    db.close()
