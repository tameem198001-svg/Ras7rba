#!/usr/bin/env bash
set -euo pipefail

printf '\n====================================\n'
printf '🔎 algo-faqih health check\n'
printf '====================================\n\n'

# Detect project dir
if [ ! -d .git ] && [ ! -f requirements.txt ]; then
  echo "❌ لم يتم العثور على مشروع algo-faqih في هذا المجلد."
  echo "    انتقل إلى مجلد المشروع ثم شغّل هذا السكربت."
  exit 1
fi

# 1) Python
printf '1/8. فحص Python...\n'
python3 --version || { echo '❌ Python3 غير موجود'; exit 1; }
python3 -m pip --version || { echo '❌ pip غير موجود'; exit 1; }

# 2) requirements
printf '2/8. التحقق من المتطلبات...\n'
if [ -f requirements.txt ]; then
  python3 -m pip install -r requirements.txt >/dev/null 2>&1 || {
    echo "⚠️  تثبيت المتطلبات فشل، لكن نواصل للفحص الأساسي..."
  }
else
  echo "⚠️  requirements.txt غير موجود."
fi

# 3) folders
printf '3/8. فحص المجلدات الأساسية...\n'
for d in data db scripts app; do
  if [ -d "$d" ]; then
    echo "✅ $d موجود"
  else
    echo "⚠️  $d غير موجود"
  fi
done

# 4) Data files
printf '4/8. فحص البيانات...\n'
find data -maxdepth 2 -type f 2>/dev/null | head -n 20 || true

# 5) DB existence
printf '5/8. فحص قواعد البيانات...\n'
for f in data/*.db db/*.db; do
  if [ -f "$f" ]; then
    echo "✅ قاعدة بيانات موجودة: $f"
  fi
done

# 6) Build DB script
printf '6/8. فحص بناء قاعدة FTS5...\n'
if [ -f scripts/03_build_db.py ]; then
  echo "✅ scripts/03_build_db.py موجود"
else
  echo "⚠️  scripts/03_build_db.py غير موجود"
fi

# 7) Try sqlite FTS check if DB exists
printf '7/8. فحص FTS5 الفعلي...\n'
DB=""
if [ -f data/algo_faqih.db ]; then DB="data/algo_faqih.db";
elif [ -f db/algo_faqih.db ]; then DB="db/algo_faqih.db";
fi

if [ -n "$DB" ]; then
  echo "✅ تم اختيار قاعدة: $DB"
  sqlite3 "$DB" ".tables" 2>/dev/null || echo "⚠️  sqlite3 لا يمكن فتح قاعدة البيانات"
  sqlite3 "$DB" "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'fts%';" 2>/dev/null || true
else
  echo "⚠️  لا توجد قاعدة بيانات حتى الآن. شغّل أولاً: python3 scripts/03_build_db.py"
fi

# 8) Streamlit run test
printf '8/8. فحص Streamlit...\n'
if [ -f app/main.py ]; then
  echo "✅ app/main.py موجود"
  python3 -m py_compile app/main.py && echo "✅ بناء الـ Python للموقع صحيح"
  timeout 20s streamlit run app/main.py --server.headless true >/tmp/algo_faqih_streamlit.log 2>&1 &
  sleep 5
  if curl -fsS http://localhost:8501 >/tmp/algo_faqih_http.txt 2>/dev/null; then
    echo "✅ Streamlit يعمل على http://localhost:8501"
  else
    echo "⚠️  Streamlit لا يستجيب بعد 20 ثانية. قد تحتاج إلى إعداد المسارات أو تنفيذ التطبيق أولاً."
  fi
else
  echo "⚠️  app/main.py غير موجود"
fi

printf '\n====================================\n'
printf '🎯 النتيجة: فحص أساسي اكتمل\n'
printf '====================================\n'
printf 'إذا لم تظهر أي رسالة ❌ حرجة، فهذا يعني أن المشروع ليس فاشلاً فورياً.\n'
printf 'الخطوة التالية: شغّل بناء البيانات ثم التشغيل الفعلي.\n\n'
