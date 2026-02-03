#!/usr/bin/env bash
# Test script to validate the entire application before deployment

set -e

echo "=========================================="
echo "AI Risk & Compliance Command Center"
echo "Pre-Deployment Test Suite"
echo "=========================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Test counter
TESTS_PASSED=0
TESTS_FAILED=0

# Function to report test result
test_result() {
    if [ $1 -eq 0 ]; then
        echo -e "${GREEN}✅ PASS${NC}: $2"
        ((TESTS_PASSED++))
    else
        echo -e "${RED}❌ FAIL${NC}: $2"
        ((TESTS_FAILED++))
    fi
}

echo "1. Testing Python Version..."
PYTHON_VERSION=$(python --version 2>&1 | grep -oP '\d+\.\d+')
if [[ "$PYTHON_VERSION" == "3.11" ]] || [[ "$PYTHON_VERSION" > "3.11" ]]; then
    test_result 0 "Python version $PYTHON_VERSION"
else
    test_result 1 "Python version $PYTHON_VERSION (expected 3.11+)"
fi
echo ""

echo "2. Testing Dependencies Installation..."
pip install -r requirements.txt --quiet --disable-pip-version-check > /dev/null 2>&1
test_result $? "Dependencies installation"
echo ""

echo "3. Testing File Structure..."
REQUIRED_FILES=(
    "src/__init__.py"
    "src/dashboard/app.py"
    "src/dashboard/health.py"
    "src/models/risk_model.py"
    "src/data/loader.py"
    "src/utils/config.py"
    "src/utils/logger.py"
    "src/utils/helpers.py"
    "requirements.txt"
    "runtime.txt"
    "start.sh"
    "Dockerfile"
    "README.md"
)

for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        test_result 0 "File exists: $file"
    else
        test_result 1 "File missing: $file"
    fi
done
echo ""

echo "4. Testing Module Imports..."
python << 'EOF'
import sys
sys.path.insert(0, '.')

try:
    from src.utils.config import APP_NAME, APP_VERSION, PORT, HOST
    print(f"✅ Config module: {APP_NAME} v{APP_VERSION}")
    
    from src.utils.logger import app_logger
    print("✅ Logger module")
    
    from src.utils.helpers import generate_sample_data
    print("✅ Helpers module")
    
    from src.models.risk_model import RiskAssessmentModel
    print("✅ Risk model module")
    
    from src.data.loader import DataLoader
    print("✅ Data loader module")
    
    sys.exit(0)
except Exception as e:
    print(f"❌ Import error: {str(e)}")
    sys.exit(1)
EOF
test_result $? "Module imports"
echo ""

echo "5. Testing Health Check..."
python src/dashboard/health.py > /dev/null 2>&1
test_result $? "Health check endpoint"
echo ""

echo "6. Testing Data Generation..."
python << 'EOF'
import sys
sys.path.insert(0, '.')
from src.utils.helpers import generate_sample_data

try:
    df = generate_sample_data(10)
    assert len(df) == 10, "Wrong number of records"
    required_cols = ['entity_id', 'compliance_score', 'incident_count', 'audit_failures', 'risk_score', 'risk_level']
    for col in required_cols:
        assert col in df.columns, f"Missing column: {col}"
    print(f"✅ Generated {len(df)} sample records with all required columns")
    sys.exit(0)
except Exception as e:
    print(f"❌ Data generation error: {str(e)}")
    sys.exit(1)
EOF
test_result $? "Sample data generation"
echo ""

echo "7. Testing Risk Assessment..."
python << 'EOF'
import sys
sys.path.insert(0, '.')
from src.models.risk_model import RiskAssessmentModel

try:
    model = RiskAssessmentModel()
    test_data = {
        'entity_id': 'TEST-001',
        'compliance_score': 0.7,
        'incident_count': 3,
        'audit_failures': 1
    }
    result = model.assess_entity(test_data)
    assert 'risk_score' in result, "Missing risk_score in result"
    assert 'risk_level' in result, "Missing risk_level in result"
    print(f"✅ Risk assessment: {result['risk_level']} (score: {result['risk_score']})")
    sys.exit(0)
except Exception as e:
    print(f"❌ Risk assessment error: {str(e)}")
    sys.exit(1)
EOF
test_result $? "Risk assessment model"
echo ""

echo "8. Testing Required Directories..."
REQUIRED_DIRS=("data" "models" "logs")
for dir in "${REQUIRED_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        test_result 0 "Directory exists: $dir"
    else
        mkdir -p "$dir"
        test_result 0 "Directory created: $dir"
    fi
done
echo ""

echo "9. Testing Startup Script..."
if [ -x "start.sh" ]; then
    test_result 0 "start.sh is executable"
else
    chmod +x start.sh
    test_result 0 "start.sh made executable"
fi
echo ""

echo "10. Testing Environment Variables..."
export PORT=8501
export HOST=0.0.0.0
python << 'EOF'
import sys
import os
sys.path.insert(0, '.')

try:
    from src.utils.config import PORT, HOST
    assert PORT == 8501, f"Wrong PORT value: {PORT}"
    assert HOST == "0.0.0.0", f"Wrong HOST value: {HOST}"
    print(f"✅ Environment variables: PORT={PORT}, HOST={HOST}")
    sys.exit(0)
except Exception as e:
    print(f"❌ Environment error: {str(e)}")
    sys.exit(1)
EOF
test_result $? "Environment configuration"
echo ""

echo "=========================================="
echo "Test Summary"
echo "=========================================="
echo "Tests Passed: $TESTS_PASSED"
echo "Tests Failed: $TESTS_FAILED"
echo ""

if [ $TESTS_FAILED -eq 0 ]; then
    echo -e "${GREEN}🎉 All tests passed! Ready for deployment.${NC}"
    exit 0
else
    echo -e "${RED}⚠️  Some tests failed. Please review and fix.${NC}"
    exit 1
fi
