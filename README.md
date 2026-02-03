# 🛡️ AI Risk & Compliance Command Center

**Production-ready risk assessment and compliance monitoring platform**  
*Used by Banks, SaaS, FinTech, and AI Companies*

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3119/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Features

- **Real-time Risk Assessment**: Monitor and assess risks across your organization
- **Compliance Tracking**: Track compliance scores and audit results
- **Interactive Dashboards**: Visual analytics with Plotly charts
- **Machine Learning Models**: AI-powered risk prediction
- **Production Ready**: Health checks, logging, and monitoring built-in
- **Cloud Deployable**: Optimized for Render, Docker, and other platforms

## 📁 Project Structure

```
AI-Risk-Compliance-Command-Center/
├── src/
│   ├── __init__.py
│   ├── dashboard/
│   │   ├── __init__.py
│   │   ├── app.py              # Main Streamlit application
│   │   └── health.py           # Health check endpoint
│   ├── models/
│   │   ├── __init__.py
│   │   └── risk_model.py       # Risk assessment ML model
│   ├── data/
│   │   ├── __init__.py
│   │   └── loader.py           # Data loading utilities
│   └── utils/
│       ├── __init__.py
│       ├── config.py           # Configuration management
│       ├── logger.py           # Production logging
│       └── helpers.py          # Helper functions
├── data/                        # Data directory (created at runtime)
├── models/                      # Saved models directory
├── logs/                        # Application logs
├── requirements.txt             # Python dependencies
├── runtime.txt                  # Python version for Render
├── Dockerfile                   # Docker configuration
├── .dockerignore               # Docker ignore patterns
├── .gitignore                  # Git ignore patterns
├── start.sh                    # Startup script for deployment
└── README.md                   # This file
```

## 🔧 Prerequisites

- Python 3.11.9 or higher
- pip package manager
- (Optional) Docker for containerized deployment

## 💻 Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ravigohel142996/AI-Risk-Compliance-Command-Center.git
cd AI-Risk-Compliance-Command-Center
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
# Using Streamlit directly
streamlit run src/dashboard/app.py

# Or using the startup script
chmod +x start.sh
./start.sh
```

### 5. Access the Application

Open your browser and navigate to:
```
http://localhost:8501
```

## ☁️ Render Deployment

### Quick Deploy to Render

1. **Fork this repository** to your GitHub account

2. **Create a new Web Service** on [Render](https://render.com)
   - Connect your GitHub repository
   - Select the branch you want to deploy

3. **Configure the service**:
   - **Name**: `ai-risk-compliance-center`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `./start.sh`

4. **Environment Variables** (Optional):
   ```
   PORT=8501
   LOG_LEVEL=INFO
   DEBUG=False
   ```

5. **Click "Create Web Service"**

The application will automatically:
- Install dependencies from `requirements.txt`
- Use Python 3.11.9 (from `runtime.txt`)
- Bind to `$PORT` environment variable
- Start with health checks enabled

### Render Configuration Files

The following files are pre-configured for Render deployment:

- ✅ `runtime.txt` - Specifies Python 3.11.9
- ✅ `requirements.txt` - All dependencies with versions
- ✅ `start.sh` - Startup script that binds to $PORT
- ✅ Health checks via `src/dashboard/health.py`
- ✅ Production logging configured

## 🐳 Docker Deployment

### Build the Docker Image

```bash
docker build -t ai-risk-compliance .
```

### Run the Container

```bash
docker run -p 8501:8501 \
  -e PORT=8501 \
  -e LOG_LEVEL=INFO \
  ai-risk-compliance
```

### Using Docker Compose

Create a `docker-compose.yml`:

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8501:8501"
    environment:
      - PORT=8501
      - LOG_LEVEL=INFO
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
    restart: unless-stopped
```

Run with:
```bash
docker-compose up -d
```

## 🔍 Health Checks

The application includes built-in health checks:

```bash
# Check application health
python src/dashboard/health.py
```

Health check endpoint validates:
- ✅ Application imports
- ✅ Configuration loading
- ✅ Logging system
- ✅ Required directories
- ✅ System status

## 📊 Features & Usage

### Risk Assessment
- Upload CSV data with compliance metrics
- View real-time risk scores and levels
- Filter and export assessment results

### Compliance Monitoring
- Track compliance scores over time
- Identify critical risk entities
- Monitor incident counts and audit failures

### Interactive Visualizations
- Risk distribution pie charts
- Timeline analysis
- Compliance heatmaps
- Customizable filters and exports

## 🔐 Security Best Practices

- ✅ Non-root user in Docker containers
- ✅ XSRF protection enabled
- ✅ Environment-based configuration
- ✅ Input validation and sanitization
- ✅ Secure dependency versions
- ✅ Health monitoring and logging

## 🧪 Testing

### Run Health Check
```bash
python src/dashboard/health.py
```

### Validate Import Paths
```bash
python -c "from src.utils.config import APP_NAME; print(f'✅ Imports working: {APP_NAME}')"
```

### Test Local Server
```bash
streamlit run src/dashboard/app.py --server.port=8501
```

## 📝 Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `8501` | Port for the Streamlit server |
| `HOST` | `0.0.0.0` | Server bind address |
| `LOG_LEVEL` | `INFO` | Logging level (DEBUG, INFO, WARNING, ERROR) |
| `DEBUG` | `False` | Enable debug mode |

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Import Errors
If you encounter `ModuleNotFoundError: No module named 'src'`:
- Ensure you're running from the project root directory
- The `app.py` file includes automatic path configuration

### Port Already in Use
```bash
# Find and kill process using port 8501
lsof -ti:8501 | xargs kill -9
```

### Permission Denied on start.sh
```bash
chmod +x start.sh
```

## 📞 Support

For issues and questions:
- 📧 Email: ravi.gohel142996@marwadiuniversity.ac.in
- 🐛 Issues: [GitHub Issues](https://github.com/ravigohel142996/AI-Risk-Compliance-Command-Center/issues)

## 🎯 Roadmap

- [ ] Advanced ML models for risk prediction
- [ ] Integration with external compliance APIs
- [ ] Multi-tenancy support
- [ ] Advanced reporting and analytics
- [ ] Mobile-responsive design
- [ ] Real-time alerts and notifications

---

**Built with ❤️ for Banks, SaaS, FinTech, and AI Companies**
