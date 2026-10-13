# Architecture — algo-faqih (v0.1)

نظرة عامة هندسية للمشروع الفرعي algo-faqih — المرحلة الأولى (v0.1).

مكونات رئيسية
- ETL (scripts/): تنزيل المصادر، تنظيفها، تقسيمها، وبناء قاعدة FTS5.
- البيانات (data/): raw/ و processed/ وملف قاعدة البيانات sqlite (algo_faqih.db).
- DB: SQLite مع FTS5 جدول `texts(title, body, source, source_ref, tags)`.
- واجهة (app/): Streamlit لتجربة البحث وعرض provenance.
- اختبارات (tests/): pytest لفحص بناء القاعدة واسترجاع النتائج.
- CI: GitHub Actions لتشغيل الاختبارات تلقائياً عند push/PR.

تدفق البيانات
1. scripts/01_download_quran.py و 02_download_hadith.py يحفظان ملفات في data/raw/.
2. scripts/03_preprocess.py ينقح النص ويضع النسخ في data/processed/.
3. scripts/04_build_db.py يبني قاعدة SQLite FTS5 في data/algo_faqih.db مع حفظ provenance.
4. app/main.py يستخدم قاعدة البيانات للاستعلام وعرض النتائج مع حقول المصدر.

اعتبارات هندسية
- البساطة أولاً: SQLite FTS5 مناسب للمرحلة التجريبية وسهل النقل.
- إثبات المصدر (provenance) مطلوب لكل قطعة نصية.
- إقصاء أي سلوك قد يُفهم كـ"فتوى آلية" على مستوى الواجهة والمنطق.

ملاحظات نشر
- لا تدفع ملفات البيانات الكبيرة إلى المستودع.
- أدرج قواعد نسخ احتياطية لقواعد البيانات خارج الريبو.

