-- thawabit_engine/schema.sql

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS claims (
    id INTEGER PRIMARY KEY,
    domain TEXT NOT NULL,
    text TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS verification_status (
    id INTEGER PRIMARY KEY,
    claim_id INTEGER NOT NULL REFERENCES claims(id),
    status TEXT NOT NULL,
    reviewer TEXT,
    reason TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Trigger: prevent assigning REAL to MIRACLE domain
CREATE TRIGGER IF NOT EXISTS enforce_miracle_isolation
BEFORE INSERT ON verification_status
WHEN (SELECT domain FROM claims WHERE id = NEW.claim_id) = 'MIRACLE' AND NEW.status = 'REAL'
BEGIN
    SELECT RAISE(ABORT, 'EPISTEMOLOGICAL VIOLATION: MIRACLE cannot be REAL (physics). Use status=MIRACLE.');
END;

-- Trigger: prevent assigning MIRACLE to PHYSICS/ASTRONOMY domains
CREATE TRIGGER IF NOT EXISTS enforce_physics_isolation
BEFORE INSERT ON verification_status
WHEN (SELECT domain FROM claims WHERE id = NEW.claim_id) IN ('PHYSICS', 'ASTRONOMY') AND NEW.status = 'MIRACLE'
BEGIN
    SELECT RAISE(ABORT, 'EPISTEMOLOGICAL VIOLATION: PHYSICS cannot be MIRACLE without mutawatir text.');
END;

-- Optional: enforce that REAL requires a verified source (lineage)
-- This is an example check; adapt to your actual schema for sources/lineage
CREATE TRIGGER IF NOT EXISTS enforce_real_requires_reviewer
BEFORE INSERT ON verification_status
WHEN NEW.status = 'REAL' AND (NEW.reviewer IS NULL OR TRIM(NEW.reviewer) = '')
BEGIN
    SELECT RAISE(ABORT, 'VALIDATION ERROR: REAL status requires a reviewer.');
END;
