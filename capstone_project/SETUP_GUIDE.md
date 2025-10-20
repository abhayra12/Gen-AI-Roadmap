# 🚀 Manufacturing Copilot - Complete Setup Guide

This guide will help you set up and run the Manufacturing Copilot from scratch.

## 📋 Prerequisites Checklist

Before starting, ensure you have:

- [ ] **Python 3.11+** installed ([download](https://www.python.org/downloads/))
- [ ] **Git** installed ([download](https://git-scm.com/downloads))
- [ ] **HuggingFace Account** ([sign up free](https://huggingface.co/join))
- [ ] **HuggingFace API Token** ([create here](https://huggingface.co/settings/tokens))

**Optional** (for full production setup):
- [ ] Docker & Docker Compose
- [ ] PostgreSQL 15+

## ⚡ Quick Start (5 Minutes)

### Step 1: Clone Repository

```bash
git clone https://github.com/abhayra12/Gen-AI-Roadmap.git
cd Gen-AI-Roadmap/capstone_project
```

### Step 2: Create Virtual Environment

**Windows (PowerShell)**:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This installs:
- FastAPI & Uvicorn (web framework)
- LangChain & LangGraph (agent orchestration)
- HuggingFace libraries (model integration)
- ChromaDB (vector database for RAG)
- All required utilities

**Note**: No PyTorch installation needed! We use HuggingFace Inference API.

### Step 4: Configure Environment Variables

1. **Copy the example file**:
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` file** and add your HuggingFace token:
   ```bash
   HUGGINGFACE_TOKEN=hf_your_token_here
   ```

3. **Verify configuration**:
   ```bash
   python scripts/test_setup.py
   ```

   This will test:
   - ✅ Environment variables loaded
   - ✅ HuggingFace authentication
   - ✅ Embeddings model access
   - ✅ LLM endpoint connectivity
   - ✅ ChromaDB setup

### Step 5: Run the API Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8080
INFO:     Application startup complete.
```

### Step 6: Test the API

Open your browser to **http://localhost:8080/docs**

You'll see the interactive API documentation (Swagger UI).

**Try this**:
1. Click on `POST /v1/diagnose`
2. Click "Try it out"
3. Use this example request:
   ```json
   {
     "plant_id": "PUNE-IN",
     "equipment_id": "CNC-A-102",
     "problem_description": "Machine overheating during operation",
     "image_id": "test_img_001"
   }
   ```
4. Add header: `X-Auth-Token: Bearer technician-test123`
5. Click "Execute"

You should get a complete diagnosis response with:
- Vision analysis
- RAG-based maintenance guidance
- Generated incident report

## 🧪 Running Tests

### Unit & Integration Tests

```bash
pytest tests/ -v
```

### With Coverage Report

```bash
pytest tests/ --cov=app --cov-report=html
open htmlcov/index.html  # View detailed coverage
```

### Test Specific Module

```bash
pytest tests/test_api.py -v          # API tests
pytest tests/test_models.py -v       # Model validation tests
pytest tests/test_security.py -v     # Security tests
```

## 🐳 Docker Deployment (Optional)

### Using Docker Compose (Recommended)

This sets up the full stack: API + PostgreSQL + ChromaDB

```bash
docker-compose up --build
```

Access:
- API: http://localhost:8080
- API Docs: http://localhost:8080/docs

### Building Docker Image Only

```bash
docker build -t manufacturing-copilot:latest .
```

### Running Container

```bash
docker run -p 8080:8080 \
  -e HUGGINGFACE_TOKEN=your_token_here \
  manufacturing-copilot:latest
```

## 🔧 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'langchain_huggingface'"

**Solution**:
```bash
pip install langchain-huggingface
```

Or reinstall all dependencies:
```bash
pip install -r requirements.txt --force-reinstall
```

### Issue: "HuggingFace token not found"

**Solution**:
1. Check that `.env` file exists in `capstone_project/` directory
2. Verify token is set: `cat .env | grep HUGGINGFACE_TOKEN`
3. Ensure no extra spaces: `HUGGINGFACE_TOKEN=hf_...` (no quotes, no spaces)

### Issue: "Model loading timeout"

**Solution**:
First time accessing HuggingFace Inference API may take 30-60 seconds as models "wake up". 

Increase timeout in `.env`:
```bash
REQUEST_TIMEOUT=60
```

### Issue: "ChromaDB collection error"

**Solution**:
Delete and recreate the database:
```bash
rm -rf ./chroma_db
python -c "from app.agents import rag_agent; print('ChromaDB reset')"
```

### Issue: "Port 8080 already in use"

**Solution**:
Use a different port:
```bash
uvicorn app.main:app --reload --port 8000
```

Or kill the process using port 8080:
```bash
# Windows
netstat -ano | findstr :8080
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:8080 | xargs kill -9
```

## 📊 Understanding the Architecture

### Agent Flow

```
User Request
    ↓
FastAPI Endpoint (/v1/diagnose)
    ↓
LangGraph Orchestrator
    ↓
┌───────────┬───────────┬───────────┐
│  Vision   │    RAG    │  Report   │
│  Agent    │   Agent   │  Agent    │
└─────┬─────┴─────┬─────┴─────┬─────┘
      ↓           ↓           ↓
  BLIP-2 VLM   Llama-2     Llama-2
  (HF API)     (HF API)    (HF API)
      ↓           ↓           ↓
  Defect     RAG Query   Report
  Detection  w/ ChromaDB Generation
      ↓           ↓           ↓
      └───────────┴───────────┘
                  ↓
          Combined Response
```

### Key Components

1. **Vision Agent** (`app/agents.py` - `VisionAgent`)
   - Uses BLIP-2 VLM via HuggingFace Inference API
   - Analyzes product images for manufacturing defects
   - Returns detected defects with confidence scores

2. **RAG Agent** (`app/agents.py` - `RAGAgent`)
   - Retrieves relevant maintenance documentation
   - Uses sentence-transformers for embeddings
   - ChromaDB for vector storage
   - Llama-2 for generating guidance
   - Cites source documents (SOPs, manuals)

3. **Report Agent** (`app/agents.py` - `ReportAgent`)
   - Generates professional incident reports
   - Uses Llama-2 via HuggingFace Inference API
   - Synthesizes vision + RAG outputs

4. **LangGraph Orchestrator** (`app/agents.py` - workflow)
   - Manages sequential execution of agents
   - Handles state between agents
   - Error handling and recovery

## 🎯 Production Deployment

### Deploy to Google Cloud Run

```bash
cd terraform
terraform init
terraform plan -var="project_id=your-gcp-project"
terraform apply -var="project_id=your-gcp-project"
```

Or use the deployment script:

```bash
python scripts/deploy_cloud_run.py \
  --project your-gcp-project \
  --region us-central1 \
  --service-name manufacturing-copilot
```

### Environment Variables for Production

In production, use **Google Secret Manager** or similar for:

```bash
HUGGINGFACE_TOKEN=<from secret manager>
DATABASE_URL=<cloud SQL connection>
LOG_LEVEL=INFO
ENABLE_TELEMETRY=true
```

## 📈 Monitoring & Observability

Every API request includes:
- **X-Request-Trace-ID**: Unique identifier for tracing
- **X-Response-Time-ms**: Response time in milliseconds

High latency warnings (>500ms) are automatically logged.

### Viewing Logs

**Local Development**:
```bash
# Logs are printed to console
# Check for warnings/errors
```

**Production (Docker)**:
```bash
docker-compose logs -f
```

**Production (Cloud Run)**:
```bash
gcloud logging read "resource.type=cloud_run_revision" --limit 50
```

## 🔐 Security Notes

1. **Never commit `.env` file** - it contains sensitive tokens
2. **Use environment variables** for all secrets in production
3. **Rotate HuggingFace tokens** periodically
4. **Enable CORS** appropriately for your frontend
5. **Use HTTPS** in production (handled by Cloud Run/GKE)

## 📚 Next Steps

1. ✅ **Complete Setup** - Follow this guide
2. 📖 **Read API Docs** - Explore http://localhost:8080/docs
3. 🧪 **Run Tests** - `pytest tests/ -v`
4. 🎨 **Customize Agents** - Edit `app/agents.py` for your use case
5. 🚀 **Deploy** - Use Terraform or Docker Compose

## 🤝 Getting Help

- **Issues**: Open a GitHub issue
- **Questions**: Check [FAQ](../FAQ.md)
- **Course**: Review Week 11-12 notebooks

---

**Built with ❤️ for the Gen AI Masters Program**

🎓 This capstone demonstrates production-ready Gen AI engineering skills!
