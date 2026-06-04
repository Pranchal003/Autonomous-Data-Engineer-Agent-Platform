import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="ETL Manager - ADE Platform",
    page_icon="🔧",
    layout="wide"
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
    
    .pipeline-item {
        background: rgba(30, 41, 59, 0.5);
        border-left: 4px solid #14b8a6;
        padding: 16px;
        border-radius: 8px;
        margin: 12px 0;
    }
    
    .status-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
    }
    
    .status-running {
        background: rgba(16, 185, 129, 0.2);
        color: #10b981;
        border: 1px solid rgba(16, 185, 129, 0.4);
    }
    
    .status-success {
        background: rgba(34, 197, 94, 0.2);
        color: #22c55e;
        border: 1px solid rgba(34, 197, 94, 0.4);
    }
    
    .status-error {
        background: rgba(239, 68, 68, 0.2);
        color: #ef4444;
        border: 1px solid rgba(239, 68, 68, 0.4);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #14b8a6;'>🔧 ETL Pipeline Manager</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Pipelines", "12", "↑ 2 new")
with col2:
    st.metric("Running", "3", "All healthy")
with col3:
    st.metric("Success Rate", "98.7%", "↑ 0.3%")

st.markdown("---")

# Create New Pipeline
with st.expander("➕ Create New Pipeline", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        pipeline_name = st.text_input("Pipeline Name", placeholder="e.g., sales_data_etl")
        pipeline_source = st.selectbox("Data Source", ["CSV", "Database", "API", "Cloud Storage"])
    with col2:
        pipeline_dest = st.selectbox("Destination", ["Data Lake", "Data Warehouse", "Database", "Cloud"])
        schedule = st.selectbox("Schedule", ["Hourly", "Daily", "Weekly", "Monthly", "Manual"])
    
    if st.button("🚀 Create Pipeline"):
        st.success(f"Pipeline '{pipeline_name}' created successfully!")

st.markdown("---")

st.markdown("<h3 style='color: #14b8a6;'>📋 Active Pipelines</h3>", unsafe_allow_html=True)

pipelines = [
    {"name": "sales_etl", "status": "running", "progress": 75, "last_run": "2 hours ago"},
    {"name": "customer_data", "status": "success", "progress": 100, "last_run": "1 hour ago"},
    {"name": "inventory_sync", "status": "running", "progress": 45, "last_run": "Just started"},
    {"name": "product_catalog", "status": "success", "progress": 100, "last_run": "3 hours ago"},
]

for pipeline in pipelines:
    status_class = f"status-{pipeline['status']}"
    status_icon = "🟢" if pipeline['status'] == "success" else "🟡"
    
    st.markdown(f"""
    <div class="pipeline-item">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h4 style="margin: 0; color: #f1f5f9;">{status_icon} {pipeline['name']}</h4>
                <p style="margin: 4px 0; color: #94a3b8; font-size: 0.9rem;">Last run: {pipeline['last_run']}</p>
            </div>
            <div>
                <span class="{status_class}">{pipeline['status'].upper()}</span>
            </div>
        </div>
        <div style="width: 100%; height: 8px; background: rgba(148, 163, 184, 0.1); border-radius: 4px; margin-top: 12px; overflow: hidden;">
            <div style="width: {pipeline['progress']}%; height: 100%; background: linear-gradient(90deg, #14b8a6, #06b6d4); border-radius: 4px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("<h3 style='color: #14b8a6;'>📊 Pipeline Performance</h3>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

metrics = [
    ("Avg Duration", "2m 34s", "#14b8a6"),
    ("Throughput", "125MB/s", "#06b6d4"),
    ("Error Rate", "0.3%", "#8b5cf6"),
    ("Uptime", "99.8%", "#f59e0b"),
]

for col, (label, value, color) in zip([col1, col2, col3, col4], metrics):
    with col:
        st.markdown(f"""
        <div class="glass-card" style="text-align: center; border-top: 3px solid {color};">
            <p style="color: #94a3b8; margin: 0; font-size: 0.9rem;">{label}</p>
            <h3 style="color: {color}; margin: 8px 0;">{value}</h3>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("<h3 style='color: #14b8a6;'>⚙️ Pipeline Configuration</h3>", unsafe_allow_html=True)

with st.form("pipeline_config"):
    col1, col2 = st.columns(2)
    with col1:
        retry_attempts = st.slider("Retry Attempts", 0, 5, 3)
        timeout = st.number_input("Timeout (seconds)", min_value=30, value=300)
    with col2:
        parallel_tasks = st.slider("Parallel Tasks", 1, 10, 4)
        notification = st.checkbox("Enable Notifications", value=True)
    
    if st.form_submit_button("💾 Save Configuration"):
        st.success("Configuration saved successfully!")
