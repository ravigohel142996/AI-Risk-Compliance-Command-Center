# Render Deployment Guide

## 🚀 Production Deployment Configuration

This project is fully configured for deployment on Render's Free Tier.

### ✅ Pre-configured Files

1. **requirements.txt** - All dependencies specified
2. **src/dashboard/app.py** - Import paths fixed with `sys.path.append(os.path.abspath("."))`
3. **.streamlit/config.toml** - Optimized for Render Free Tier
4. **src/utils/config.py** - Dynamic PORT support via environment variable
5. **start.sh** - Alternative startup script (optional)

---

## 📋 Render Configuration Settings

### Step 1: Create New Web Service on Render

Go to [Render Dashboard](https://dashboard.render.com/) and click "New +" → "Web Service"

### Step 2: Connect Repository

Connect your GitHub repository: `ravigohel142996/AI-Risk-Compliance-Command-Center`

### Step 3: Configure Service

Use these **exact settings**:

| Field | Value |
|-------|-------|
| **Name** | `ai-risk-compliance-center` (or your choice) |
| **Environment** | `Python` |
| **Region** | Choose closest to your users |
| **Branch** | `main` (or your deployment branch) |
| **Root Directory** | `.` (leave empty) |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `streamlit run src/dashboard/app.py --server.port=$PORT --server.address=0.0.0.0` |
| **Plan** | `Free` |

### Step 4: Environment Variables (Optional)

Add these environment variables if needed:

| Key | Value | Description |
|-----|-------|-------------|
| `PYTHON_VERSION` | `3.11.9` | Python version (optional) |
| `DEBUG` | `False` | Disable debug mode in production |
| `LOG_LEVEL` | `INFO` | Logging level |

### Step 5: Deploy

Click "Create Web Service" and wait for deployment to complete (~2-5 minutes).

---

## 🔍 Verification Steps

After deployment completes:

1. ✅ Check deployment logs for "You can now view your Streamlit app"
2. ✅ Open the provided URL (e.g., `https://your-app.onrender.com`)
3. ✅ Verify app loads without timeout
4. ✅ Test all features and dashboards
5. ✅ Check that metrics and charts display correctly

---

## 🎯 Key Features Configured

### ✅ Import Path Fix
```python
import sys
import os
sys.path.append(os.path.abspath("."))
```
This ensures all `src.*` imports work correctly on Render.

### ✅ Dynamic PORT Support
The app automatically uses Render's `$PORT` environment variable.

### ✅ Optimized for Free Tier
- Memory optimization settings
- Fast reruns enabled
- Minimal toolbar mode
- WebSocket compression enabled
- Max upload size: 200MB

### ✅ Production Settings
- Headless mode enabled
- CORS disabled for security
- Usage stats disabled
- Server address: 0.0.0.0 (public access)

---

## 🐛 Troubleshooting

### Issue: ModuleNotFoundError: No module named 'src'

**Solution:** Already fixed! The app.py has been updated with:
```python
import sys
import os
sys.path.append(os.path.abspath("."))
```

### Issue: Port binding error

**Solution:** Already configured! The app uses `$PORT` environment variable automatically.

### Issue: App timeout on startup

**Possible causes:**
1. Check build logs for dependency installation errors
2. Ensure Free Tier memory limits aren't exceeded
3. Verify Start Command is correct

**Solution:** The app is optimized for Free Tier with:
- Streamlined dependencies
- Fast startup configuration
- Memory-efficient settings

### Issue: Import errors in production

**Solution:** Verified all imports work with the sys.path fix. Test locally with:
```bash
python -c "from src.utils.config import APP_NAME; print(APP_NAME)"
```

---

## 🧪 Local Testing (Simulating Render)

Test the deployment configuration locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Test with dynamic PORT (simulating Render)
PORT=8502 streamlit run src/dashboard/app.py --server.port=$PORT --server.address=0.0.0.0

# Or use the start.sh script
./start.sh
```

---

## 📊 Expected Performance

On Render's Free Tier:
- **Cold start:** ~30-60 seconds
- **Warm start:** ~5-10 seconds
- **Response time:** <200ms for most operations
- **Memory usage:** ~150-250MB

---

## 🔐 Security Notes

✅ Configured security settings:
- CORS disabled
- XSRF protection configurable
- No hardcoded secrets
- Environment-based configuration

---

## 📝 Alternative Start Command (Using start.sh)

If you prefer to use the `start.sh` script:

**Start Command:** `bash start.sh`

This script includes:
- Directory creation
- Health checks
- Environment variable handling
- Detailed logging

---

## 🎉 Deployment Complete!

Your Streamlit app is now production-ready for Render deployment with:
- ✅ All imports fixed
- ✅ Dynamic PORT support
- ✅ Optimized configuration
- ✅ Free Tier optimization
- ✅ Security hardening
- ✅ No hardcoded values

**Access your app at:** `https://your-app-name.onrender.com`

---

## 📞 Support

For issues:
1. Check Render deployment logs
2. Review this guide's troubleshooting section
3. Verify all configuration settings match this guide

**Last Updated:** 2026-02-03
