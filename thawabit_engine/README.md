# thawabit_engine/README.md

Thawabit Engine scaffold

This directory contains a minimal scaffold for the Thawabit engine described in issue #19.

- schema.sql: sqlite schema + triggers that enforce domain isolation rules (MIRACLE vs PHYSICS)
- engine.py: small engine with VALID_STATUSES and ThawabitEngine wrapper
- cli.py: lightweight CLI to add claims and set status
- evaluators/: placeholders for domain-specific evaluators
- tests/: pytest tests for DB triggers and engine behavior

Apply and run tests:

$ python -c "import sqlite3; print(sqlite3.sqlite_version)"
$ pytest thawabit_engine/tests -q
