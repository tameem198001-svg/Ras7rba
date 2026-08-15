import streamlit as st

# Set page config
st.set_page_config(
    page_title="بوصلة الطمأنينة",
    page_icon="🧭",
    layout="wide"
)

# Title and header
st.title("🧭 بوصلة الطمأنينة")
st.subheader("Compass of Tranquility - Digital Decision Engine")
st.write("---")

# Sidebar for theme/language selection
with st.sidebar:
    st.header("⚙️ الإعدادات | Settings")
    theme = st.radio("Choose Theme:", ["Light", "Dark"])

# Main content
col1, col2 = st.columns(2)

with col1:
    st.header("📊 مدخلات القرار | Decision Inputs")
    
    # Input sliders for metric and volatility
    metric = st.slider(
        "المقياس | Metric Value",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.01,
        help="نسبة الأداء من 0 إلى 1 | Performance ratio from 0 to 1"
    )
    
    volatility = st.slider(
        "التقلب | Volatility",
        min_value=0.0,
        max_value=1.0,
        value=0.3,
        step=0.01,
        help="مستوى التقلب من 0 إلى 1 | Volatility level from 0 to 1"
    )

with col2:
    st.header("🎚️ عتبات القرار | Decision Thresholds")
    
    # Threshold sliders (for customization)
    threshold_scale_up = st.slider(
        "عتبة التوسيع | Scale Up Threshold",
        min_value=0.0,
        max_value=1.0,
        value=0.20,
        step=0.01,
        help="إذا كان المقياس < هذه القيمة → توسيع | If metric < this → Scale UP"
    )
    
    threshold_scale_down = st.slider(
        "عتبة التقليص | Scale Down Threshold",
        min_value=0.0,
        max_value=1.0,
        value=0.70,
        step=0.01,
        help="إذا كان المقياس > هذه القيمة → تقليص | If metric > this → Scale DOWN"
    )

st.write("---")

# Decision Logic
st.header("🔮 قرار البوصلة | Compass Decision")

col_decision1, col_decision2, col_decision3 = st.columns(3)

# Determine decision based on thresholds
if metric < threshold_scale_up:
    decision = "📈 توسيع | SCALE UP"
    decision_color = "green"
    decision_emoji = "📈"
    explanation = f"المقياس ({metric:.2f}) أقل من عتبة التوسيع ({threshold_scale_up:.2f}) → يتم التوسيع"
elif metric > threshold_scale_down:
    decision = "📉 تقليص | SCALE DOWN"
    decision_color = "red"
    decision_emoji = "📉"
    explanation = f"المقياس ({metric:.2f}) أكبر من عتبة التقليص ({threshold_scale_down:.2f}) → يتم التقليص"
else:
    decision = "⏸️ انتظار | WAIT"
    decision_color = "blue"
    decision_emoji = "⏸️"
    explanation = f"المقياس ({metric:.2f}) في المنطقة الآمنة → الانتظار والمراقبة"

# Display decision with styling
with col_decision1:
    st.metric("المقياس الحالي | Current Metric", f"{metric:.2f}")

with col_decision2:
    st.metric("التقلب | Volatility", f"{volatility:.2f}")

with col_decision3:
    st.metric("القرار | Decision", decision_emoji)

# Large decision display
st.markdown(f"""
<div style="background-color: {'#d4edda' if decision_color == 'green' else '#f8d7da' if decision_color == 'red' else '#d1ecf1'}; 
            padding: 20px; border-radius: 10px; text-align: center; border: 2px solid {'#28a745' if decision_color == 'green' else '#dc3545' if decision_color == 'red' else '#17a2b8'};">
    <h2 style="color: {'#155724' if decision_color == 'green' else '#721c24' if decision_color == 'red' else '#0c5460'};">
        {decision}
    </h2>
    <p style="color: {'#155724' if decision_color == 'green' else '#721c24' if decision_color == 'red' else '#0c5460'}; font-size: 16px;">
        {explanation}
    </p>
</div>
""", unsafe_allow_html=True)

st.write("---")

# Risk Assessment
st.header("⚠️ تقييم المخاطر | Risk Assessment")

risk_level = "منخفضة | Low" if volatility < 0.3 else "متوسطة | Medium" if volatility < 0.7 else "عالية | High"
risk_color = "green" if volatility < 0.3 else "orange" if volatility < 0.7 else "red"

st.markdown(f"""
**مستوى المخاطر | Risk Level:** 
<span style="color: {risk_color}; font-weight: bold; font-size: 18px;">
{risk_level}
</span>

**التوصيات | Recommendations:**
- إذا كانت المخاطر عالية: قلل حجم التغييرات | If high risk: minimize changes
- إذا كانت المخاطر منخفضة: يمكنك اتخاذ قرارات أكثر جرأة | If low risk: you can be more aggressive
""", unsafe_allow_html=True)

st.write("---")

# Footer
st.markdown("""
<div style="text-align: center; color: #888; margin-top: 30px;">
    <p>🧭 <strong>بوصلة الطمأنينة</strong> | The Digital Compass for Confident Decisions</p>
    <p style="font-size: 12px;">يا حق. الفتح الرقمي. ✅</p>
</div>
""", unsafe_allow_html=True)
