# Ras7rba — Noor Wall — V11.0

This branch implements the "united" V11.0 plan: multiple numerical simulators, a Streamlit multi-page UI, a ledger (SQLite) created on first run, CI tests, and helper deployment/scheduler scripts.

Highlights:
- mother_core.py: Klein-Gordon, Schrodinger (Crank–Nicolson), Lotka–Volterra, Forced Damped Oscillator, Burgers shock.
- streamlit_app.py: Multi-page interface to run all or single simulations and inspect the ledger.
- create_ledger.py: Create and log results to `noor_wall_ledger.db` (the DB file is not added to repo).
- tests: simple pytest for Schrodinger normalization.
- .github/workflows/ci.yml: runs pytest on PRs.

How to run locally:
1. python -m venv .venv && source .venv/bin/activate
2. pip install -r requirements.txt
3. python streamlit_app.py (or `streamlit run streamlit_app.py`)

