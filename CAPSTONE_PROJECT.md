# 🏭 Capstone Project: Intelligent Manufacturing Quality Assistant

> **Production-Grade Gen AI System for Smart Manufacturing**

---

## 🎯 Project Overview

### What You'll Build

An **Intelligent Manufacturing Quality Control & Predictive Maintenance System** that combines:
- 🔍 **Visual Quality Inspection** using Vision-Language Models
- 📊 **Predictive Maintenance RAG** system
- 🤖 **Agentic AI** for root-cause analysis
- 📝 **Multi-lingual Report Generation**
- 🚀 **Production-Ready Deployment** on GCP

### Why This Project?

- ✅ **Industry-Relevant:** Manufacturing is a ₹50+ trillion sector in India
- ✅ **Resume Standout:** Shows end-to-end ML engineering skills
- ✅ **Scalable:** Applicable to automotive, pharma, electronics, FMCG
- ✅ **Open-Source:** Uses free/open-source tools
- ✅ **Production-Grade:** Containerized, monitored, CI/CD enabled

---

## 🏢 Use Case: Smart Manufacturing Quality Control

### Problem Statement

Manufacturing facilities in India face:
1. **Manual quality inspections** → slow, error-prone
2. **Reactive maintenance** → costly downtime
3. **Knowledge silos** → expertise not shared
4. **Language barriers** → English-only systems

### Solution

An AI-powered assistant that:
1. **Inspects products** using computer vision
2. **Predicts failures** before they happen
3. **Answers questions** from maintenance manuals
4. **Generates reports** in Hindi, Tamil, Gujarati, English
5. **Learns continuously** from feedback

---

## 🛠️ Technical Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      User Interface                          │
│              (FastAPI + Streamlit Dashboard)                 │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────────────┐
│                   API Gateway (FastAPI)                      │
│  Routes: /inspect, /predict, /query, /generate-report       │
└───────────────────────┬─────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Vision Agent │ │   RAG Agent  │ │ Report Agent │
│  (Quality)   │ │ (Maintenance)│ │ (Multi-lang) │
└──────┬───────┘ └──────┬───────┘ └──────┬───────┘
       │                │                │
       ▼                ▼                ▼
┌────────────────────────────────────────────────┐
│        LangGraph Agent Orchestrator            │
│    (State Management, Tool Calling, Memory)    │
└────────────┬───────────────────────────────────┘
             │
   ┌─────────┼─────────┐
   │         │         │
   ▼         ▼         ▼
┌─────┐  ┌──────┐  ┌──────────┐
│ VLM │  │ LLM  │  │ Vector DB│
│Model│  │Model │  │(ChromaDB)│
└─────┘  └──────┘  └──────────┘
   │         │         │
   └─────────┴─────────┘
             │
   HuggingFace Inference API

┌─────────────────────────────────────────┐
│         Supporting Services             │
├─────────────────────────────────────────┤
│ • PostgreSQL (Metadata & Logs)          │
│ • Redis (Caching)                       │
│ • Prometheus (Metrics)                  │
│ • Grafana (Dashboards)                  │
└─────────────────────────────────────────┘
```

### Components Breakdown

#### 1. Vision Agent (Quality Inspection)
- **Model:** BLIP-2 or LLaVA (via HuggingFace)
- **Function:** Analyze product images, detect defects
- **Input:** Product images
- **Output:** Quality assessment, defect classification

#### 2. RAG Agent (Predictive Maintenance)
- **Components:** 
  - Document Loader (maintenance manuals, logs)
  - Embeddings Model (sentence-transformers)
  - Vector Store (ChromaDB)
  - LLM (Mistral 7B or Llama 2 via HF)
- **Function:** Answer maintenance questions, predict failures
- **Input:** Sensor data, maintenance history
- **Output:** Recommendations, predictions

#### 3. Report Agent (Multi-lingual)
- **Model:** mBART or IndicTrans2
- **Function:** Generate reports in multiple Indian languages
- **Input:** Inspection results, maintenance data
- **Output:** PDF reports in user's language

#### 4. Orchestration Layer (LangGraph)
- **Function:** Coordinate agents, manage state
- **Features:**
  - Tool calling
  - Memory management
  - Error handling
  - Human-in-the-loop

---

## 📊 Data Architecture

### Data Sources

1. **Product Images**
   - Sample dataset: Generate synthetic defect images
   - Real-world: Camera feeds from production line

2. **Maintenance Manuals**
   - PDF documents (equipment manuals)
   - Structured data (maintenance logs)

3. **Sensor Data**
   - Time-series data (temperature, vibration, pressure)
   - Historical failure data

4. **Knowledge Base**
   - SOPs (Standard Operating Procedures)
   - Best practices
   - Troubleshooting guides

### Data Pipeline

```
Raw Data → Ingestion → Processing → Embedding → Vector Store
              │            │            │            │
         (S3/GCS)    (Preprocessing) (sentence-    (ChromaDB)
                                     transformers)
```

---

## 🚀 Development Phases

### Phase 1: Foundation (Week 11 - Days 1-2)

#### Setup & Architecture
- [ ] Initialize project structure
- [ ] Set up GitHub repository
- [ ] Create development environment
- [ ] Design API contracts
- [ ] Write technical design document

**Deliverables:**
```
capstone/
├── README.md
├── docs/
│   ├── architecture.md
│   ├── api_design.md
│   └── data_model.md
├── src/
├── tests/
└── requirements.txt
```

---

### Phase 2: RAG System (Week 11 - Days 3-4)

#### Build Document Processing Pipeline
- [ ] Implement document loaders (PDF, DOCX)
- [ ] Set up chunking strategy
- [ ] Configure embedding model
- [ ] Initialize ChromaDB
- [ ] Build retriever

#### Code Example
```python
# src/rag/document_processor.py
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

class DocumentProcessor:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        
    def process_documents(self, file_paths):
        documents = []
        for path in file_paths:
            loader = PyPDFLoader(path)
            docs = loader.load()
            documents.extend(docs)
        
        chunks = self.text_splitter.split_documents(documents)
        vectorstore = Chroma.from_documents(
            chunks,
            self.embeddings,
            persist_directory="./chroma_db"
        )
        return vectorstore
```

**Deliverables:**
- [ ] Working RAG pipeline
- [ ] Unit tests
- [ ] Sample queries and responses

---

### Phase 3: Vision Agent (Week 11 - Days 5-6)

#### Implement Quality Inspection
- [ ] Set up HuggingFace Inference API
- [ ] Create vision model wrapper
- [ ] Build defect detection logic
- [ ] Create image preprocessing pipeline

#### Code Example
```python
# src/agents/vision_agent.py
from huggingface_hub import InferenceClient
from PIL import Image
import base64
from io import BytesIO

class VisionQualityAgent:
    def __init__(self, hf_token):
        self.client = InferenceClient(token=hf_token)
        self.model = "Salesforce/blip2-opt-2.7b"
    
    def inspect_product(self, image_path):
        image = Image.open(image_path)
        
        prompt = """Analyze this product image and provide:
        1. Overall quality assessment (Good/Defective)
        2. List of visible defects (if any)
        3. Severity level (Low/Medium/High)
        4. Recommended action
        """
        
        result = self.client.visual_question_answering(
            image=image,
            question=prompt,
            model=self.model
        )
        
        return self._parse_result(result)
    
    def _parse_result(self, raw_result):
        # Parse and structure the result
        return {
            "quality": "Good" or "Defective",
            "defects": [],
            "severity": "Low",
            "action": "Pass" or "Inspect" or "Reject"
        }
```

**Deliverables:**
- [ ] Vision agent implementation
- [ ] Sample image analysis
- [ ] Performance benchmarks

---

### Phase 4: Agent Orchestration (Week 11 - Day 7)

#### Build LangGraph Workflow
- [ ] Define agent states
- [ ] Create agent nodes
- [ ] Implement routing logic
- [ ] Add memory management

#### Code Example
```python
# src/agents/orchestrator.py
from langgraph.graph import StateGraph, END
from langchain.schema import HumanMessage

class ManufacturingAssistant:
    def __init__(self, vision_agent, rag_agent, report_agent):
        self.vision_agent = vision_agent
        self.rag_agent = rag_agent
        self.report_agent = report_agent
        self.graph = self._build_graph()
    
    def _build_graph(self):
        workflow = StateGraph(dict)
        
        # Add nodes
        workflow.add_node("classify", self._classify_query)
        workflow.add_node("vision", self._handle_vision)
        workflow.add_node("rag", self._handle_rag)
        workflow.add_node("report", self._generate_report)
        
        # Add edges
        workflow.add_conditional_edges(
            "classify",
            self._route_query,
            {
                "vision": "vision",
                "maintenance": "rag",
                "report": "report"
            }
        )
        
        workflow.add_edge("vision", "report")
        workflow.add_edge("rag", "report")
        workflow.add_edge("report", END)
        
        workflow.set_entry_point("classify")
        
        return workflow.compile()
    
    def _classify_query(self, state):
        # Classify user intent
        query_type = self._detect_intent(state["input"])
        state["query_type"] = query_type
        return state
    
    def _route_query(self, state):
        return state["query_type"]
    
    def process(self, user_input):
        result = self.graph.invoke({"input": user_input})
        return result
```

**Deliverables:**
- [ ] Working agent orchestration
- [ ] State management
- [ ] End-to-end workflow

---

### Phase 5: API Development (Week 12 - Days 1-2)

#### Build FastAPI Backend
- [ ] Create API endpoints
- [ ] Add request validation
- [ ] Implement authentication
- [ ] Add rate limiting
- [ ] Set up CORS

#### Code Example
```python
# src/api/main.py
from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os

app = FastAPI(
    title="Manufacturing Quality Assistant API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str
    context: Optional[dict] = None

class InspectionRequest(BaseModel):
    product_id: str
    line_number: str

@app.post("/api/v1/inspect")
async def inspect_product(
    file: UploadFile = File(...),
    request: InspectionRequest = Depends()
):
    """Inspect product quality from image"""
    try:
        # Save uploaded image
        image_path = f"/tmp/{file.filename}"
        with open(image_path, "wb") as f:
            f.write(await file.read())
        
        # Process with vision agent
        result = vision_agent.inspect_product(image_path)
        
        # Log to database
        log_inspection(request.product_id, result)
        
        return {
            "product_id": request.product_id,
            "timestamp": datetime.now().isoformat(),
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/query")
async def query_rag(request: QueryRequest):
    """Query maintenance knowledge base"""
    try:
        result = rag_agent.query(request.query, request.context)
        return {
            "answer": result["answer"],
            "sources": result["sources"],
            "confidence": result["confidence"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/generate-report")
async def generate_report(product_id: str, language: str = "en"):
    """Generate multi-lingual quality report"""
    try:
        data = get_inspection_data(product_id)
        report = report_agent.generate(data, language)
        return {"report_url": report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}
```

**Deliverables:**
- [ ] Complete API implementation
- [ ] API documentation (Swagger)
- [ ] Postman collection

---

### Phase 6: Containerization (Week 12 - Days 3-4)

#### Docker Setup
- [ ] Create Dockerfile
- [ ] Set up docker-compose
- [ ] Configure multi-stage builds
- [ ] Optimize image size

#### Dockerfile
```dockerfile
# Dockerfile
FROM python:3.10-slim as base

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY src/ ./src/
COPY models/ ./models/

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### docker-compose.yml
```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - HUGGINGFACE_TOKEN=${HUGGINGFACE_TOKEN}
      - DATABASE_URL=postgresql://user:pass@db:5432/manufacturing
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis
      - chromadb
    volumes:
      - ./models:/app/models
      - ./data:/app/data

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=manufacturing
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  chromadb:
    image: chromadb/chroma:latest
    ports:
      - "8001:8000"
    volumes:
      - chroma_data:/chroma/chroma

  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana_data:/var/lib/grafana
      - ./monitoring/grafana:/etc/grafana/provisioning

volumes:
  postgres_data:
  chroma_data:
  prometheus_data:
  grafana_data:
```

**Deliverables:**
- [ ] Working Docker containers
- [ ] docker-compose setup
- [ ] Container health checks

---

### Phase 7: Infrastructure as Code (Week 12 - Day 5)

#### Terraform Setup for GCP
- [ ] Define GCP resources
- [ ] Set up Cloud Run
- [ ] Configure networking
- [ ] Set up secrets management

#### Terraform Files
```hcl
# infrastructure/terraform/main.tf
terraform {
  required_version = ">= 1.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
  
  backend "gcs" {
    bucket = "manufacturing-ai-tfstate"
    prefix = "terraform/state"
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# Cloud Run Service
resource "google_cloud_run_service" "api" {
  name     = "manufacturing-quality-api"
  location = var.region

  template {
    spec {
      containers {
        image = "gcr.io/${var.project_id}/manufacturing-api:latest"
        
        ports {
          container_port = 8000
        }
        
        env {
          name = "HUGGINGFACE_TOKEN"
          value_from {
            secret_key_ref {
              name = google_secret_manager_secret.hf_token.secret_id
              key  = "latest"
            }
          }
        }
        
        resources {
          limits = {
            cpu    = "2"
            memory = "4Gi"
          }
        }
      }
    }
    
    metadata {
      annotations = {
        "autoscaling.knative.dev/minScale" = "1"
        "autoscaling.knative.dev/maxScale" = "10"
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

# Secret Manager
resource "google_secret_manager_secret" "hf_token" {
  secret_id = "huggingface-token"
  
  replication {
    automatic = true
  }
}

# Cloud SQL (PostgreSQL)
resource "google_sql_database_instance" "main" {
  name             = "manufacturing-db"
  database_version = "POSTGRES_15"
  region           = var.region

  settings {
    tier = "db-f1-micro"
    
    ip_configuration {
      ipv4_enabled = false
      private_network = google_compute_network.main.id
    }
  }
}

# VPC Network
resource "google_compute_network" "main" {
  name                    = "manufacturing-network"
  auto_create_subnetworks = true
}

# IAM
data "google_iam_policy" "noauth" {
  binding {
    role = "roles/run.invoker"
    members = [
      "allUsers",
    ]
  }
}

resource "google_cloud_run_service_iam_policy" "noauth" {
  location = google_cloud_run_service.api.location
  project  = google_cloud_run_service.api.project
  service  = google_cloud_run_service.api.name

  policy_data = data.google_iam_policy.noauth.policy_data
}

# Output
output "api_url" {
  value = google_cloud_run_service.api.status[0].url
}
```

**Deliverables:**
- [ ] Complete Terraform configuration
- [ ] GCP resources provisioned
- [ ] Infrastructure documentation

---

### Phase 8: CI/CD Pipeline (Week 12 - Day 6)

#### GitHub Actions Setup
- [ ] Create build workflow
- [ ] Add testing pipeline
- [ ] Set up deployment workflow
- [ ] Configure secrets

#### GitHub Actions Workflow
```yaml
# .github/workflows/ci-cd.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  GCP_PROJECT_ID: ${{ secrets.GCP_PROJECT_ID }}
  GCP_REGION: us-central1
  IMAGE_NAME: manufacturing-api

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
          
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
          
      - name: Run tests
        run: |
          pytest tests/ --cov=src --cov-report=xml
          
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml

  build:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Cloud SDK
        uses: google-github-actions/setup-gcloud@v1
        with:
          service_account_key: ${{ secrets.GCP_SA_KEY }}
          project_id: ${{ secrets.GCP_PROJECT_ID }}
          
      - name: Configure Docker
        run: |
          gcloud auth configure-docker
          
      - name: Build Docker image
        run: |
          docker build -t gcr.io/$GCP_PROJECT_ID/$IMAGE_NAME:${{ github.sha }} .
          docker tag gcr.io/$GCP_PROJECT_ID/$IMAGE_NAME:${{ github.sha }} \
                     gcr.io/$GCP_PROJECT_ID/$IMAGE_NAME:latest
          
      - name: Push to GCR
        run: |
          docker push gcr.io/$GCP_PROJECT_ID/$IMAGE_NAME:${{ github.sha }}
          docker push gcr.io/$GCP_PROJECT_ID/$IMAGE_NAME:latest

  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Cloud SDK
        uses: google-github-actions/setup-gcloud@v1
        with:
          service_account_key: ${{ secrets.GCP_SA_KEY }}
          project_id: ${{ secrets.GCP_PROJECT_ID }}
          
      - name: Deploy to Cloud Run
        run: |
          gcloud run deploy manufacturing-quality-api \
            --image gcr.io/$GCP_PROJECT_ID/$IMAGE_NAME:${{ github.sha }} \
            --region $GCP_REGION \
            --platform managed \
            --allow-unauthenticated \
            --set-env-vars HUGGINGFACE_TOKEN=${{ secrets.HUGGINGFACE_TOKEN }}
          
      - name: Get service URL
        run: |
          gcloud run services describe manufacturing-quality-api \
            --region $GCP_REGION \
            --format 'value(status.url)'
```

**Deliverables:**
- [ ] Working CI/CD pipeline
- [ ] Automated testing
- [ ] Automated deployment

---

### Phase 9: Monitoring & Observability (Week 12 - Day 7)

#### Set Up Monitoring
- [ ] Configure Prometheus metrics
- [ ] Create Grafana dashboards
- [ ] Set up logging
- [ ] Configure alerts

#### Prometheus Configuration
```yaml
# monitoring/prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'manufacturing-api'
    static_configs:
      - targets: ['api:8000']
    metrics_path: '/metrics'

  - job_name: 'chromadb'
    static_configs:
      - targets: ['chromadb:8000']

alerting:
  alertmanagers:
    - static_configs:
        - targets: ['alertmanager:9093']

rule_files:
  - 'alerts.yml'
```

#### Application Metrics
```python
# src/monitoring/metrics.py
from prometheus_client import Counter, Histogram, Gauge
import time

# Request metrics
request_count = Counter(
    'api_requests_total',
    'Total API requests',
    ['method', 'endpoint', 'status']
)

request_duration = Histogram(
    'api_request_duration_seconds',
    'API request duration',
    ['method', 'endpoint']
)

# Model metrics
model_inference_duration = Histogram(
    'model_inference_duration_seconds',
    'Model inference duration',
    ['model_type']
)

active_requests = Gauge(
    'api_active_requests',
    'Number of active requests'
)

# RAG metrics
rag_query_count = Counter(
    'rag_queries_total',
    'Total RAG queries'
)

rag_cache_hits = Counter(
    'rag_cache_hits_total',
    'RAG cache hits'
)

def track_request(method, endpoint):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            active_requests.inc()
            start_time = time.time()
            
            try:
                result = await func(*args, **kwargs)
                status = 'success'
                return result
            except Exception as e:
                status = 'error'
                raise e
            finally:
                duration = time.time() - start_time
                request_count.labels(method, endpoint, status).inc()
                request_duration.labels(method, endpoint).observe(duration)
                active_requests.dec()
        
        return wrapper
    return decorator
```

**Deliverables:**
- [ ] Metrics collection
- [ ] Grafana dashboards
- [ ] Alert rules
- [ ] Logging aggregation

---

## 📈 Success Metrics

### Technical Metrics
- **API Response Time:** < 2 seconds (p95)
- **System Uptime:** > 99%
- **Model Accuracy:** > 85% for quality inspection
- **RAG Relevance:** > 0.8 (cosine similarity)

### Business Metrics
- **Defect Detection Rate:** > 95%
- **False Positive Rate:** < 5%
- **Maintenance Prediction Accuracy:** > 80%
- **User Satisfaction:** > 4/5

---

## 🧪 Testing Strategy

### Unit Tests
```python
# tests/test_vision_agent.py
import pytest
from src.agents.vision_agent import VisionQualityAgent

def test_inspect_good_product():
    agent = VisionQualityAgent(token="test")
    result = agent.inspect_product("tests/fixtures/good_product.jpg")
    assert result["quality"] == "Good"
    assert len(result["defects"]) == 0

def test_inspect_defective_product():
    agent = VisionQualityAgent(token="test")
    result = agent.inspect_product("tests/fixtures/defective_product.jpg")
    assert result["quality"] == "Defective"
    assert len(result["defects"]) > 0
```

### Integration Tests
```python
# tests/test_integration.py
import pytest
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_full_inspection_workflow():
    # Upload image
    with open("tests/fixtures/product.jpg", "rb") as f:
        response = client.post(
            "/api/v1/inspect",
            files={"file": f},
            data={"product_id": "TEST-001", "line_number": "LINE-1"}
        )
    
    assert response.status_code == 200
    assert "result" in response.json()
```

### Load Tests
```python
# tests/load_test.py
from locust import HttpUser, task, between

class ManufacturingAPIUser(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def query_rag(self):
        self.client.post("/api/v1/query", json={
            "query": "What is the recommended maintenance interval?"
        })
    
    @task(2)
    def health_check(self):
        self.client.get("/health")
```

---

## 📊 Project Timeline

| Week | Days | Phase | Deliverable |
|------|------|-------|-------------|
| 11 | 1-2 | Foundation | Project setup, architecture |
| 11 | 3-4 | RAG System | Working knowledge base |
| 11 | 5-6 | Vision Agent | Quality inspection module |
| 11 | 7 | Orchestration | Agent coordination |
| 12 | 1-2 | API | REST API endpoints |
| 12 | 3-4 | Containerization | Docker setup |
| 12 | 5 | IaC | Terraform deployment |
| 12 | 6 | CI/CD | Automated pipeline |
| 12 | 7 | Monitoring | Production monitoring |

---

## 🎓 Learning Objectives

By completing this capstone, you will:

✅ **Understand** end-to-end ML system design  
✅ **Build** production-grade Gen AI applications  
✅ **Deploy** containerized services to cloud  
✅ **Implement** CI/CD pipelines  
✅ **Monitor** ML systems in production  
✅ **Create** multi-agent systems with LangGraph  
✅ **Apply** RAG at scale  
✅ **Use** open-source tools effectively  

---

## 📚 Resources

### Documentation
- [LangChain Docs](https://python.langchain.com/)
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
- [HuggingFace Inference API](https://huggingface.co/docs/api-inference/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Terraform GCP Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs)

### Sample Datasets
- [Manufacturing Defect Dataset](https://www.kaggle.com/datasets/ravirajsinh45/real-life-industrial-dataset-of-casting-product)
- [Maintenance Data](https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification)

---

## 🏆 Evaluation Criteria

### Code Quality (20%)
- Clean, maintainable code
- Proper documentation
- Following best practices

### Functionality (30%)
- All features working
- Edge cases handled
- Error handling

### Production Readiness (30%)
- Containerized
- CI/CD pipeline
- Monitoring setup
- Security considerations

### Innovation (20%)
- Creative solutions
- Performance optimizations
- User experience

---

## 🎯 Next Steps

1. **Review** this document thoroughly
2. **Set up** your development environment
3. **Start** with Phase 1
4. **Track** your progress daily
5. **Ask questions** in community forums
6. **Demo** your project at the end!

---

## 🆘 Getting Help

- **Technical Issues:** Open GitHub Issues
- **Design Questions:** Use Discussions
- **Clarifications:** Check FAQ
- **Code Reviews:** Request peer reviews

---

**Ready to build something amazing? Let's go! 🚀**

---

<div align="center">
Capstone Project | Gen AI Masters Program | 2025
</div>
