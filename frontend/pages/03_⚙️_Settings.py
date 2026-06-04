import streamlit as st

st.set_page_config(
    page_title="Settings - ADE Platform",
    page_icon="⚙️",
    layout="wide",
)

st.markdown("""
<style>
    .glass-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(20, 184, 166, 0.2);
        border-radius: 20px;
        padding: 24px;
        margin: 16px 0;
        box-shadow: 0 8px 32px rgba(20, 184, 166, 0.1);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #14b8a6;'>⚙️ Settings</h1>", unsafe_allow_html=True)

st.markdown("### 👤 User Preferences")
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    theme = st.selectbox("Theme", ["Dark Mode", "Light Mode", "Auto"])
    language = st.selectbox("Language", ["English", "Spanish", "French", "German"])

with col2:
    timezone = st.selectbox("Timezone", ["UTC", "EST", "CST", "PST", "IST"])
    notifications = st.checkbox("Enable Notifications", value=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

st.markdown("### 🔐 Security Settings")
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    two_fa = st.checkbox("Enable 2FA", value=False)
    api_key = st.text_input("API Key", type="password", value="sk_live_......")

with col2:
    auto_logout = st.slider("Auto-logout (minutes)", 15, 480, 60)
    session_timeout = st.slider("Session Timeout (minutes)", 5, 120, 30)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

st.markdown("### 📊 Data Settings")
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

retention = st.slider("Data Retention (days)", 7, 365, 90)
export_format = st.selectbox("Default Export Format", ["CSV", "JSON", "Parquet", "Excel"])
compression = st.checkbox("Enable Compression", value=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

st.markdown("### 🔔 Notification Preferences")
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    email_alerts = st.checkbox("Email Alerts", value=True)
    pipeline_failures = st.checkbox("Pipeline Failures", value=True)

with col2:
    data_quality = st.checkbox("Data Quality Issues", value=True)
    performance = st.checkbox("Performance Alerts", value=False)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns([3, 1])
with col2:
    if st.button("💾 Save Settings"):
        st.success("✓ Settings saved successfully!")

st.markdown("---")

st.markdown("### 📝 About")
st.markdown("""
<div class="glass-card">
    <p><b>ADE Platform v1.0.0</b></p>
    <p style="color: #94a3b8;">Autonomous Data Engineer Agent Platform</p>
    <p style="color: #94a3b8; font-size: 0.9rem;">© 2024 - Advanced Data Engineering Solutions</p>
</div>
""", unsafe_allow_html=True)
