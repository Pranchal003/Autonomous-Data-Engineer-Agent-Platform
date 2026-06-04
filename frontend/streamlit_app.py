import streamlit as st
import pandas as pd
from datetime import datetime
import time
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="ADE Platform - Data Engineering AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CUSTOM CSS ====================
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1a1f35 50%, #0f172a 100%);
        font-family: 'Segoe UI', 'Roboto', system-ui, -apple-system, sans-serif;
    }
    
    .glass-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(20, 184, 166, 0.2);
        border-radius: 20px;
        padding: 24px;
        margin: 16px 0;
        box-shadow: 0 8px 32px rgba(20, 184, 166, 0.1);
        transition: all 0.3s ease;
    }
    
    .glass-card:hover {
        background: rgba(30, 41, 59, 0.9);
        border-color: rgba(20, 184, 166, 0.4);
        box-shadow: 0 12px 48px rgba(20, 184, 166, 0.2);
        transform: translateY(-2px);
    }
    
    .header-section {
        text-align: center;
        padding: 40px 20px;
        background: linear-gradient(135deg, rgba(20, 184, 166, 0.1), rgba(13, 148, 136, 0.05));
        border-radius: 24px;
        margin-bottom: 40px;
        border: 1px solid rgba(20, 184, 166, 0.2);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    }
    
    .header-section h1 {
        font-size: 3.5rem;
        background: linear-gradient(135deg, #14b8a6, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
        margin-bottom: 12px;
    }
    
    .feature-card {
        background: rgba(20, 184, 166, 0.05);
        border: 2px solid rgba(20, 184, 166, 0.2);
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        transition: all 0.4s;
    }
    
    .feature-card:hover {
        background: rgba(20, 184, 166, 0.15);
        border-color: rgba(20, 184, 166, 0.6);
        transform: scale(1.05) translateY(-4px);
        box-shadow: 0 20px 40px rgba(20, 184, 166, 0.3);
    }
    
    .metric-card {
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid rgba(20, 184, 166, 0.2);
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        backdrop-filter: blur(10px);
    }
</style>
""", unsafe_allow_html=True)

# ==================== HEADER SECTION ====================
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div class="header-section">
        <h1>🤖 ADE Platform</h1>
        <p style="font-size: 1.1rem; color: #cbd5e1; margin: 12px 0;">Autonomous Data Engineering with AI</p>
        <p style="font-size: 0.9rem; color: #94a3b8;">Transform your data pipelines with intelligent automation</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ==================== QUICK STATS ====================
st.markdown("### 📊 Platform Overview")
col1, col2, col3, col4, col5 = st.columns(5)

stats = [
    ("Total Pipelines", "24", "↑ 8"),
    ("Running", "5", "Active"),
    ("Success Rate", "99.2%", "↑ 0.5%"),
    ("Data Processed", "2.4TB", "Today"),
    ("Issues Found", "3", "Minor")
]

for col, (label, value, trend) in zip([col1, col2, col3, col4, col5], stats):
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <p style="color: #94a3b8; margin: 0; font-size: 0.85rem;">{label}</p>
            <h3 style="color: #14b8a6; margin: 8px 0;">{value}</h3>
            <p style="color: #10b981; margin: 0; font-size: 0.8rem;">{trend}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# ==================== CORE FEATURES ====================
st.markdown("### ✨ Core Features")
col1, col2, col3, col4 = st.columns(4)

features = [
    {"icon": "📊", "title": "Data Ingestion", "desc": "Smart data loading from multiple sources"},
    {"icon": "🔄", "title": "ETL Pipeline", "desc": "Automated workflows & transformations"},
    {"icon": "✅", "title": "Quality Check", "desc": "Advanced data validation & rules"},
    {"icon": "📈", "title": "Analytics", "desc": "Real-time insights & reporting"}
]

for idx, (col, feature) in enumerate(zip([col1, col2, col3, col4], features)):
    with col:
        st.markdown(f"""
        <div class="feature-card">
            <div style="font-size: 2.5rem; margin-bottom: 12px;">{feature['icon']}</div>
            <b style="color: #f1f5f9;">{feature['title']}</b>
            <p style="font-size: 0.85rem; color: #94a3b8;">{feature['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# ==================== TABBED INTERFACE ====================
tab1, tab2, tab3, tab4 = st.tabs(["📁 Upload Data", "🚀 Quick Start", "📚 Documentation", "🔗 Integration"])

# TAB 1: UPLOAD DATA
with tab1:
    st.markdown("### 📂 Upload & Process Your Data")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="glass-card">
            <h4 style="color: #14b8a6; margin-top: 0;">📁 File Upload</h4>
            <p style="color: #cbd5e1;">Upload your CSV, Excel, or Parquet files for processing</p>
        </div>
        """, unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(
            "Drop your file here",
            type=["csv", "xlsx", "parquet"],
            label_visibility="collapsed"
        )
        
        if uploaded_file:
            col_a, col_b, col_c = st.columns([1, 2, 1])
            with col_b:
                with st.spinner("🔄 Processing your data..."):
                    time.sleep(0.5)
                    st.markdown("""
                    <div class="glass-card" style="background: rgba(16, 185, 129, 0.1); border-color: rgba(16, 185, 129, 0.4);">
                        <div style="text-align: center; color: #10b981;">
                            <h3>✅ Success!</h3>
                            <p>File uploaded and ready for analysis</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            
            try:
                df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.DataFrame()
                
                if not df.empty:
                    # File Stats
                    st.markdown("#### 📊 File Statistics")
                    col_i, col_j, col_k = st.columns(3)
                    
                    with col_i:
                        st.markdown(f"""
                        <div class="metric-card">
                            <h4 style="color: #14b8a6; margin: 0;">{len(df)}</h4>
                            <p style="color: #94a3b8; margin: 0;">Rows</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col_j:
                        st.markdown(f"""
                        <div class="metric-card">
                            <h4 style="color: #06b6d4; margin: 0;">{len(df.columns)}</h4>
                            <p style="color: #94a3b8; margin: 0;">Columns</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col_k:
                        size_kb = uploaded_file.size / 1024
                        st.markdown(f"""
                        <div class="metric-card">
                            <h4 style="color: #8b5cf6; margin: 0;">{size_kb:.1f} KB</h4>
                            <p style="color: #94a3b8; margin: 0;">Size</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Data Preview
                    st.markdown("#### 📋 Data Preview")
                    st.dataframe(df.head(10), use_container_width=True)
                    
                    # Column Analysis
                    st.markdown("#### 🔍 Column Analysis")
                    col_x, col_y = st.columns(2)
                    
                    with col_x:
                        st.markdown("<b style='color: #14b8a6;'>Data Types</b>", unsafe_allow_html=True)
                        st.write(df.dtypes)
                    
                    with col_y:
                        st.markdown("<b style='color: #06b6d4;'>Missing Values</b>", unsafe_allow_html=True)
                        missing = df.isnull().sum()
                        st.write(missing)
                    
            except Exception as e:
                st.error(f"Error reading file: {str(e)}")
    
    with col2:
        st.markdown("""
        <div class="glass-card">
            <h4 style="color: #14b8a6;">✨ Supported Formats</h4>
            <ul style="color: #cbd5e1;">
                <li>CSV Import</li>
                <li>Excel (.xlsx)</li>
                <li>Parquet</li>
                <li>Auto Validation</li>
                <li>Schema Detection</li>
            </ul>
        </div>
        
        <div class="glass-card">
            <h4 style="color: #06b6d4;">⚙️ Processing Options</h4>
            <ul style="color: #cbd5e1;">
                <li>Data Cleaning</li>
                <li>Format Conversion</li>
                <li>Sampling</li>
                <li>Compression</li>
                <li>Encryption</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# TAB 2: QUICK START
with tab2:
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #14b8a6; margin-top: 0;">🚀 Getting Started Guide</h3>
        
        <h4 style="color: #06b6d4;">Step 1: Prepare Your Data</h4>
        <p style="color: #cbd5e1;">Ensure your data is in CSV, Excel, or Parquet format with proper headers</p>
        
        <h4 style="color: #06b6d4;">Step 2: Upload File</h4>
        <p style="color: #cbd5e1;">Use the file upload section in the Upload Data tab to select your data file</p>
        
        <h4 style="color: #06b6d4;">Step 3: Configure Pipeline</h4>
        <p style="color: #cbd5e1;">Navigate to ETL Manager to set up extraction, transformation, and loading rules</p>
        
        <h4 style="color: #06b6d4;">Step 4: Monitor & Validate</h4>
        <p style="color: #cbd5e1;">Track pipeline progress in Dashboard and validate data quality</p>
    </div>
    """, unsafe_allow_html=True)
    
    col_tip1, col_tip2 = st.columns(2)
    
    with col_tip1:
        st.markdown("""
        <div class="glass-card">
            <h3 style="color: #8b5cf6;">💡 Pro Tips</h3>
            <p style="color: #cbd5e1;"><b>• Data Format:</b> Use consistent column names without special characters</p>
            <p style="color: #cbd5e1;"><b>• Performance:</b> Keep files under 1GB for optimal speed</p>
            <p style="color: #cbd5e1;"><b>• Encoding:</b> Use UTF-8 encoding for text data</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_tip2:
        st.markdown("""
        <div class="glass-card">
            <h3 style="color: #f59e0b;">⚡ Best Practices</h3>
            <p style="color: #cbd5e1;"><b>• Scheduling:</b> Set up automatic daily or hourly runs</p>
            <p style="color: #cbd5e1;"><b>• Notifications:</b> Enable alerts on pipeline failures</p>
            <p style="color: #cbd5e1;"><b>• Monitoring:</b> Regularly check data quality metrics</p>
        </div>
        """, unsafe_allow_html=True)

# TAB 3: DOCUMENTATION
with tab3:
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #14b8a6; margin-top: 0;">📚 Documentation & Resources</h3>
        
        <h4 style="color: #06b6d4;">📥 Data Ingestion</h4>
        <p style="color: #cbd5e1;">Supported formats: CSV, JSON, Parquet, Excel, SQL Databases, APIs, Cloud Storage (S3, GCS, Azure)</p>
        
        <h4 style="color: #06b6d4;">🔄 Transformations</h4>
        <p style="color: #cbd5e1;">SQL queries, Python scripts, built-in functions, regex, conditional logic, aggregations</p>
        
        <h4 style="color: #06b6d4;">✅ Data Quality</h4>
        <p style="color: #cbd5e1;">Schema validation, duplicate detection, null handling, type checking, range validation</p>
        
        <h4 style="color: #06b6d4;">🔌 API Reference</h4>
        <p style="color: #cbd5e1;">REST endpoints, GraphQL, webhooks, SDK documentation, Python/Node.js examples</p>
    </div>
    """, unsafe_allow_html=True)

# TAB 4: INTEGRATION & ANALYSIS
with tab4:
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #14b8a6; margin-top: 0;">🔗 Integrations & Connectors</h3>
        <p style="color: #cbd5e1;">Connect with 100+ data sources and tools</p>
    </div>
    """, unsafe_allow_html=True)
    
    integrations = [
        ("🗄️ Databases", "PostgreSQL, MySQL, MongoDB, Redis, Cassandra, Oracle"),
        ("☁️ Cloud Storage", "AWS S3, Google Cloud Storage, Azure Blob, Dropbox"),
        ("🔌 APIs", "REST, GraphQL, SOAP, Webhooks, gRPC"),
        ("🔄 Big Data", "Apache Spark, Hadoop, Hive, Presto"),
        ("📊 Analytics", "Tableau, Power BI, Looker, Qlik, Superset"),
        ("📨 Messaging", "Kafka, RabbitMQ, SQS, SNS, Pub/Sub")
    ]
    
    cols = st.columns(3)
    for idx, (title, services) in enumerate(integrations):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="glass-card">
                <h5 style="color: #06b6d4; margin-top: 0;">{title}</h5>
                <p style="color: #cbd5e1; font-size: 0.9rem; margin: 0;">{services}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Analysis & Visualization Section
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #06b6d4; margin-top: 0;">📊 Data Analysis & Insights</h3>
    </div>
    """, unsafe_allow_html=True)
    
    analysis_col1, analysis_col2 = st.columns(2)
    
    with analysis_col1:
        st.markdown("<h4 style='color: #14b8a6;'>📈 Pipeline Execution Trends</h4>", unsafe_allow_html=True)
        
        dates = pd.date_range('2024-01-01', periods=30)
        trend_data = pd.DataFrame({
            'Date': dates,
            'Executions': np.random.randint(50, 150, 30),
            'Success_Rate': np.random.uniform(95, 99.9, 30)
        })
        
        fig_trend = px.line(
            trend_data, 
            x='Date', 
            y='Executions',
            title='30-Day Pipeline Execution Count',
            markers=True
        )
        fig_trend.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(15,23,42,0)',
            plot_bgcolor='rgba(15,23,42,0)',
            font=dict(color='#cbd5e1', size=11),
            hovermode='x unified',
            height=350
        )
        st.plotly_chart(fig_trend, use_container_width=True)
    
    with analysis_col2:
        st.markdown("<h4 style='color: #14b8a6;'>🎯 Connector Usage Distribution</h4>", unsafe_allow_html=True)
        
        connector_data = pd.DataFrame({
            'Connector': ['PostgreSQL', 'S3', 'API', 'MongoDB', 'Kafka', 'Spark'],
            'Usage': [450, 380, 290, 210, 180, 140]
        })
        
        fig_pie = px.pie(
            connector_data,
            names='Connector',
            values='Usage',
            title='Connector Usage Distribution'
        )
        fig_pie.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(15,23,42,0)',
            font=dict(color='#cbd5e1', size=11),
            height=350
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    st.markdown("---")
    
    # Performance Metrics Section
    perf_col1, perf_col2, perf_col3, perf_col4 = st.columns(4)
    
    metrics_data = [
        ("Avg Latency", "245ms", "#14b8a6"),
        ("Success Rate", "99.8%", "#10b981"),
        ("Data Throughput", "1.2TB/h", "#06b6d4"),
        ("Connection Uptime", "99.95%", "#8b5cf6")
    ]
    
    for col, (label, value, color) in zip([perf_col1, perf_col2, perf_col3, perf_col4], metrics_data):
        with col:
            st.markdown(f"""
            <div class="glass-card" style="text-align: center; border-top: 3px solid {color};">
                <p style="color: #94a3b8; margin: 0; font-size: 0.9rem;">{label}</p>
                <h3 style="color: {color}; margin: 8px 0;">{value}</h3>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Error Analysis Section
    st.markdown("<h4 style='color: #14b8a6;'>⚠️ Error Analytics</h4>", unsafe_allow_html=True)
    
    error_col1, error_col2 = st.columns(2)
    
    with error_col1:
        error_data = pd.DataFrame({
            'Error_Type': ['Connection Timeout', 'Invalid Data', 'Authentication', 'Rate Limit', 'Server Error'],
            'Count': [45, 32, 18, 12, 8]
        })
        
        fig_error = px.bar(
            error_data,
            x='Error_Type',
            y='Count',
            title='Error Distribution (Last 24h)',
            color='Count',
            color_continuous_scale='Reds'
        )
        fig_error.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(15,23,42,0)',
            plot_bgcolor='rgba(15,23,42,0)',
            font=dict(color='#cbd5e1', size=11),
            showlegend=False,
            height=350,
            xaxis_tickangle=-45
        )
        st.plotly_chart(fig_error, use_container_width=True)
    
    with error_col2:
        status_data = pd.DataFrame({
            'Status': ['Operational', 'Degraded', 'Alert', 'Error'],
            'Services': [156, 23, 8, 2]
        })
        
        color_map = {
            'Operational': '#10b981',
            'Degraded': '#f59e0b',
            'Alert': '#f97316',
            'Error': '#ef4444'
        }
        
        fig_status = go.Figure(data=[go.Pie(
            labels=status_data['Status'],
            values=status_data['Services'],
            marker=dict(colors=[color_map[s] for s in status_data['Status']]),
            hole=0.4,
            title='System Status Overview'
        )])
        fig_status.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(15,23,42,0)',
            font=dict(color='#cbd5e1', size=11),
            height=350
        )
        st.plotly_chart(fig_status, use_container_width=True)

st.markdown("---")

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("""
    <div class="glass-card" style="text-align: center;">
        <h3 style="color: #14b8a6; margin-top: 0;">⚙️ Control Panel</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Quick Actions")
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🆕 New Pipeline"):
            st.success("✓ Opening pipeline builder...")
    with col_b:
        if st.button("📊 View Reports"):
            st.info("📊 Loading reports...")
    
    st.markdown("---")
    st.markdown("### 📋 Configuration")
    
    mode = st.radio("Processing Mode", ["Auto", "Manual", "Streaming"], label_visibility="collapsed")
    schedule = st.selectbox("Schedule", ["Hourly", "Daily", "Weekly", "Monthly"], label_visibility="collapsed")
    
    st.markdown("---")
    st.markdown("### 📈 System Statistics")
    
    col_stat1, col_stat2 = st.columns(2)
    with col_stat1:
        st.metric("Active Jobs", "5", "↑ 2")
    with col_stat2:
        st.metric("System Load", "42%", "↓ 5%")
    
    col_stat3, col_stat4 = st.columns(2)
    with col_stat3:
        st.metric("Memory Used", "2.1GB", "Stable")
    with col_stat4:
        st.metric("Uptime", "99.8%", "↑ 0.1%")
    
    st.markdown("---")
    st.markdown("### 📡 Connection Status")
    
    st.markdown("""
    <div class="glass-card" style="padding: 12px; text-align: center;">
        <p style="color: #10b981; margin: 0;">🟢 Connected</p>
        <p style="color: #94a3b8; font-size: 0.85rem;">All systems operational</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown(f"""
    <div style="text-align: center; color: #94a3b8; font-size: 0.85rem;">
        <p style="margin: 0;">ADE Platform v1.0.0</p>
        <p style="margin: 0;">Last sync: {datetime.now().strftime("%H:%M:%S")}</p>
        <p style="margin: 0; font-size: 0.75rem;">Status: 🟢 Healthy</p>
    </div>
    """, unsafe_allow_html=True)

# ==================== FOOTER ====================
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #94a3b8; padding: 24px;">
    <p style="margin: 4px; font-size: 1rem;"><b>🚀 Autonomous Data Engineer Agent Platform</b></p>
    <p style="margin: 4px; font-size: 0.9rem;">Powered by Streamlit, Python & AI</p>
    <p style="margin: 4px; font-size: 0.85rem;">© 2024 - Advanced Data Engineering Solutions</p>
    <p style="margin: 8px 0 0 0; font-size: 0.8rem;">Version 1.0.0 | Last Updated: {datetime.now().strftime("%B %d, %Y")}</p>
</div>
""", unsafe_allow_html=True)
