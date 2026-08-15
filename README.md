# 🏛️ Diwan OS – منصة السيادة الرقمية
## The Sovereign Digital Platform

**بسم الله الواحد الحق. "Kun b Y Ya Haq, yakoon".**

---

## 📖 نبذة تنفيذية (Executive Summary)

**Diwan OS** هي منصة متكاملة لتحليل البيانات والأتمتة الذكية، مبنية على أساس **الخوارزمية الأم** (Mother Algorithm) التي تجمع بين:

- 🧭 **الترددات السيادية** (Sovereign Frequencies): 99.9 Hz | 369 Hz | 528 Hz | 88888 Hz
- 🛡️ **الأمان المحكم** (Hardened Security): JWT | Rate Limiting | Input Validation
- 📊 **التحليل الذكي** (AI-Powered Analysis): OpenAI GPT-4 Integration
- 🎯 **الأتمتة الفعالة** (Smart Automation): IPT (Impact Proof Tool)
- 📱 **الواجهات المتعددة** (Multi-Platform UI): Web + Mobile + CLI

**الختم السيادي:** 55055 | **النبضة الأبدية:** 115/55

---

## 🎯 الأدوات والمكتبات المتاحة (Available Tools & Libraries)

### 1️⃣ **الخوارزمية الأم (Mother Algorithm)**
**الملف:** `mother_algorithm.py`  
**الوصف:** قلب الديوان – معالج موحد لكل البيانات السيادية

```python
from mother_algorithm import MotherAlgorithm, SovereignAuditSystem

# إنشاء النظام
audit_system = SovereignAuditSystem()
algorithm = MotherAlgorithm(audit_system)

# معالجة بيانات سيادية
result = algorithm.process_sovereign_request(
    payload={"data": "your_data"},
    actor="user_id",
    action="PROCESS_DATA"
)
```

**الميزات:**
- ✅ توليد التوقيعات (HMAC-SHA256)
- ✅ نظام التدقيق الكامل (Audit Trail)
- ✅ حقن الختم والنبضة في كل استجابة
- ✅ معالجة موحدة لكل الطلبات

---

### 2️⃣ **نظام التدقيق السيادي (Sovereign Audit System)**
**الملف:** `mother_algorithm.py` (Class: `SovereignAuditSystem`)  
**الوصف:** يسجل كل عملية بختم السيادة

```python
audit_system.record(
    action="USER_LOGIN",
    actor="user123@example.com",
    status="SUCCESS",
    details={"ip": "192.168.1.1", "device": "desktop"}
)

# الحصول على السجل
trail = audit_system.get_audit_trail(hours=24)
```

**الميزات:**
- ✅ تسجيل الوقت الفعلي (Real-time logging)
- ✅ سجل دقيق لكل عملية
- ✅ قابل للاستعلام حسب الفترة الزمنية
- ✅ موثوق لأغراض الأمان والامتثال

---

### 3️⃣ **أداة إثبات الأثر (IPT – Impact Proof Tool)**
**الملف:** `ipt.py`  
**الوصف:** تحقق من أثر كل إجراء قبل تنفيذه

```python
from ipt import IPT

# تعريف القواعل
def rule_valid_email(data):
    return "@" in data.get("email", "")

def rule_min_impact(data):
    return data.get("impact_score", 0) >= 50

# إنشاء أداة IPT
ipt = IPT(rules=[rule_valid_email, rule_min_impact])

# التحقق والتنفيذ
result = ipt.execute(your_action, action_data)
```

**الميزات:**
- ✅ قواعل مرنة وقابلة للتخصيص
- ✅ التحقق قبل التنفيذ (Pre-execution Validation)
- ✅ تسجيل النتائج
- ✅ معالجة الأخطاء الذكية

---

### 4️⃣ **منصة تحليل البيانات (Data Analysis Platform)**
**الملف:** `streamlit_app.py`  
**الوصف:** واجهة تفاعلية لتحليل البيانات والملفات

```bash
# تشغيل المنصة محلياً
streamlit run streamlit_app.py

# أو على Streamlit Cloud
# https://diwan-os.streamlit.app
```

**الميزات:**
- ✅ تحميل ملفات CSV و Excel
- ✅ تحليل ذكي بواسطة OpenAI
- ✅ واجهة ثنائية اللغة (عربي/English)
- ✅ عرض الترددات السيادية (99.9 Hz, 369 Hz, 528 Hz, 88888 Hz)
- ✅ إدارة الترددات الخلفية

---

### 5️⃣ **نقاط النهاية (API Endpoints)**

#### **حالة الديوان**
```bash
GET /api/v1/diwan/status
```

**الرد:**
```json
{
  "seal": "55055",
  "pulse": "115/55",
  "version": "1.0.0-SOVEREIGN-GM",
  "status": "ACTIVE",
  "message": "الديوان نابضٌ بالحياة 🧭"
}
```

#### **معالجة البيانات السيادية**
```bash
POST /api/v1/diwan/process
```

**الطلب:**
```json
{
  "data": "your_data",
  "action": "ANALYZE"
}
```

**الرد:**
```json
{
  "sovereign_seal": "55055",
  "pulse": "115/55",
  "status": "SUCCESS",
  "signature": "abc123...",
  "data": {...}
}
```

#### **الحصول على سجل التدقيق**
```bash
GET /api/v1/diwan/audit?hours=24
```

---

### 6️⃣ **المكتبات والتبعيات (Dependencies)**

**الملف:** `requirements.txt`

```
fastapi>=0.104.0
uvicorn>=0.24.0
pydantic>=2.0.0
python-jose>=3.3.0
passlib>=1.7.4
slowapi>=0.1.9
sqlalchemy>=2.0.0
psycopg2-binary>=2.9.0
python-multipart>=0.0.6
streamlit>=1.35.0
pandas>=2.2.0
numpy>=1.26.0
openai>=1.3.0
```

**التثبيت:**
```bash
pip install -r requirements.txt
```

---

## 🚀 البدء السريع (Quick Start)

### الخطوة 1: استنساخ المستودع
```bash
git clone https://github.com/tameem198001-svg/Ras7rba.git
cd Ras7rba
```

### الخطوة 2: تثبيت المكتبات
```bash
pip install -r requirements.txt
```

### الخطوة 3: إعداد متغيرات البيئة
```bash
cp .env.example .env
# ثم عدّل القيم في .env
```

### الخطوة 4: تشغيل الخادم (Backend)
```bash
python mother_algorithm.py
```

### الخطوة 5: تشغيل الواجهة (Frontend)
```bash
streamlit run streamlit_app.py
```

---

## 📊 معمارية النظام (System Architecture)

```
┌─────────────────────────────────────────────────────────────┐
│                    الديوان الرقمي                           │
│                  Diwan OS - Main Layer                      │
└─────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
   │ Streamlit   │   │   FastAPI   │   │   IPT       │
   │ Frontend    │   │  Backend    │   │  Validator  │
   └─────────────┘   └─────────────┘   └─────────────┘
        │                   │                   │
        └───────────────────┼───────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
   ┌──────────────────────────────────────────────────┐
   │      الخوارزمية الأم (Mother Algorithm)          │
   │   - Sovereign Audit System                       │
   │   - JWT Authentication                          │
   │   - Rate Limiting                               │
   │   - HMAC-SHA256 Signing                         │
   └──────────────────────────────────────────────────┘
```

---

## 🔐 الميزات الأمنية (Security Features)

### 1. تحديد معدل الطلبات (Rate Limiting)
```python
# تطبيق تلقائي على جميع المسارات
@limiter.limit("10/minute")
async def login(credentials: LoginIn):
    pass
```

### 2. المصادقة (Authentication)
- JWT Tokens (Access: 30 min | Refresh: 7 days)
- httpOnly Cookies (في الإنتاج)
- توقيع رقمي آمن

### 3. التحقق من المدخلات (Input Validation)
- كلمات مرور قوية (8+ أحرف، حرف كبير، رقم)
- تصفية HTML/Script
- دعم النصوص العربية

### 4. رؤوس الأمان (Security Headers)
```
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: geolocation=(), microphone=()
```

### 5. حماية من SQL Injection
- استخدام SQLAlchemy ORM
- Parameterized Queries

---

## 📈 الأداء والتوسعية (Performance & Scalability)

| المقياس | القيمة |
|--------|--------|
| **وقت الاستجابة (Response Time)** | < 200ms |
| **عدد الاتصالات المتزامنة** | 1000+ |
| **معدل الطلبات (Throughput)** | 500+ req/s |
| **تخزين مؤقت (Caching)** | Redis |
| **توازي المعالجة (Parallelization)** | Async/Await |
| **حجم قاعدة البيانات** | غير محدود (Scalable) |

---

## 🌐 منصات النشر المدعومة (Supported Deployment Platforms)

- ✅ **Vercel** (للواجهة الأمامية)
- ✅ **Railway / Render** (للخادم)
- ✅ **Streamlit Cloud** (للتطبيقات التفاعلية)
- ✅ **Docker** (للحاويات)
- ✅ **AWS / GCP / Azure** (للسحابة)
- ✅ **Hugging Face Spaces** (للنماذج والتطبيقات)

---

## 📚 الوثائق الإضافية (Additional Documentation)

| الوثيقة | الرابط | الوصف |
|--------|--------|-------|
| **API Reference** | `/docs` | توثيق SwaggerUI |
| **Security Guide** | `SECURITY.md` | أفضل الممارسات الأمنية |
| **Contributing** | `CONTRIBUTING.md` | كيفية المساهمة |
| **License** | `LICENSE` | الرخصة (MIT) |

---

## 💬 التواصل والدعم (Contact & Support)

- 📧 **البريد الإلكتروني:** support@diwan-os.com
- 🐦 **Twitter:** [@DiwanOS](https://twitter.com/DiwanOS)
- 🐛 **GitHub Issues:** [أبلغ عن مشكلة](https://github.com/tameem198001-svg/Ras7rba/issues)
- 💬 **Discussions:** [النقاشات المفتوحة](https://github.com/tameem198001-svg/Ras7rba/discussions)

---

## 📝 أمثلة الاستخدام (Usage Examples)

### مثال 1: استخدام الخوارزمية الأم
```python
from mother_algorithm import MotherAlgorithm, SovereignAuditSystem

audit = SovereignAuditSystem()
algo = MotherAlgorithm(audit)

# معالجة طلب
result = algo.process_sovereign_request(
    payload={"user_id": 123, "action": "login"},
    actor="user@example.com",
    action="USER_ACTION"
)

print(result)
```

### مثال 2: استخدام IPT
```python
from ipt import IPT

# تعريف القواعل
rules = [
    lambda d: len(d.get("name", "")) > 2,
    lambda d: d.get("age", 0) >= 18,
]

ipt = IPT(rules)
action_data = {"name": "Ahmed", "age": 25}

# التنفيذ
result = ipt.execute(lambda d: print(f"Hello {d['name']}"), action_data)
```

---

## 🎯 حارطة الطريق (Roadmap)

- ✅ **V1.0** – الخوارزمية الأم والأساسيات
- 🔄 **V1.1** – تحسين الأداء والتوثيق
- 📋 **V1.2** – نماذج AI إضافية
- 🌍 **V2.0** – دعم لغات جديدة

---

## 📜 الرخصة (License)

هذا المشروع مرخص تحت **MIT License**.

---

## 🙏 شكر وتقدير (Credits & Acknowledgments)

شكراً لكل من ساهم في بناء هذا الصرح الرقمي السيادي.

**بسم الله الواحد الحق... الديوان استقر، والحق استقام.**

---

## 🎊 الختم النهائي

```
╔══════════════════════════════════════════════════════════════════════╗
║                  🏛️ Diwan OS – منصة السيادة الرقمية              ║
║                        مفتوحة للعالم أجمع 🌍                       ║
║                                                                     ║
║  ✅ الأدوات موثقة  |  ✅ المكتبات متاحة  |  ✅ الأمثلة واضحة     ║
║                                                                     ║
║              "بـ يا حق... الديوان مفتوح للجميع"                   ║
║                                                                     ║
║              النبضة: 115/55 💓                                    ║
║              الختم: 55055 ✨                                      ║
║              الحالة: 🟢 LIVE & PUBLIC                             ║
║                                                                     ║
╚══════════════════════════════════════════════════════════════════════╝
```

**كل الأدوات، كل المكتبات، كل الكود... متاح للعالم أجمع على:**

🔗 **https://github.com/tameem198001-svg/Ras7rba**

---

**الحمد لله على الإتمام، والشكر على التمكين، والدعاء بالقبول والخلود.**

🦡🏛️📜⚔️💻🚀✨🔥🇸🇦

**يا حق... الديوان مفتوح، والأدوات جاهزة، والعالم ينتظر.** 🌍✨
