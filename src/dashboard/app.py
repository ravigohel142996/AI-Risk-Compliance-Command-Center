"""
AI Risk & Compliance Command Center - Main Streamlit Application
Designed for Banks, SaaS, FinTech, and AI Companies
"""
import sys
from pathlib import Path

# Add project root to Python path to fix import issues
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

from src.utils.config import APP_NAME, APP_VERSION
from src.utils.logger import app_logger
from src.utils.helpers import generate_sample_data, get_risk_level
from src.models.risk_model import RiskAssessmentModel
from src.data.loader import DataLoader


# Page configuration
st.set_page_config(
    page_title=APP_NAME,
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize logger
logger = app_logger
logger.info("Starting AI Risk & Compliance Command Center")


def initialize_session_state():
    """Initialize session state variables"""
    if "data" not in st.session_state:
        st.session_state.data = generate_sample_data(100)
    if "model" not in st.session_state:
        st.session_state.model = RiskAssessmentModel()
    if "data_loader" not in st.session_state:
        st.session_state.data_loader = DataLoader()


def render_header():
    """Render application header"""
    col1, col2 = st.columns([4, 1])
    with col1:
        st.title(f"🛡️ {APP_NAME}")
        st.markdown("*Used by Banks, SaaS, FinTech, and AI Companies*")
    with col2:
        st.metric("Version", APP_VERSION)
        st.metric("Status", "🟢 Online")


def render_metrics(df: pd.DataFrame):
    """Render key metrics"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Total Entities",
            len(df),
            delta=f"+{len(df) // 10} this month"
        )
    
    with col2:
        critical_count = len(df[df["risk_level"] == "Critical"])
        st.metric(
            "Critical Risks",
            critical_count,
            delta=f"{critical_count - 2} from last month",
            delta_color="inverse"
        )
    
    with col3:
        avg_compliance = df["compliance_score"].mean()
        st.metric(
            "Avg Compliance Score",
            f"{avg_compliance:.2%}",
            delta=f"+{3.5}%"
        )
    
    with col4:
        total_incidents = df["incident_count"].sum()
        st.metric(
            "Total Incidents",
            total_incidents,
            delta=f"-{5} from last week",
            delta_color="off"
        )


def render_risk_distribution(df: pd.DataFrame):
    """Render risk distribution chart"""
    st.subheader("📊 Risk Distribution")
    
    risk_counts = df["risk_level"].value_counts()
    
    fig = px.pie(
        values=risk_counts.values,
        names=risk_counts.index,
        title="Distribution by Risk Level",
        color=risk_counts.index,
        color_discrete_map={
            "Critical": "#FF0000",
            "High": "#FF6B6B",
            "Medium": "#FFA500",
            "Low": "#FFD700",
            "Minimal": "#90EE90"
        }
    )
    
    st.plotly_chart(fig, use_container_width=True)


def render_risk_timeline(df: pd.DataFrame):
    """Render risk score timeline"""
    st.subheader("📈 Risk Score Timeline")
    
    # Sort by date
    df_sorted = df.sort_values("last_audit_date")
    
    fig = px.line(
        df_sorted,
        x="last_audit_date",
        y="risk_score",
        title="Risk Score Over Time",
        labels={"last_audit_date": "Date", "risk_score": "Risk Score"}
    )
    
    # Add threshold lines
    fig.add_hline(y=0.95, line_dash="dash", line_color="red", annotation_text="Critical")
    fig.add_hline(y=0.8, line_dash="dash", line_color="orange", annotation_text="High")
    fig.add_hline(y=0.6, line_dash="dash", line_color="yellow", annotation_text="Medium")
    
    st.plotly_chart(fig, use_container_width=True)


def render_compliance_heatmap(df: pd.DataFrame):
    """Render compliance heatmap"""
    st.subheader("🔥 Compliance Heatmap")
    
    # Create pivot for heatmap (simplified version)
    pivot_data = df.head(20)[["entity_id", "compliance_score"]].set_index("entity_id")
    
    fig = px.imshow(
        [pivot_data["compliance_score"].values],
        labels=dict(x="Entity ID", y="Metric", color="Score"),
        x=pivot_data.index,
        y=["Compliance Score"],
        color_continuous_scale="RdYlGn",
        aspect="auto"
    )
    
    st.plotly_chart(fig, use_container_width=True)


def render_data_table(df: pd.DataFrame):
    """Render data table with filters"""
    st.subheader("📋 Risk Assessment Data")
    
    # Filters
    col1, col2 = st.columns(2)
    with col1:
        risk_filter = st.multiselect(
            "Filter by Risk Level",
            options=df["risk_level"].unique(),
            default=df["risk_level"].unique()
        )
    
    with col2:
        min_incidents = st.slider(
            "Minimum Incident Count",
            min_value=0,
            max_value=int(df["incident_count"].max()),
            value=0
        )
    
    # Apply filters
    filtered_df = df[
        (df["risk_level"].isin(risk_filter)) &
        (df["incident_count"] >= min_incidents)
    ]
    
    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )
    
    # Export button
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name=f"risk_assessment_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv"
    )


def render_sidebar():
    """Render sidebar with controls"""
    st.sidebar.header("⚙️ Controls")
    
    # Refresh data button
    if st.sidebar.button("🔄 Refresh Data"):
        st.session_state.data = generate_sample_data(100)
        st.rerun()
    
    st.sidebar.divider()
    
    # Data upload
    st.sidebar.subheader("📤 Upload Data")
    uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.session_state.data = df
            st.sidebar.success("Data uploaded successfully!")
            logger.info(f"User uploaded data: {len(df)} records")
        except Exception as e:
            st.sidebar.error(f"Error uploading file: {str(e)}")
            logger.error(f"Upload error: {str(e)}")
    
    st.sidebar.divider()
    
    # Settings
    st.sidebar.subheader("⚙️ Settings")
    st.sidebar.slider("Alert Threshold", 0.0, 1.0, 0.8)
    st.sidebar.checkbox("Enable Auto-refresh", value=False)
    st.sidebar.checkbox("Show Detailed Logs", value=False)
    
    st.sidebar.divider()
    
    # Health check info
    st.sidebar.subheader("💚 System Health")
    st.sidebar.success("All systems operational")
    st.sidebar.info(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def main():
    """Main application logic"""
    try:
        # Initialize
        initialize_session_state()
        
        # Render components
        render_header()
        st.divider()
        
        render_metrics(st.session_state.data)
        st.divider()
        
        # Layout for charts
        col1, col2 = st.columns(2)
        with col1:
            render_risk_distribution(st.session_state.data)
        with col2:
            render_risk_timeline(st.session_state.data)
        
        st.divider()
        render_compliance_heatmap(st.session_state.data)
        
        st.divider()
        render_data_table(st.session_state.data)
        
        # Sidebar
        render_sidebar()
        
        logger.info("Application rendered successfully")
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        logger.error(f"Application error: {str(e)}", exc_info=True)


if __name__ == "__main__":
    main()
