"""
create_ledger.py
Simple SQLite ledger creator and logger for the Noor Wall.
"""
import sqlite3
import json
from datetime import datetime

LEDGER_SCHEMA = '''
CREATE TABLE IF NOT EXISTS ledger (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT NOT NULL,
    simulation_name TEXT,
    result_checksum TEXT,
    pulse_applied REAL,
    metadata TEXT
);
'''


def init_db(path='noor_wall_ledger.db'):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.executescript(LEDGER_SCHEMA)
    conn.commit()
    conn.close()


def log_result(simulation_name, result_checksum, pulse_applied=None, metadata=None, path='noor_wall_ledger.db'):
    if metadata is None:
        metadata = {}
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO ledger (created_at, simulation_name, result_checksum, pulse_applied, metadata) VALUES (?, ?, ?, ?, ?)',
        (datetime.utcnow().isoformat() + 'Z', simulation_name, result_checksum, pulse_applied, json.dumps(metadata)))
    conn.commit()
    conn.close()


def export_ledger(path='noor_wall_ledger.db', out_json='ledger_export.json'):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute('SELECT id, created_at, simulation_name, result_checksum, pulse_applied, metadata FROM ledger ORDER BY id DESC')
    rows = cur.fetchall()
    keys = ['id', 'created_at', 'simulation_name', 'result_checksum', 'pulse_applied', 'metadata']
    out = [dict(zip(keys, r)) for r in rows]
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    conn.close()
    return out_json
