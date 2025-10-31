# Phase 4: FastAPI Backend

## 🎯 Goals
- Build REST API with FastAPI
- Create health check and diagnosis endpoints
- Add authentication
- Implement error handling
- Add API documentation

## Understanding FastAPI

**What is FastAPI?**
- Modern Python web framework
- Automatic API documentation (Swagger/ReDoc)
- Type validation with Pydantic
- Async support for high performance

**Why FastAPI?**
- Fast to develop (3-5x faster than Flask)
- Fast to run (similar to NodeJS/Go)
- Automatic validation
- OpenAPI (Swagger) docs out of the box

## Step 1: Create Main Application

Create `app/main.py`:

```python
# app/main.py

import logging
from uuid import UUID
from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.models import DiagnosisRequest, DiagnosisResponse, HealthStatus
from app.agents import orchestrator

# Optional imports for ML and Analytics agents
try:
    from app.ml_agent import ml_agent
    ML_AGENT_AVAILABLE = True
except ImportError:
    ML_AGENT_AVAILABLE = False
    logging.warning("ML Agent not available")

try:
    from app.analytics_agent import analytics_agent
    ANALYTICS_AGENT_AVAILABLE = True
except ImportError:
    ANALYTICS_AGENT_AVAILABLE = False
    logging.warning("Analytics Agent not available")

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Security
security = HTTPBearer()

# =============================================================================
# FastAPI APPLICATION
# =============================================================================

app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION,
    description="""
    Manufacturing Copilot API - AI-powered equipment diagnosis and maintenance guidance.
    
    ## Features
    - 🔍 Visual inspection using Vision-Language Models
    - 📚 Knowledge retrieval from SOPs and manuals (RAG)
    - 📝 Structured maintenance report generation
    - 🤖 Predictive maintenance using Machine Learning
    - 📊 Historical analytics and insights
    
    ## Workflow
    1. Submit equipment issue with optional image
    2. AI agents analyze the problem
    3. Receive comprehensive diagnosis and recommendations
    """,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =============================================================================
# AUTHENTICATION
# =============================================================================

def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)) -> str:
    """
    Verify the authentication token.
    
    In production, this would:
    - Validate JWT tokens
    - Check against database
    - Verify permissions
    
    Args:
        credentials: HTTP Bearer token
        
    Returns:
        User identifier
        
    Raises:
        HTTPException: If authentication fails
    """
    token = credentials.credentials
    
    # Simple validation: check prefix
    if not token.startswith(settings.VALID_AUTH_TOKEN_PREFIX.replace("Bearer ", "")):
        logger.warning(f"Invalid token prefix: {token[:20]}...")
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication token"
        )
    
    logger.info(f"Authenticated request with token: {token[:20]}...")
    return token

# =============================================================================
# API ENDPOINTS
# =============================================================================

@app.get("/health", response_model=HealthStatus, tags=["Health"])
async def health_check():
    """
    Health check endpoint.
    
    Returns:
        HealthStatus: Simple status response
    """
    logger.info("Health check requested")
    return HealthStatus(status="ok")

@app.post("/v1/diagnose", response_model=DiagnosisResponse, tags=["Diagnosis"])
async def diagnose_equipment(
    request: DiagnosisRequest,
    user: str = Depends(verify_token)
) -> DiagnosisResponse:
    """
    Main diagnosis endpoint - orchestrates all AI agents.
    
    This endpoint:
    1. Validates the request
    2. Runs Vision Agent (if image provided)
    3. Runs RAG Agent (retrieves relevant documentation)
    4. Runs Report Agent (generates structured report)
    5. Optionally runs ML Agent (predictive maintenance)
    6. Optionally runs Analytics Agent (historical insights)
    
    Args:
        request: DiagnosisRequest with equipment details
        user: Authenticated user (from dependency)
        
    Returns:
        DiagnosisResponse with comprehensive diagnosis
        
    Raises:
        HTTPException: If diagnosis fails
    """
    logger.info(
        f"Diagnosis request for equipment {request.equipment_id} "
        f"at plant {request.plant_id}"
    )
    
    try:
        # Run main diagnostic workflow
        result = orchestrator.diagnose(
            plant_id=request.plant_id,
            equipment_id=request.equipment_id,
            problem_description=request.problem_description,
            image_id=request.image_id
        )
        
        # Prepare response
        response = DiagnosisResponse(
            request_id=UUID(result["request_id"]),
            vision_analysis=result["vision_analysis"],
            rag_guidance=result["rag_guidance"],
            generated_report=result["generated_report"],
            confidence_score=result["confidence_score"],
            safety_disclaimer="Always follow standard safety procedures"
        )
        
        # Add ML prediction if available
        if ML_AGENT_AVAILABLE:
            try:
                ml_prediction = ml_agent.predict(
                    equipment_id=request.equipment_id,
                    sensor_data={}  # Would come from real-time sensors
                )
                response.ml_prediction = ml_prediction
                logger.info("ML prediction added to response")
            except Exception as e:
                logger.error(f"ML prediction failed: {e}")
        
        # Add analytics insights if available
        if ANALYTICS_AGENT_AVAILABLE:
            try:
                analytics = analytics_agent.get_equipment_insights(
                    equipment_id=request.equipment_id
                )
                response.analytics_insights = analytics
                logger.info("Analytics insights added to response")
            except Exception as e:
                logger.error(f"Analytics retrieval failed: {e}")
        
        logger.info(f"Diagnosis complete for request {result['request_id']}")
        return response
        
    except Exception as e:
        logger.error(f"Diagnosis failed: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Diagnosis failed: {str(e)}"
        )

@app.post("/v1/predict", tags=["Machine Learning"])
async def predict_failure(
    equipment_id: str,
    user: str = Depends(verify_token)
):
    """
    Predict equipment failure probability.
    
    Args:
        equipment_id: Equipment identifier
        user: Authenticated user
        
    Returns:
        ML prediction with risk level and recommendations
    """
    if not ML_AGENT_AVAILABLE:
        raise HTTPException(
            status_code=503,
            detail="ML Agent not available"
        )
    
    logger.info(f"Prediction request for equipment {equipment_id}")
    
    try:
        # In production, sensor_data would come from real-time streaming
        sensor_data = {}  # Placeholder
        
        prediction = ml_agent.predict(
            equipment_id=equipment_id,
            sensor_data=sensor_data
        )
        
        logger.info(f"Prediction complete for {equipment_id}")
        return prediction
        
    except Exception as e:
        logger.error(f"Prediction failed: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )

@app.get("/v1/analytics/{equipment_id}", tags=["Analytics"])
async def get_analytics(
    equipment_id: str,
    user: str = Depends(verify_token)
):
    """
    Get historical analytics and insights for equipment.
    
    Args:
        equipment_id: Equipment identifier
        user: Authenticated user
        
    Returns:
        Analytics insights with trends and KPIs
    """
    if not ANALYTICS_AGENT_AVAILABLE:
        raise HTTPException(
            status_code=503,
            detail="Analytics Agent not available"
        )
    
    logger.info(f"Analytics request for equipment {equipment_id}")
    
    try:
        insights = analytics_agent.get_equipment_insights(equipment_id)
        
        logger.info(f"Analytics retrieved for {equipment_id}")
        return insights
        
    except Exception as e:
        logger.error(f"Analytics retrieval failed: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Analytics retrieval failed: {str(e)}"
        )

# =============================================================================
# STARTUP/SHUTDOWN EVENTS
# =============================================================================

@app.on_event("startup")
async def startup_event():
    """Run on application startup."""
    logger.info("=" * 60)
    logger.info(f"{settings.APP_TITLE} v{settings.APP_VERSION}")
    logger.info("=" * 60)
    logger.info("Application starting up...")
    logger.info(f"Log level: {settings.LOG_LEVEL}")
    logger.info(f"ML Agent available: {ML_AGENT_AVAILABLE}")
    logger.info(f"Analytics Agent available: {ANALYTICS_AGENT_AVAILABLE}")
    logger.info("Ready to serve requests!")

@app.on_event("shutdown")
async def shutdown_event():
    """Run on application shutdown."""
    logger.info("Application shutting down...")
    # Cleanup resources if needed
    logger.info("Shutdown complete")

# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Enable auto-reload during development
        log_level=settings.LOG_LEVEL.lower()
    )
```

## Understanding the Code

### 1. Application Structure

```python
app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION,
    description="...",
    docs_url="/docs",      # Swagger UI at /docs
    redoc_url="/redoc"     # ReDoc at /redoc
)
```

**What This Does**:
- Creates FastAPI application instance
- Configures automatic documentation
- Sets metadata (title, version, description)

**Try It**: After running the app, visit http://localhost:8000/docs to see interactive API documentation!

### 2. CORS Middleware

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (dev only!)
    ...
)
```

**What is CORS?**
- Cross-Origin Resource Sharing
- Security feature that restricts which websites can call your API
- Needed if frontend is on different domain than backend

**Production Configuration**:
```python
allow_origins=[
    "https://yourfrontend.com",
    "https://app.yourcompany.com"
]
```

### 3. Authentication

```python
def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    
    if not token.startswith("technician-"):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    return token
```

**How It Works**:
1. Client sends request with header: `Authorization: Bearer technician-12345`
2. FastAPI extracts token using `HTTPBearer()`
3. `verify_token()` validates the token
4. If valid, request proceeds; if not, returns 401 error

**Production Implementation**:
```python
# Use JWT tokens instead
import jwt

def verify_token(credentials):
    token = credentials.credentials
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("sub")
        return user_id
    except jwt.ExpiredSignatureError:
        raise HTTPException(401, "Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(401, "Invalid token")
```

### 4. Endpoint Patterns

#### Pattern 1: Simple GET Endpoint
```python
@app.get("/health", response_model=HealthStatus)
async def health_check():
    return HealthStatus(status="ok")
```

**Use Case**: Health checks, status endpoints

#### Pattern 2: POST with Authentication
```python
@app.post("/v1/diagnose", response_model=DiagnosisResponse)
async def diagnose_equipment(
    request: DiagnosisRequest,
    user: str = Depends(verify_token)
):
    ...
```

**Features**:
- Automatic request body validation (Pydantic)
- Automatic authentication check
- Automatic response validation

#### Pattern 3: Path Parameters
```python
@app.get("/v1/analytics/{equipment_id}")
async def get_analytics(equipment_id: str, ...):
    ...
```

**Use Case**: RESTful resource URLs

### 5. Error Handling

```python
try:
    result = orchestrator.diagnose(...)
    return DiagnosisResponse(...)
    
except Exception as e:
    logger.error(f"Diagnosis failed: {e}", exc_info=True)
    raise HTTPException(
        status_code=500,
        detail=f"Diagnosis failed: {str(e)}"
    )
```

**Best Practices**:
- Always log errors with `exc_info=True` (includes stack trace)
- Return user-friendly error messages
- Use appropriate HTTP status codes
- Never expose internal errors to users in production

### 6. Lifecycle Events

```python
@app.on_event("startup")
async def startup_event():
    logger.info("Starting up...")
    # Initialize connections, load models, etc.

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")
    # Cleanup: close connections, save state, etc.
```

**Use Cases**:
- Database connection pooling
- Model loading
- Cache warming
- Graceful shutdown

## Step 2: Testing the API

Create `tests/test_api.py`:

```python
# tests/test_api.py

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    """Test health check endpoint."""
    response = client.get("/health")
    
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_diagnose_without_auth():
    """Test that diagnosis requires authentication."""
    response = client.post(
        "/v1/diagnose",
        json={
            "plant_id": "PUNE-IN",
            "equipment_id": "CNC-A-102",
            "problem_description": "Machine making noise"
        }
    )
    
    assert response.status_code == 403  # Forbidden

def test_diagnose_with_auth():
    """Test diagnosis with authentication."""
    response = client.post(
        "/v1/diagnose",
        json={
            "plant_id": "PUNE-IN",
            "equipment_id": "CNC-A-102",
            "problem_description": "Machine making noise"
        },
        headers={"Authorization": "Bearer technician-12345"}
    )
    
    assert response.status_code == 200
    data = response.json()
    
    assert "request_id" in data
    assert "vision_analysis" in data
    assert "rag_guidance" in data
    assert "generated_report" in data
    assert "confidence_score" in data
    assert 0 <= data["confidence_score"] <= 1

def test_invalid_request():
    """Test that invalid requests are rejected."""
    response = client.post(
        "/v1/diagnose",
        json={
            "plant_id": "INVALID",  # Should match pattern ^[A-Z]{3,4}-\w{2,3}$
            "equipment_id": "C",    # Too short (min 4 chars)
            "problem_description": ""  # Required field
        },
        headers={"Authorization": "Bearer technician-12345"}
    )
    
    assert response.status_code == 422  # Validation error

def test_openapi_docs():
    """Test that API documentation is available."""
    response = client.get("/openapi.json")
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["info"]["title"] == "Manufacturing Copilot API"
    assert "paths" in data
    assert "/v1/diagnose" in data["paths"]
```

Run tests:
```powershell
pytest tests/test_api.py -v
```

## Step 3: Running the Application

### Development Mode

```powershell
# Ensure virtual environment is activated
.\venv\Scripts\Activate.ps1

# Run with auto-reload
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Or use the built-in method
python app/main.py
```

**What `--reload` Does**: Automatically restarts server when code changes

### Production Mode

```powershell
# Install production server
pip install gunicorn

# Run with multiple workers
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

# Explanation:
# -w 4: 4 worker processes (use CPU count * 2 + 1)
# -k uvicorn.workers.UvicornWorker: Use Uvicorn worker class
# --bind 0.0.0.0:8000: Listen on all interfaces, port 8000
```

## Step 4: Testing with cURL

### Health Check
```powershell
curl http://localhost:8000/health
```

Expected response:
```json
{"status": "ok"}
```

### Diagnosis Request
```powershell
curl -X POST http://localhost:8000/v1/diagnose `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer technician-12345" `
  -d '{
    "plant_id": "PUNE-IN",
    "equipment_id": "CNC-A-102",
    "problem_description": "Machine making strange noise from bearing assembly",
    "image_id": "IMG_001"
  }'
```

### Using PowerShell's Invoke-RestMethod
```powershell
$headers = @{
    "Authorization" = "Bearer technician-12345"
    "Content-Type" = "application/json"
}

$body = @{
    plant_id = "PUNE-IN"
    equipment_id = "CNC-A-102"
    problem_description = "Machine making strange noise"
    image_id = "IMG_001"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/v1/diagnose" `
                  -Method Post `
                  -Headers $headers `
                  -Body $body
```

## Step 5: Interactive API Testing

Visit http://localhost:8000/docs in your browser. You'll see:

1. **Swagger UI** - Interactive API documentation
   - Click on any endpoint to expand
   - Click "Try it out"
   - Fill in parameters
   - Click "Execute"
   - See response in real-time

2. **Authentication**
   - Click "Authorize" button (top right)
   - Enter: `technician-12345`
   - All subsequent requests will include auth

3. **Schemas**
   - Scroll down to see all Pydantic models
   - Shows validation rules
   - Example values

## Common Issues & Solutions

### Issue 1: Port Already in Use

**Error**: `OSError: [WinError 10048] Only one usage of each socket address`

**Solution**:
```powershell
# Find process using port 8000
netstat -ano | findstr :8000

# Kill the process (replace PID with actual process ID)
taskkill /PID <PID> /F

# Or use a different port
uvicorn app.main:app --port 8001
```

### Issue 2: Import Errors

**Error**: `ModuleNotFoundError: No module named 'app'`

**Solution**:
```powershell
# Ensure you're in the project root
cd c:\path\to\manufacturing-copilot

# Add current directory to PYTHONPATH
$env:PYTHONPATH = (Get-Location).Path

# Run with python -m
python -m uvicorn app.main:app --reload
```

### Issue 3: HuggingFace Token Not Found

**Error**: `ValidationError: field required (type=value_error.missing)`

**Solution**:
```powershell
# Check .env file exists
ls .env

# Verify token is set
cat .env | findstr HUGGINGFACE_TOKEN

# If missing, add it
"HUGGINGFACE_TOKEN=hf_your_token_here" | Out-File -Append .env
```

## Performance Optimization

### 1. Caching
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def get_rag_response(query: str):
    # Expensive operation
    return rag_agent.retrieve_guidance(query)
```

### 2. Async/Await
```python
# If you have async operations
@app.post("/v1/diagnose")
async def diagnose_equipment(...):
    # Run agents in parallel
    vision_task = asyncio.create_task(vision_agent.analyze(...))
    rag_task = asyncio.create_task(rag_agent.retrieve(...))
    
    vision_result, rag_result = await asyncio.gather(vision_task, rag_task)
```

### 3. Connection Pooling
```python
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

engine = create_engine(
    settings.DATABASE_URL,
    poolclass=QueuePool,
    pool_size=10,
    max_overflow=20
)
```

## ✅ Phase 4 Checkpoint

You should now have:
- [ ] `app/main.py` - Complete FastAPI application
- [ ] `tests/test_api.py` - API tests
- [ ] Application running locally
- [ ] API documentation accessible at /docs
- [ ] All endpoints tested and working
- [ ] Authentication working

**Test Checklist**:
```powershell
# 1. Health check
curl http://localhost:8000/health

# 2. API documentation
start http://localhost:8000/docs

# 3. Run tests
pytest tests/test_api.py -v

# 4. Test diagnosis endpoint
# Use Swagger UI at /docs or cURL command above
```

**Next**: Phase 5 - Machine Learning Integration

