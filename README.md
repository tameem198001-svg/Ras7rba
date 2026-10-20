# 🏛️ RUBY MOTHER ALGORITHM (v1.0)
> The Sovereign Epistemic Verification & Adaptive Control Engine

[![System Status](https://img.shields.io/badge/System_Status-REAL_GREEN-brightgreen)](https://github.com/tameem198001-svg/Ras7rba)
[![Framework](https://img.shields.io/badge/Architecture-THAWABIT_v1.0-blue)](WAQF_CHARTER.md)
[![License](https://img.shields.io/badge/Governance-Open_Science_Waqf-gold)](WAQF_CHARTER.md)

---

## 📌 Executive Overview

The Ruby Mother Algorithm is a sovereign, zero-trust epistemic verification platform designed to filter informational noise ("Hebd"), enforce data provenance, and provide resilient resource control for mission-critical operations.

It combines traditional Hadith validation methodologies (Jarh wa Ta'dil) with modern computer science primitives (formal verification, append-only storage, and automated pattern detection).

---

## 🏗️ Architecture Stack

The system consists of four primary sovereign layers:

```text
 ┌─────────────────────────────────────────────────────────────┐
 │                1. THAWABIT Core (الميزان)                   │
 │   Classifies inputs into REAL, SYMBOLIC, or INVALID        │
 └──────────────────────────────┬──────────────────────────────┘
                                │
 ┌──────────────────────────────▼──────────────────────────────┐
 │               2. ZarqaCatBot Radar (الرادار)                 │
 │   Regex & Natural-Language Pattern Matching Sentinel        │
 └──────────────────────────────┬──────────────────────────────┘
                                │
 ┌──────────────────────────────▼──────────────────────────────┘
 │             3. Shamsi Controller (المتحكم)                  │
 │   Predictive Resource Allocation & Clamping Anti-Windup     │
 └──────────────────────────────┬──────────────────────────────┘
                                │
 ┌──────────────────────────────▼──────────────────────────────┘
 │             4. Human Ratification Gate (الخاتم)            │
 │   Mandatory Human Gate: Zero Unsupervised Deployment       │
 └─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Prerequisites & Environment

Ensure your local hardware context meets the following requirements before setup:

- OS: Linux (Ubuntu 22.04+ / Debian 12+) or macOS
- Runtime: Python 3.10+
- Database: PostgreSQL 15+ (preferred) or SQLite 3.35+ for development/testing
- Cache / Queue: Redis 7+ (optional for high concurrency)
- Version Control: Git

---

## 🚀 Quick Start & Installation

### 1) Clone the repository

```bash
git clone https://github.com/tameem198001-svg/Ras7rba.git
cd Ras7rba
```

### 2) Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Database setup

Use PostgreSQL for production-grade behavior; SQLite is acceptable for local testing and development.

```bash
export DATABASE_URL="postgresql://user:password@localhost:5432/thawabit_db"
```

If the project uses a schema or database initializer, run:

```bash
python3 -m core.db_init
```

---

## 💻 Running System Components

### A. Run ZarqaCatBot observer

```bash
python3 sentinels/zarqa_cat_bot.py --log-file memory/session_logs.md
```

### B. Run verification and testing suite

```bash
pytest tests/ -v
```

---

## 📜 Governance & Waqf Status

This project is governed under the Sovereign Waqf Charter in `WAQF_CHARTER.md`.

Key governance principles:

- Epistemic Core: free and open access forever for researchers, scholars, and institutions.
- Cybersecurity Shield: commercial B2G/B2B support dedicated exclusively to sustaining infrastructure and ongoing research.
- Human Gate: no unsupervised deployment; every significant action must pass the human ratification gate.

For the full charter and legal-intellectual framework, see:

- [WAQF_CHARTER.md](WAQF_CHARTER.md)

---

## 🛡️ License and Governance

Dedicated as Open Science Waqf.

Immutable governance — 55055.

---

## 🧭 Project Map

This repository currently contains the following structural elements:

- `algo-faqih/` — lightweight Islamic research project using SQLite/FTS-style indexing
- `docs/` — technical and governance references
- `WAQF_CHARTER.md` — sovereign foundation charter
- `README.md` — system overview and local deployment path

---

## 📎 Local Execution Snapshot

A minimal local execution pattern is:

```bash
mkdir -p docs memory
cat > README.md <<'EOF'
# 🏛️ RUBY MOTHER ALGORITHM (v1.0)
> The Sovereign Epistemic Verification & Adaptive Control Engine

[![System Status](https://img.shields.io/badge/System_Status-REAL_GREEN-brightgreen)](https://github.com/tameem198001-svg/Ras7rba)
[![Framework](https://img.shields.io/badge/Architecture-THAWABIT_v1.0-blue)](WAQF_CHARTER.md)
[![License](https://img.shields.io/badge/Governance-Open_Science_Waqf-gold)](WAQF_CHARTER.md)

## Overview
The Ruby Mother Algorithm is a sovereign, zero-trust epistemic verification platform designed to filter informational noise ("Hebd"), enforce provenance, and provide resilient control for critical operations.
EOF

git add README.md WAQF_CHARTER.md
git commit -m "docs: add technical README and waqf charter"
git push
```

---

## 🧠 Closing Statement

This project is not a conventional SaaS product.
It is a sovereign epistemic framework: a living balance between research, governance, protection, and human verification.

The aim is simple:

- preserve truth,
- guard the evidence trail,
- keep the code auditable,
- and constrain hallucination through human and formal review.

Tata Tata — on the balance that stands, the shield that protects, and the code that remains accountable.

---

# Ras7rba

## الخريطة

هذا المستودع هو مستودع موحد (monorepo) يضم:

- `algo-faqih/` — مشروع بحث شرعي خفيف مبني على SQLite FTS5
- `docs/` — وثائق ومنهجية التوثيق والتدقيق
- `WAQF_CHARTER.md` — الميثاق الرسمي للوقف والمعايير
- `README.md` — خريطة المشروع فقط

## المعيار الأساسي

- `Issues` = مسودات ومناقشات تاريخية
- `Files` = المرجع المعتمد
- `README.md` = خريطة المشروع فقط
- `WAQF_CHARTER.md` = الدستور

## الخلاصة الخماسية

- الثابت لا يُفرقع.
- المشتق لا يُقدس.
- العمل يثبت الباطن.
- المنهج يحدد القبول والرفض.
- اليقين يأتي بعد التمييز.

## المراجع

- [WAQF_CHARTER.md](WAQF_CHARTER.md)
- [algo-faqih/README.md](algo-faqih/README.md)

تاتا تاتا — على الثبات بعد التمييز 🌙🐺
