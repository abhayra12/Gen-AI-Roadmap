# 🏭 Manufacturing Copilot - Capstone Project

> **A production-grade, multi-agent AI system for smart manufacturing**

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.1+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**⚡ Cloud-Native Design**: Uses **HuggingFace Inference Endpoints** - **no local GPU required**! Run on any machine with just CPU and internet connection.

---

## 🎓 **Want to Build This from Scratch?**

📚 **[See Complete Step-by-Step Guides →](guides/)**

Learn by building! We've created comprehensive guides to help you implement this project from an empty folder:
- 🚀 **[guides/START_HERE.md](guides/START_HERE.md)** - Navigation and overview
- 🏗️ **[guides/BUILD_FROM_SCRATCH_GUIDE.md](guides/BUILD_FROM_SCRATCH_GUIDE.md)** - Phases 1-7 (Foundation & Agents)
- 🔗 **[guides/BUILD_FROM_SCRATCH_GUIDE_PART2.md](guides/BUILD_FROM_SCRATCH_GUIDE_PART2.md)** - Phases 8-12 (Integration & Deploy)
- 📊 **[guides/IMPLEMENTATION_ROADMAP.md](guides/IMPLEMENTATION_ROADMAP.md)** - Visual diagrams
- ⚡ **[guides/QUICK_START_REFERENCE.md](guides/QUICK_START_REFERENCE.md)** - Quick commands

**Total Time**: 9-12 hours | **Difficulty**: Intermediate | **12 Detailed Phases**

---

## 📋 Table of Contents

1. [Overview](#-overview)
2. [Features](#-features)
3. [Architecture](#%EF%B8%8F-architecture)
4. [Quick Start](#-quick-start---5-minutes)
5. [Detailed Setup Guide](#-detailed-setup-guide)
6. [API Documentation](#-api-documentation)
7. [Testing](#-testing)
8. [Deployment Options](#-deployment-options) ⭐ **NEW: Kubernetes**
9. [Troubleshooting](#-troubleshooting)
10. [Project Structure](#-project-structure)

---

## 🎯 Overview

The Manufacturing Copilot is an intelligent system that combines three specialized AI agents to solve real-world factory challenges:

### 🤖 Three Specialized Agents

1. **Vision Agent** 👁️
   - Analyzes product images to identify manufacturing defects
   - Uses BLIP-2 Vision-Language Model via HuggingFace Inference API
   - Equipment-specific defect detection (CNC, Welding, Assembly, Coating)
   - Confidence scoring and detailed analysis

2. **RAG Agent** 📚
   - Provides expert maintenance guidance from technical documentation
   - Uses Llama-2 LLM + ChromaDB vector database
   - Pre-loaded with 5 comprehensive SOP documents
   - Cites source documents for traceability

3. **Report Agent** 📝
   - Generates structured, professional incident reports
   - Uses Llama-2 for natural language generation
   - Synthesizes insights from Vision and RAG agents
   - Structured format with Summary, Findings, Actions, Priority

### 🎓 Learning Outcomes

This capstone demonstrates:
- ✅ Multi-agent system design with LangGraph
- ✅ Retrieval-Augmented Generation (RAG)
- ✅ Production FastAPI backend
- ✅ HuggingFace model integration
- ✅ Docker containerization
- ✅ Infrastructure as Code (Terraform)
- ✅ CI/CD pipelines
- ✅ Real-world problem solving

---

## ✨ Features

### Core Capabilities

- 🔍 **Visual Defect Detection** - Automated quality inspection using Vision-Language Models
- 🧠 **Intelligent Maintenance Guidance** - RAG-powered technical support from SOP manuals
- 📊 **Automated Reporting** - Professional incident reports with structured format
- 🔄 **Multi-Agent Orchestration** - LangGraph-based workflow management
- 🔐 **Secure API** - Bearer token authentication and input validation
- 📈 **Production Monitoring** - Request tracing, performance metrics, structured logging

### Technical Highlights

- **No GPU Required** - Uses HuggingFace Inference API (runs on CPU)
- **Vector Search** - ChromaDB for efficient document retrieval
- **Knowledge Base** - Pre-populated with manufacturing SOPs
- **Error Handling** - Comprehensive fallbacks and recovery
- **Containerized** - Docker and Docker Compose ready
- **Cloud Deployable** - Terraform configs for GCP Cloud Run
- **CI/CD Ready** - GitHub Actions workflows included

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│              User/Client Application             │
│        (API Client, Streamlit, cURL, etc.)       │
└─────────────────────┬───────────────────────────┘
                      │ HTTP/REST API
┌─────────────────────▼───────────────────────────┐
│           FastAPI Backend (Port 8080)            │
│    • Authentication (Bearer Token)               │
│    • Request Validation (Pydantic)               │
│    • Observability (Tracing, Metrics)            │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│      LangGraph Orchestrator (app/agents.py)      │
│      Sequential Workflow: Vision→RAG→Report      │
└──┬──────────────────┬──────────────────┬─────────┘
   │                  │                  │
   ▼                  ▼                  ▼
┌─────────┐     ┌─────────┐      ┌──────────┐
│ Vision  │     │   RAG   │      │  Report  │
│ Agent   │     │  Agent  │      │  Agent   │
│         │     │         │      │          │
│ BLIP-2  │     │ Llama-2 │      │ Llama-2  │
│  VLM    │     │+ ChDB   │      │   LLM    │
└────┬────┘     └────┬────┘      └────┬─────┘
     │               │                │
     └───────────────┼────────────────┘
                     │
       ┌─────────────▼─────────────┐
       │  HuggingFace Inference API │
       │  • BLIP-2 (Vision)         │
       │  • Llama-2 (LLM)           │
       │  • Embeddings (RAG)        │
       └────────────────────────────┘
```

### Data Flow

1. **Client Request** → FastAPI endpoint `/v1/diagnose`
2. **Authentication** → Validates bearer token
3. **Validation** → Pydantic models check input
4. **LangGraph** → Initiates sequential agent workflow
5. **Vision Agent** → Analyzes image for defects
6. **RAG Agent** → Retrieves relevant docs + generates guidance
7. **Report Agent** → Creates incident report
8. **Response** → Structured JSON with all agent outputs

---

## 🚀 Quick Start - 5 Minutes

### Prerequisites Checklist

- [ ] Python 3.11+ installed ([download](https://www.python.org/downloads/))
- [ ] Git installed
- [ ] HuggingFace account ([sign up](https://huggingface.co/join))
- [ ] HuggingFace API token ([create](https://huggingface.co/settings/tokens))

### Installation Steps

```bash
# 1. Clone the repository
git clone https://github.com/abhayra12/Gen-AI-Roadmap.git
cd Gen-AI-Roadmap/capstone_project

# 2. Create virtual environment
python -m venv venv

# Windows
.\venv\Scripts\Activate.ps1

# Mac/Linux
source venv/bin/activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env and add your HuggingFace token:
# HUGGINGFACE_TOKEN=hf_your_token_here

# 5. Run the API server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

### Test the API

**Option 1: Interactive Docs** (Recommended)
- Open browser: http://localhost:8080/docs
- Try the `/v1/diagnose` endpoint with example data

**Option 2: cURL**
```bash
curl -X POST "http://localhost:8080/v1/diagnose" \
  -H "Content-Type: application/json" \
  -H "X-Auth-Token: Bearer technician-test123" \
  -d '{
    "plant_id": "PUNE-IN",
    "equipment_id": "CNC-A-102",
    "problem_description": "Machine overheating during operation",
    "image_id": "test_img_001"
  }'
```

**Option 3: Python**
```python
import requests

response = requests.post(
    "http://localhost:8080/v1/diagnose",
    headers={"X-Auth-Token": "Bearer technician-test123"},
    json={
        "plant_id": "PUNE-IN",
        "equipment_id": "CNC-A-102",
        "problem_description": "Machine overheating during operation",
        "image_id": "test_img_001"
    }
)

print(response.json())
```

---

## 📚 Detailed Setup Guide

### 1. Environment Configuration

Create `.env` file with these variables:

```bash
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
REQUEST_TIMEOUT=60
TEMPERATURE=0.7
MAX_TOKENS=512

# ChromaDB (Vector Database)
CHROMA_PERSIST_DIR=./chroma_db

# Database (Optional for logging)
DATABASE_URL=postgresql://copilot:copilot_pwd@localhost:5432/manufacturing_db

# Authentication
VALID_AUTH_TOKEN_PREFIX="Bearer technician-"
```

### 2. Get HuggingFace Token

1. **Sign up**: https://huggingface.co/join
2. **Create token**: https://huggingface.co/settings/tokens
   - Token type: Read
   - Name: manufacturing-copilot
3. **Accept Llama-2 terms**: https://huggingface.co/meta-llama/Llama-2-7b-chat-hf
   - Click "Agree and access repository"
4. **Copy token** to `.env` file

### 3. Verify Setup

```bash
# Run the setup test script
python scripts/test_setup.py
```

This validates:
- ✅ Environment variables loaded
- ✅ HuggingFace authentication
- ✅ Embeddings model access
- ✅ LLM endpoint connectivity
- ✅ ChromaDB initialization

### 4. Understanding the Knowledge Base

The RAG agent comes pre-loaded with 5 manufacturing SOPs:

1. **SOP-123**: CNC Machine Troubleshooting
2. **MAINT-GUIDE-V2**: Welding Equipment Maintenance
3. **SOP-456**: Assembly Line Quality Control
4. **COATING-MANUAL-2024**: Surface Coating Guidelines
5. **SAFETY-SOP-001**: Emergency Response Procedures

Location: Automatically populated in `app/agents.py` → `RAGAgent._populate_sample_docs()`

### 5. Running with Docker

```bash
# Build and run with Docker Compose (includes PostgreSQL)
docker-compose up --build

# Or build Docker image only
docker build -t manufacturing-copilot:latest .

# Run container
docker run -p 8080:8080 \
  -e HUGGINGFACE_TOKEN=hf_your_token_here \
  manufacturing-copilot:latest
```

---

## � API Documentation

### Endpoints

#### Health Check
```http
GET /health
```
**Response**:
```json
{"status": "ok"}
```

#### Diagnose Manufacturing Issue
```http
POST /v1/diagnose
```

**Headers**:
```
X-Auth-Token: Bearer technician-<user_id>
Content-Type: application/json
```

**Request Body**:
```json
{
  "plant_id": "PUNE-IN",           // Format: [A-Z]{3,4}-\w{2,3}
  "equipment_id": "CNC-A-102",      // Min length: 4
  "problem_description": "Machine overheating during operation",
  "image_id": "img_12345"           // Optional
}
```

**Response** (200 OK):
```json
{
  "request_id": "uuid-here",
  "vision_analysis": {
    "defects_found": ["micro-fracture", "surface-roughness"],
    "confidence": 0.87,
    "model_used": "Salesforce/blip2-opt-2.7b",
    "image_analyzed": "img_12345"
  },
  "rag_guidance": {
    "recommended_steps": [
      "1. Check coolant levels in the reservoir...",
      "2. Inspect coolant lines for leaks...",
      "3. Verify coolant pump operation..."
    ],
    "cited_documents": ["SOP-123", "MAINT-GUIDE-V2"],
    "confidence": 0.85
  },
  "generated_report": "MANUFACTURING INCIDENT REPORT\n\nSUMMARY:...",
  "confidence_score": 0.86,
  "safety_disclaimer": "Always follow standard safety procedures..."
}
```

**Observability Headers** (in response):
```
X-Request-Trace-ID: <uuid>
X-Response-Time-ms: <milliseconds>
```

### Authentication

Bearer token format: `Bearer technician-<user_id>`

Example:
```
X-Auth-Token: Bearer technician-john-doe
```

In production, implement proper user management and token validation.

---

## 🧪 Testing

### Run All Tests
```bash
pytest tests/ -v
```

### Run with Coverage
```bash
pytest tests/ --cov=app --cov-report=html
open htmlcov/index.html
```

### Run Specific Tests
```bash
pytest tests/test_api.py -v              # API tests
pytest tests/test_models.py -v           # Model validation
pytest tests/test_security.py -v         # Security tests
```

### Test Categories

1. **API Tests** (`tests/test_api.py`)
   - Health check endpoint
   - Authentication (valid/invalid tokens)
   - Diagnosis endpoint
   - Response structure validation
   - Observability middleware

2. **Model Tests** (`tests/test_models.py`)
   - Pydantic model validation
   - Input sanitization
   - Field constraints

3. **Security Tests** (`tests/test_security.py`)
   - Token validation
   - Input injection prevention
   - Rate limiting (TODO)

---

## 🌐 Deployment

### Option 1: Local Development
```bash
uvicorn app.main:app --reload --port 8080
```

### Option 2: Docker
```bash
docker-compose up --build
```

### Option 3: Google Cloud Run (Production)

#### Using Terraform:
```bash
cd terraform
terraform init
terraform plan -var="project_id=your-gcp-project"
terraform apply -var="project_id=your-gcp-project"
```

#### Using Deployment Script:
```bash
python scripts/deploy_cloud_run.py \
  --project your-gcp-project \
  --region us-central1 \
  --service-name manufacturing-copilot
```

### Environment Variables for Production

Use **Google Secret Manager** or equivalent:

```bash
# Required
HUGGINGFACE_TOKEN=<from secret manager>

# Optional
DATABASE_URL=<cloud SQL connection>
LOG_LEVEL=INFO
ENABLE_TELEMETRY=true
```

---

## 🔧 Troubleshooting

### Common Issues

#### 1. "HUGGINGFACE_TOKEN not found"
**Solution**:
```bash
# Check .env file exists
ls -la .env

# Verify content
cat .env | grep HUGGINGFACE_TOKEN

# Ensure no extra spaces
# Correct: HUGGINGFACE_TOKEN=hf_abc123
# Wrong:   HUGGINGFACE_TOKEN = hf_abc123
```

#### 2. "Model loading timeout"
**Solution**:
- First HF API call takes 30-60 seconds (cold start)
- Increase timeout in `.env`: `REQUEST_TIMEOUT=90`
- Try smaller model: `HF_LLM_MODEL=google/flan-t5-large`

#### 3. "ChromaDB collection error"
**Solution**:
```bash
# Delete and recreate
rm -rf ./chroma_db
python -c "from app.agents import rag_agent; print('Reset complete')"
```

#### 4. "Port 8080 already in use"
**Solution**:
```bash
# Use different port
uvicorn app.main:app --port 8000

# Or kill existing process (Windows)
netstat -ano | findstr :8080
taskkill /PID <PID> /F

# Or kill existing process (Mac/Linux)
lsof -ti:8080 | xargs kill -9
```

#### 5. "Import Error: langchain_huggingface"
**Solution**:
```bash
pip install langchain-huggingface --force-reinstall
```

### Getting Help

1. **Check logs**: Look for detailed error messages in console
2. **Run test script**: `python scripts/test_setup.py`
3. **Review documentation**: See `SETUP_GUIDE.md` for detailed setup
4. **Open issue**: https://github.com/abhayra12/Gen-AI-Roadmap/issues

---

## 📁 Project Structure

```
capstone_project/
├── app/                          # Main application code
│   ├── __init__.py
│   ├── main.py                   # FastAPI application
│   ├── agents.py                 # Agent implementations (600+ lines)
│   │   ├── VisionAgent          # BLIP-2 VLM for defect detection
│   │   ├── RAGAgent              # Llama-2 + ChromaDB for guidance
│   │   ├── ReportAgent           # Llama-2 for report generation
│   │   └── LangGraph workflow    # Sequential orchestration
│   ├── models.py                 # Pydantic models
│   ├── config.py                 # Configuration settings
│   ├── security.py               # Authentication logic
│   └── functions/                # Cloud functions (optional)
│       └── feedback/
│
├── tests/                        # Test suite
│   ├── __init__.py
│   ├── conftest.py              # Test fixtures
│   ├── test_api.py              # API integration tests
│   ├── test_models.py           # Model validation tests
│   └── test_security.py         # Security tests
│
├── terraform/                    # Infrastructure as Code
│   ├── main.tf                  # Main Terraform config
│   ├── variables.tf
│   ├── outputs.tf
│   └── modules/                 # Terraform modules
│
├── .github/workflows/           # CI/CD Pipelines
│   ├── ci.yml                   # Continuous Integration
│   └── deploy.yml               # Continuous Deployment
│
├── scripts/                     # Utility scripts
│   ├── test_setup.py           # Validates HF setup
│   └── deploy_cloud_run.py     # GCP deployment
│
├── charts/                      # Kubernetes Helm charts
│
├── .env.example                # Environment template
├── .env                        # Your config (not committed)
├── .gitignore
├── Dockerfile                  # Container definition
├── docker-compose.yml          # Local dev stack
├── requirements.txt            # Production dependencies
├── requirements-dev.txt        # Development dependencies
├── README.md                   # This file
├── SETUP_GUIDE.md             # Detailed setup instructions
└── PRODUCTION_READINESS.md    # Production checklist
```

---

## 🤝 Contributing

This is a capstone project for the Gen AI Masters Program. Contributions welcome!

### Development Setup

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run linters
black app/
flake8 app/
mypy app/ --ignore-missing-imports

# Run tests with coverage
pytest tests/ --cov=app --cov-report=term-missing
```

### Code Quality Standards

- **Black** for formatting
- **Flake8** for linting
- **MyPy** for type checking
- **Pytest** for testing (>80% coverage goal)
- **Docstrings** for all public functions

---

## 📄 License

This project is part of the Gen AI Masters Program curriculum.

---

## 🙏 Acknowledgments

- **HuggingFace** for Inference API and model hosting
- **LangChain** team for the agent framework
- **FastAPI** for the excellent web framework
- **Anthropic** for Model Context Protocol inspiration

---

## 📞 Support & Contact

- **Documentation**: See `SETUP_GUIDE.md` and `PRODUCTION_READINESS.md`
- **Issues**: https://github.com/abhayra12/Gen-AI-Roadmap/issues
- **Course FAQ**: `../FAQ.md`
- **Setup Guide**: `../GETTING_STARTED.md`

---

## 🎓 Learning Resources

This capstone demonstrates skills from:
- **Week 1-2**: Python & ML Foundations
- **Week 3-4**: Deep Learning & NLP
- **Week 5-6**: LLMs & RAG
- **Week 7-8**: LangChain & Agents (LangGraph orchestration)
- **Week 11-12**: Production Deployment

**Full course**: https://github.com/abhayra12/Gen-AI-Roadmap

---

**Built with ❤️ for the Gen AI Masters Program**

Ready to deploy → Portfolio ready → Career ready 🚀

### Run all tests:
```bash
pytest tests/ -v
```

### Run with coverage:
```bash
pytest tests/ --cov=app --cov-report=html
```

### Run specific test file:
```bash
pytest tests/test_api.py -v
```

## � Deployment Options

### 1. Kubernetes (Production) ⭐ **Recommended**

**Full Kubernetes deployment with Helm charts and plain manifests** for production environments.

**Quick Start:**
```bash
# Using Helm (recommended)
./scripts/kubernetes/deploy-k8s.sh prod

# Or using kubectl only
kubectl apply -f kubernetes/ --namespace=manufacturing-copilot
```

**Features:**
- ✅ Horizontal Pod Autoscaling (2-10 replicas)
- ✅ High Availability (Pod Disruption Budget)
- ✅ Network Policies for security
- ✅ Prometheus monitoring integration
- ✅ Ingress with TLS support
- ✅ Persistent storage for ChromaDB
- ✅ Multi-cloud support (GKE, EKS, AKS)

**📖 Complete Guide**: See [KUBERNETES_DEPLOYMENT.md](KUBERNETES_DEPLOYMENT.md) for:
- GKE, EKS, AKS deployment guides
- Minikube local development
- Configuration and secrets management
- Monitoring and scaling
- Troubleshooting

---

### 2. Docker Compose (Development)

**Quick local setup** for development and testing.

```bash
# Start all services
docker-compose up --build

# Access API at http://localhost:8080/docs
```

Includes:
- FastAPI backend
- ChromaDB (if needed)
- Auto-reload for development
- Volume mounts for live code updates

---

### 3. Docker (Manual)

**Build and run** the container manually:

```bash
# Build the Docker image
docker build -t manufacturing-copilot:latest .

# Run the container
docker run -p 8080:8080 \
  -e HUGGINGFACE_TOKEN=hf_your_token_here \
  -e LOG_LEVEL=INFO \
  manufacturing-copilot:latest
```

---

### 4. Cloud Run (Serverless GCP)

**Terraform-based deployment** to Google Cloud Run:

```bash
# Navigate to terraform directory
cd terraform

# Initialize Terraform
terraform init

# Plan the deployment
terraform plan -var="project_id=your-gcp-project"

# Deploy
terraform apply -var="project_id=your-gcp-project"
```

**Or using the deployment script:**
```bash
python scripts/deploy_cloud_run.py \
  --project your-gcp-project \
  --region us-central1 \
  --service-name manufacturing-copilot
```

---

### Deployment Comparison

| Feature | Kubernetes | Docker Compose | Docker | Cloud Run |
|---------|------------|----------------|--------|-----------|
| **Use Case** | Production | Development | Testing | Serverless |
| **Scalability** | Auto-scaling | Manual | Manual | Auto-scaling |
| **HA/Failover** | ✅ Yes | ❌ No | ❌ No | ✅ Yes |
| **Complexity** | High | Low | Low | Medium |
| **Cost** | Medium | Free | Free | Pay-per-use |
| **Setup Time** | 10 min | 2 min | 5 min | 10 min |

**Choose:**
- **Kubernetes** → Production deployments, enterprise environments
- **Docker Compose** → Local development, quick testing
- **Docker** → Simple testing, CI/CD builds
- **Cloud Run** → Serverless, pay-per-request workloads

## 🔐 Security

- **Authentication**: Bearer token authentication for all diagnosis endpoints
- **Input Validation**: Pydantic models with strict validation rules
- **Rate Limiting**: (TODO: Implement rate limiting middleware)
- **Secrets Management**: Environment variables and GCP Secret Manager

## 📊 Monitoring & Observability

Every request includes:
- **X-Request-Trace-ID**: Unique identifier for request tracing
- **X-Response-Time-ms**: Response time in milliseconds

High latency warnings (>500ms) are automatically logged.

## 🛠️ Development

### Code Quality Tools:

```bash
# Lint code
flake8 app

# Format code
black app

# Type checking
mypy app --ignore-missing-imports

# Sort imports
isort app
```

### Pre-commit hooks:
```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run manually
pre-commit run --all-files
```

## 📦 Project Structure

```
capstone_project/
├── app/                    # Application code
│   ├── main.py            # FastAPI application
│   ├── agents.py          # Agent orchestration logic
│   ├── models.py          # Pydantic models
│   ├── config.py          # Configuration settings
│   ├── security.py        # Authentication logic
│   └── functions/         # Cloud functions
├── tests/                 # Test suite
│   ├── test_api.py        # API integration tests
│   ├── test_models.py     # Model unit tests
│   └── test_security.py   # Security tests
├── terraform/             # Infrastructure as Code
│   ├── main.tf           # Main Terraform config
│   └── modules/          # Terraform modules
├── .github/workflows/     # CI/CD pipelines
│   ├── ci.yml            # Continuous Integration
│   └── deploy.yml        # Continuous Deployment
├── scripts/              # Deployment and utility scripts
├── Dockerfile            # Container definition
├── docker-compose.yml    # Local development stack
├── requirements.txt      # Production dependencies
└── requirements-dev.txt  # Development dependencies
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is part of the Gen AI Masters Program curriculum.

## 🙏 Acknowledgments

- HuggingFace for Transformers library
- LangChain team for the agent framework
- FastAPI for the excellent web framework

## 📞 Support

For questions or issues, please:
- Open an issue in the repository
- Check the main course [FAQ](../FAQ.md)
- Review the [Getting Started Guide](../GETTING_STARTED.md)

---

Built with ❤️ for the Gen AI Masters Program
