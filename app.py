"""
AI Risk & Compliance Command Center
Production-grade dashboard for monitoring AI systems
"""
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import custom modules
import config
from ui.components import *
from services.risk_engine import RiskEngine
from services.compliance_engine import ComplianceEngine
from services.alert_engine import AlertEngine

# Page configuration
st.set_page_config(
    page_title=config.APP_NAME,
    page_icon=config.APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
load_css()

# Initialize engines
@st.cache_resource
def get_engines():
    return {
        'risk': RiskEngine(),
        'compliance': ComplianceEngine(),
        'alert': AlertEngine()
    }

engines = get_engines()

# Render sidebar and get selected page
current_page = render_sidebar()

# ============================================================================
# OVERVIEW PAGE
# ============================================================================
if current_page == "Overview":
    render_header("AI Risk & Compliance Overview", "Real-time monitoring of AI systems in production")
    
    # Top KPIs
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        risk_metrics = engines['risk'].get_risk_metrics()
        render_kpi_card("Overall Risk", f"{risk_metrics['overall_risk']}%", "↑ 3% from last week", "inverse")
    
    with col2:
        compliance_score = engines['compliance'].get_compliance_score()
        render_kpi_card("Compliance", f"{compliance_score}%", "↑ 2% improvement", "normal")
    
    with col3:
        alert_stats = engines['alert'].get_alert_statistics()
        render_kpi_card("Active Alerts", str(alert_stats['total_alerts']), f"{alert_stats['resolved_24h']} resolved today", "normal")
    
    with col4:
        render_kpi_card("Models Monitored", str(risk_metrics['models_monitored']), "2 new this week", "normal")
    
    with col5:
        cost_metrics = engines['alert'].get_cost_metrics()
        render_kpi_card("Monthly Cost", f"${cost_metrics['monthly_projection']:,.0f}", f"{cost_metrics['cost_trend']}", "normal" if cost_metrics['cost_trend'] == 'decreasing' else "inverse")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Main dashboard area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Risk trends
        st.markdown("### 📈 Risk Trends (30 Days)")
        risk_trends = engines['risk'].generate_risk_trends(30)
        fig = create_multi_line_chart(
            risk_trends,
            'date',
            ['risk_score', 'model_risk', 'security_risk', 'compliance_risk'],
            "Risk Metrics Over Time"
        )
        st.plotly_chart(fig, use_container_width=True, config=config.CHART_CONFIG)
    
    with col2:
        # Risk breakdown
        st.markdown("### 🎯 Risk Distribution")
        risk_breakdown = engines['risk'].get_risk_breakdown()
        top_risks = sorted(risk_breakdown.items(), key=lambda x: x[1], reverse=True)[:4]
        
        fig = create_pie_chart(
            [r[0] for r in top_risks],
            [r[1] for r in top_risks],
            "Top Risk Categories"
        )
        st.plotly_chart(fig, use_container_width=True, config=config.CHART_CONFIG)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Alerts and Compliance
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🚨 Recent Critical Alerts")
        alerts = engines['alert'].get_active_alerts()[:5]
        
        for alert in alerts:
            if alert['severity'] in ['critical', 'high']:
                with st.expander(f"{config.ALERT_SEVERITY[alert['severity']]['icon']} {alert['type']} - {alert['id']}", expanded=False):
                    st.write(f"**Severity:** {alert['severity'].upper()}")
                    st.write(f"**Source:** {alert['source']}")
                    st.write(f"**Status:** {alert['status']}")
                    st.write(f"**Detected:** {alert['timestamp'].strftime('%Y-%m-%d %H:%M')}")
                    st.write(f"**Description:** {alert['description']}")
    
    with col2:
        st.markdown("### ✅ Compliance Status")
        compliance_status = engines['compliance'].get_compliance_status()
        
        for standard, status in list(compliance_status.items())[:5]:
            col_a, col_b, col_c = st.columns([2, 1, 1])
            with col_a:
                st.write(f"**{standard}**")
            with col_b:
                st.write(f"{status['score']}%")
            with col_c:
                if status['status'] == 'compliant':
                    st.success("✓ Compliant")
                else:
                    st.warning("⚠ At Risk")
    
    # Top Risks Table
    st.markdown("### 🎯 Top Risks Requiring Attention")
    top_risks = engines['risk'].get_top_risks(10)
    
    df_risks = pd.DataFrame(top_risks)
    df_risks['detected'] = df_risks['detected'].dt.strftime('%Y-%m-%d %H:%M')
    st.dataframe(
        df_risks[['id', 'category', 'score', 'level', 'detected', 'affected_models']],
        use_container_width=True,
        hide_index=True
    )

# ============================================================================
# RISK MONITOR PAGE
# ============================================================================
elif current_page == "Risk Monitor":
    render_header("Risk Monitoring Dashboard", "Real-time AI system risk analysis and scoring")
    
    # Risk metrics
    risk_metrics = engines['risk'].get_risk_metrics()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card("Overall Risk", f"{risk_metrics['overall_risk']}%")
    with col2:
        render_kpi_card("Active Risks", str(risk_metrics['active_risks']))
    with col3:
        render_kpi_card("Critical Risks", str(risk_metrics['critical_risks']))
    with col4:
        render_kpi_card("Trend", risk_metrics['risk_trend'].title())
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Risk gauge and breakdown
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### Overall Risk Score")
        fig = create_gauge_chart(risk_metrics['overall_risk'], "Current Risk Level")
        st.plotly_chart(fig, use_container_width=True, config=config.CHART_CONFIG)
    
    with col2:
        st.markdown("### Risk Factor Breakdown")
        risk_breakdown = engines['risk'].get_risk_breakdown()
        fig = create_radar_chart(
            list(risk_breakdown.keys()),
            list(risk_breakdown.values()),
            "Risk Categories"
        )
        st.plotly_chart(fig, use_container_width=True, config=config.CHART_CONFIG)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Risk heatmap
    st.markdown("### 🔥 Risk Heatmap by Model and Timeframe")
    models = ['GPT-4 API', 'Claude-3', 'Llama-2', 'Custom Model A', 'Custom Model B']
    timeframes = ['1h', '6h', '24h', '7d', '30d']
    heatmap_data = engines['risk'].get_risk_heatmap_data(models, timeframes)
    
    fig = create_heatmap(heatmap_data, 'timeframe', 'model', 'risk_score', 'Model Risk Scores')
    st.plotly_chart(fig, use_container_width=True, config=config.CHART_CONFIG)
    
    # Risk trends
    st.markdown("### 📊 Historical Risk Trends")
    risk_trends = engines['risk'].generate_risk_trends(30)
    
    fig = create_multi_line_chart(
        risk_trends,
        'date',
        ['risk_score', 'model_risk', 'data_risk', 'security_risk'],
        "30-Day Risk Trend Analysis"
    )
    st.plotly_chart(fig, use_container_width=True, config=config.CHART_CONFIG)
    
    # Anomalies
    anomalies = engines['risk'].detect_risk_anomalies(risk_trends)
    if anomalies:
        st.markdown("### ⚠️ Detected Anomalies")
        for anomaly in anomalies[:5]:
            render_alert_box(
                anomaly['severity'],
                f"Risk Anomaly Detected",
                f"{anomaly['message']} on {anomaly['date'].strftime('%Y-%m-%d')}"
            )
    
    # Top risks
    st.markdown("### 🎯 Top Risks")
    top_risks = engines['risk'].get_top_risks(15)
    df_risks = pd.DataFrame(top_risks)
    df_risks['detected'] = df_risks['detected'].dt.strftime('%Y-%m-%d %H:%M')
    st.dataframe(df_risks, use_container_width=True, hide_index=True)

# ============================================================================
# COMPLIANCE PAGE
# ============================================================================
elif current_page == "Compliance":
    render_header("Compliance Monitoring", "Track adherence to regulatory standards and policies")
    
    # Compliance metrics
    overall_score = engines['compliance'].get_compliance_score()
    audit_summary = engines['compliance'].get_audit_summary()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card("Compliance Score", f"{overall_score}%")
    with col2:
        render_kpi_card("Total Checks", str(audit_summary['total_checks']))
    with col3:
        render_kpi_card("Violations", str(audit_summary['failed']))
    with col4:
        render_kpi_card("Compliance Rate", f"{audit_summary['compliance_rate']}%")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Compliance status by standard
    st.markdown("### 📋 Compliance Status by Standard")
    compliance_status = engines['compliance'].get_compliance_status()
    
    # Create a clean table
    status_data = []
    for standard, status in compliance_status.items():
        status_data.append({
            'Standard': standard,
            'Score': f"{status['score']}%",
            'Status': status['status'].upper(),
            'Violations': status['violations'],
            'Last Audit': status['last_audit'].strftime('%Y-%m-%d')
        })
    
    df_status = pd.DataFrame(status_data)
    st.dataframe(df_status, use_container_width=True, hide_index=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Compliance trends and policy coverage
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 Compliance Trends")
        compliance_trends = engines['compliance'].get_compliance_trends(30)
        fig = create_multi_line_chart(
            compliance_trends,
            'date',
            ['overall_score', 'gdpr_score', 'soc2_score'],
            "Compliance Scores Over Time"
        )
        st.plotly_chart(fig, use_container_width=True, config=config.CHART_CONFIG)
    
    with col2:
        st.markdown("### 🎯 Policy Coverage")
        policy_coverage = engines['compliance'].get_policy_coverage()
        fig = create_bar_chart(
            list(policy_coverage.keys()),
            list(policy_coverage.values()),
            "Coverage by Category",
            color='#43A047'
        )
        st.plotly_chart(fig, use_container_width=True, config=config.CHART_CONFIG)
    
    # Violations
    st.markdown("### ⚠️ Active Violations")
    violations = engines['compliance'].detect_violations()
    
    for violation in violations[:10]:
        severity_color = {
            'critical': 'error',
            'high': 'warning',
            'medium': 'info',
            'low': 'success'
        }
        
        with st.expander(f"{config.ALERT_SEVERITY.get(violation['severity'], {}).get('icon', '⚠️')} {violation['id']} - {violation['category']}", expanded=False):
            col_a, col_b = st.columns(2)
            with col_a:
                st.write(f"**Standard:** {violation['standard']}")
                st.write(f"**Severity:** {violation['severity'].upper()}")
                st.write(f"**Status:** {violation['status']}")
            with col_b:
                st.write(f"**Detected:** {violation['detected'].strftime('%Y-%m-%d %H:%M')}")
                st.write(f"**Affected Systems:** {violation['affected_systems']}")
            st.write(f"**Description:** {violation['description']}")
    
    # Remediation timeline
    st.markdown("### 🔧 Remediation Timeline")
    timeline = engines['compliance'].get_remediation_timeline()
    df_timeline = pd.DataFrame(timeline)
    df_timeline['reported'] = pd.to_datetime(df_timeline['reported']).dt.strftime('%Y-%m-%d')
    df_timeline['deadline'] = pd.to_datetime(df_timeline['deadline']).dt.strftime('%Y-%m-%d')
    st.dataframe(df_timeline, use_container_width=True, hide_index=True)

# ============================================================================
# COST TRACKING PAGE
# ============================================================================
elif current_page == "Cost Tracking":
    render_header("Cost Tracking & Optimization", "Monitor and optimize AI infrastructure costs")
    
    # Cost metrics
    cost_metrics = engines['alert'].get_cost_metrics()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card("Current Daily Cost", f"${cost_metrics['current_cost']:,.2f}")
    with col2:
        render_kpi_card("Monthly Projection", f"${cost_metrics['monthly_projection']:,.2f}")
    with col3:
        render_kpi_card("vs Baseline", f"${abs(cost_metrics['current_cost'] - cost_metrics['baseline_cost']):,.2f}")
    with col4:
        render_kpi_card("Trend", cost_metrics['cost_trend'].title())
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Cost breakdown
    st.markdown("### 💰 Cost Breakdown by Service")
    cost_by_service = cost_metrics['cost_by_service']
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = create_pie_chart(
            list(cost_by_service.keys()),
            list(cost_by_service.values()),
            "Daily Cost Distribution"
        )
        st.plotly_chart(fig, use_container_width=True, config=config.CHART_CONFIG)
    
    with col2:
        fig = create_bar_chart(
            list(cost_by_service.keys()),
            list(cost_by_service.values()),
            "Cost by Service ($)",
            color='#43A047'
        )
        st.plotly_chart(fig, use_container_width=True, config=config.CHART_CONFIG)
    
    # Cost trends
    st.markdown("### 📊 Cost Trends (30 Days)")
    dates = pd.date_range(end=datetime.now(), periods=30, freq='D')
    daily_costs = [cost_metrics['baseline_cost'] + np.random.normal(0, 500) for _ in range(30)]
    
    df_costs = pd.DataFrame({
        'date': dates,
        'cost': daily_costs,
        'training': [np.random.uniform(1000, 3000) for _ in range(30)],
        'inference': [np.random.uniform(2000, 5000) for _ in range(30)],
        'storage': [np.random.uniform(500, 1500) for _ in range(30)]
    })
    
    fig = create_multi_line_chart(
        df_costs,
        'date',
        ['cost', 'training', 'inference', 'storage'],
        "Cost Trends by Category"
    )
    st.plotly_chart(fig, use_container_width=True, config=config.CHART_CONFIG)
    
    # Cost anomalies
    st.markdown("### 🔍 Cost Anomaly Detection")
    
    anomaly = engines['alert'].detect_cost_anomaly(
        cost_metrics['current_cost'],
        cost_metrics['baseline_cost']
    )
    
    if anomaly['is_anomaly']:
        render_alert_box(
            anomaly['severity'],
            "Cost Anomaly Detected",
            f"Current cost ${anomaly['current_cost']:,.2f} is {abs(anomaly['percent_change']):.1f}% {'higher' if anomaly['percent_change'] > 0 else 'lower'} than baseline ${anomaly['baseline_cost']:,.2f}"
        )
    else:
        st.success("✓ No cost anomalies detected. Spending is within normal range.")
    
    # Optimization recommendations
    st.markdown("### 💡 Cost Optimization Recommendations")
    
    recommendations = [
        {"title": "Reduce Model Training Frequency", "savings": "$1,200/month", "priority": "High"},
        {"title": "Optimize Inference Batch Size", "savings": "$800/month", "priority": "Medium"},
        {"title": "Implement Caching Strategy", "savings": "$600/month", "priority": "High"},
        {"title": "Archive Old Data", "savings": "$400/month", "priority": "Low"}
    ]
    
    for rec in recommendations:
        with st.expander(f"💰 {rec['title']} - Potential savings: {rec['savings']}", expanded=False):
            st.write(f"**Priority:** {rec['priority']}")
            st.write(f"**Estimated Savings:** {rec['savings']}")
            st.write(f"**Implementation:** Recommended for cost optimization")

# ============================================================================
# SECURITY ALERTS PAGE
# ============================================================================
elif current_page == "Security Alerts":
    render_header("Security Alert Center", "Monitor and respond to security incidents")
    
    # Alert statistics
    alert_stats = engines['alert'].get_alert_statistics()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card("Total Alerts", str(alert_stats['total_alerts']))
    with col2:
        render_kpi_card("Critical", str(alert_stats['critical']))
    with col3:
        render_kpi_card("Resolved (24h)", str(alert_stats['resolved_24h']))
    with col4:
        render_kpi_card("Avg Resolution", alert_stats['avg_resolution_time'])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Alert trends
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 Alert Trends (7 Days)")
        alert_trends = engines['alert'].get_alert_trends(7)
        
        df_trends = pd.DataFrame({
            'Date': alert_trends['dates'],
            'Critical': alert_trends['critical'],
            'High': alert_trends['high'],
            'Medium': alert_trends['medium'],
            'Low': alert_trends['low']
        })
        
        fig = create_multi_line_chart(
            df_trends,
            'Date',
            ['Critical', 'High', 'Medium', 'Low'],
            "Alerts by Severity"
        )
        st.plotly_chart(fig, use_container_width=True, config=config.CHART_CONFIG)
    
    with col2:
        st.markdown("### 🎯 Alerts by Source")
        alert_by_source = engines['alert'].get_alert_by_source()
        fig = create_bar_chart(
            list(alert_by_source.keys()),
            list(alert_by_source.values()),
            "Alert Count by Source",
            color='#E91E63'
        )
        st.plotly_chart(fig, use_container_width=True, config=config.CHART_CONFIG)
    
    # MTTR by severity
    st.markdown("### ⏱️ Mean Time To Resolution (MTTR)")
    mttr = engines['alert'].get_mttr_by_severity()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Critical", f"{mttr['critical']} min")
    with col2:
        st.metric("High", f"{mttr['high']} min")
    with col3:
        st.metric("Medium", f"{mttr['medium']} min")
    with col4:
        st.metric("Low", f"{mttr['low']} min")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Active alerts
    st.markdown("### 🚨 Active Security Alerts")
    
    # Filter options
    col1, col2, col3 = st.columns(3)
    with col1:
        severity_filter = st.multiselect("Severity", ["critical", "high", "medium", "low"], default=["critical", "high"])
    with col2:
        status_filter = st.multiselect("Status", ["new", "investigating", "contained", "resolved"], default=["new", "investigating"])
    with col3:
        source_filter = st.selectbox("Source", ["All"] + engines['alert'].alert_sources)
    
    alerts = engines['alert'].get_active_alerts()
    
    # Apply filters
    filtered_alerts = [
        a for a in alerts
        if a['severity'] in severity_filter and a['status'] in status_filter
        and (source_filter == "All" or a['source'] == source_filter)
    ]
    
    # Display alerts
    for alert in filtered_alerts:
        severity_icon = config.ALERT_SEVERITY[alert['severity']]['icon']
        
        with st.expander(f"{severity_icon} {alert['id']} - {alert['type']}", expanded=alert['severity'] == 'critical'):
            col_a, col_b = st.columns(2)
            with col_a:
                st.write(f"**Severity:** {alert['severity'].upper()}")
                st.write(f"**Type:** {alert['type']}")
                st.write(f"**Source:** {alert['source']}")
                st.write(f"**Status:** {alert['status']}")
            with col_b:
                st.write(f"**Timestamp:** {alert['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
                st.write(f"**Affected Systems:** {alert['affected_systems']}")
                st.write(f"**Assigned To:** {alert['assigned_to']}")
            
            st.write(f"**Description:** {alert['description']}")
            
            # Action buttons
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("Investigate", key=f"inv_{alert['id']}"):
                    st.info("Investigation started")
            with col2:
                if st.button("Escalate", key=f"esc_{alert['id']}"):
                    st.warning("Alert escalated")
            with col3:
                if st.button("Resolve", key=f"res_{alert['id']}"):
                    st.success("Alert resolved")
    
    # Recent incidents
    st.markdown("### 📋 Recent Security Incidents")
    incidents = engines['alert'].get_recent_incidents(10)
    df_incidents = pd.DataFrame(incidents)
    df_incidents['timestamp'] = pd.to_datetime(df_incidents['timestamp']).dt.strftime('%Y-%m-%d %H:%M')
    st.dataframe(df_incidents, use_container_width=True, hide_index=True)

# ============================================================================
# AUDIT LOGS PAGE
# ============================================================================
elif current_page == "Audit Logs":
    render_header("Audit Logs & Activity", "Track system activities and changes")
    
    # Audit statistics
    audit_summary = engines['compliance'].get_audit_summary()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card("Total Audits", str(audit_summary['total_checks']))
    with col2:
        render_kpi_card("Passed", str(audit_summary['passed']))
    with col3:
        render_kpi_card("Failed", str(audit_summary['failed']))
    with col4:
        render_kpi_card("Success Rate", f"{audit_summary['compliance_rate']}%")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Audit timeline
    st.markdown("### 📅 Audit Schedule")
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**Last Audit:** {audit_summary['last_audit'].strftime('%Y-%m-%d')}")
    with col2:
        st.info(f"**Next Audit:** {audit_summary['next_audit'].strftime('%Y-%m-%d')}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Activity logs
    st.markdown("### 📋 Recent Activity Logs")
    
    # Generate sample activity logs
    activities = []
    activity_types = ["User Login", "Model Update", "Config Change", "Data Access", "Alert Triggered", "Policy Update"]
    users = ["admin@company.com", "ml-engineer@company.com", "security@company.com", "analyst@company.com"]
    
    for i in range(50):
        activities.append({
            'Timestamp': (datetime.now() - timedelta(minutes=i*30)).strftime('%Y-%m-%d %H:%M:%S'),
            'User': np.random.choice(users),
            'Activity': np.random.choice(activity_types),
            'Resource': f"Resource-{np.random.randint(1, 100)}",
            'Status': np.random.choice(['Success', 'Success', 'Success', 'Failed']),
            'IP Address': f"192.168.{np.random.randint(1, 255)}.{np.random.randint(1, 255)}"
        })
    
    df_activities = pd.DataFrame(activities)
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        activity_filter = st.multiselect("Activity Type", activity_types, default=activity_types)
    with col2:
        user_filter = st.multiselect("User", users, default=users)
    with col3:
        status_filter = st.multiselect("Status", ["Success", "Failed"], default=["Success", "Failed"])
    
    # Apply filters
    filtered_df = df_activities[
        (df_activities['Activity'].isin(activity_filter)) &
        (df_activities['User'].isin(user_filter)) &
        (df_activities['Status'].isin(status_filter))
    ]
    
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
    
    # Export option
    st.markdown("### 📥 Export Logs")
    if st.button("Export to CSV"):
        st.download_button(
            label="Download CSV",
            data=filtered_df.to_csv(index=False),
            file_name=f"audit_logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
    
    # Log analysis
    st.markdown("### 📊 Log Analysis")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Activity Distribution")
        activity_counts = df_activities['Activity'].value_counts()
        fig = create_bar_chart(
            activity_counts.index.tolist(),
            activity_counts.values.tolist(),
            "Activities by Type",
            color='#9C27B0'
        )
        st.plotly_chart(fig, use_container_width=True, config=config.CHART_CONFIG)
    
    with col2:
        st.markdown("#### User Activity")
        user_counts = df_activities['User'].value_counts()
        fig = create_pie_chart(
            user_counts.index.tolist(),
            user_counts.values.tolist(),
            "Activities by User"
        )
        st.plotly_chart(fig, use_container_width=True, config=config.CHART_CONFIG)

# Footer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #B0BEC5; padding: 1rem;">
    <p>{config.APP_ICON} {config.APP_NAME} v{config.APP_VERSION}</p>
    <p style="font-size: 0.8rem;">Enterprise AI Risk & Compliance Monitoring Platform</p>
    <p style="font-size: 0.8rem;">Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
</div>
""", unsafe_allow_html=True)
