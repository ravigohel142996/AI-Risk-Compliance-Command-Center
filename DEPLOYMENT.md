# 🚀 Deployment Guide

## Quick Start

### Local Development

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   streamlit run app.py
   ```

3. **Access the Dashboard**
   - Open browser to `http://localhost:8501`

---

## Docker Deployment

### Build Image
```bash
docker build -t ai-risk-center .
```

### Run Container
```bash
docker run -p 8501:8501 ai-risk-center
```

### Run with Custom Port
```bash
docker run -p 8080:8501 -e PORT=8501 ai-risk-center
```

---

## Render Deployment

### Configuration

1. **Connect GitHub Repository**
   - Go to Render Dashboard
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

2. **Settings**
   - **Name**: ai-risk-compliance-center
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true`
   - **Instance Type**: Starter (or higher)

3. **Environment Variables** (Optional)
   - `PORT`: Auto-configured by Render
   - `HOST`: `0.0.0.0`

4. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment to complete
   - Access via provided URL

### Health Check
Render will automatically check `/_stcore/health` endpoint.

---

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | `8501` |
| `HOST` | Server address | `0.0.0.0` |

---

## Production Considerations

### Performance
- ✅ Caching enabled (`@st.cache_resource`)
- ✅ Lazy loading of data
- ✅ Optimized chart rendering

### Security
- ✅ No secrets in code
- ✅ Environment-based configuration
- ✅ HTTPS required in production

### Monitoring
- Health check: `GET /_stcore/health`
- Returns: `ok` when healthy

---

## Troubleshooting

### App Won't Start
- Check Python version (3.11+)
- Verify all dependencies installed
- Check port availability

### Charts Not Displaying
- Clear browser cache
- Check JavaScript enabled
- Verify Plotly loaded

### Performance Issues
- Increase instance size
- Enable caching
- Reduce data simulation frequency

---

## Scaling

### Horizontal Scaling
- Deploy multiple instances behind load balancer
- Use sticky sessions for user experience

### Vertical Scaling
- Increase instance memory/CPU
- Recommended: 2GB RAM minimum

---

## Support

For issues or questions:
- GitHub Issues: [Repository Issues](https://github.com/ravigohel142996/AI-Risk-Compliance-Command-Center/issues)
- Documentation: See README.md
