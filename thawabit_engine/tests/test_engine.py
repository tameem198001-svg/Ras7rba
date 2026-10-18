import sqlite3
import pytest
from thawabit_engine.engine import ThawabitEngine

SCHEMA = open('thawabit_engine/schema.sql').read()

def test_miracle_cannot_be_real(tmp_path):
    db = tmp_path / 'db.sqlite'
    conn = sqlite3.connect(str(db))
    engine = ThawabitEngine(conn)
    engine.apply_schema(SCHEMA)
    conn.execute("INSERT INTO claims(id, domain, text) VALUES (1, 'MIRACLE', 'x')")
    with pytest.raises(sqlite3.DatabaseError) as exc:
        conn.execute("INSERT INTO verification_status(claim_id, status) VALUES (1, 'REAL')")
    assert 'EPISTEMOLOGICAL VIOLATION' in str(exc.value)

def test_physics_cannot_be_miracle(tmp_path):
    db = tmp_path / 'db.sqlite'
    conn = sqlite3.connect(str(db))
    engine = ThawabitEngine(conn)
    engine.apply_schema(SCHEMA)
    conn.execute("INSERT INTO claims(id, domain, text) VALUES (2, 'PHYSICS', 'y')")
    with pytest.raises(sqlite3.DatabaseError) as exc:
        conn.execute("INSERT INTO verification_status(claim_id, status) VALUES (2, 'MIRACLE')")
    assert 'EPISTEMOLOGICAL VIOLATION' in str(exc.value)

def test_engine_policy_prevents_real_without_reviewer(tmp_path):
    db = tmp_path / 'db.sqlite'
    conn = sqlite3.connect(str(db))
    engine = ThawabitEngine(conn)
    engine.apply_schema(SCHEMA)
    conn.execute("INSERT INTO claims(id, domain, text) VALUES (3, 'PHYSICS', 'z')")
    with pytest.raises(sqlite3.DatabaseError) as exc:
        conn.execute("INSERT INTO verification_status(claim_id, status) VALUES (3, 'REAL')")
    assert 'VALIDATION ERROR' in str(exc.value)
