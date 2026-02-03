# Deployment Guide

## Render.com Deployment

### Step-by-Step Instructions

1. **Push Code to GitHub**
   - Ensure all files are committed to your repository
   - Push to the main or deployment branch

2. **Create Web Service on Render**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

3. **Configure Service**
   ```
   Name: ai-risk-compliance-center
   Environment: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: ./start.sh
   ```

4. **Advanced Settings** (Optional)
   - Instance Type: Starter (or higher for production)
   - Health Check Path: `/` (Streamlit default)
   - Auto-Deploy: Yes (recommended)

5. **Environment Variables**
   ```
   LOG_LEVEL=INFO
   DEBUG=False
   ```
   Note: PORT is automatically provided by Render

6. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment to complete (2-5 minutes)
   - Access your app at the provided URL

### Verification

After deployment:
1. Visit your app URL
2. Check health status: `https://your-app.onrender.com`
3. Verify all features are working

## Docker Deployment

### Local Docker Testing

```bash
# Build image
docker build -t ai-risk-compliance .

# Run container
docker run -p 8501:8501 ai-risk-compliance

# Access at http://localhost:8501
```

### Docker Compose

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8501:8501"
    environment:
      - LOG_LEVEL=INFO
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
    restart: unless-stopped
```

Run: `docker-compose up -d`

## AWS/Azure/GCP Deployment

### General Steps

1. Use the Dockerfile provided
2. Build and push to container registry
3. Deploy to your preferred service:
   - AWS: ECS, Fargate, or App Runner
   - Azure: Container Instances or App Service
   - GCP: Cloud Run or App Engine

4. Set environment variables:
   - PORT (if not auto-detected)
   - LOG_LEVEL=INFO
   - DEBUG=False

## Troubleshooting

### Common Issues

1. **Module Import Errors**
   - Ensure `src/__init__.py` exists
   - Check Python path configuration in `app.py`

2. **Port Binding Issues**
   - Verify PORT environment variable is set
   - Check start.sh permissions: `chmod +x start.sh`

3. **Missing Dependencies**
   - Ensure requirements.txt is up to date
   - Run: `pip install -r requirements.txt`

4. **Health Check Failures**
   - Test locally: `python src/dashboard/health.py`
   - Check logs for errors

### Logs

View logs on Render:
- Dashboard → Your Service → Logs
- Real-time log streaming available

## Performance Optimization

### Production Settings

1. **Streamlit Config** (`.streamlit/config.toml`):
   ```toml
   [server]
   headless = true
   enableCORS = false
   enableXsrfProtection = true
   
   [browser]
   gatherUsageStats = false
   ```

2. **Caching**
   - Use `@st.cache_data` for data loading
   - Use `@st.cache_resource` for models

3. **Resource Limits**
   - Monitor memory usage
   - Adjust instance type as needed

## Security Checklist

- [x] Non-root user in Docker
- [x] Environment variables for sensitive data
- [x] XSRF protection enabled
- [x] CORS properly configured
- [x] Dependencies pinned with versions
- [x] Logs directory with proper permissions
- [x] Health checks enabled

## Monitoring

### Health Checks

```bash
# Manual health check
curl https://your-app.onrender.com

# Or locally
python src/dashboard/health.py
```

### Metrics to Monitor

- Response time
- Error rate
- Memory usage
- CPU usage
- Request count

## Scaling

### Horizontal Scaling

For Render:
- Upgrade to higher tier for auto-scaling
- Add more instances in advanced settings

### Vertical Scaling

- Start with Starter instance
- Upgrade to Standard/Pro as needed

## Backup & Recovery

### Data Backup

```bash
# Backup data directory
tar -czf backup-$(date +%Y%m%d).tar.gz data/

# Restore
tar -xzf backup-YYYYMMDD.tar.gz
```

### Database Considerations

For production, consider:
- External database (PostgreSQL/MongoDB)
- S3/Cloud Storage for data files
- Redis for caching

## Support

For deployment issues:
- Check Render logs
- Review health check output
- Consult README.md
- Open GitHub issue
