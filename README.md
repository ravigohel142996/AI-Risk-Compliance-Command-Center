# 🛡️ AI Risk & Compliance Command Center

> **Production-Grade AI Risk Monitoring Platform**  
> Used by Banks, SaaS, FinTech, and AI Companies to ensure safe, compliant, and cost-effective AI operations.

[![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![Plotly](https://img.shields.io/badge/Plotly-5.18.0-3F4F75?style=for-the-badge&logo=plotly)](https://plotly.com/)

---

## 📋 Overview

The **AI Risk & Compliance Command Center** is an enterprise-grade dashboard designed to monitor, analyze, and mitigate risks associated with AI systems in production. It provides real-time insights into model performance, compliance status, security alerts, and cost optimization opportunities.

### ✨ Key Features

- 🎯 **Risk Scoring Engine** - ML-based risk assessment across multiple dimensions
- ✅ **Compliance Monitoring** - Track adherence to GDPR, SOC 2, ISO 27001, HIPAA, PCI DSS, CCPA
- 🚨 **Security Alerts** - Real-time alert classification and incident management
- 💰 **Cost Tracking** - Anomaly detection and optimization recommendations
- 📊 **Advanced Analytics** - Interactive Plotly dashboards with heatmaps, trends, and radar charts
- 🎨 **Modern UI** - Dark theme with glassmorphism effects and smooth animations
- 🔄 **Real-time Simulation** - Live data generation for monitoring and testing

---

## 🏗️ Architecture

```
ai-risk-command-center/
│
├── app.py                      # Main Streamlit application
├── config.py                   # Configuration and constants
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container configuration
│
├── services/                   # Business logic layer
│   ├── risk_engine.py         # Risk scoring and analysis
│   ├── compliance_engine.py   # Compliance monitoring
│   └── alert_engine.py        # Alert classification and cost tracking
│
├── ui/                        # User interface components
│   ├── theme.css              # Custom styling (glassmorphism, animations)
│   └── components.py          # Reusable widgets and charts
│
├── data/                      # Data storage (gitignored)
└── models/                    # ML models (gitignored)
```

### 🔧 Tech Stack

| Layer          | Technology                  |
|----------------|-----------------------------|
| **Frontend**   | Streamlit + Custom CSS      |
| **UI Design**  | Glassmorphism + Dark Theme  |
| **Charts**     | Plotly (Interactive)        |
| **Backend**    | Python 3.11                 |
| **AI Engine**  | Scikit-learn + NumPy        |
| **Deployment** | Render / Docker             |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ravigohel142996/AI-Risk-Compliance-Command-Center.git
   cd AI-Risk-Compliance-Command-Center
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser**
   - Navigate to `http://localhost:8501`

---

## 🐳 Docker Deployment

### Build and Run

```bash
# Build Docker image
docker build -t ai-risk-center .

# Run container
docker run -p 8501:8501 ai-risk-center
```

### Deploy to Render

1. Connect your GitHub repository to Render
2. Create a new Web Service
3. Use the following settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true`
4. Deploy!

---

## 📊 Dashboard Pages

### 1. 📊 Overview
- **KPIs:** Overall risk, compliance score, active alerts, monitored models, monthly cost
- **Risk Trends:** 30-day historical analysis
- **Alert Summary:** Recent critical alerts
- **Compliance Status:** Quick view of all standards

### 2. ⚠️ Risk Monitor
- **Real-time Risk Scoring:** ML-based risk assessment
- **Risk Heatmap:** Model-by-timeframe risk visualization
- **Anomaly Detection:** Automatic identification of risk spikes
- **Factor Breakdown:** Radar chart of risk categories

### 3. ✅ Compliance
- **Multi-Standard Tracking:** GDPR, SOC 2, ISO 27001, HIPAA, PCI DSS, CCPA
- **Violation Management:** Active violations with remediation timelines
- **Audit Summary:** Pass/fail rates and compliance trends
- **Policy Coverage:** Coverage metrics by category

### 4. 💰 Cost Tracking
- **Cost Breakdown:** By service (training, inference, storage, etc.)
- **Anomaly Detection:** Automatic alerts for cost spikes
- **Trend Analysis:** 30-day cost trends
- **Optimization Recommendations:** AI-driven cost-saving suggestions

### 5. 🔒 Security Alerts
- **Alert Classification:** Critical, high, medium, low severity
- **MTTR Tracking:** Mean time to resolution by severity
- **Multi-source Integration:** WAF, IDS/IPS, SIEM, API Gateway, etc.
- **Incident History:** Recent security incidents with root cause analysis

### 6. 📋 Audit Logs
- **Activity Tracking:** User actions, model updates, config changes
- **Filtering & Search:** By user, activity type, status
- **Export Capabilities:** CSV download for compliance reporting
- **Visual Analytics:** Activity distribution and user behavior charts

---

## 🎨 UI Features

### Design System
- **Dark Theme:** Eye-friendly for 24/7 monitoring
- **Glassmorphism Cards:** Modern, frosted-glass effect
- **Gradient Headers:** Professional, enterprise look
- **Animated Badges:** Pulsing status indicators
- **Hover Effects:** Smooth transitions and shadows
- **Responsive Layout:** Mobile-friendly design

### Color Palette
- Primary: `#1E88E5` (Blue)
- Success: `#4CAF50` (Green)
- Warning: `#FF9800` (Orange)
- Error: `#F44336` (Red)
- Background: `#0F1419` → `#1A1F2E` (Gradient)

---

## ⚙️ Configuration

Edit `config.py` to customize:

```python
# Risk thresholds
RISK_LEVELS = {
    "critical": {"threshold": 80, "color": "#FF4444"},
    "high": {"threshold": 60, "color": "#FF8C00"},
    ...
}

# Compliance standards
COMPLIANCE_STANDARDS = ["GDPR", "SOC 2", "ISO 27001", ...]

# Cost anomaly threshold
COST_THRESHOLD_PERCENT = 20  # Alert if cost increases >20%

# Cache settings
CACHE_TTL = 300  # 5 minutes
```

---

## 🧪 Features in Detail

### Risk Scoring Engine
- **Multi-dimensional Analysis:** Model accuracy, data quality, security, compliance, performance, drift
- **Weighted Scoring:** Customizable weight assignments
- **Trend Detection:** Historical risk patterns
- **Anomaly Detection:** Statistical outlier identification

### Compliance Engine
- **Automated Checks:** 500-1000 compliance checks per audit
- **Policy Coverage:** Tracks 8+ categories (data privacy, encryption, logging, etc.)
- **Violation Tracking:** Severity classification and remediation timelines
- **Multi-standard Support:** Simultaneous monitoring of 6+ standards

### Alert Engine
- **Severity Classification:** ML-based alert prioritization
- **Multi-source Integration:** 8+ alert sources
- **Cost Anomaly Detection:** Statistical baseline comparison
- **MTTR Tracking:** Performance metrics by severity

---

## 🚦 Performance Optimization

- **Caching:** `@st.cache_resource` for engine initialization
- **Lazy Loading:** On-demand data generation
- **Efficient Rendering:** Optimized Plotly charts with minimal config
- **Responsive Design:** Mobile-optimized layouts

---

## 📈 Roadmap

### Phase 1 (Current)
- ✅ Core risk, compliance, and alert engines
- ✅ 6 interactive dashboard pages
- ✅ Modern UI with glassmorphism
- ✅ Docker deployment support

### Phase 2 (Q2 2026)
- [ ] Real API integrations (AWS, Azure, GCP)
- [ ] Advanced ML models for risk prediction
- [ ] Custom alert rules engine
- [ ] Email/Slack notifications
- [ ] User authentication & RBAC

### Phase 3 (Q3 2026)
- [ ] Multi-tenant support
- [ ] Historical data persistence
- [ ] Advanced reporting & exports
- [ ] Integration with ticketing systems (Jira, ServiceNow)
- [ ] Mobile app

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👤 Author

**Ravi Gohel**
- GitHub: [@ravigohel142996](https://github.com/ravigohel142996)

---

## 🙏 Acknowledgments

- Streamlit team for the amazing framework
- Plotly for interactive visualizations
- The open-source community

---

## 📞 Support

For issues, questions, or feature requests:
- Open an issue on GitHub
- Contact: ravigohel142996@github.com

---

<div align="center">
  <strong>Built with ❤️ for Enterprise AI Safety</strong>
</div>
