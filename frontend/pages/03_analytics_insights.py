import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Analytics & Insights - ADE Platform",
    page_icon="📊",
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
    
    .metric-box {
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid rgba(20, 184, 166, 0.2);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #14b8a6;'>📊 Analytics & Insights Dashboard</h1>", unsafe_allow_html=True)

# KPI Section
col1, col2, col3, col4 = st.columns(4)

metrics = [
    ("Total Pipelines", "142", "↑ 12%", "#14b8a6"),
    ("Data Processed", "5.2TB", "↑ 8.5%", "#06b6d4"),
    ("Success Rate", "99.8%", "↑ 0.2%", "#10b981"),
    ("Avg Response", "342ms", "↓ 15%", "#8b5cf6")
]

for col, (label, value, trend, color) in zip([col1, col2, col3, col4], metrics):
    with col:
        st.markdown(f"""
        <div class="metric-box" style="border-top: 3px solid {color};">
            <p style="color: #94a3b8; margin: 0; font-size: 0.9rem;">{label}</p>
            <h2 style="color: {color}; margin: 8px 0;">{value}</h2>
            <p style="color: #10b981; margin: 0; font-size: 0.85rem;">{trend}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Time Series Analysis
st.markdown("<h3 style='color: #14b8a6;'>📈 Time Series Analysis</h3>", unsafe_allow_html=True)

dates = pd.date_range(end=datetime.now(), periods=60)
ts_data = pd.DataFrame({
    'Date': dates,
    'Throughput_MB': np.cumsum(np.random.randint(10, 50, 60)) + 500,
    'Latency_ms': 100 + np.random.normal(0, 20, 60),
    'Error_Count': np.random.poisson(2, 60)
})

fig_ts = go.Figure()
fig_ts.add_trace(go.Scatter(
    x=ts_data['Date'],
    y=ts_data['Throughput_MB'],
    name='Data Throughput (MB)',
    yaxis='y1',
    line=dict(color='#14b8a6', width=3),
    fill='tozeroy'
))
fig_ts.add_trace(go.Scatter(
    x=ts_data['Date'],
    y=ts_data['Latency_ms'],
    name='Latency (ms)',
    yaxis='y2',
    line=dict(color='#06b6d4', width=2)
))

fig_ts.update_layout(
    title='System Performance Over 60 Days',
    xaxis=dict(title='Date'),
    yaxis=dict(title='Throughput (MB)', titlefont=dict(color='#14b8a6'), tickfont=dict(color='#14b8a6')),
    yaxis2=dict(title='Latency (ms)', titlefont=dict(color='#06b6d4'), tickfont=dict(color='#06b6d4'), overlaying='y', side='right'),
    template='plotly_dark',
    paper_bgcolor='rgba(15,23,42,0)',
    plot_bgcolor='rgba(15,23,42,0)',
    font=dict(color='#cbd5e1', size=11),
    hovermode='x unified',
    height=400
)

st.plotly_chart(fig_ts, use_container_width=True)

st.markdown("---")

# Multi-Dimensional Analysis
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("<h4 style='color: #14b8a6;'>🔄 Pipeline Status Distribution</h4>", unsafe_allow_html=True)
    
    status_data = pd.DataFrame({
        'Status': ['Completed', 'Running', 'Queued', 'Failed', 'Paused'],
        'Count': [95, 23, 12, 5, 7]
    })
    
    colors_map = {'Completed': '#10b981', 'Running': '#f59e0b', 'Queued': '#06b6d4', 'Failed': '#ef4444', 'Paused': '#94a3b8'}
    fig_status = px.bar(
        status_data,
        x='Status',
        y='Count',
        color='Status',
        color_discrete_map=colors_map,
        title='Pipeline Execution Status'
    )
    fig_status.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(15,23,42,0)',
        plot_bgcolor='rgba(15,23,42,0)',
        font=dict(color='#cbd5e1', size=11),
        showlegend=False,
        height=350
    )
    st.plotly_chart(fig_status, use_container_width=True)

with col_b:
    st.markdown("<h4 style='color: #14b8a6;'>⏱️ Execution Duration Distribution</h4>", unsafe_allow_html=True)
    
    duration_data = pd.DataFrame({
        'Duration_Min': np.random.uniform(1, 120, 500)
    })
    
    fig_hist = px.histogram(
        duration_data,
        x='Duration_Min',
        nbins=30,
        title='Pipeline Execution Duration',
        labels={'Duration_Min': 'Duration (minutes)', 'count': 'Frequency'}
    )
    fig_hist.update_traces(marker_color='#06b6d4')
    fig_hist.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(15,23,42,0)',
        plot_bgcolor='rgba(15,23,42,0)',
        font=dict(color='#cbd5e1', size=11),
        height=350
    )
    st.plotly_chart(fig_hist, use_container_width=True)

st.markdown("---")

# Data Source Analysis
col_c, col_d = st.columns(2)

with col_c:
    st.markdown("<h4 style='color: #14b8a6;'>📊 Data Source Contribution</h4>", unsafe_allow_html=True)
    
    source_data = pd.DataFrame({
        'Source': ['PostgreSQL', 'AWS S3', 'API Endpoints', 'MongoDB', 'Kafka Topics', 'CSV Files'],
        'Records_Processed': [1250000, 980000, 450000, 680000, 320000, 200000]
    })
    
    fig_source = px.pie(
        source_data,
        names='Source',
        values='Records_Processed',
        title='Data Source Contribution'
    )
    fig_source.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(15,23,42,0)',
        font=dict(color='#cbd5e1', size=11),
        height=350
    )
    st.plotly_chart(fig_source, use_container_width=True)

with col_d:
    st.markdown("<h4 style='color: #14b8a6;'>🎯 Connector Performance</h4>", unsafe_allow_html=True)
    
    connector_perf = pd.DataFrame({
        'Connector': ['PostgreSQL', 'S3', 'API', 'MongoDB', 'Kafka', 'Spark'],
        'Latency_ms': [45, 120, 280, 35, 15, 450],
        'Throughput_Mbps': [850, 1200, 420, 680, 950, 2100]
    })
    
    fig_connector = px.scatter(
        connector_perf,
        x='Latency_ms',
        y='Throughput_Mbps',
        size='Throughput_Mbps',
        color='Connector',
        hover_name='Connector',
        title='Connector Performance Matrix',
        labels={'Latency_ms': 'Latency (ms)', 'Throughput_Mbps': 'Throughput (Mbps)'}
    )
    fig_connector.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(15,23,42,0)',
        plot_bgcolor='rgba(15,23,42,0)',
        font=dict(color='#cbd5e1', size=11),
        height=350
    )
    st.plotly_chart(fig_connector, use_container_width=True)

st.markdown("---")

# Error Analysis & Trends
st.markdown("<h3 style='color: #14b8a6;'>⚠️ Error Analytics</h3>", unsafe_allow_html=True)

col_e, col_f = st.columns(2)

with col_e:
    error_trend = pd.DataFrame({
        'Date': pd.date_range(end=datetime.now(), periods=30),
        'Error_Count': np.random.poisson(5, 30) + np.arange(30) * 0.1
    })
    
    fig_error_trend = px.line(
        error_trend,
        x='Date',
        y='Error_Count',
        title='Error Trend (30 Days)',
        markers=True
    )
    fig_error_trend.update_traces(line_color='#ef4444', marker_size=8)
    fig_error_trend.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(15,23,42,0)',
        plot_bgcolor='rgba(15,23,42,0)',
        font=dict(color='#cbd5e1', size=11),
        height=350
    )
    st.plotly_chart(fig_error_trend, use_container_width=True)

with col_f:
    error_types = pd.DataFrame({
        'Error_Type': ['Timeout', 'Connection', 'Validation', 'Auth', 'Rate Limit', 'Memory'],
        'Occurrences': [45, 32, 28, 15, 12, 8]
    })
    
    fig_error_type = px.bar(
        error_types,
        x='Occurrences',
        y='Error_Type',
        orientation='h',
        color='Occurrences',
        color_continuous_scale='Reds',
        title='Error Types (Last 24h)'
    )
    fig_error_type.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(15,23,42,0)',
        plot_bgcolor='rgba(15,23,42,0)',
        font=dict(color='#cbd5e1', size=11),
        showlegend=False,
        height=350
    )
    st.plotly_chart(fig_error_type, use_container_width=True)

st.markdown("---")

# Data Quality Metrics
st.markdown("<h3 style='color: #14b8a6;'>✅ Data Quality Metrics</h3>", unsafe_allow_html=True)

dq_col1, dq_col2, dq_col3, dq_col4 = st.columns(4)

dq_metrics = [
    ("Completeness", "97.3%", "#14b8a6"),
    ("Uniqueness", "98.9%", "#06b6d4"),
    ("Accuracy", "99.1%", "#10b981"),
    ("Consistency", "96.7%", "#8b5cf6")
]

for col, (metric, value, color) in zip([dq_col1, dq_col2, dq_col3, dq_col4], dq_metrics):
    with col:
        st.markdown(f"""
        <div class="metric-box" style="border-left: 4px solid {color};">
            <p style="color: #94a3b8; margin: 0; font-size: 0.9rem;">{metric}</p>
            <h3 style="color: {color}; margin: 8px 0;">{value}</h3>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Advanced Heatmap
st.markdown("<h4 style='color: #14b8a6;'>🔥 Hourly Activity Heatmap</h4>", unsafe_allow_html=True)

heatmap_data = np.random.randint(10, 100, (24, 7))
heatmap_df = pd.DataFrame(
    heatmap_data,
    index=[f"{h:02d}:00" for h in range(24)],
    columns=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
)

fig_heatmap = px.imshow(
    heatmap_df,
    title='Pipeline Activity Heatmap (Executions by Hour)',
    labels=dict(x='Day of Week', y='Hour of Day', color='Executions'),
    color_continuous_scale='Turbo',
    aspect='auto'
)
fig_heatmap.update_layout(
    template='plotly_dark',
    paper_bgcolor='rgba(15,23,42,0)',
    font=dict(color='#cbd5e1', size=11),
    height=400
)
st.plotly_chart(fig_heatmap, use_container_width=True)
