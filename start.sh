#!/usr/bin/env bash

# Startup script for Render deployment
# This script handles environment setup and starts the Streamlit application

set -e

echo "🚀 Starting AI Risk & Compliance Command Center..."

# Get port from environment or use default
PORT=${PORT:-8501}

# Create required directories
echo "📁 Creating required directories..."
mkdir -p data models logs

# Health check
echo "💚 Running health check..."
python src/dashboard/health.py || echo "⚠️  Health check failed but continuing..."

# Start Streamlit application
echo "🌐 Starting Streamlit on port $PORT..."
streamlit run src/dashboard/app.py \
    --server.port=$PORT \
    --server.address=0.0.0.0 \
    --server.headless=true \
    --server.enableCORS=false \
    --server.enableXsrfProtection=true \
    --browser.serverAddress=0.0.0.0 \
    --browser.gatherUsageStats=false
