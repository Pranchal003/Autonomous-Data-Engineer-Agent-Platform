import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Dashboard - ADE Platform",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
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
        background: linear-gradient(135deg, rgba(20, 184, 166, 0.1), rgba(13, 148, 136, 0.05));
        border: 1px solid rgba(20, 184, 166, 0.3);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #14b8a6;'>📊 Real-Time Dashboard</h1>", unsafe_allow_html=True)

# Sample data
date_range = pd.date_range(start=datetime.now() - timedelta(days=30), periods=30)
df_sales = pd.DataFrame({
    'date': date_range,
    'sales': [1000 + i * 50 + (i % 7) * 200 for i in range(30)],
    'customers': [50 + i * 2 + (i % 5) * 15 for i in range(30)],
    'conversion': [2.5 + (i % 10) * 0.3 for i in range(30)]
})

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""
    <div class="metric-box">
        <h3 style="color: #14b8a6; margin: 0;">$45,234</h3>
        <p style="color: #94a3b8; margin: 0;">Total Revenue</p>
        <p style="color: #10b981; margin: 0; font-size: 0.85rem;">↑ 12.5%</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-box">
        <h3 style="color: #06b6d4; margin: 0;">1,234</h3>
        <p style="color: #94a3b8; margin: 0;">Active Users</p>
        <p style="color: #10b981; margin: 0; font-size: 0.85rem;">↑ 8.2%</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-box">
        <h3 style="color: #8b5cf6; margin: 0;">94.2%</h3>
        <p style="color: #94a3b8; margin: 0;">Data Quality</p>
        <p style="color: #10b981; margin: 0; font-size: 0.85rem;">✓ Excellent</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-box">
        <h3 style="color: #f59e0b; margin: 0;">847ms</h3>
        <p style="color: #94a3b8; margin: 0;">Avg Response</p>
        <p style="color: #10b981; margin: 0; font-size: 0.85rem;">↓ 2.1%</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3 style='color: #14b8a6;'>📈 Sales Trend</h3>", unsafe_allow_html=True)
    fig_sales = px.line(df_sales, x='date', y='sales', 
                        color_discrete_sequence=['#14b8a6'],
                        template='plotly_dark')
    fig_sales.update_layout(
        hovermode='x unified',
        paper_bgcolor='rgba(15,23,42,0)',
        plot_bgcolor='rgba(30,41,59,0.3)',
        height=400,
        font=dict(color='#cbd5e1'),
        margin=dict(l=0, r=0, t=0, b=0)
    )
    st.plotly_chart(fig_sales, use_container_width=True, config={'displayModeBar': False})

with col2:
    st.markdown("<h3 style='color: #14b8a6;'>👥 Customer Growth</h3>", unsafe_allow_html=True)
    fig_customers = px.bar(df_sales, x='date', y='customers',
                           color_discrete_sequence=['#06b6d4'],
                           template='plotly_dark')
    fig_customers.update_layout(
        hovermode='x unified',
        paper_bgcolor='rgba(15,23,42,0)',
        plot_bgcolor='rgba(30,41,59,0.3)',
        height=400,
        font=dict(color='#cbd5e1'),
        margin=dict(l=0, r=0, t=0, b=0)
    )
    st.plotly_chart(fig_customers, use_container_width=True, config={'displayModeBar': False})

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3 style='color: #14b8a6;'>📊 Distribution</h3>", unsafe_allow_html=True)
    fig_pie = px.pie(values=[40, 35, 25], labels=['Category A', 'Category B', 'Category C'],
                     color_discrete_sequence=['#14b8a6', '#06b6d4', '#8b5cf6'],
                     template='plotly_dark')
    fig_pie.update_layout(
        paper_bgcolor='rgba(15,23,42,0)',
        font=dict(color='#cbd5e1'),
        height=400,
        margin=dict(l=0, r=0, t=0, b=0)
    )
    st.plotly_chart(fig_pie, use_container_width=True, config={'displayModeBar': False})

with col2:
    st.markdown("<h3 style='color: #14b8a6;'>⏱️ Performance</h3>", unsafe_allow_html=True)
    fig_gauge = go.Figure(data=[go.Indicator(
        mode="gauge+number+delta",
        value=94.2,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Quality Score"},
        delta={'reference': 90},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#14b8a6"},
            'steps': [
                {'range': [0, 50], 'color': "rgba(239, 68, 68, 0.1)"},
                {'range': [50, 80], 'color': "rgba(251, 146, 60, 0.1)"},
                {'range': [80, 100], 'color': "rgba(16, 185, 129, 0.1)"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    )])
    fig_gauge.update_layout(
        paper_bgcolor='rgba(15,23,42,0)',
        font=dict(color='#cbd5e1'),
        height=400,
        margin=dict(l=0, r=0, t=40, b=0)
    )
    st.plotly_chart(fig_gauge, use_container_width=True, config={'displayModeBar': False})

st.markdown("---")

st.markdown(f"""
<div class="glass-card" style="text-align: center; color: #94a3b8;">
    <p style="margin: 0;">Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
</div>
""", unsafe_allow_html=True)
