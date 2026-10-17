## 🏛️ THAWABIT Engine v0.3.0 — Zero-Trust Core + Piece 1
### محرك الثوابت v0.3.0 — النواة الصلبة + القطعة الأولى

### 📌 Overview | نظرة عامة
This PR establishes the foundational architecture for the THAWABIT Evidence & Provenance Engine, including the official `FOUNDATION.md` manifesto.
*يؤسس هذا الدمج البنية الأساسية لمحرك الثوابت، بما في ذلك دستور الميزان `FOUNDATION.md`.*

### 🛠️ What's Included | ما تم إنجازه
- **Documentation:** Added `docs/FOUNDATION.md` (Bilingual).
- **Core Separation:** Claims are strictly separated from Sources and Evidence.
- **Piece 1 (Hadith Base):** Added `narrators` and `isnads` tables. If a chain contains a `REJECTED` narrator, the claim cannot become `REAL`.
- **Database Triggers:** Hardcoded SQL-level protection against moving a claim to `REAL` without the required criteria.

### 🛡️ Zero-Trust Guarantee | ضمان الثقة المعدومة
Even if the Python application layer is bypassed, the SQLite triggers will `ABORT` any attempt to elevate a claim to `REAL` without verification.

### ✅ Testing | الاختبارات
- `15 passed` locally. All rules are covered by `pytest`.

---
### 🔍 Reviewer Checklist | قائمة فحص المراجع
- [ ] **Triggers Integrity:** Does SQLite prevent any transition to `REAL` without `VERIFIED` source, evidence, or reason?
- [ ] **Append-Only History:** Is `revision_history` protected against deletion?
- [ ] **CI Green:** Did all `pytest` (15/15) pass via GitHub Actions?

**Out of Scope (Locked for v0.4+) | خارج النطاق:**
- Advanced Hadith evaluator (Tawatur, Mawdu, Munqati).
- Astronomy evaluator (Apogee vs. Biruni).
- Knowledge Wall Importer.
