"""
Health check endpoint for production monitoring
"""
import json
from datetime import datetime
from pathlib import Path
import sys

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.config import APP_NAME, APP_VERSION, PORT, HOST
from src.utils.logger import app_logger


def health_check():
    """
    Perform health check and return status
    
    Returns:
        Dictionary with health status
    """
    try:
        health_status = {
            "status": "healthy",
            "app_name": APP_NAME,
            "version": APP_VERSION,
            "timestamp": datetime.now().isoformat(),
            "checks": {
                "imports": "ok",
                "config": "ok",
                "logging": "ok"
            }
        }
        
        # Check if critical directories exist
        from src.utils.config import DATA_DIR, MODELS_DIR, LOGS_DIR
        
        health_status["checks"]["data_dir"] = "ok" if DATA_DIR.exists() else "missing"
        health_status["checks"]["models_dir"] = "ok" if MODELS_DIR.exists() else "missing"
        health_status["checks"]["logs_dir"] = "ok" if LOGS_DIR.exists() else "missing"
        
        # Overall status
        if all(v == "ok" for v in health_status["checks"].values()):
            health_status["status"] = "healthy"
        else:
            health_status["status"] = "degraded"
        
        return health_status
        
    except Exception as e:
        app_logger.error(f"Health check failed: {str(e)}")
        return {
            "status": "unhealthy",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }


if __name__ == "__main__":
    status = health_check()
    print(json.dumps(status, indent=2))
    sys.exit(0 if status["status"] == "healthy" else 1)
