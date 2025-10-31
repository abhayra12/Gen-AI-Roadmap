# 🏗️ Building the Manufacturing Copilot from Scratch
## A Complete Step-by-Step Implementation Guide

> **Purpose**: This guide will walk you through building the entire Manufacturing Copilot project from the ground up, one component at a time. Perfect for learning and understanding every piece of the system.

---

## 📚 Table of Contents

1. [Overview & Learning Path](#-overview--learning-path)
2. [Prerequisites](#-prerequisites)
3. [Phase 1: Project Setup & Environment](#phase-1-project-setup--environment-30-minutes)
4. [Phase 2: Configuration Management](#phase-2-configuration-management-20-minutes)
5. [Phase 3: Data Models & Validation](#phase-3-data-models--validation-30-minutes)
6. [Phase 4: Security & Authentication](#phase-4-security--authentication-20-minutes)
7. [Phase 5: Build the Vision Agent](#phase-5-build-the-vision-agent-45-minutes)
8. [Phase 6: Build the RAG Agent](#phase-6-build-the-rag-agent-90-minutes)
9. [Phase 7: Build the Report Agent](#phase-7-build-the-report-agent-30-minutes)
10. [Phase 8: LangGraph Orchestration](#phase-8-langgraph-orchestration-60-minutes)
11. [Phase 9: FastAPI Backend](#phase-9-fastapi-backend-45-minutes)
12. [Phase 10: Testing](#phase-10-testing-60-minutes)
13. [Phase 11: Docker & Containerization](#phase-11-docker--containerization-30-minutes)
14. [Phase 12: Kubernetes Deployment](#phase-12-kubernetes-deployment-60-minutes)
15. [Testing Your Complete System](#-testing-your-complete-system)
16. [Troubleshooting Guide](#-troubleshooting-guide)
17. [Next Steps & Enhancements](#-next-steps--enhancements)

**Total Time Estimate**: 9-12 hours (can be spread over multiple days)

---

## 🎯 Overview & Learning Path

### What You'll Build

A **production-grade AI system** with:
- 🤖 **3 Specialized AI Agents** (Vision, RAG, Report)
- 🔗 **LangGraph Orchestration** (sequential workflow)
- 🚀 **FastAPI REST API** (with authentication)
- 📦 **Vector Database** (ChromaDB for RAG)
- 🐳 **Docker Containers** (for deployment)
- ☸️ **Kubernetes Manifests** (for production)

### Architecture You'll Implement

```
User Request
    ↓
FastAPI (Authentication + Validation)
    ↓
LangGraph Orchestrator
    ↓
┌────────────────────────────────────┐
│  Vision Agent (BLIP-2)             │ → Analyzes images
└────────────────────────────────────┘
    ↓
┌────────────────────────────────────┐
│  RAG Agent (Llama-2 + ChromaDB)    │ → Retrieves docs & generates guidance
└────────────────────────────────────┘
    ↓
┌────────────────────────────────────┐
│  Report Agent (Llama-2)            │ → Creates incident report
└────────────────────────────────────┘
    ↓
JSON Response
```

### Skills You'll Learn

✅ Multi-agent system design  
✅ LangGraph state management  
✅ RAG implementation with ChromaDB  
✅ HuggingFace Inference API integration  
✅ FastAPI production patterns  
✅ Docker containerization  
✅ Kubernetes deployment  

---

## 📋 Prerequisites

### Required Knowledge (from your course)

- ✅ **Week 1-2**: Python basics, OOP
- ✅ **Week 3-4**: Neural networks, transformers
- ✅ **Week 5-6**: LLMs, RAG concepts
- ✅ **Week 7-8**: LangChain, agents
- ✅ **Week 11-12**: FastAPI, deployment

### Tools You Need

| Tool | Version | Purpose | Install Link |
|------|---------|---------|--------------|
| Python | 3.11+ | Programming language | [python.org](https://python.org) |
| Git | Latest | Version control | [git-scm.com](https://git-scm.com) |
| VS Code | Latest | Code editor | [code.visualstudio.com](https://code.visualstudio.com) |
| Docker Desktop | Latest | Containerization | [docker.com](https://docker.com) |
| Postman | Latest | API testing | [postman.com](https://postman.com) |

### Accounts You Need

1. **HuggingFace** (Required)
   - Sign up: https://huggingface.co/join
   - Create API token: https://huggingface.co/settings/tokens
   - Accept Llama-2 license: https://huggingface.co/meta-llama/Llama-2-7b-chat-hf

2. **GitHub** (Optional)
   - For version control and CI/CD

3. **Google Cloud** (Optional)
   - For Cloud Run deployment

---

## Phase 1: Project Setup & Environment (30 minutes)

### Step 1.1: Create Project Structure

```powershell
# Create project directory
mkdir manufacturing-copilot
cd manufacturing-copilot

# Create folder structure
mkdir app, tests, scripts, kubernetes, terraform, .github\workflows

# Create subdirectories
mkdir app\functions, app\functions\feedback
mkdir scripts\kubernetes
mkdir terraform\modules, terraform\modules\cloud_run, terraform\modules\secrets

# Create empty files
New-Item -ItemType File -Path app\__init__.py
New-Item -ItemType File -Path app\main.py
New-Item -ItemType File -Path app\agents.py
New-Item -ItemType File -Path app\config.py
New-Item -ItemType File -Path app\models.py
New-Item -ItemType File -Path app\security.py

New-Item -ItemType File -Path tests\__init__.py
New-Item -ItemType File -Path tests\conftest.py
New-Item -ItemType File -Path tests\test_api.py
New-Item -ItemType File -Path tests\test_models.py
New-Item -ItemType File -Path tests\test_security.py

New-Item -ItemType File -Path requirements.txt
New-Item -ItemType File -Path requirements-dev.txt
New-Item -ItemType File -Path .env.example
New-Item -ItemType File -Path .gitignore
New-Item -ItemType File -Path Dockerfile
New-Item -ItemType File -Path docker-compose.yml
New-Item -ItemType File -Path README.md
```

### Step 1.2: Create Virtual Environment

```powershell
# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\Activate.ps1

# Upgrade pip
python -m pip install --upgrade pip
```

### Step 1.3: Create requirements.txt

```powershell
# Create requirements.txt
@"
# Manufacturing Copilot API - Requirements
# Production dependencies

# Web Framework
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
pydantic-settings==2.1.0

# AI/ML Libraries - HuggingFace Ecosystem
transformers==4.35.2
sentence-transformers==2.2.2
huggingface-hub==0.19.4

# LangChain with HuggingFace Integration
langchain==0.1.0
langchain-community==0.0.10
langchain-huggingface==0.0.1
langgraph==0.0.20

# Vector Database
chromadb==0.4.18

# Utilities
python-dotenv==1.0.0
python-multipart==0.0.6
httpx==0.25.2
requests==2.31.0

# Monitoring & Logging
prometheus-fastapi-instrumentator==6.1.0
"@ | Out-File -FilePath requirements.txt -Encoding UTF8
```

### Step 1.4: Create requirements-dev.txt

```powershell
@"
-r requirements.txt

# Testing
pytest==7.4.3
pytest-asyncio==0.21.1
pytest-cov==4.1.0
httpx==0.25.2

# Code Quality
black==23.11.0
flake8==6.1.0
mypy==1.7.1
isort==5.12.0

# Development Tools
ipython==8.18.1
ipdb==0.13.13
"@ | Out-File -FilePath requirements-dev.txt -Encoding UTF8
```

### Step 1.5: Install Dependencies

```powershell
# Install production dependencies
pip install -r requirements.txt

# Install dev dependencies (optional)
pip install -r requirements-dev.txt
```

### Step 1.6: Create .gitignore

```powershell
@"
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/
*.egg-info/
dist/
build/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Environment
.env
.env.local

# ChromaDB
chroma_db/

# Logs
*.log
logs/

# Testing
.pytest_cache/
htmlcov/
.coverage
.tox/

# Docker
*.tar

# Kubernetes
secrets.yaml
"@ | Out-File -FilePath .gitignore -Encoding UTF8
```

### ✅ Checkpoint 1

Verify your setup:

```powershell
# Check Python version
python --version  # Should be 3.11+

# Check installed packages
pip list | Select-String "fastapi|langchain|chromadb"

# Directory structure
tree /F  # Should match the structure created
```

---

## Phase 2: Configuration Management (20 minutes)

### Step 2.1: Create .env.example

Create `c:\Users\abhay.ahirkar\OneDrive - TRIDIAGONAL.AI PRIVATE LIMITED\learning\Gen AI\T_Tech\manufacturing-copilot\.env.example`:

```env
# Application Settings
APP_TITLE=Manufacturing Copilot API
APP_VERSION=1.0.0
LOG_LEVEL=INFO

# HuggingFace Configuration (REQUIRED)
HUGGINGFACE_TOKEN=hf_your_token_here

# Model Configuration
VLM_MODEL_ID=Salesforce/blip2-opt-2.7b
LLM_MODEL_ID=meta-llama/Llama-2-7b-chat-hf
EMBEDDING_MODEL_ID=sentence-transformers/all-MiniLM-L6-v2

# API Configuration
MAX_RETRIES=3
REQUEST_TIMEOUT=30
TEMPERATURE=0.7
MAX_TOKENS=512

# ChromaDB Configuration
CHROMA_PERSIST_DIR=./chroma_db

# Authentication
VALID_AUTH_TOKEN_PREFIX=Bearer technician-

# Database (Optional)
DATABASE_URL=postgresql://copilot:copilot_pwd@localhost:5432/manufacturing_db
```

### Step 2.2: Create Your Actual .env File

```powershell
# Copy example to .env
Copy-Item .env.example .env

# Open .env in notepad to add your HuggingFace token
notepad .env
```

**Important**: Replace `hf_your_token_here` with your actual HuggingFace token!

### Step 2.3: Implement Configuration Module

Create `app/config.py`:

```python
# app/config.py

import os
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    """Application configuration settings."""
    
    # Application
    APP_TITLE: str = "Manufacturing Copilot API"
    APP_VERSION: str = "1.0.0"
    LOG_LEVEL: str = Field(default="INFO", env="LOG_LEVEL")
    
    # Security
    VALID_AUTH_TOKEN_PREFIX: str = "Bearer technician-"
    
    # HuggingFace Configuration (REQUIRED)
    HUGGINGFACE_TOKEN: str = Field(..., env="HUGGINGFACE_TOKEN")
    
    # Model Configuration
    VLM_MODEL_ID: str = Field(
        default="Salesforce/blip2-opt-2.7b", 
        env="VLM_MODEL_ID"
    )
    LLM_MODEL_ID: str = Field(
        default="meta-llama/Llama-2-7b-chat-hf", 
        env="LLM_MODEL_ID"
    )
    EMBEDDING_MODEL_ID: str = Field(
        default="sentence-transformers/all-MiniLM-L6-v2", 
        env="EMBEDDING_MODEL_ID"
    )
    
    # API Configuration
    MAX_RETRIES: int = Field(default=3, env="MAX_RETRIES")
    REQUEST_TIMEOUT: int = Field(default=30, env="REQUEST_TIMEOUT")
    TEMPERATURE: float = Field(default=0.7, env="TEMPERATURE")
    MAX_TOKENS: int = Field(default=512, env="MAX_TOKENS")
    
    # ChromaDB Configuration
    CHROMA_PERSIST_DIR: str = Field(
        default="./chroma_db", 
        env="CHROMA_PERSIST_DIR"
    )
    
    # Database (Optional)
    DATABASE_URL: str = Field(
        default="postgresql://copilot:copilot_pwd@localhost:5432/manufacturing_db",
        env="DATABASE_URL"
    )

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": False
    }

# Create global settings instance
settings = Settings()
```

### ✅ Checkpoint 2

Test your configuration:

```powershell
# Create test script
@"
from app.config import settings

print(f"App Title: {settings.APP_TITLE}")
print(f"HF Token: {settings.HUGGINGFACE_TOKEN[:10]}...")
print(f"LLM Model: {settings.LLM_MODEL_ID}")
print(f"ChromaDB Path: {settings.CHROMA_PERSIST_DIR}")
"@ | Out-File -FilePath test_config.py -Encoding UTF8

# Run test
python test_config.py

# Clean up
Remove-Item test_config.py
```

---

## Phase 3: Data Models & Validation (30 minutes)

### Step 3.1: Create Pydantic Models

Create `app/models.py`:

```python
# app/models.py

from typing import List, Optional, Dict, Any
from uuid import UUID
from pydantic import BaseModel, Field, validator

class DiagnosisRequest(BaseModel):
    """Request model for the main diagnosis endpoint."""
    
    plant_id: str = Field(
        ...,
        pattern=r"^[A-Z]{3,4}-\w{2,3}$",
        description="Unique plant identifier, e.g., 'PUNE-IN' or 'MEX-GTO'.",
        examples=["PUNE-IN"],
    )
    
    equipment_id: str = Field(
        ..., 
        min_length=4, 
        description="Tag or ID of the equipment.", 
        examples=["CNC-A-102"]
    )
    
    problem_description: str = Field(
        ...,
        min_length=10,
        max_length=500,
        description="Technician's description of the issue.",
        examples=["Machine overheating during operation"]
    )
    
    image_id: Optional[str] = Field(
        None, 
        description="ID of the uploaded image for visual inspection.",
        examples=["img_12345"]
    )
    
    @validator("problem_description")
    def sanitize_description(cls, v):
        """Prevent injection attacks."""
        dangerous_chars = ["<", ">", "{", "}", ";", "`"]
        for char in dangerous_chars:
            if char in v:
                raise ValueError(
                    f"Invalid character '{char}' in problem description"
                )
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
                "plant_id": "PUNE-IN",
                "equipment_id": "CNC-A-102",
                "problem_description": "Machine overheating during operation",
                "image_id": "img_12345"
            }
        }


class VisionAnalysisResult(BaseModel):
    """Result from Vision Agent."""
    
    defects_found: List[str] = Field(
        default_factory=list,
        description="List of detected defects"
    )
    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Confidence score for the analysis"
    )
    model_used: str = Field(
        ...,
        description="Vision model identifier"
    )
    image_analyzed: Optional[str] = Field(
        None,
        description="ID of the analyzed image"
    )


class RAGGuidanceResult(BaseModel):
    """Result from RAG Agent."""
    
    recommended_steps: List[str] = Field(
        default_factory=list,
        description="Step-by-step maintenance guidance"
    )
    cited_documents: List[str] = Field(
        default_factory=list,
        description="SOP document IDs referenced"
    )
    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Confidence in the guidance"
    )


class DiagnosisResponse(BaseModel):
    """Response model containing the combined output from all agents."""
    
    request_id: UUID = Field(
        ...,
        description="Unique identifier for this request"
    )
    
    vision_analysis: Dict[str, Any] = Field(
        ...,
        description="Results from Vision Agent"
    )
    
    rag_guidance: Dict[str, Any] = Field(
        ...,
        description="Guidance from RAG Agent"
    )
    
    generated_report: str = Field(
        ...,
        description="Incident report from Report Agent"
    )
    
    confidence_score: float = Field(
        ..., 
        ge=0.0, 
        le=1.0, 
        description="Overall confidence in the recommendation"
    )
    
    safety_disclaimer: str = Field(
        default="Always follow standard safety procedures and consult a supervisor if unsure.",
        description="Safety warning"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "request_id": "123e4567-e89b-12d3-a456-426614174000",
                "vision_analysis": {
                    "defects_found": ["micro-fracture", "surface-roughness"],
                    "confidence": 0.87,
                    "model_used": "Salesforce/blip2-opt-2.7b",
                    "image_analyzed": "img_12345"
                },
                "rag_guidance": {
                    "recommended_steps": [
                        "1. Check coolant levels",
                        "2. Inspect coolant lines",
                        "3. Verify pump operation"
                    ],
                    "cited_documents": ["SOP-123", "MAINT-GUIDE-V2"],
                    "confidence": 0.85
                },
                "generated_report": "MANUFACTURING INCIDENT REPORT\n\nSUMMARY: ...",
                "confidence_score": 0.86,
                "safety_disclaimer": "Always follow standard safety procedures..."
            }
        }


class HealthStatus(BaseModel):
    """Response model for the health check endpoint."""
    status: str = "ok"
```

### Step 3.2: Test Your Models

Create a test script:

```python
# Create test_models_manual.py
from app.models import DiagnosisRequest, DiagnosisResponse
from uuid import uuid4

# Test valid request
try:
    request = DiagnosisRequest(
        plant_id="PUNE-IN",
        equipment_id="CNC-A-102",
        problem_description="Machine overheating during operation",
        image_id="img_001"
    )
    print("✅ Valid request created:", request.plant_id)
except Exception as e:
    print("❌ Error:", e)

# Test invalid plant_id
try:
    request = DiagnosisRequest(
        plant_id="invalid",
        equipment_id="CNC-A-102",
        problem_description="Machine overheating during operation"
    )
except Exception as e:
    print("✅ Correctly rejected invalid plant_id:", str(e)[:50])

# Test injection attempt
try:
    request = DiagnosisRequest(
        plant_id="PUNE-IN",
        equipment_id="CNC-A-102",
        problem_description="Machine <script>alert('xss')</script>"
    )
except Exception as e:
    print("✅ Correctly rejected injection attempt:", str(e)[:50])

print("\n✅ All model validations working correctly!")
```

Run the test:

```powershell
python test_models_manual.py
Remove-Item test_models_manual.py
```

### ✅ Checkpoint 3

You should see:
- ✅ Valid request created successfully
- ✅ Invalid formats rejected
- ✅ Injection attempts blocked

---

## Phase 4: Security & Authentication (20 minutes)

### Step 4.1: Implement Authentication

Create `app/security.py`:

```python
# app/security.py

import logging
from fastapi import Header, HTTPException, status
from .config import settings

logger = logging.getLogger("manufacturing_copilot_api")


async def authorize_request(x_auth_token: str = Header(...)) -> str:
    """
    Validates bearer token authentication.
    
    Expected format: "Bearer technician-<user_id>"
    
    In production, replace with:
    - OAuth2/OIDC
    - API key management system
    - JWT validation
    
    Args:
        x_auth_token: Authorization header value
        
    Returns:
        user_id: Extracted user identifier
        
    Raises:
        HTTPException: If token is invalid
    """
    logger.debug(f"Validating auth token: {x_auth_token[:20]}...")
    
    # Check if token has the correct prefix
    if not x_auth_token.startswith(settings.VALID_AUTH_TOKEN_PREFIX):
        logger.warning(f"Invalid token format received")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token format",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Extract user_id (everything after "Bearer technician-")
    try:
        user_id = x_auth_token.replace(settings.VALID_AUTH_TOKEN_PREFIX, "")
        
        if not user_id or len(user_id) < 3:
            raise ValueError("User ID too short")
        
        logger.info(f"Authenticated user: {user_id}")
        return user_id
        
    except Exception as e:
        logger.error(f"Token validation error: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
            headers={"WWW-Authenticate": "Bearer"},
        )


def validate_api_key(api_key: str) -> bool:
    """
    Validates API key (alternative authentication method).
    
    In production, check against database or secret manager.
    
    Args:
        api_key: API key to validate
        
    Returns:
        bool: True if valid
    """
    # TODO: Implement actual API key validation
    # For now, accept any key starting with "mk_"
    return api_key.startswith("mk_")
```

### Step 4.2: Test Authentication

Create test script:

```python
# test_security_manual.py
from app.security import authorize_request
from fastapi import HTTPException
import asyncio

async def test_auth():
    # Test valid token
    try:
        user = await authorize_request("Bearer technician-john-doe")
        print(f"✅ Valid token accepted: {user}")
    except HTTPException as e:
        print(f"❌ Unexpected error: {e.detail}")
    
    # Test invalid token
    try:
        user = await authorize_request("InvalidToken")
        print(f"❌ Should have rejected invalid token")
    except HTTPException as e:
        print(f"✅ Correctly rejected invalid token: {e.detail}")
    
    # Test empty token
    try:
        user = await authorize_request("Bearer technician-")
        print(f"❌ Should have rejected empty user_id")
    except HTTPException as e:
        print(f"✅ Correctly rejected empty user_id: {e.detail}")

asyncio.run(test_auth())
```

Run the test:

```powershell
python test_security_manual.py
Remove-Item test_security_manual.py
```

### ✅ Checkpoint 4

You should see:
- ✅ Valid tokens accepted
- ✅ Invalid tokens rejected
- ✅ Security validations working

---

## Phase 5: Build the Vision Agent (45 minutes)

### Step 5.1: Understand the Vision Agent

**Purpose**: Analyze equipment images for manufacturing defects using Vision-Language Models (VLM)

**Model**: BLIP-2 (Salesforce/blip2-opt-2.7b)
- Vision + Language understanding
- Can answer questions about images
- Detects visual defects

### Step 5.2: Implement Vision Agent (Simplified Version)

Start with a simulated version, then we'll add real HuggingFace integration.

Add to `app/agents.py`:

```python
# app/agents.py
"""
Manufacturing Copilot Agents using HuggingFace Inference Endpoints.
"""

import logging
from typing import Dict, Any, Optional
from .config import settings

logger = logging.getLogger("manufacturing_copilot_api")


# ============================================================================
# VISION AGENT - Defect Detection
# ============================================================================

class VisionAgent:
    """
    Vision Agent for manufacturing defect detection.
    Uses HuggingFace VLM (BLIP-2) to analyze product images.
    """
    
    def __init__(self):
        """Initialize VLM endpoint."""
        self.model_id = settings.VLM_MODEL_ID
        self.hf_token = settings.HUGGINGFACE_TOKEN
        logger.info(f"Vision Agent initialized with model: {self.model_id}")
    
    async def analyze_image(
        self, 
        image_id: Optional[str], 
        equipment_id: str,
        problem_description: str
    ) -> Dict[str, Any]:
        """
        Analyze product image for manufacturing defects.
        
        Args:
            image_id: ID of the image to analyze
            equipment_id: Equipment that produced the product
            problem_description: Description of the problem
            
        Returns:
            Dict containing defects found and confidence scores
        """
        try:
            logger.info(f"Analyzing image {image_id} for equipment {equipment_id}")
            
            # If no image provided, return empty analysis
            if not image_id:
                return {
                    "defects_found": [],
                    "confidence": 0.0,
                    "model_used": self.model_id,
                    "image_analyzed": None,
                    "note": "No image provided for analysis"
                }
            
            # Simulated analysis based on equipment type
            # TODO: Replace with actual HuggingFace API call
            defect_keywords = {
                "CNC": ["micro-fracture", "surface-roughness"],
                "WELDING": ["weld-porosity", "incomplete-fusion"],
                "ASSEMBLY": ["misalignment", "missing-component"],
                "COATING": ["surface-discoloration", "coating-thickness-variation"],
            }
            
            # Detect equipment type and return relevant defects
            detected_defects = []
            for equip_type, defects in defect_keywords.items():
                if equip_type in equipment_id.upper():
                    detected_defects = defects[:2]  # Return top 2 defects
                    break
            
            # If no match, use generic defects
            if not detected_defects:
                detected_defects = ["visual-anomaly"]
            
            return {
                "defects_found": detected_defects,
                "confidence": 0.87,
                "model_used": self.model_id,
                "image_analyzed": image_id,
                "analysis_method": "simulated"  # TODO: Remove when using real API
            }
            
        except Exception as e:
            logger.error(f"Vision Agent error: {e}")
            return {
                "defects_found": [],
                "confidence": 0.0,
                "model_used": self.model_id,
                "image_analyzed": image_id,
                "error": str(e)
            }
```

### Step 5.3: Test Vision Agent

Create test script:

```python
# test_vision_agent.py
import asyncio
from app.agents import VisionAgent

async def test_vision():
    agent = VisionAgent()
    
    # Test with CNC equipment
    result = await agent.analyze_image(
        image_id="img_001",
        equipment_id="CNC-A-102",
        problem_description="Overheating"
    )
    print("CNC Analysis:", result)
    
    # Test with WELDING equipment
    result = await agent.analyze_image(
        image_id="img_002",
        equipment_id="WELDING-B-205",
        problem_description="Poor weld quality"
    )
    print("Welding Analysis:", result)
    
    # Test without image
    result = await agent.analyze_image(
        image_id=None,
        equipment_id="CNC-A-102",
        problem_description="Overheating"
    )
    print("No Image Analysis:", result)

asyncio.run(test_vision())
```

Run test:

```powershell
python test_vision_agent.py
Remove-Item test_vision_agent.py
```

### ✅ Checkpoint 5

You should see:
- ✅ CNC defects detected (micro-fracture, surface-roughness)
- ✅ Welding defects detected (weld-porosity, incomplete-fusion)
- ✅ Empty analysis when no image provided

---

## Phase 6: Build the RAG Agent (90 minutes)

This is the most complex agent! Take your time here.

### Step 6.1: Understand RAG Architecture

```
User Query: "CNC machine overheating"
    ↓
Embedding Model: Convert to vector (384 dimensions)
    ↓
ChromaDB: Find similar SOP documents
    ↓
Retrieved Docs: "SOP-123: CNC Troubleshooting", "MAINT-GUIDE-V2"
    ↓
LLM (Llama-2): Generate guidance using retrieved context
    ↓
Output: Step-by-step maintenance guidance + citations
```

### Step 6.2: Create Sample SOP Documents

Add to `app/agents.py`:

```python
# Add after VisionAgent class

# ============================================================================
# SAMPLE SOP DOCUMENTS
# ============================================================================

SAMPLE_SOP_DOCUMENTS = [
    {
        "doc_id": "SOP-123",
        "title": "CNC Machine Troubleshooting Guide",
        "content": """
        CNC MACHINE TROUBLESHOOTING - SOP-123
        
        OVERHEATING ISSUES:
        1. Check coolant levels in the reservoir - should be above minimum mark
        2. Inspect coolant lines for leaks, cracks, or blockages
        3. Verify coolant pump operation - listen for unusual noises
        4. Check coolant filter - replace if clogged
        5. Inspect spindle bearings for wear - excessive heat indicates damage
        6. Verify cutting parameters - reduce feed rate if excessive
        7. Check ambient temperature - ensure adequate ventilation
        
        SURFACE DEFECTS:
        1. Inspect cutting tool condition - replace if worn or chipped
        2. Verify tool alignment and tool offset settings
        3. Check workpiece clamping - ensure rigid setup
        4. Review cutting parameters - adjust speed and feed
        5. Verify material specifications match program
        
        DIMENSIONAL ISSUES:
        1. Perform machine calibration using precision test bar
        2. Check ballscrew backlash - adjust if exceeding tolerance
        3. Verify encoder function - replace if faulty
        4. Inspect linear guides for wear
        5. Check thermal expansion compensation settings
        
        PREVENTIVE MAINTENANCE:
        - Daily: Check coolant level, clean chip conveyor
        - Weekly: Lubricate guide ways, check air pressure
        - Monthly: Replace coolant, inspect filters
        - Quarterly: Calibrate machine, update parameters
        """
    },
    {
        "doc_id": "MAINT-GUIDE-V2",
        "title": "Welding Equipment Maintenance Manual",
        "content": """
        WELDING EQUIPMENT MAINTENANCE - MAINT-GUIDE-V2
        
        WELD QUALITY ISSUES:
        1. Check electrode condition - replace if contaminated or worn
        2. Verify welding parameters - voltage, current, travel speed
        3. Inspect gas flow rate - adjust to manufacturer specifications
        4. Check ground connection - ensure proper electrical contact
        5. Verify wire feed speed - adjust for consistent arc
        6. Clean welding tip and nozzle - remove spatter buildup
        
        POROSITY PROBLEMS:
        1. Inspect shielding gas supply - check for leaks
        2. Verify gas purity - replace if contaminated
        3. Clean base material - remove rust, paint, oil
        4. Check gas flow rate - typically 15-20 CFH for MIG
        5. Inspect torch angle - maintain proper technique
        6. Reduce travel speed if gas coverage insufficient
        
        INCOMPLETE FUSION:
        1. Increase heat input - adjust voltage/current
        2. Reduce travel speed - allow proper penetration
        3. Clean joint preparation - remove mill scale
        4. Verify electrode angle - maintain 15-30 degrees
        5. Check for fit-up gaps - should be within tolerance
        
        EQUIPMENT CHECKS:
        - Pre-shift: Verify gas pressure, check connections
        - Daily: Clean equipment, inspect cables
        - Weekly: Test ground clamp, check wire feeder
        - Monthly: Calibrate voltage/current, replace consumables
        """
    },
    {
        "doc_id": "SOP-456",
        "title": "Assembly Line Quality Control",
        "content": """
        ASSEMBLY LINE QUALITY CONTROL - SOP-456
        
        ALIGNMENT ISSUES:
        1. Use precision measuring tools - dial indicators, gauges
        2. Check fixture condition - replace worn locating pins
        3. Verify torque specifications - use calibrated torque wrench
        4. Inspect fasteners - replace if damaged threads
        5. Follow proper assembly sequence per engineering drawings
        6. Verify component orientation before tightening
        
        MISSING COMPONENTS:
        1. Implement visual inspection at each station
        2. Use work instruction sheets with checkboxes
        3. Perform end-of-line verification
        4. Utilize poka-yoke (error-proofing) devices
        5. Conduct random audits throughout shift
        
        TORQUE VERIFICATION:
        1. Calibrate torque tools monthly
        2. Record torque values for critical fasteners
        3. Use torque marker paint for visual verification
        4. Re-torque after initial run-in period
        5. Check for proper torque sequence (star pattern)
        
        QUALITY GATES:
        - Station 1: Component verification
        - Station 2: Alignment check
        - Station 3: Torque verification
        - Final: 100% functional test
        """
    },
    {
        "doc_id": "COATING-MANUAL-2024",
        "title": "Surface Coating Application Guidelines",
        "content": """
        SURFACE COATING GUIDELINES - COATING-MANUAL-2024
        
        SURFACE PREPARATION:
        1. Clean surface - remove oil, grease, and contaminants
        2. Abrasive blast to specified profile (2-3 mils)
        3. Remove blast media residue with clean, dry air
        4. Verify surface cleanliness using solvent wipe test
        5. Check surface temperature - must be above dew point
        6. Apply coating within 4 hours of surface prep
        
        COATING APPLICATION:
        1. Mix coating per manufacturer instructions
        2. Check viscosity using Zahn cup
        3. Maintain spray gun distance (6-8 inches)
        4. Apply in thin, uniform coats
        5. Allow flash time between coats (10-15 minutes)
        6. Measure wet film thickness with comb gauge
        
        THICKNESS VERIFICATION:
        1. Use dry film thickness (DFT) gauge
        2. Target: 3-5 mils per coat
        3. Take minimum 5 readings per square meter
        4. Document all measurements
        5. Apply additional coats if below specification
        
        ENVIRONMENTAL CONDITIONS:
        - Temperature: 50-90°F optimal
        - Humidity: Below 85% RH
        - Surface temp: 5°F above dew point minimum
        
        DEFECT PREVENTION:
        - Orange peel: Adjust spray pressure, reduce viscosity
        - Runs/sags: Reduce film thickness, increase flash time
        - Pinholing: Improve surface prep, reduce application speed
        """
    },
    {
        "doc_id": "SAFETY-SOP-001",
        "title": "Emergency Response Procedures",
        "content": """
        EMERGENCY RESPONSE PROCEDURES - SAFETY-SOP-001
        
        EQUIPMENT EMERGENCY SHUTDOWN:
        1. Press emergency stop button (red mushroom)
        2. Isolate power supply - turn off circuit breaker
        3. Tag out using lockout/tagout procedure
        4. Notify supervisor and maintenance immediately
        5. Clear area of personnel
        6. Document incident in logbook
        
        FIRE RESPONSE:
        1. Activate fire alarm
        2. Use appropriate fire extinguisher (Class A/B/C)
        3. Evacuate if fire cannot be controlled
        4. Close fire doors behind you
        5. Muster at designated assembly point
        6. Do NOT re-enter until cleared by emergency response
        
        CHEMICAL SPILL:
        1. Evacuate affected area
        2. Alert others using proper channels
        3. Consult SDS (Safety Data Sheet) for chemical
        4. Use spill kit for small spills (< 1 gallon)
        5. Contact HAZMAT team for large spills
        6. Document spill details and cleanup actions
        
        PERSONAL PROTECTIVE EQUIPMENT (PPE):
        - Safety glasses: Required in all production areas
        - Steel-toed boots: Required on shop floor
        - Hearing protection: Required near equipment > 85dB
        - Gloves: Required when handling sharp or hot materials
        - Face shield: Required during grinding operations
        
        LOCKOUT/TAGOUT:
        1. Notify affected employees
        2. Shutdown equipment using normal procedures
        3. Isolate all energy sources
        4. Apply lockout devices
        5. Attach personal tag with date/name
        6. Verify zero energy state before work
        """
    }
]
```

### Step 6.3: Implement RAG Agent

Add to `app/agents.py`:

```python
# Add these imports at the top
from langchain_huggingface import HuggingFaceEndpoint, HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

# Add after SAMPLE_SOP_DOCUMENTS

# ============================================================================
# RAG AGENT - Retrieval-Augmented Generation
# ============================================================================

class RAGAgent:
    """
    RAG Agent for maintenance guidance.
    Uses Llama-2 LLM + ChromaDB for document retrieval.
    """
    
    def __init__(self):
        """Initialize RAG components."""
        try:
            logger.info("Initializing RAG Agent...")
            
            # 1. Initialize embeddings model
            logger.info(f"Loading embeddings: {settings.EMBEDDING_MODEL_ID}")
            self.embeddings = HuggingFaceEmbeddings(
                model_name=settings.EMBEDDING_MODEL_ID,
                model_kwargs={"device": "cpu"},
                encode_kwargs={"normalize_embeddings": True}
            )
            
            # 2. Initialize vector database
            logger.info(f"Initializing ChromaDB at: {settings.CHROMA_PERSIST_DIR}")
            self.vectorstore = Chroma(
                collection_name="manufacturing_sops",
                embedding_function=self.embeddings,
                persist_directory=settings.CHROMA_PERSIST_DIR
            )
            
            # 3. Populate knowledge base (if empty)
            self._populate_sample_docs()
            
            # 4. Initialize LLM
            logger.info(f"Initializing LLM: {settings.LLM_MODEL_ID}")
            self.llm = HuggingFaceEndpoint(
                repo_id=settings.LLM_MODEL_ID,
                huggingfacehub_api_token=settings.HUGGINGFACE_TOKEN,
                temperature=settings.TEMPERATURE,
                max_new_tokens=settings.MAX_TOKENS,
                timeout=settings.REQUEST_TIMEOUT
            )
            
            # 5. Create retrieval chain
            self.retrieval_chain = self._create_retrieval_chain()
            
            logger.info("✅ RAG Agent initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize RAG Agent: {e}")
            raise
    
    def _populate_sample_docs(self):
        """Populate ChromaDB with sample SOP documents."""
        try:
            # Check if collection already has documents
            collection_count = self.vectorstore._collection.count()
            
            if collection_count > 0:
                logger.info(f"ChromaDB already contains {collection_count} documents")
                return
            
            logger.info("Populating ChromaDB with sample SOPs...")
            
            # Convert SOPs to LangChain Documents
            documents = []
            for sop in SAMPLE_SOP_DOCUMENTS:
                doc = Document(
                    page_content=sop["content"],
                    metadata={
                        "doc_id": sop["doc_id"],
                        "title": sop["title"],
                        "type": "SOP"
                    }
                )
                documents.append(doc)
            
            # Add to vectorstore
            self.vectorstore.add_documents(documents)
            logger.info(f"✅ Added {len(documents)} SOP documents to ChromaDB")
            
        except Exception as e:
            logger.error(f"Error populating SOPs: {e}")
            # Don't raise - allow agent to continue with empty DB
    
    def _create_retrieval_chain(self):
        """Creates LangChain RAG pipeline."""
        
        # Create retriever (finds relevant documents)
        retriever = self.vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 3}  # Retrieve top 3 relevant docs
        )
        
        # Create prompt template
        template = """You are an expert manufacturing technician assistant.
Use the following maintenance documentation to answer the question.
Provide clear, step-by-step guidance based on the documentation.

Documentation:
{context}

Question: {question}

Instructions:
1. Provide step-by-step maintenance guidance
2. Reference the SOP document IDs you used
3. Be specific and actionable
4. If documentation doesn't cover the issue, say so

Guidance:"""
        
        prompt = PromptTemplate(
            template=template,
            input_variables=["context", "question"]
        )
        
        # Create the chain
        chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | self.llm
            | StrOutputParser()
        )
        
        return chain
    
    async def get_guidance(
        self, 
        query: str,
        vision_results: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Retrieve relevant docs and generate maintenance guidance.
        
        Args:
            query: Problem description
            vision_results: Optional vision analysis results
            
        Returns:
            Dict with recommended steps and cited documents
        """
        try:
            logger.info(f"RAG query: {query[:100]}...")
            
            # Enhance query with vision results if available
            enhanced_query = query
            if vision_results and vision_results.get("defects_found"):
                defects = ", ".join(vision_results["defects_found"])
                enhanced_query = f"{query}. Visual defects observed: {defects}"
            
            # Invoke RAG chain
            response = await asyncio.to_thread(
                self.retrieval_chain.invoke,
                enhanced_query
            )
            
            # Parse response into steps
            steps = self._parse_steps(response)
            
            # Extract cited documents
            cited_docs = self._extract_cited_docs(response)
            
            return {
                "recommended_steps": steps,
                "cited_documents": cited_docs,
                "confidence": 0.85,
                "raw_response": response
            }
            
        except Exception as e:
            logger.error(f"RAG Agent error: {e}")
            return self._fallback_guidance(query)
    
    def _parse_steps(self, response: str) -> List[str]:
        """Parse response into numbered steps."""
        steps = []
        lines = response.split('\n')
        
        for line in lines:
            line = line.strip()
            # Look for numbered steps or bullet points
            if line and (
                line[0].isdigit() or 
                line.startswith('-') or 
                line.startswith('•') or
                line.startswith('*')
            ):
                steps.append(line)
        
        # If no structured steps found, split into sentences
        if not steps:
            sentences = response.split('.')
            steps = [s.strip() + '.' for s in sentences if len(s.strip()) > 20]
        
        return steps[:10]  # Return max 10 steps
    
    def _extract_cited_docs(self, response: str) -> List[str]:
        """Extract SOP document IDs from response."""
        cited = []
        
        # Look for SOP document IDs in response
        for sop in SAMPLE_SOP_DOCUMENTS:
            if sop["doc_id"] in response:
                cited.append(sop["doc_id"])
        
        return cited
    
    def _fallback_guidance(self, query: str) -> Dict[str, Any]:
        """Fallback guidance when RAG fails."""
        return {
            "recommended_steps": [
                "1. Ensure equipment is safely shut down and locked out",
                "2. Consult the equipment manual for troubleshooting guidance",
                "3. Contact maintenance supervisor for expert assistance",
                "4. Document all observations and actions taken"
            ],
            "cited_documents": [],
            "confidence": 0.3,
            "note": "Fallback guidance - RAG system temporarily unavailable"
        }


# Add import at top
import asyncio
```

### Step 6.4: Test RAG Agent

Create test script:

```python
# test_rag_agent.py
import asyncio
from app.agents import RAGAgent

async def test_rag():
    print("Initializing RAG Agent (this may take 30-60 seconds on first run)...")
    agent = RAGAgent()
    
    print("\n" + "="*60)
    print("TEST 1: CNC Overheating")
    print("="*60)
    result = await agent.get_guidance(
        query="CNC machine is overheating during operation",
        vision_results={"defects_found": ["surface-roughness"]}
    )
    print(f"\nRecommended Steps:")
    for step in result["recommended_steps"]:
        print(f"  {step}")
    print(f"\nCited Documents: {result['cited_documents']}")
    print(f"Confidence: {result['confidence']}")
    
    print("\n" + "="*60)
    print("TEST 2: Welding Quality Issues")
    print("="*60)
    result = await agent.get_guidance(
        query="Welding equipment producing porous welds"
    )
    print(f"\nRecommended Steps:")
    for step in result["recommended_steps"]:
        print(f"  {step}")
    print(f"\nCited Documents: {result['cited_documents']}")
    
    print("\n✅ RAG Agent tests complete!")

asyncio.run(test_rag())
```

Run test (this will take 1-2 minutes on first run):

```powershell
python test_rag_agent.py
```

**Note**: First run will be slow (30-60 seconds) because:
1. Downloads embedding model (~90MB)
2. Populates ChromaDB with SOPs
3. Initializes HuggingFace Inference API

### ✅ Checkpoint 6

You should see:
- ✅ RAG Agent initialized successfully
- ✅ ChromaDB populated with 5 SOPs
- ✅ Relevant maintenance steps retrieved
- ✅ SOP documents cited (e.g., "SOP-123")

---

## Phase 7: Build the Report Agent (30 minutes)

### Step 7.1: Implement Report Agent

Add to `app/agents.py`:

```python
# Add after RAGAgent class

# ============================================================================
# REPORT AGENT - Incident Report Generation
# ============================================================================

class ReportAgent:
    """
    Report Agent for generating incident reports.
    Uses Llama-2 to create structured, professional reports.
    """
    
    def __init__(self):
        """Initialize LLM for report generation."""
        try:
            logger.info("Initializing Report Agent...")
            
            self.llm = HuggingFaceEndpoint(
                repo_id=settings.LLM_MODEL_ID,
                huggingfacehub_api_token=settings.HUGGINGFACE_TOKEN,
                temperature=0.5,  # Slightly lower for more consistent reports
                max_new_tokens=700,  # Longer for full reports
                timeout=settings.REQUEST_TIMEOUT
            )
            
            logger.info("✅ Report Agent initialized")
            
        except Exception as e:
            logger.error(f"Failed to initialize Report Agent: {e}")
            raise
    
    async def generate_report(self, state: Dict[str, Any]) -> str:
        """
        Generate incident report from diagnosis results.
        
        Args:
            state: Dictionary containing all diagnosis data
            
        Returns:
            Formatted incident report string
        """
        try:
            logger.info("Generating incident report...")
            
            # Extract data from state
            plant_id = state.get("plant_id", "Unknown")
            equipment_id = state.get("equipment_id", "Unknown")
            problem = state.get("problem_description", "Not specified")
            
            vision = state.get("vision_analysis", {})
            rag = state.get("rag_guidance", {})
            
            defects = vision.get("defects_found", [])
            steps = rag.get("recommended_steps", [])
            docs = rag.get("cited_documents", [])
            
            # Build prompt
            prompt = f"""Generate a professional manufacturing incident report.

INCIDENT DETAILS:
- Plant ID: {plant_id}
- Equipment ID: {equipment_id}
- Problem Description: {problem}

VISUAL INSPECTION:
- Defects Found: {', '.join(defects) if defects else 'None'}
- Confidence: {vision.get('confidence', 'N/A')}

TECHNICAL GUIDANCE:
{chr(10).join(steps) if steps else 'See supervisor'}

Documentation References: {', '.join(docs) if docs else 'None'}

Create a structured incident report with these sections:
1. SUMMARY (2-3 sentences overview)
2. DEFECTS IDENTIFIED (bullet points)
3. RECOMMENDED ACTIONS (numbered steps)
4. SAFETY NOTES (important warnings)
5. FOLLOW-UP REQUIRED (next steps)

Write professionally for maintenance logs.

INCIDENT REPORT:"""
            
            # Generate report
            report = await asyncio.to_thread(
                self.llm.invoke,
                prompt
            )
            
            # Clean up response
            report = report.strip()
            
            # Add header if not present
            if not report.startswith("MANUFACTURING INCIDENT REPORT"):
                report = "MANUFACTURING INCIDENT REPORT\n\n" + report
            
            logger.info("✅ Report generated successfully")
            return report
            
        except Exception as e:
            logger.error(f"Report Agent error: {e}")
            return self._fallback_report(state)
    
    def _fallback_report(self, state: Dict[str, Any]) -> str:
        """Generate basic report when LLM fails."""
        plant = state.get("plant_id", "Unknown")
        equipment = state.get("equipment_id", "Unknown")
        problem = state.get("problem_description", "Not specified")
        
        return f"""MANUFACTURING INCIDENT REPORT

SUMMARY:
Equipment {equipment} at plant {plant} requires maintenance attention.
Issue reported: {problem}

RECOMMENDED ACTIONS:
1. Safely shut down equipment
2. Contact maintenance supervisor
3. Consult equipment manual
4. Document all findings

SAFETY NOTES:
- Follow lockout/tagout procedures
- Wear appropriate PPE
- Do not attempt repairs without authorization

FOLLOW-UP REQUIRED:
- Supervisor approval needed
- Schedule maintenance window
- Update maintenance logs

Generated: Fallback report due to system issue
"""
```

### Step 7.2: Test Report Agent

Create test script:

```python
# test_report_agent.py
import asyncio
from app.agents import ReportAgent

async def test_report():
    print("Initializing Report Agent...")
    agent = ReportAgent()
    
    # Mock state data
    state = {
        "plant_id": "PUNE-IN",
        "equipment_id": "CNC-A-102",
        "problem_description": "Machine overheating during operation",
        "vision_analysis": {
            "defects_found": ["micro-fracture", "surface-roughness"],
            "confidence": 0.87
        },
        "rag_guidance": {
            "recommended_steps": [
                "1. Check coolant levels in the reservoir",
                "2. Inspect coolant lines for leaks",
                "3. Verify coolant pump operation"
            ],
            "cited_documents": ["SOP-123", "MAINT-GUIDE-V2"],
            "confidence": 0.85
        }
    }
    
    print("\nGenerating report (this may take 30-60 seconds)...")
    report = await agent.generate_report(state)
    
    print("\n" + "="*60)
    print("GENERATED REPORT:")
    print("="*60)
    print(report)
    print("="*60)
    print("\n✅ Report Agent test complete!")

asyncio.run(test_report())
```

Run test:

```powershell
python test_report_agent.py
```

### ✅ Checkpoint 7

You should see:
- ✅ Professional incident report generated
- ✅ All sections included (Summary, Defects, Actions, Safety, Follow-up)
- ✅ Referenced SOPs cited in report

---

Due to length constraints, I'll create this as a multi-part guide. Let me continue with the remaining phases in the file:

