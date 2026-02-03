"""
UI Components - Reusable widgets for the dashboard
"""
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import config

def load_css():
    """Load custom CSS"""
    with open('ui/theme.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def render_header(title: str, subtitle: str = ""):
    """Render page header with gradient styling"""
    st.markdown(f"""
        <div class="main-header">
            <h1 style="margin:0; color: white;">{config.APP_ICON} {title}</h1>
            {f'<p style="margin:0.5rem 0 0 0; color: rgba(255,255,255,0.8);">{subtitle}</p>' if subtitle else ''}
        </div>
    """, unsafe_allow_html=True)

def render_kpi_card(label: str, value: str, delta: str = None, delta_color: str = "normal"):
    """Render a KPI card with glassmorphism effect"""
    delta_html = ""
    if delta:
        color = "#4CAF50" if delta_color == "normal" else "#F44336" if delta_color == "inverse" else "#FFC107"
        delta_html = f'<div style="color: {color}; font-size: 0.9rem; margin-top: 0.5rem;">{delta}</div>'
    
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
            {delta_html}
        </div>
    """, unsafe_allow_html=True)

def render_status_badge(status: str, text: str = None):
    """Render status badge with animation"""
    display_text = text or status.upper()
    st.markdown(f"""
        <span class="status-badge status-{status}">{display_text}</span>
    """, unsafe_allow_html=True)

def render_metric_row(metrics: list):
    """Render a row of metrics using Streamlit columns"""
    cols = st.columns(len(metrics))
    for col, metric in zip(cols, metrics):
        with col:
            if 'delta' in metric:
                st.metric(
                    label=metric['label'],
                    value=metric['value'],
                    delta=metric.get('delta'),
                    delta_color=metric.get('delta_color', 'normal')
                )
            else:
                render_kpi_card(
                    label=metric['label'],
                    value=str(metric['value']),
                    delta=metric.get('delta'),
                    delta_color=metric.get('delta_color', 'normal')
                )

def create_trend_chart(df, x_col, y_col, title, color='#1E88E5'):
    """Create a trend line chart"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df[x_col],
        y=df[y_col],
        mode='lines+markers',
        line=dict(color=color, width=3),
        marker=dict(size=8, color=color),
        fill='tonexty',
        fillcolor=f'rgba(30, 136, 229, 0.2)'
    ))
    
    fig.update_layout(
        title=title,
        template='plotly_dark',
        paper_bgcolor='rgba(26, 31, 46, 0.5)',
        plot_bgcolor='rgba(26, 31, 46, 0.5)',
        font=dict(color='#B0BEC5'),
        hovermode='x unified',
        showlegend=False,
        margin=dict(l=40, r=40, t=60, b=40)
    )
    
    return fig

def create_bar_chart(categories, values, title, color='#1E88E5'):
    """Create a bar chart"""
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=categories,
        y=values,
        marker=dict(
            color=color,
            line=dict(color='rgba(255,255,255,0.2)', width=1)
        )
    ))
    
    fig.update_layout(
        title=title,
        template='plotly_dark',
        paper_bgcolor='rgba(26, 31, 46, 0.5)',
        plot_bgcolor='rgba(26, 31, 46, 0.5)',
        font=dict(color='#B0BEC5'),
        margin=dict(l=40, r=40, t=60, b=40)
    )
    
    return fig

def create_heatmap(df, x_col, y_col, value_col, title):
    """Create a heatmap"""
    pivot_df = df.pivot(index=y_col, columns=x_col, values=value_col)
    
    fig = go.Figure(data=go.Heatmap(
        z=pivot_df.values,
        x=pivot_df.columns,
        y=pivot_df.index,
        colorscale='RdYlGn_r',
        text=pivot_df.values,
        texttemplate='%{text:.1f}',
        textfont={"size": 10},
        colorbar=dict(title="Risk Score")
    ))
    
    fig.update_layout(
        title=title,
        template='plotly_dark',
        paper_bgcolor='rgba(26, 31, 46, 0.5)',
        plot_bgcolor='rgba(26, 31, 46, 0.5)',
        font=dict(color='#B0BEC5'),
        margin=dict(l=40, r=40, t=60, b=40)
    )
    
    return fig

def create_pie_chart(labels, values, title):
    """Create a pie chart"""
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.4,
        marker=dict(
            colors=['#F44336', '#FF9800', '#FFC107', '#4CAF50'],
            line=dict(color='rgba(255,255,255,0.2)', width=2)
        )
    )])
    
    fig.update_layout(
        title=title,
        template='plotly_dark',
        paper_bgcolor='rgba(26, 31, 46, 0.5)',
        plot_bgcolor='rgba(26, 31, 46, 0.5)',
        font=dict(color='#B0BEC5'),
        showlegend=True,
        margin=dict(l=40, r=40, t=60, b=40)
    )
    
    return fig

def create_gauge_chart(value, title, max_value=100):
    """Create a gauge chart"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title, 'font': {'size': 20, 'color': '#B0BEC5'}},
        gauge={
            'axis': {'range': [None, max_value], 'tickcolor': '#B0BEC5'},
            'bar': {'color': '#1E88E5'},
            'steps': [
                {'range': [0, 50], 'color': 'rgba(76, 175, 80, 0.3)'},
                {'range': [50, 75], 'color': 'rgba(255, 193, 7, 0.3)'},
                {'range': [75, 100], 'color': 'rgba(244, 67, 54, 0.3)'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 80
            }
        }
    ))
    
    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(26, 31, 46, 0.5)',
        font=dict(color='#B0BEC5'),
        height=300,
        margin=dict(l=40, r=40, t=60, b=40)
    )
    
    return fig

def create_radar_chart(categories, values, title):
    """Create a radar chart"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        fillcolor='rgba(30, 136, 229, 0.3)',
        line=dict(color='#1E88E5', width=2),
        marker=dict(size=8, color='#1E88E5')
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                gridcolor='rgba(255, 255, 255, 0.1)',
                tickfont=dict(color='#B0BEC5')
            ),
            angularaxis=dict(
                gridcolor='rgba(255, 255, 255, 0.1)',
                tickfont=dict(color='#B0BEC5')
            ),
            bgcolor='rgba(26, 31, 46, 0.5)'
        ),
        showlegend=False,
        title=title,
        template='plotly_dark',
        paper_bgcolor='rgba(26, 31, 46, 0.5)',
        font=dict(color='#B0BEC5'),
        margin=dict(l=80, r=80, t=60, b=40)
    )
    
    return fig

def create_multi_line_chart(df, x_col, y_cols, title, colors=None):
    """Create a multi-line chart"""
    fig = go.Figure()
    
    if colors is None:
        colors = ['#1E88E5', '#43A047', '#E91E63', '#FF9800', '#9C27B0']
    
    for i, y_col in enumerate(y_cols):
        fig.add_trace(go.Scatter(
            x=df[x_col],
            y=df[y_col],
            mode='lines+markers',
            name=y_col.replace('_', ' ').title(),
            line=dict(color=colors[i % len(colors)], width=2),
            marker=dict(size=6)
        ))
    
    fig.update_layout(
        title=title,
        template='plotly_dark',
        paper_bgcolor='rgba(26, 31, 46, 0.5)',
        plot_bgcolor='rgba(26, 31, 46, 0.5)',
        font=dict(color='#B0BEC5'),
        hovermode='x unified',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        margin=dict(l=40, r=40, t=80, b=40)
    )
    
    return fig

def render_alert_box(severity: str, title: str, message: str):
    """Render an alert box"""
    icons = {
        'critical': '🔴',
        'high': '🟠',
        'medium': '🟡',
        'low': '🟢'
    }
    
    st.markdown(f"""
        <div class="alert-box alert-{severity}">
            <strong>{icons.get(severity, '⚠️')} {title}</strong><br>
            {message}
        </div>
    """, unsafe_allow_html=True)

def render_sidebar():
    """Render sidebar navigation"""
    with st.sidebar:
        st.markdown(f"""
            <div style="text-align: center; padding: 2rem 0;">
                <h2 style="color: #1E88E5; margin: 0;">{config.APP_ICON}</h2>
                <h3 style="color: white; margin: 0.5rem 0;">AI Risk Center</h3>
                <p style="color: #B0BEC5; font-size: 0.8rem;">v{config.APP_VERSION}</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        page = st.radio(
            "Navigation",
            ["📊 Overview", "⚠️ Risk Monitor", "✅ Compliance", "💰 Cost Tracking", "🔒 Security Alerts", "📋 Audit Logs"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # System status
        st.markdown("### System Status")
        st.success("✓ All Systems Operational")
        
        # Quick stats
        st.markdown("### Quick Stats")
        st.metric("Active Monitors", "24")
        st.metric("Today's Alerts", "47")
        
        st.markdown("---")
        st.caption(f"Last updated: {datetime.now().strftime('%H:%M:%S')}")
        
        return page.split(" ", 1)[1]  # Return page name without emoji
