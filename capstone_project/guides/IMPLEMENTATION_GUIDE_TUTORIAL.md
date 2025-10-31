# 🎓 Manufacturing Copilot: Complete Implementation Guide
## Build This Project From Scratch - Step by Step Tutorial

> **Your Personal Tutor**: This guide will walk you through building the complete Manufacturing Copilot system from an empty folder to a production-ready application. Perfect for learning!

---

## 📚 Table of Contents

1. [Prerequisites & Setup](#phase-1-prerequisites--setup)
2. [Project Foundation](#phase-2-project-foundation)
3. [GenAI Agents (Core)](#phase-3-genai-agents-core)
4. [FastAPI Backend](#phase-4-fastapi-backend)
5. [Machine Learning Integration](#phase-5-machine-learning-integration)
6. [Data Engineering Layer](#phase-6-data-engineering-layer)
7. [Testing & Validation](#phase-7-testing--validation)
8. [Dockerization](#phase-8-dockerization)
9. [Production Deployment](#phase-9-production-deployment)

---

## 🎯 Learning Objectives

By the end of this guide, you'll understand:
- ✅ How to build multi-agent AI systems with LangGraph
- ✅ How to implement RAG (Retrieval Augmented Generation)
- ✅ How to integrate ML models with GenAI
- ✅ How to build production-ready APIs with FastAPI
- ✅ How to set up real-time data pipelines with Kafka
- ✅ How to containerize and deploy ML applications

---

## 📖 How to Use This Guide

### Learning Modes

**🎓 Tutorial Mode** (Recommended for Beginners)
- Follow each phase sequentially
- Type out code manually (don't copy-paste)
- Understand each line before moving on
- Test after each phase

**🚀 Fast Track Mode** (For Experienced Developers)
- Skim through explanations
- Copy code blocks
- Focus on architecture decisions
- Jump to phases you need

**🔧 Reference Mode** (For Troubleshooting)
- Use table of contents to find specific topics
- Check "Common Issues" sections
- Review "Why This Matters" boxes

### Time Estimates

| Phase | Beginner | Intermediate | Advanced |
|-------|----------|--------------|----------|
| 1-2 | 2 hours | 1 hour | 30 min |
| 3-4 | 4 hours | 2 hours | 1 hour |
| 5-6 | 6 hours | 3 hours | 1.5 hours |
| 7-9 | 4 hours | 2 hours | 1 hour |
| **Total** | **16 hours** | **8 hours** | **4 hours** |

---

## Phase 1: Prerequisites & Setup

### 🎯 Goals
- Install required software
- Set up development environment
- Understand the project architecture

### 📦 Required Software

#### 1. Python 3.11+
```powershell
# Check Python version
python --version

# Should show: Python 3.11.x or higher
# If not, download from: https://www.python.org/downloads/
```

**Why This Matters**: Python 3.11+ provides better performance and type hints for modern AI libraries.

#### 2. Git
```powershell
# Check Git installation
git --version

# Download from: https://git-scm.com/downloads
```

#### 3. VS Code (Recommended)
- Download: https://code.visualstudio.com/
- Extensions to install:
  - Python (Microsoft)
  - Pylance (Microsoft)
  - Docker (Microsoft)
  - GitLens (Optional but helpful)

#### 4. Docker Desktop
```powershell
# Check Docker installation
docker --version
docker-compose --version

# Download from: https://www.docker.com/products/docker-desktop
# Allocate at least 8GB RAM (16GB recommended for full stack)
```

### 🔑 Required Accounts

#### 1. HuggingFace Account
1. Sign up: https://huggingface.co/join
2. Create API token: https://huggingface.co/settings/tokens
   - Click "New token"
   - Name: "manufacturing-copilot"
   - Type: Read
   - Copy and save the token (starts with `hf_`)

3. Accept Llama-2 license:
   - Visit: https://huggingface.co/meta-llama/Llama-2-7b-chat-hf
   - Click "Agree and access repository"

**Why This Matters**: We use HuggingFace Inference API to avoid needing expensive GPUs locally.

#### 2. Google Cloud (Optional for BigQuery)
- Sign up: https://console.cloud.google.com/
- $300 free credits available
- Only needed for production analytics

### ✅ Verification Checklist

Before proceeding, verify:
- [ ] Python 3.11+ installed
- [ ] Git installed
- [ ] VS Code installed (or your preferred IDE)
- [ ] Docker Desktop running
- [ ] HuggingFace account created
- [ ] HuggingFace API token saved
- [ ] Llama-2 access granted

---

## Phase 2: Project Foundation

### 🎯 Goals
- Create project structure
- Set up virtual environment
- Install dependencies
- Configure environment variables

### Step 1: Create Project Directory

```powershell
# Create project root
mkdir manufacturing-copilot
cd manufacturing-copilot

# Initialize git repository
git init
```

### Step 2: Create Directory Structure

```powershell
# Create main directories
mkdir app
mkdir ml_models
mkdir data_engineering
mkdir tests
mkdir scripts
mkdir guides

# Create subdirectories
mkdir app\functions
mkdir ml_models\predictive_maintenance
mkdir ml_models\anomaly_detection
mkdir ml_models\quality_prediction
mkdir data_engineering\streaming_pipeline
mkdir data_engineering\batch_pipeline
mkdir data_engineering\airflow_dags
mkdir data_engineering\dbt_transformations
```

**Why This Structure**: 
- `app/` - Main application code (FastAPI + Agents)
- `ml_models/` - Machine learning models
- `data_engineering/` - Data pipelines
- `tests/` - Unit and integration tests
- `scripts/` - Utility scripts
- `guides/` - Documentation

### Step 3: Set Up Virtual Environment

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Verify activation (should show (venv) in prompt)
```

**💡 Pro Tip**: Always activate your virtual environment before working on the project!

### Step 4: Create requirements.txt

Create `requirements.txt`:

```txt
# Web Framework
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
pydantic-settings==2.1.0

# AI/ML Libraries
transformers==4.35.2
sentence-transformers==2.2.2
huggingface-hub==0.19.4

# LangChain
langchain==0.1.0
langchain-community==0.0.10
langchain-huggingface==0.0.1
langgraph==0.0.20

# Vector Database
chromadb==0.4.18

# Machine Learning
scikit-learn==1.3.2
xgboost==2.0.2
joblib==1.3.2

# Data Processing
pandas==2.1.3
numpy==1.26.2

# Database
psycopg2-binary==2.9.9
sqlalchemy==2.0.23

# Utilities
python-dotenv==1.0.0
python-multipart==0.0.6
httpx==0.25.2
requests==2.31.0
```

### Step 5: Install Dependencies

```powershell
# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies (may take 5-10 minutes)
pip install -r requirements.txt

# Verify installation
pip list
```

**Common Issues**:
- If `psycopg2-binary` fails on Windows: Install Visual C++ Build Tools
- If installation is slow: Try `pip install --no-cache-dir -r requirements.txt`

### Step 6: Create Environment File

Create `.env.example`:

```env
# Application Settings
APP_TITLE="Manufacturing Copilot API"
APP_VERSION="1.0.0"
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

# ChromaDB
CHROMA_PERSIST_DIR=./chroma_db

# Database (Optional)
DATABASE_URL=postgresql://copilot:copilot_pwd@localhost:5432/manufacturing_db

# Authentication
VALID_AUTH_TOKEN_PREFIX="Bearer technician-"
```

Create `.env` (actual configuration):

```powershell
# Copy example to actual
cp .env.example .env

# Edit .env and add your HuggingFace token
# Replace hf_your_token_here with your actual token
```

### Step 7: Create .gitignore

Create `.gitignore`:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Environment
.env
.venv

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Project specific
chroma_db/
data_lake/
*.log
*.parquet
ml_models/*/model.joblib
ml_models/*/scaler.joblib
```

### ✅ Phase 2 Checkpoint

Verify your setup:
```powershell
# Check virtual environment
python --version  # Should show 3.11+

# Check installed packages
pip list | findstr fastapi
pip list | findstr langchain

# Check structure
tree /F  # Should show directory structure
```

You should now have:
- [ ] Complete directory structure
- [ ] Virtual environment activated
- [ ] All dependencies installed
- [ ] Environment variables configured
- [ ] .gitignore in place

---

## Phase 3: GenAI Agents (Core)

### 🎯 Goals
- Understand LangGraph architecture
- Build Vision Agent
- Build RAG Agent
- Build Report Agent
- Create orchestration workflow

### Understanding the Architecture

**What is LangGraph?**
- State machine for AI agents
- Orchestrates multiple agents in sequence or parallel
- Maintains shared state across agents

**Our Agent Flow**:
```
User Query → LangGraph
              ↓
    ┌─────────┴─────────┐
    ▼         ▼         ▼
Vision     RAG      Report
Agent     Agent     Agent
    │         │         │
    └─────────┬─────────┘
              ▼
      Unified Response
```

### Step 1: Create Configuration Module

Create `app/config.py`:

```python
# app/config.py

import os
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    """Application configuration settings."""
    APP_TITLE: str = "Manufacturing Copilot API"
    APP_VERSION: str = "1.0.0"
    LOG_LEVEL: str = Field(default="INFO", env="LOG_LEVEL")
    
    # Authentication
    VALID_AUTH_TOKEN_PREFIX: str = "Bearer technician-"
    
    # Database configuration
    DATABASE_URL: str = Field(
        default="postgresql://copilot:copilot_pwd@localhost:5432/manufacturing_db",
        env="DATABASE_URL"
    )
    
    # HuggingFace Configuration (REQUIRED)
    HUGGINGFACE_TOKEN: str = Field(..., env="HUGGINGFACE_TOKEN")
    
    # Model Configuration
    VLM_MODEL_ID: str = Field(default="Salesforce/blip2-opt-2.7b", env="VLM_MODEL_ID")
    LLM_MODEL_ID: str = Field(default="meta-llama/Llama-2-7b-chat-hf", env="LLM_MODEL_ID")
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
    CHROMA_PERSIST_DIR: str = Field(default="./chroma_db", env="CHROMA_PERSIST_DIR")

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": False
    }

settings = Settings()
```

**Why Pydantic Settings?**
- Type validation
- Environment variable loading
- Default values
- Configuration documentation

### Step 2: Create Data Models

Create `app/models.py`:

```python
# app/models.py

from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, Field

class DiagnosisRequest(BaseModel):
    """Request model for the main diagnosis endpoint."""
    plant_id: str = Field(
        ...,
        pattern=r"^[A-Z]{3,4}-\w{2,3}$",
        description="Unique plant identifier, e.g., 'PUNE-IN'",
        examples=["PUNE-IN"],
    )
    equipment_id: str = Field(
        ...,
        min_length=4,
        description="Tag or ID of the equipment",
        examples=["CNC-A-102"]
    )
    problem_description: str = Field(
        ...,
        description="Technician's description of the issue"
    )
    image_id: Optional[str] = Field(
        None,
        description="ID of the uploaded image for visual inspection"
    )

class DiagnosisResponse(BaseModel):
    """Response model containing output from all agents."""
    request_id: UUID
    vision_analysis: dict
    rag_guidance: dict
    generated_report: str
    confidence_score: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Overall confidence in the recommendation"
    )
    # Optional ML and Analytics insights
    ml_prediction: Optional[dict] = Field(
        None,
        description="ML Agent prediction results"
    )
    analytics_insights: Optional[dict] = Field(
        None,
        description="Analytics Agent insights"
    )
    safety_disclaimer: str = "Always follow standard safety procedures"

class HealthStatus(BaseModel):
    """Response model for health check endpoint."""
    status: str = "ok"
```

**Why Pydantic Models?**
- Automatic validation
- API documentation (Swagger)
- Type safety
- Clear contracts

### Step 3: Build the Agents

Create `app/agents.py`:

**(Due to length, I'll provide the implementation in the next file)**

---

Let me continue with creating the complete implementation guide in a structured format...

