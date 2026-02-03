# AI Risk & Compliance Command Center - File Structure

## Generated: $(date)

## Complete File Tree

```
AI-Risk-Compliance-Command-Center/
├── .dockerignore                # Docker build exclusions
├── .env.example                 # Environment variables template
├── .gitignore                   # Git exclusions
├── .streamlit/
│   └── config.toml             # Streamlit production config
├── data/
│   └── .gitkeep                # Keep directory in git
├── logs/
│   └── .gitkeep                # Keep directory in git
├── models/
│   └── .gitkeep                # Keep directory in git
├── src/
│   ├── __init__.py             # Main package init
│   ├── dashboard/
│   │   ├── __init__.py         # Dashboard package init
│   │   ├── app.py              # Main Streamlit application (7.8 KB)
│   │   └── health.py           # Health check endpoint (1.8 KB)
│   ├── data/
│   │   ├── __init__.py         # Data package init
│   │   └── loader.py           # Data loading utilities (2.3 KB)
│   ├── models/
│   │   ├── __init__.py         # Models package init
│   │   └── risk_model.py       # Risk assessment model (3.5 KB)
│   └── utils/
│       ├── __init__.py         # Utils package init
│       ├── config.py           # Configuration management (1.1 KB)
│       ├── helpers.py          # Helper functions (2.4 KB)
│       └── logger.py           # Production logging (1.3 KB)
├── Dockerfile                   # Multi-stage Docker build (1.5 KB)
├── README.md                    # Main documentation (7.5 KB)
├── DEPLOYMENT.md               # Deployment guide (4.2 KB)
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Python version (3.11.9)
└── start.sh                    # Startup script for Render
```

## Key Components

### Application Core
- **src/dashboard/app.py**: Main Streamlit application with interactive UI
- **src/models/risk_model.py**: Machine learning model for risk assessment
- **src/data/loader.py**: Data loading and preprocessing
- **src/utils/**: Configuration, logging, and helper utilities

### Deployment Files
- **runtime.txt**: Specifies Python 3.11.9 for Render
- **start.sh**: Startup script that binds to $PORT
- **Dockerfile**: Optimized multi-stage Docker build
- **.streamlit/config.toml**: Production Streamlit configuration

### Configuration
- **.env.example**: Template for environment variables
- **.gitignore**: Excludes logs, data, and Python artifacts
- **.dockerignore**: Optimizes Docker build

### Documentation
- **README.md**: Complete setup and deployment instructions
- **DEPLOYMENT.md**: Detailed deployment guide
- **FILE_STRUCTURE.md**: This file

## Import Structure

All imports are resolved using absolute imports from the `src` package:

```python
from src.utils.config import APP_NAME, APP_VERSION
from src.utils.logger import app_logger
from src.utils.helpers import generate_sample_data
from src.models.risk_model import RiskAssessmentModel
from src.data.loader import DataLoader
```

The `app.py` file automatically adds the project root to `sys.path`:

```python
import sys
from pathlib import Path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))
```

## Environment Variables

The application uses these environment variables:

- `PORT`: Server port (default: 8501, auto-set by Render)
- `HOST`: Bind address (default: 0.0.0.0)
- `LOG_LEVEL`: Logging level (default: INFO)
- `DEBUG`: Debug mode (default: False)

## Data Directories

Created automatically at startup:
- `data/`: Store CSV files and exports
- `models/`: Store trained ML models
- `logs/`: Application logs

## Production Ready Features

✅ Python 3.11.9 compatibility
✅ Proper package structure with __init__.py files
✅ Import path resolution fixed
✅ Render port binding ($PORT)
✅ Health check endpoint
✅ Production logging
✅ Optimized Docker image
✅ Security best practices
✅ Comprehensive documentation

## Testing

All components tested and verified:
- ✅ Import system working correctly
- ✅ Health check returns healthy status
- ✅ Sample data generation
- ✅ Risk calculation and assessment
- ✅ Streamlit application starts successfully
- ✅ All dependencies installed correctly

## Deployment Commands

### Local Testing
```bash
pip install -r requirements.txt
streamlit run src/dashboard/app.py
```

### Render Deployment
Build Command: `pip install -r requirements.txt`
Start Command: `./start.sh`

### Docker Deployment
```bash
docker build -t ai-risk-compliance .
docker run -p 8501:8501 ai-risk-compliance
```

## File Sizes Summary

- Source Code: ~19 KB (Python files)
- Documentation: ~12 KB (Markdown files)
- Configuration: ~2 KB (Config files)
- Total: ~33 KB (excluding dependencies)

## Dependencies

Core dependencies specified in requirements.txt:
- streamlit >= 1.28.0
- pandas >= 2.0.0
- numpy >= 1.24.0
- scikit-learn >= 1.3.0
- plotly >= 5.17.0
- python-dotenv >= 1.0.0
- Plus additional utilities

