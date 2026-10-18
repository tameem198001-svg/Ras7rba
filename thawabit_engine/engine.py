"""thawabit_engine/engine.py

Minimal engine scaffold: VALID_STATUSES, DomainPolicy, ThawabitEngine.
"""
import sqlite3
from typing import Optional, List

VALID_STATUSES = ['PENDING', 'REAL', 'FAKE', 'MIRACLE', 'UNKNOWN']

class DomainPolicy:
    """Policy checks per domain. Extendable per-domain evaluators live under evaluators/.
    """
    @staticmethod
    def validate_transition(domain: str, new_status: str, reviewer: Optional[str]=None, reason: Optional[str]=None):
        # Basic checks that mirror the DB triggers; keep minimal so tests run even without DB triggers
        if domain == 'MIRACLE' and new_status == 'REAL':
            raise ValueError('EPISTEMOLOGICAL VIOLATION: MIRACLE cannot be REAL (physics).')
        if domain in ('PHYSICS', 'ASTRONOMY') and new_status == 'MIRACLE':
            raise ValueError('EPISTEMOLOGICAL VIOLATION: PHYSICS/ASTRONOMY cannot be MIRACLE without mutawatir text.')
        if new_status == 'REAL' and (not reviewer or not reviewer.strip()):
            raise ValueError('VALIDATION ERROR: REAL status requires a reviewer.')

class ThawabitEngine:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.conn.execute('PRAGMA foreign_keys = ON;')

    def apply_schema(self, schema_sql: str):
        with self.conn:
            self.conn.executescript(schema_sql)

    def add_claim(self, claim_id: int, domain: str, text: str):
        with self.conn:
            self.conn.execute('INSERT INTO claims(id, domain, text) VALUES (?, ?, ?)', (claim_id, domain, text))

    def set_status(self, claim_id: int, status: str, reviewer: Optional[str]=None, reason: Optional[str]=None):
        if status not in VALID_STATUSES:
            raise ValueError(f"Invalid status: {status}")
        # fetch domain
        cur = self.conn.execute('SELECT domain FROM claims WHERE id = ?', (claim_id,))
        row = cur.fetchone()
        if not row:
            raise ValueError(f'Unknown claim id: {claim_id}')
        domain = row[0]
        # policy checks
        DomainPolicy.validate_transition(domain, status, reviewer, reason)
        with self.conn:
            self.conn.execute('INSERT INTO verification_status(claim_id, status, reviewer, reason) VALUES (?, ?, ?, ?)',
                              (claim_id, status, reviewer, reason))

    def list_claims(self) -> List[sqlite3.Row]:
        cur = self.conn.execute('SELECT c.id, c.domain, c.text, vs.status, vs.reviewer, vs.reason, vs.created_at\nFROM claims c LEFT JOIN verification_status vs ON c.id = vs.claim_id ORDER BY c.id DESC')
        return cur.fetchall()
