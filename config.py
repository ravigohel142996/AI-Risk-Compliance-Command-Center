"""
Configuration for AI Risk & Compliance Command Center
"""
import os

# Application Settings
APP_NAME = "AI Risk & Compliance Command Center"
APP_ICON = "🛡️"
APP_VERSION = "1.0.0"

# Deployment Settings
PORT = int(os.getenv("PORT", 8501))
HOST = os.getenv("HOST", "0.0.0.0")

# Risk Thresholds
RISK_LEVELS = {
    "critical": {"threshold": 80, "color": "#FF4444"},
    "high": {"threshold": 60, "color": "#FF8C00"},
    "medium": {"threshold": 40, "color": "#FFD700"},
    "low": {"threshold": 20, "color": "#90EE90"},
    "minimal": {"threshold": 0, "color": "#4CAF50"}
}

# Compliance Standards
COMPLIANCE_STANDARDS = [
    "GDPR",
    "SOC 2",
    "ISO 27001",
    "HIPAA",
    "PCI DSS",
    "CCPA"
]

# Alert Severity
ALERT_SEVERITY = {
    "critical": {"icon": "🔴", "priority": 1},
    "high": {"icon": "🟠", "priority": 2},
    "medium": {"icon": "🟡", "priority": 3},
    "low": {"icon": "🟢", "priority": 4}
}

# Cost Anomaly Settings
COST_THRESHOLD_PERCENT = 20  # Alert if cost increases by >20%
COST_BASELINE_DAYS = 30

# UI Theme Colors
THEME = {
    "primary": "#1E88E5",
    "secondary": "#43A047",
    "accent": "#E91E63",
    "background": "#0F1419",
    "surface": "#1A1F2E",
    "text_primary": "#FFFFFF",
    "text_secondary": "#B0BEC5",
    "success": "#4CAF50",
    "warning": "#FF9800",
    "error": "#F44336",
    "info": "#2196F3"
}

# Chart Settings
CHART_CONFIG = {
    "displayModeBar": False,
    "displaylogo": False,
    "responsive": True
}

# Cache Settings
CACHE_TTL = 300  # 5 minutes

# Simulation Settings
SIMULATE_REAL_TIME = True
UPDATE_INTERVAL = 5  # seconds
