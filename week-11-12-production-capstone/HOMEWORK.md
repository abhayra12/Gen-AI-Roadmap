# 📝 Homework Assignment - Week 11-12

**Module:** Production Deployment & Capstone Project  
**Due:** End of Week 12  
**Points:** 200 (Capstone Project)

---

## 🎯 Assignment: Complete Capstone Project

This is your final assignment - a comprehensive, production-ready Gen AI application. See [CAPSTONE_PROJECT.md](../CAPSTONE_PROJECT.md) for complete implementation guide.

---

## 🏭 Project Overview

**Title:** Intelligent Manufacturing Quality Assistant

**Description:** A multi-agent AI system that:
- Performs visual quality inspection using vision models
- Provides maintenance Q&A using RAG
- Generates reports in multiple languages
- Orchestrates complex workflows with LangGraph

**Real-world Impact:** Reduces defects, improves efficiency, supports workers

---

## 📊 Project Requirements

### Core Features (Must Have)
1. **Vision Agent**: Defect detection from images
2. **RAG System**: Document-based Q&A
3. **Report Generator**: Multi-lingual summaries
4. **Agent Orchestration**: LangGraph workflow
5. **REST API**: FastAPI endpoints
6. **Database**: PostgreSQL + ChromaDB
7. **Monitoring**: Prometheus + Grafana

### Production Features (Must Have)
1. **Docker**: Multi-stage containerization
2. **Terraform**: GCP infrastructure
3. **CI/CD**: GitHub Actions
4. **Cloud Deployment**: GCP Cloud Run
5. **Secrets Management**: GCP Secret Manager
6. **Logging**: Structured logs
7. **Testing**: Unit + integration tests

---

## 📋 Implementation Phases

### Phase 1: Foundation (Days 1-2)
- Set up project structure
- Define data models
- Create database schemas
- Design architecture

### Phase 2: RAG System (Days 3-4)
- Implement document processing
- Set up vector database
- Build retrieval pipeline
- Create Q&A endpoint

### Phase 3: Vision Agent (Days 5-6)
- Integrate vision model
- Build defect detection
- Process image uploads
- Return classifications

### Phase 4: Agent Orchestration (Day 7)
- Define LangGraph workflow
- Create specialized agents
- Implement state management
- Test multi-agent flow

### Phase 5: API Development (Days 8-9)
- Build FastAPI endpoints
- Add validation
- Implement authentication
- Write API tests

### Phase 6: Containerization (Days 10-11)
- Create Dockerfiles
- Build multi-stage images
- Set up docker-compose
- Test containers locally

### Phase 7: Infrastructure (Day 12)
- Write Terraform configs
- Provision GCP resources
- Set up networking
- Configure secrets

### Phase 8: CI/CD (Day 13)
- Create GitHub workflows
- Add automated tests
- Set up deployment
- Configure environments

### Phase 9: Production (Day 14)
- Deploy to GCP
- Set up monitoring
- Load test application
- Prepare demo

---

## 🎯 Grading Rubric (200 points)

### Functionality (60 points)
| Component | Points | Criteria |
|-----------|--------|----------|
| Vision Agent | 15 | Accurate defect detection |
| RAG System | 15 | Relevant document retrieval |
| Report Generation | 10 | Multi-lingual support |
| Agent Orchestration | 20 | Proper LangGraph workflow |

### Code Quality (40 points)
| Aspect | Points | Criteria |
|--------|--------|----------|
| Architecture | 10 | Clean separation, modularity |
| Code Style | 10 | PEP8, type hints, docstrings |
| Testing | 10 | Unit + integration tests |
| Documentation | 10 | README, API docs, comments |

### Production Readiness (50 points)
| Component | Points | Criteria |
|-----------|--------|----------|
| Docker | 10 | Multi-stage, optimized |
| CI/CD | 10 | Automated, reliable |
| Cloud Deployment | 15 | Working on GCP |
| Monitoring | 10 | Prometheus, logs |
| Security | 5 | Secrets, auth |

### Innovation (20 points)
- Creative solutions
- Additional features
- Performance optimizations
- User experience

### Presentation (30 points)
| Deliverable | Points | Criteria |
|-------------|--------|----------|
| Live Demo | 15 | Working end-to-end |
| Documentation | 10 | Complete and clear |
| Code Review | 5 | Clean, well-organized |

---

## 💡 Implementation Guide

### Project Structure
```
capstone/
├── README.md
├── requirements.txt
├── .env.example
├── docker-compose.yml
├── Dockerfile
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── .github/
│   └── workflows/
│       ├── test.yml
│       └── deploy.yml
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── agents/
│   │   ├── vision_agent.py
│   │   ├── rag_agent.py
│   │   └── report_agent.py
│   ├── api/
│   │   ├── routes.py
│   │   └── models.py
│   ├── database/
│   │   ├── postgres.py
│   │   └── vector_store.py
│   └── utils/
│       ├── logging.py
│       └── monitoring.py
├── tests/
│   ├── test_agents.py
│   ├── test_api.py
│   └── test_integration.py
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API.md
│   └── DEPLOYMENT.md
└── monitoring/
    ├── prometheus.yml
    └── grafana_dashboard.json
```

### Key Code Snippets

#### 1. LangGraph Workflow
```python
from langgraph.graph import StateGraph, END

# Define state
class ManufacturingState(TypedDict):
    image: bytes
    question: str
    defects: List[str]
    answer: str
    report: str

# Build graph
workflow = StateGraph(ManufacturingState)

workflow.add_node("vision_agent", vision_agent)
workflow.add_node("rag_agent", rag_agent)
workflow.add_node("report_agent", report_agent)

workflow.add_edge("vision_agent", "rag_agent")
workflow.add_edge("rag_agent", "report_agent")
workflow.add_edge("report_agent", END)

workflow.set_entry_point("vision_agent")

app = workflow.compile()
```

#### 2. FastAPI Endpoint
```python
from fastapi import FastAPI, UploadFile, Depends
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Manufacturing Quality Assistant")

# Monitoring
Instrumentator().instrument(app).expose(app)

@app.post("/api/v1/inspect")
async def inspect_quality(
    image: UploadFile,
    question: str,
    language: str = "en"
):
    # Process through LangGraph
    result = await app.ainvoke({
        "image": await image.read(),
        "question": question
    })
    
    return {
        "defects": result["defects"],
        "answer": result["answer"],
        "report": result["report"]
    }
```

#### 3. Terraform Configuration
```hcl
# main.tf
resource "google_cloud_run_service" "app" {
  name     = "manufacturing-assistant"
  location = var.region

  template {
    spec {
      containers {
        image = var.docker_image
        
        env {
          name = "DATABASE_URL"
          value_from {
            secret_key_ref {
              name = "database-url"
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
  }
}
```

#### 4. GitHub Actions CI/CD
```yaml
# .github/workflows/deploy.yml
name: Deploy to GCP

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: |
          pip install -r requirements.txt
          pytest tests/
      
  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Build Docker image
        run: docker build -t gcr.io/$PROJECT/app:$SHA .
      
      - name: Push to GCR
        run: docker push gcr.io/$PROJECT/app:$SHA
      
      - name: Deploy with Terraform
        run: |
          cd terraform
          terraform init
          terraform apply -auto-approve
```

---

## 📦 Submission Requirements

### 1. GitHub Repository
- Complete source code
- Comprehensive README
- All configuration files
- Tests with >70% coverage

### 2. Live Deployment
- Working GCP deployment
- Public endpoint URL
- Monitoring dashboard
- API documentation

### 3. Documentation
- Architecture diagram
- Deployment guide
- API reference
- User manual
- Lessons learned

### 4. Demo Video (5-10 mins)
- Feature walkthrough
- Live demonstration
- Code explanation
- Results showcase

---

## ✅ Submission Checklist

### Code & Tests
- [ ] All features implemented
- [ ] Tests passing (>70% coverage)
- [ ] Code follows best practices
- [ ] Documentation complete

### Infrastructure
- [ ] Docker images built
- [ ] Terraform working
- [ ] CI/CD pipeline passing
- [ ] Secrets configured

### Deployment
- [ ] Deployed to GCP
- [ ] Monitoring active
- [ ] API accessible
- [ ] Performance tested

### Documentation
- [ ] README comprehensive
- [ ] Architecture documented
- [ ] API docs complete
- [ ] Deployment guide clear

### Presentation
- [ ] Demo video recorded
- [ ] Live demo prepared
- [ ] Slides ready
- [ ] Q&A rehearsed

---

## 🚀 Bonus Challenges (+20 points each)

1. **Mobile App**: Build Flutter/React Native frontend
2. **Edge Deployment**: Deploy model to edge devices
3. **A/B Testing**: Implement experiment framework
4. **Auto-scaling**: Configure horizontal scaling
5. **Multi-region**: Deploy to multiple regions

---

## 📚 Reference Materials

### Complete Guide
See [CAPSTONE_PROJECT.md](../CAPSTONE_PROJECT.md) for:
- Detailed architecture
- Step-by-step implementation
- Code templates
- Troubleshooting guide

### Example Repositories
- [LangGraph Examples](https://github.com/langchain-ai/langgraph/tree/main/examples)
- [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices)
- [MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp)

---

## 🎉 Final Notes

This capstone project demonstrates your ability to:
- Build complex Gen AI systems
- Deploy production applications
- Follow MLOps best practices
- Create portfolio-worthy projects

**Give it your best effort - this is your masterpiece! 🚀**

---

<div align="center">

**Week 11-12 Capstone** | Production Gen AI | Build something amazing! 🎯

[📖 Capstone Guide](../CAPSTONE_PROJECT.md) | [🏠 Course Home](../README.md)

</div>
