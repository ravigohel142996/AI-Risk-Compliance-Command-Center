"""
Configuration management for AI Risk & Compliance Command Center
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base directories
BASE_DIR = Path(__file__).parent.parent.parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"
LOGS_DIR = BASE_DIR / "logs"

# Create directories if they don't exist
for directory in [DATA_DIR, MODELS_DIR, LOGS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Server configuration
PORT = int(os.getenv("PORT", 8501))
HOST = os.getenv("HOST", "0.0.0.0")

# Application configuration
APP_NAME = "AI Risk & Compliance Command Center"
APP_VERSION = "1.0.0"
DEBUG_MODE = os.getenv("DEBUG", "False").lower() == "true"

# Logging configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Risk thresholds
RISK_THRESHOLDS = {
    "low": 0.3,
    "medium": 0.6,
    "high": 0.8,
    "critical": 0.95
}

# Model configuration
MODEL_CONFIG = {
    "default_model": "risk_assessment_v1",
    "confidence_threshold": 0.75,
    "max_predictions": 100
}
