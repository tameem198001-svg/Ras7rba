---
title: feat(united-v11.0): نُسْخَةُ "الْكُلِّ الْمُتَّحِدِ" — محاكيات، واجهة، جدول النور، CI
---

بِسْمِ اللهِ الرَّحْمَـٰنِ الرَّحِيمِ

هَذَا PR يُدْمِجُ الخُطَّةَ الْمُتَكَامِلَةَ V11.0 مِنْ فَرْعِ feat/united-v11.0 إِلَى main.

المميزات:
- إضافة محاكيات عددية: Klein–Gordon، Schrodinger (Crank–Nicolson)، Lotka–Volterra، Forced Damped Oscillator، Burgers shock.
- واجهة Streamlit متعددة الصفحات لتشغيل وعرض النتائج.
- ledger SQLite يُنشَأ عند التشغيل وتُسَجَّلُ فيه النبضات.
- اختبارات pytest بسيطة للتأكد من تطبيع Schrodinger.
- GitHub Actions CI لتشغيل pytest على PRs والـ branch.

ملاحظات تشغيل:
- لا تُرفع ملفات DB ثنائية إلى الريبو. يتم إنشاؤها محليًا بواسطة create_ledger.init_db.
- يمكن تعديل إعدادات المحاكيات وحجم الشبكات في mother_core.py حسب الحاجة.

الرجاء مراجعة الدوال العددية والاختبارات. إن وافقتم، دمجوا النبضُ.
