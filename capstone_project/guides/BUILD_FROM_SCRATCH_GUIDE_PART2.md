# 🏗️ Building from Scratch - Part 2
## Phases 8-12: Integration, Testing, and Deployment

> **Continuation of BUILD_FROM_SCRATCH_GUIDE.md**

---

## Phase 8: LangGraph Orchestration (60 minutes)

### Step 8.1: Understand LangGraph

**LangGraph** orchestrates your agents in a **sequential workflow**:

```
Vision Agent → RAG Agent → Report Agent → END
```

Each agent adds its results to a **shared state** that flows through the graph.

### Step 8.2: Define State Schema

Add to `app/agents.py` (at the top, after imports):

```python
from typing import TypedDict, List, Annotated
import operator
from langgraph.graph import StateGraph, END
from uuid import uuid4


# ============================================================================
# STATE DEFINITION FOR LANGGRAPH
# ============================================================================

class AgentState(TypedDict):
    """State schema for the LangGraph workflow."""
    
    # Inputs (from user request)
    request_id: str
    plant_id: str
    equipment_id: str
    problem_description: str
    image_id: str
    
    # Agent Outputs
    vision_analysis: Dict[str, Any]
    rag_guidance: Dict[str, Any]
    generated_report: str
    
    # Metadata
    confidence_score: float
    errors: Annotated[List[str], operator.add]  # Accumulates errors
```

### Step 8.3: Create Agent Nodes

Add to `app/agents.py` (after all agent classes):

```python
# ============================================================================
# LANGGRAPH WORKFLOW
# ============================================================================

# Initialize agents globally
logger.info("Initializing agents...")
vision_agent = VisionAgent()
rag_agent = RAGAgent()
report_agent = ReportAgent()
logger.info("✅ All agents initialized")


# Define workflow nodes
async def vision_node(state: AgentState) -> AgentState:
    """Step 1: Analyze image for defects."""
    logger.info(f"[{state['request_id']}] Running Vision Agent...")
    
    try:
        vision_results = await vision_agent.analyze_image(
            image_id=state.get("image_id"),
            equipment_id=state["equipment_id"],
            problem_description=state["problem_description"]
        )
        state["vision_analysis"] = vision_results
        
    except Exception as e:
        logger.error(f"Vision node error: {e}")
        state["vision_analysis"] = {
            "defects_found": [],
            "confidence": 0.0,
            "error": str(e)
        }
        state["errors"].append(f"Vision: {str(e)}")
    
    return state


async def rag_node(state: AgentState) -> AgentState:
    """Step 2: Retrieve docs and generate guidance."""
    logger.info(f"[{state['request_id']}] Running RAG Agent...")
    
    try:
        rag_results = await rag_agent.get_guidance(
            query=state["problem_description"],
            vision_results=state.get("vision_analysis")
        )
        state["rag_guidance"] = rag_results
        
    except Exception as e:
        logger.error(f"RAG node error: {e}")
        state["rag_guidance"] = {
            "recommended_steps": ["Contact supervisor for assistance"],
            "cited_documents": [],
            "confidence": 0.0,
            "error": str(e)
        }
        state["errors"].append(f"RAG: {str(e)}")
    
    return state


async def report_node(state: AgentState) -> AgentState:
    """Step 3: Generate incident report."""
    logger.info(f"[{state['request_id']}] Running Report Agent...")
    
    try:
        report = await report_agent.generate_report(state)
        state["generated_report"] = report
        
        # Calculate overall confidence
        vision_conf = state["vision_analysis"].get("confidence", 0.0)
        rag_conf = state["rag_guidance"].get("confidence", 0.0)
        state["confidence_score"] = (vision_conf + rag_conf) / 2
        
    except Exception as e:
        logger.error(f"Report node error: {e}")
        state["generated_report"] = report_agent._fallback_report(state)
        state["confidence_score"] = 0.0
        state["errors"].append(f"Report: {str(e)}")
    
    return state


# Build the workflow graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("vision", vision_node)
workflow.add_node("rag", rag_node)
workflow.add_node("report", report_node)

# Define edges (execution order)
workflow.set_entry_point("vision")
workflow.add_edge("vision", "rag")
workflow.add_edge("rag", "report")
workflow.add_edge("report", END)

# Compile the graph
agent_graph = workflow.compile()

logger.info("✅ LangGraph workflow compiled")
```

### Step 8.4: Create Orchestration Function

Add to `app/agents.py` (after graph compilation):

```python
# ============================================================================
# MAIN ORCHESTRATION FUNCTION
# ============================================================================

async def run_copilot_inference(request: Any) -> Any:
    """
    Main function to run the multi-agent copilot.
    
    Args:
        request: DiagnosisRequest object
        
    Returns:
        DiagnosisResponse object
    """
    from .models import DiagnosisResponse
    from uuid import uuid4
    
    request_id = str(uuid4())
    logger.info(f"[{request_id}] Starting copilot inference")
    
    # Initialize state
    initial_state = {
        "request_id": request_id,
        "plant_id": request.plant_id,
        "equipment_id": request.equipment_id,
        "problem_description": request.problem_description,
        "image_id": request.image_id,
        "vision_analysis": {},
        "rag_guidance": {},
        "generated_report": "",
        "confidence_score": 0.0,
        "errors": []
    }
    
    # Run the graph
    try:
        final_state = await agent_graph.ainvoke(initial_state)
        
        logger.info(f"[{request_id}] Copilot inference complete")
        
        # Build response
        response = DiagnosisResponse(
            request_id=request_id,
            vision_analysis=final_state["vision_analysis"],
            rag_guidance=final_state["rag_guidance"],
            generated_report=final_state["generated_report"],
            confidence_score=final_state["confidence_score"],
            safety_disclaimer="Always follow standard safety procedures and consult a supervisor if unsure."
        )
        
        return response
        
    except Exception as e:
        logger.error(f"[{request_id}] Copilot inference failed: {e}")
        raise
```

### Step 8.5: Test Complete Workflow

Create test script:

```python
# test_workflow.py
import asyncio
from app.models import DiagnosisRequest
from app.agents import run_copilot_inference

async def test_workflow():
    print("="*70)
    print("TESTING COMPLETE MULTI-AGENT WORKFLOW")
    print("="*70)
    
    # Create test request
    request = DiagnosisRequest(
        plant_id="PUNE-IN",
        equipment_id="CNC-A-102",
        problem_description="Machine overheating during operation with visible surface defects",
        image_id="img_test_001"
    )
    
    print("\nRequest:")
    print(f"  Plant: {request.plant_id}")
    print(f"  Equipment: {request.equipment_id}")
    print(f"  Problem: {request.problem_description}")
    print(f"  Image: {request.image_id}")
    
    print("\n" + "-"*70)
    print("Running agents (this may take 1-2 minutes)...")
    print("-"*70)
    
    # Run workflow
    response = await run_copilot_inference(request)
    
    print("\n" + "="*70)
    print("RESULTS")
    print("="*70)
    
    print(f"\n📊 Request ID: {response.request_id}")
    print(f"\n👁️  VISION ANALYSIS:")
    print(f"  Defects: {response.vision_analysis.get('defects_found', [])}")
    print(f"  Confidence: {response.vision_analysis.get('confidence', 0):.2f}")
    
    print(f"\n📚 RAG GUIDANCE:")
    print(f"  Steps ({len(response.rag_guidance.get('recommended_steps', []))}):")
    for i, step in enumerate(response.rag_guidance.get('recommended_steps', [])[:5], 1):
        print(f"    {step[:80]}...")
    print(f"  Cited Docs: {response.rag_guidance.get('cited_documents', [])}")
    
    print(f"\n📝 GENERATED REPORT:")
    print(response.generated_report[:500] + "...")
    
    print(f"\n⭐ Overall Confidence: {response.confidence_score:.2f}")
    
    print("\n" + "="*70)
    print("✅ WORKFLOW TEST COMPLETE!")
    print("="*70)

asyncio.run(test_workflow())
```

Run test:

```powershell
python test_workflow.py
```

### ✅ Checkpoint 8

You should see:
- ✅ All three agents execute in sequence
- ✅ Vision → RAG → Report flow
- ✅ Complete diagnosis response with all sections
- ✅ Overall confidence score calculated

---

## Phase 9: FastAPI Backend (45 minutes)

### Step 9.1: Implement Main FastAPI App

Create/update `app/main.py`:

```python
# app/main.py

import time
import logging
from uuid import uuid4

from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .models import DiagnosisRequest, DiagnosisResponse, HealthStatus
from .security import authorize_request
from .agents import run_copilot_inference

# --- Application Setup ---
app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION,
    description="Multi-agent AI system for smart manufacturing diagnostics",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware (for web clients)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Logging Configuration ---
logging.basicConfig(
    level=settings.LOG_LEVEL.upper(),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("manufacturing_copilot_api")


# --- Middleware for Observability ---
@app.middleware("http")
async def add_observability_headers(request: Request, call_next):
    """
    Middleware to add custom headers for timing and tracing.
    """
    trace_id = str(uuid4())
    request.state.trace_id = trace_id
    
    start_time = time.perf_counter()
    
    # Process the request
    response = await call_next(request)
    
    # Calculate duration
    duration_ms = (time.perf_counter() - start_time) * 1000
    
    # Add custom headers
    response.headers["X-Request-Trace-ID"] = trace_id
    response.headers["X-Response-Time-ms"] = f"{duration_ms:.2f}"
    
    logger.info(
        f"{request.method} {request.url.path} completed in {duration_ms:.2f}ms",
        extra={"trace_id": trace_id, "duration_ms": duration_ms}
    )
    
    # Warn if latency exceeds SLA
    if duration_ms > 500:
        logger.warning(
            f"High latency: {duration_ms:.2f}ms on {request.url.path}",
            extra={"trace_id": trace_id}
        )
    
    return response


# --- API Endpoints ---

@app.get("/", tags=["Info"])
async def root():
    """Root endpoint with API information."""
    return {
        "name": settings.APP_TITLE,
        "version": settings.APP_VERSION,
        "status": "operational",
        "docs": "/docs"
    }


@app.get("/health", response_model=HealthStatus, tags=["Monitoring"])
async def health_check():
    """
    Health check endpoint for load balancers and monitoring.
    """
    return HealthStatus(status="ok")


@app.post("/v1/diagnose", response_model=DiagnosisResponse, tags=["Copilot"])
async def diagnose_problem(
    request: DiagnosisRequest,
    user_id: str = Depends(authorize_request)
):
    """
    Main endpoint to diagnose a manufacturing problem.
    
    This orchestrates Vision, RAG, and Report agents to provide
    comprehensive analysis and recommendations.
    
    **Authentication**: Requires Bearer token in X-Auth-Token header
    
    **Rate Limit**: TODO - Implement rate limiting
    """
    logger.info(
        f"Diagnosis request from user '{user_id}' for plant '{request.plant_id}'",
        extra={"user_id": user_id, "plant_id": request.plant_id}
    )
    
    try:
        # Run the multi-agent workflow
        response = await run_copilot_inference(request)
        
        logger.info(
            f"Diagnosis complete for {request.equipment_id}",
            extra={"confidence": response.confidence_score}
        )
        
        return response
        
    except Exception as e:
        logger.error(f"Diagnosis failed: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )


# --- Startup Event ---
@app.on_event("startup")
async def startup_event():
    """Initialize agents on startup."""
    logger.info(f"Starting {settings.APP_TITLE} v{settings.APP_VERSION}")
    logger.info("Agents initialized in agents.py module")


# --- Shutdown Event ---
@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown."""
    logger.info("Shutting down Manufacturing Copilot API")
```

### Step 9.2: Test FastAPI App

Start the server:

```powershell
# Start server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

The server should start successfully. You'll see:
```
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Step 9.3: Test with Swagger UI

1. Open your browser: http://localhost:8080/docs
2. You should see the interactive API documentation
3. Try the `/health` endpoint first (no auth needed)
4. Then try `/v1/diagnose` with authentication

### Step 9.4: Test with PowerShell

Open a **new PowerShell window** (keep server running):

```powershell
# Test health endpoint
Invoke-RestMethod -Uri "http://localhost:8080/health" -Method Get

# Test diagnosis endpoint
$headers = @{
    "X-Auth-Token" = "Bearer technician-john-doe"
    "Content-Type" = "application/json"
}

$body = @{
    plant_id = "PUNE-IN"
    equipment_id = "CNC-A-102"
    problem_description = "Machine overheating during operation"
    image_id = "img_test_001"
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri "http://localhost:8080/v1/diagnose" -Method Post -Headers $headers -Body $body

# Display results
Write-Host "`nRequest ID: $($response.request_id)"
Write-Host "Confidence Score: $($response.confidence_score)"
Write-Host "`nDefects Found:"
$response.vision_analysis.defects_found | ForEach-Object { Write-Host "  - $_" }
Write-Host "`nCited Documents:"
$response.rag_guidance.cited_documents | ForEach-Object { Write-Host "  - $_" }
```

### ✅ Checkpoint 9

You should see:
- ✅ FastAPI server running
- ✅ Swagger UI accessible
- ✅ Health check working
- ✅ Diagnosis endpoint returning complete responses
- ✅ Authentication working

---

## Phase 10: Testing (60 minutes)

### Step 10.1: Create Test Configuration

Create `tests/conftest.py`:

```python
# tests/conftest.py

import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    """Create test client."""
    return TestClient(app)


@pytest.fixture
def valid_auth_headers():
    """Valid authentication headers."""
    return {"X-Auth-Token": "Bearer technician-test-user"}


@pytest.fixture
def invalid_auth_headers():
    """Invalid authentication headers."""
    return {"X-Auth-Token": "InvalidToken"}


@pytest.fixture
def sample_diagnosis_request():
    """Sample valid diagnosis request."""
    return {
        "plant_id": "PUNE-IN",
        "equipment_id": "CNC-A-102",
        "problem_description": "Machine overheating during operation",
        "image_id": "img_test_001"
    }
```

### Step 10.2: Create API Tests

Create `tests/test_api.py`:

```python
# tests/test_api.py

import pytest
from fastapi import status


def test_root_endpoint(client):
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "name" in data
    assert "version" in data


def test_health_check(client):
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "ok"}


def test_diagnose_without_auth(client, sample_diagnosis_request):
    """Test diagnosis endpoint without authentication."""
    response = client.post("/v1/diagnose", json=sample_diagnosis_request)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_diagnose_with_invalid_auth(client, sample_diagnosis_request, invalid_auth_headers):
    """Test diagnosis endpoint with invalid authentication."""
    response = client.post(
        "/v1/diagnose",
        json=sample_diagnosis_request,
        headers=invalid_auth_headers
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_diagnose_with_valid_auth(client, sample_diagnosis_request, valid_auth_headers):
    """Test diagnosis endpoint with valid authentication."""
    response = client.post(
        "/v1/diagnose",
        json=sample_diagnosis_request,
        headers=valid_auth_headers
    )
    
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    assert "request_id" in data
    assert "vision_analysis" in data
    assert "rag_guidance" in data
    assert "generated_report" in data
    assert "confidence_score" in data
    
    # Check vision analysis structure
    assert "defects_found" in data["vision_analysis"]
    assert "confidence" in data["vision_analysis"]
    
    # Check RAG guidance structure
    assert "recommended_steps" in data["rag_guidance"]
    assert "cited_documents" in data["rag_guidance"]
    
    # Check confidence score range
    assert 0.0 <= data["confidence_score"] <= 1.0


def test_diagnose_invalid_plant_id(client, valid_auth_headers):
    """Test diagnosis with invalid plant_id format."""
    invalid_request = {
        "plant_id": "invalid",  # Wrong format
        "equipment_id": "CNC-A-102",
        "problem_description": "Test problem"
    }
    
    response = client.post(
        "/v1/diagnose",
        json=invalid_request,
        headers=valid_auth_headers
    )
    
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_diagnose_short_description(client, valid_auth_headers):
    """Test diagnosis with too short description."""
    invalid_request = {
        "plant_id": "PUNE-IN",
        "equipment_id": "CNC-A-102",
        "problem_description": "Short"  # Too short
    }
    
    response = client.post(
        "/v1/diagnose",
        json=invalid_request,
        headers=valid_auth_headers
    )
    
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_observability_headers(client, sample_diagnosis_request, valid_auth_headers):
    """Test that observability headers are added."""
    response = client.post(
        "/v1/diagnose",
        json=sample_diagnosis_request,
        headers=valid_auth_headers
    )
    
    assert "x-request-trace-id" in response.headers
    assert "x-response-time-ms" in response.headers
```

### Step 10.3: Create Model Tests

Create `tests/test_models.py`:

```python
# tests/test_models.py

import pytest
from pydantic import ValidationError
from app.models import DiagnosisRequest


def test_valid_diagnosis_request():
    """Test valid diagnosis request creation."""
    request = DiagnosisRequest(
        plant_id="PUNE-IN",
        equipment_id="CNC-A-102",
        problem_description="Machine overheating during operation",
        image_id="img_001"
    )
    
    assert request.plant_id == "PUNE-IN"
    assert request.equipment_id == "CNC-A-102"
    assert request.image_id == "img_001"


def test_invalid_plant_id_format():
    """Test that invalid plant_id format is rejected."""
    with pytest.raises(ValidationError):
        DiagnosisRequest(
            plant_id="invalid",  # Should match pattern ^[A-Z]{3,4}-\w{2,3}$
            equipment_id="CNC-A-102",
            problem_description="Test problem description"
        )


def test_short_equipment_id():
    """Test that short equipment_id is rejected."""
    with pytest.raises(ValidationError):
        DiagnosisRequest(
            plant_id="PUNE-IN",
            equipment_id="CNC",  # Too short (min 4 chars)
            problem_description="Test problem description"
        )


def test_short_description():
    """Test that short description is rejected."""
    with pytest.raises(ValidationError):
        DiagnosisRequest(
            plant_id="PUNE-IN",
            equipment_id="CNC-A-102",
            problem_description="Short"  # Too short (min 10 chars)
        )


def test_injection_prevention():
    """Test that injection attempts are blocked."""
    with pytest.raises(ValidationError) as exc_info:
        DiagnosisRequest(
            plant_id="PUNE-IN",
            equipment_id="CNC-A-102",
            problem_description="Test <script>alert('xss')</script>"
        )
    
    assert "Invalid character" in str(exc_info.value)


def test_optional_image_id():
    """Test that image_id is optional."""
    request = DiagnosisRequest(
        plant_id="PUNE-IN",
        equipment_id="CNC-A-102",
        problem_description="Test problem description"
        # image_id not provided
    )
    
    assert request.image_id is None
```

### Step 10.4: Create Security Tests

Create `tests/test_security.py`:

```python
# tests/test_security.py

import pytest
from fastapi import HTTPException
from app.security import authorize_request


@pytest.mark.asyncio
async def test_valid_token():
    """Test that valid tokens are accepted."""
    user_id = await authorize_request("Bearer technician-john-doe")
    assert user_id == "john-doe"


@pytest.mark.asyncio
async def test_invalid_token_format():
    """Test that invalid token format is rejected."""
    with pytest.raises(HTTPException) as exc_info:
        await authorize_request("InvalidToken")
    
    assert exc_info.value.status_code == 401


@pytest.mark.asyncio
async def test_empty_user_id():
    """Test that empty user_id is rejected."""
    with pytest.raises(HTTPException) as exc_info:
        await authorize_request("Bearer technician-")
    
    assert exc_info.value.status_code == 401


@pytest.mark.asyncio
async def test_short_user_id():
    """Test that too short user_id is rejected."""
    with pytest.raises(HTTPException) as exc_info:
        await authorize_request("Bearer technician-ab")
    
    assert exc_info.value.status_code == 401
```

### Step 10.5: Run All Tests

```powershell
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=app --cov-report=html --cov-report=term

# View coverage report
Start-Process "htmlcov\index.html"
```

### ✅ Checkpoint 10

You should see:
- ✅ All tests passing
- ✅ Test coverage report generated
- ✅ API tests validating endpoints
- ✅ Model tests validating data structures
- ✅ Security tests validating authentication

---

## Phase 11: Docker & Containerization (30 minutes)

### Step 11.1: Create Dockerfile

Create `Dockerfile` in project root:

```dockerfile
# Dockerfile

# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for Docker layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/
COPY .env.example .env

# Create directory for ChromaDB
RUN mkdir -p /app/chroma_db

# Expose port
EXPOSE 8080

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV LOG_LEVEL=INFO

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8080/health')"

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
```

### Step 11.2: Create Docker Compose

Create `docker-compose.yml`:

```yaml
# docker-compose.yml

version: '3.8'

services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: manufacturing-copilot
    ports:
      - "8080:8080"
    environment:
      - HUGGINGFACE_TOKEN=${HUGGINGFACE_TOKEN}
      - LOG_LEVEL=INFO
      - CHROMA_PERSIST_DIR=/app/chroma_db
    volumes:
      - ./chroma_db:/app/chroma_db  # Persist ChromaDB data
      - ./app:/app/app  # Mount code for development
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s

  # Optional: PostgreSQL database
  # postgres:
  #   image: postgres:15-alpine
  #   container_name: manufacturing-db
  #   environment:
  #     POSTGRES_USER: copilot
  #     POSTGRES_PASSWORD: copilot_pwd
  #     POSTGRES_DB: manufacturing_db
  #   ports:
  #     - "5432:5432"
  #   volumes:
  #     - postgres_data:/var/lib/postgresql/data
  #   restart: unless-stopped

# volumes:
#   postgres_data:
```

### Step 11.3: Create .dockerignore

Create `.dockerignore`:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
venv/
env/
ENV/

# Testing
.pytest_cache/
htmlcov/
.coverage
.tox/

# IDEs
.vscode/
.idea/
*.swp

# Git
.git/
.gitignore

# Environment
.env

# Docs
*.md
docs/

# Tests
tests/

# ChromaDB (will be created in container)
chroma_db/

# Kubernetes
kubernetes/
charts/

# Terraform
terraform/
```

### Step 11.4: Build and Test Docker Image

```powershell
# Build Docker image
docker build -t manufacturing-copilot:latest .

# Run container
docker run -p 8080:8080 `
  -e HUGGINGFACE_TOKEN="your_token_here" `
  manufacturing-copilot:latest

# Or use Docker Compose
docker-compose up --build
```

Test the containerized API:

```powershell
# In new PowerShell window
Invoke-RestMethod -Uri "http://localhost:8080/health"
```

### Step 11.5: Docker Commands Reference

```powershell
# View running containers
docker ps

# View logs
docker logs manufacturing-copilot -f

# Stop container
docker-compose down

# Remove all containers and volumes
docker-compose down -v

# Rebuild without cache
docker-compose build --no-cache
```

### ✅ Checkpoint 11

You should see:
- ✅ Docker image builds successfully
- ✅ Container starts and runs
- ✅ Health check passes
- ✅ API accessible from host machine

---

## Phase 12: Kubernetes Deployment (60 minutes)

### Step 12.1: Create Namespace

Create `kubernetes/namespace.yaml`:

```yaml
# kubernetes/namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: manufacturing-copilot
  labels:
    name: manufacturing-copilot
    app: manufacturing-copilot
```

### Step 12.2: Create Secret

Create `kubernetes/secret.yaml`:

```yaml
# kubernetes/secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: manufacturing-copilot-secrets
  namespace: manufacturing-copilot
type: Opaque
stringData:
  huggingface-token: "REPLACE_WITH_YOUR_TOKEN"
  # In production, use: kubectl create secret generic ... --from-literal=...
```

**Important**: Don't commit this file with real tokens! Add to `.gitignore`.

### Step 12.3: Create ConfigMap

Create `kubernetes/configmap.yaml`:

```yaml
# kubernetes/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: manufacturing-copilot-config
  namespace: manufacturing-copilot
data:
  APP_TITLE: "Manufacturing Copilot API"
  APP_VERSION: "1.0.0"
  LOG_LEVEL: "INFO"
  VLM_MODEL_ID: "Salesforce/blip2-opt-2.7b"
  LLM_MODEL_ID: "meta-llama/Llama-2-7b-chat-hf"
  EMBEDDING_MODEL_ID: "sentence-transformers/all-MiniLM-L6-v2"
  MAX_RETRIES: "3"
  REQUEST_TIMEOUT: "30"
  TEMPERATURE: "0.7"
  MAX_TOKENS: "512"
  CHROMA_PERSIST_DIR: "/app/chroma_db"
```

### Step 12.4: Create Deployment

Create `kubernetes/deployment.yaml`:

```yaml
# kubernetes/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: manufacturing-copilot
  namespace: manufacturing-copilot
  labels:
    app: manufacturing-copilot
spec:
  replicas: 2
  selector:
    matchLabels:
      app: manufacturing-copilot
  template:
    metadata:
      labels:
        app: manufacturing-copilot
    spec:
      containers:
      - name: api
        image: manufacturing-copilot:latest
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 8080
          name: http
        env:
        - name: HUGGINGFACE_TOKEN
          valueFrom:
            secretKeyRef:
              name: manufacturing-copilot-secrets
              key: huggingface-token
        envFrom:
        - configMapRef:
            name: manufacturing-copilot-config
        resources:
          requests:
            memory: "1Gi"
            cpu: "500m"
          limits:
            memory: "4Gi"
            cpu: "2000m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 60
          periodSeconds: 30
          timeoutSeconds: 10
          failureThreshold: 3
        readinessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3
        volumeMounts:
        - name: chroma-storage
          mountPath: /app/chroma_db
      volumes:
      - name: chroma-storage
        emptyDir: {}  # In production, use PersistentVolumeClaim
```

### Step 12.5: Create Service

Create `kubernetes/service.yaml`:

```yaml
# kubernetes/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: manufacturing-copilot
  namespace: manufacturing-copilot
  labels:
    app: manufacturing-copilot
spec:
  type: ClusterIP
  ports:
  - port: 8080
    targetPort: 8080
    protocol: TCP
    name: http
  selector:
    app: manufacturing-copilot
```

### Step 12.6: Deploy to Kubernetes

```powershell
# Apply all Kubernetes manifests
kubectl apply -f kubernetes/namespace.yaml
kubectl apply -f kubernetes/secret.yaml
kubectl apply -f kubernetes/configmap.yaml
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml

# Check status
kubectl get all -n manufacturing-copilot

# View logs
kubectl logs -f deployment/manufacturing-copilot -n manufacturing-copilot

# Port forward to test locally
kubectl port-forward svc/manufacturing-copilot 8080:8080 -n manufacturing-copilot
```

Test the deployment:

```powershell
# In new PowerShell window
Invoke-RestMethod -Uri "http://localhost:8080/health"
```

### ✅ Checkpoint 12

You should see:
- ✅ Namespace created
- ✅ Secrets and ConfigMaps created
- ✅ Deployment running with 2 replicas
- ✅ Service created and accessible
- ✅ API responding to requests

---

## 🎉 Testing Your Complete System

### End-to-End Test

```powershell
# Test complete workflow
$headers = @{
    "X-Auth-Token" = "Bearer technician-jane-smith"
    "Content-Type" = "application/json"
}

$body = @{
    plant_id = "PUNE-IN"
    equipment_id = "WELDING-B-205"
    problem_description = "Welding equipment producing porous welds with incomplete fusion"
    image_id = "img_weld_001"
} | ConvertTo-Json

$response = Invoke-RestMethod `
    -Uri "http://localhost:8080/v1/diagnose" `
    -Method Post `
    -Headers $headers `
    -Body $body

# Display full response
$response | ConvertTo-Json -Depth 10
```

### Performance Test

```powershell
# Simple load test (10 requests)
1..10 | ForEach-Object -Parallel {
    $headers = @{
        "X-Auth-Token" = "Bearer technician-test$_"
        "Content-Type" = "application/json"
    }
    
    $body = @{
        plant_id = "PUNE-IN"
        equipment_id = "CNC-A-102"
        problem_description = "Test request $_"
    } | ConvertTo-Json
    
    $response = Invoke-RestMethod `
        -Uri "http://localhost:8080/v1/diagnose" `
        -Method Post `
        -Headers $headers `
        -Body $body
    
    Write-Host "Request $_ completed"
} -ThrottleLimit 5
```

---

## 🐛 Troubleshooting Guide

### Common Issues

**Issue 1: "HUGGINGFACE_TOKEN not found"**
```powershell
# Solution: Check .env file
Get-Content .env | Select-String "HUGGINGFACE_TOKEN"

# Ensure no spaces around =
# Correct:   HUGGINGFACE_TOKEN=hf_abc123
# Incorrect: HUGGINGFACE_TOKEN = hf_abc123
```

**Issue 2: "ChromaDB collection error"**
```powershell
# Solution: Reset ChromaDB
Remove-Item -Recurse -Force chroma_db
# Restart application
```

**Issue 3: "Port 8080 already in use"**
```powershell
# Find process using port
Get-NetTCPConnection -LocalPort 8080 | Select-Object -Property OwningProcess

# Kill process
Stop-Process -Id <PID> -Force

# Or use different port
uvicorn app.main:app --port 8000
```

**Issue 4: "Model loading timeout"**
```
# Solution: Increase timeout in .env
REQUEST_TIMEOUT=90

# Or try smaller model
LLM_MODEL_ID=google/flan-t5-large
```

---

## 🚀 Next Steps & Enhancements

### Immediate Improvements

1. **Add Real Image Analysis**
   - Implement actual HuggingFace Vision API calls
   - Add image upload endpoint
   - Integrate with blob storage (AWS S3, Azure Blob)

2. **Implement Rate Limiting**
   ```python
   from slowapi import Limiter
   limiter = Limiter(key_func=get_remote_address)
   @app.post("/v1/diagnose")
   @limiter.limit("10/minute")
   async def diagnose(...):
   ```

3. **Add Caching**
   ```python
   from functools import lru_cache
   @lru_cache(maxsize=100)
   def cached_rag_query(query_hash):
   ```

4. **Database Integration**
   - Log all requests to PostgreSQL
   - Store feedback for model improvement
   - Track usage metrics

### Advanced Features

5. **Streaming Responses**
   ```python
   from fastapi.responses import StreamingResponse
   async def stream_diagnosis():
       yield vision_results
       yield rag_results
       yield report
   ```

6. **Multi-Language Support**
   - Add translation layer
   - Localized SOP documents
   - Language detection

7. **Advanced RAG Patterns**
   - Implement HyDE (Hypothetical Document Embeddings)
   - Add query rewriting
   - Implement RAG Fusion

8. **Monitoring & Observability**
   - Add Prometheus metrics
   - Implement distributed tracing (Jaeger)
   - Set up Grafana dashboards

9. **CI/CD Pipeline**
   - GitHub Actions for automated testing
   - Automated Docker builds
   - Kubernetes deployments via ArgoCD

10. **Production Hardening**
    - Add JWT authentication
    - Implement API key management
    - Add request validation middleware
    - Set up WAF (Web Application Firewall)

---

## 📚 Learning Resources

### Documentation
- **FastAPI**: https://fastapi.tiangolo.com/
- **LangChain**: https://python.langchain.com/
- **LangGraph**: https://langchain-ai.github.io/langgraph/
- **HuggingFace**: https://huggingface.co/docs
- **ChromaDB**: https://docs.trychroma.com/

### Course References
- Week 5-6: LLMs & RAG concepts
- Week 7-8: LangChain & Agents
- Week 11-12: Production deployment

---

## ✅ Final Checklist

Before considering the project complete:

- [ ] All 3 agents implemented and tested
- [ ] LangGraph workflow functional
- [ ] FastAPI backend running
- [ ] Authentication working
- [ ] All tests passing (>80% coverage)
- [ ] Docker image builds successfully
- [ ] Docker Compose working
- [ ] Kubernetes deployment successful
- [ ] Documentation complete
- [ ] Code committed to Git
- [ ] Environment variables documented
- [ ] README.md updated

---

## 🎓 What You've Learned

By completing this guide, you've:

✅ Built a **production-grade multi-agent system**  
✅ Implemented **RAG** with vector databases  
✅ Used **LangGraph** for agent orchestration  
✅ Created a **FastAPI** REST API  
✅ Containerized with **Docker**  
✅ Deployed to **Kubernetes**  
✅ Implemented **authentication** and **validation**  
✅ Written **comprehensive tests**  
✅ Set up **observability** and monitoring  
✅ Applied **software engineering best practices**  

**Congratulations! You've built a portfolio-ready AI project!** 🎉

---

**Questions?** Refer to:
- Main README.md
- IMPLEMENTATION_GUIDE.md
- KUBERNETES_DEPLOYMENT.md
- Course FAQ.md

**Built with ❤️ for the Gen AI Masters Program**
