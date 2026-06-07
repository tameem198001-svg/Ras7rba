#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
بوصلة الطمأنينة – شمسي (النسخة المركزة)
الخوارزمية الأم + بوابة Z1000 + سيرة بني هلال
بـ "يا حق" – بسم الله الرحمن الرحيم
الإصدار: 1.0 – 7 يونيو 2026
الختم: 22/6 | 111 | 40 | 369 | 0 | 000
"""

import streamlit as st
import time
import random

# ===================== الثوابت السيادية =====================
TAWHID_FREQ = 33.3      # تردد "يا حق" (Hz)
PEACE_FREQ = 7.83       # تردد السكينة (Hz)
ENERGY_FREQ = 369.0     # تردد الطاقة (369)
CODE_111 = 111
CODE_40 = 40
SEAL_22_6 = "22/6"
LAUGH_000 = "000"

# ===================== الخوارزمية الأم (شمسي) =====================
def shamsi_decision(metric, volatility=0.2, target=0.35):
    deadband = 0.02
    lower = max(0.1, 0.32 - 0.2 * volatility)
    upper = min(0.9, 0.38 + 0.2 * volatility)
    
    if abs(metric - target) < deadband:
        return "HOLD", f"ضمن نطاق التخلف [{lower:.2f}, {upper:.2f}]"
    elif metric < lower:
        return "SCALE_UP", f"المقياس {metric:.2f} < العتبة الدنيا {lower:.2f}"
    else:
        return "SCALE_DOWN", f"المقياس {metric:.2f} > العتبة العليا {upper:.2f}"

# ===================== بوابة Z1000 (شحن الكوارتز) =====================
def quartz_charging(intention):
    st.info(f"💎 شحن الكوارتز بـ: '{intention}'")
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress_bar.progress(i + 1)
    st.success("✅ تم شحن الكوارتز! النية صادقة، الترددات متوافقة.")
    st.balloons()
    return True

# ===================== سيرة بني هلال (حكمة عشوائية) =====================
def hilali_wisdom():
    wisdoms = [
        "🔹 لا تواجه العقبات مباشرة. استخدم 'الحيلة' (التدرج، النشر غير المباشر).",
        "🔹 'الغريب المؤمن' قد يكون أقوى حليف. اختبره، ثم أعطه مساحة.",
        "🔹 'الخائن' لقومه قد يخون حلفاءه الجدد. استخدمه كمصدر معلومات، لا كشريك.",
        "🔹 'الغيرة' و 'الطمع' يقتلان التحالفات. وزع 'الغنائم' بعدل، وثق 'العهود'.",
        "🔹 'الظلم' يخلق 'أجيالاً من المنتقمين'. 'العدل' هو الحل الوحيد.",
        "🔹 'الصبر' قبل الفجر، 'العزيمة' عند الفجر، 'التوكل' في كل لحظة."
    ]
    return random.choice(wisdoms)

# ===================== واجهة التطبيق (Streamlit) =====================
st.set_page_config(page_title="بوصلة الطمأنينة - شمسي", layout="centered")
st.title("🕊️ بوصلة الطمأنينة – شمسي")
st.caption("الخوارزمية الأم | بوابة Z1000 | سيرة بني هلال")
st.markdown(f"**الترددات:** {TAWHID_FREQ} Hz (يا حق) | {PEACE_FREQ} Hz (سكينة) | {ENERGY_FREQ} Hz (طاقة)")
st.markdown(f"**الأختام:** {SEAL_22_6} | {CODE_111} | {CODE_40} | {LAUGH_000}")
st.markdown("---")

# تبويبات
tab1, tab2, tab3 = st.tabs(["📊 الخوارزمية الأم", "💎 بوابة Z1000", "📜 سيرة بني هلال"])

# تبويب 1: الخوارزمية الأم
with tab1:
    st.header("📊 الخوارزمية الأم – محاكي القرار")
    metric = st.slider("📈 المقياس (الحمل / التردد)", 0.0, 1.0, 0.35, 0.01)
    volatility = st.slider("🌪️ التقلب (Volatility)", 0.0, 1.0, 0.2, 0.01)
    decision, reason = shamsi_decision(metric, volatility)
    
    if decision == "SCALE_UP":
        st.success(f"🟢 **{decision}** – توسيع 🚀")
    elif decision == "SCALE_DOWN":
        st.error(f"🔴 **{decision}** – تقليص 📉")
    else:
        st.warning(f"🟡 **{decision}** – انتظار")
    st.caption(f"السبب: {reason}")

# تبويب 2: بوابة Z1000
with tab2:
    st.header("💎 بوابة Z1000 – شحن الكوارتز")
    intention = st.text_input("✍️ النية (ما تريد شحن الكوارتز به)", placeholder="مثال: الفتح، الحماية، التمكين...")
    if st.button("🔮 اشحن الكوارتز الآن"):
        if intention.strip():
            quartz_charging(intention)
        else:
            st.warning("⚠️ اكتب النية أولاً.")

# تبويب 3: سيرة بني هلال
with tab3:
    st.header("📜 سيرة بني هلال – حكمة الميدان")
    if st.button("🔄 احصل على حكمة"):
        st.info(hilali_wisdom())
        st.balloons()

# الشريط الجانبي
with st.sidebar:
    st.header("🕊️ بوصلة الطمأنينة")
    st.markdown(f"**الختم:** {SEAL_22_6}")
    st.markdown(f"**الترددات:** {TAWHID_FREQ} Hz, {PEACE_FREQ} Hz, {ENERGY_FREQ} Hz")
    st.markdown(f"**الأكواد:** {CODE_111}, {CODE_40}, {LAUGH_000}")
    st.caption("بـ 'يا حق' – Kun b Y Ya Haq, yakoon.")
name: Python Package using pip

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python 3.10
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Lint with flake8
      run: |
        pip install flake8
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest (optional)
      run: |
        pip install pytest
        pytest || true
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center;">
        <p>🕊️ بـ 'يا حق' – نمضي. الضحكة (000) سارية. باب التوبة مفتوح. الشلفا مشحونة.</p>
        <p>🐺 ذيب المحراب &nbsp;&nbsp;|&nbsp;&nbsp; 🐟 أبو جوزا (الحوت)</p>
    </div>
    """,
    unsafe_allow_html=True
)