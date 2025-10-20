# 🚀 Local Setup Guide - Zero to Running in 5 Minutes

> **Complete step-by-step guide to run the Manufacturing Copilot on your local machine**

## 📋 Table of Contents

- [System Requirements](#-system-requirements)
- [Pre-Installation Checklist](#-pre-installation-checklist)
- [Installation Steps](#-installation-steps)
- [Verification & Testing](#-verification--testing)
- [Common Issues & Solutions](#-common-issues--solutions)
- [Development Workflow](#-development-workflow)
- [Next Steps](#-next-steps)

---

## 💻 System Requirements

### Minimum Requirements

| Component | Requirement |
|-----------|-------------|
| **OS** | Windows 10/11, macOS 10.15+, Ubuntu 20.04+ |
| **Python** | 3.11 or higher |
| **RAM** | 4 GB minimum (8 GB recommended) |
| **Disk Space** | 2 GB free space |
| **Internet** | Required (for HuggingFace API) |
| **GPU** | **NOT required** (uses cloud inference) |

### Required Software

- ✅ Python 3.11+ ([download](https://www.python.org/downloads/))
- ✅ Git ([download](https://git-scm.com/downloads))
- ✅ Code editor (VS Code recommended: [download](https://code.visualstudio.com/))
- ✅ HuggingFace account (free: [sign up](https://huggingface.co/join))

### Optional Software

- 🔹 Docker Desktop (for containerized deployment)
- 🔹 PostgreSQL (for production database, optional)
- 🔹 Postman/Insomnia (for API testing)

---

## ✅ Pre-Installation Checklist

### Step 1: Verify Python Installation

**Windows (PowerShell)**:
```powershell
python --version
# Should show: Python 3.11.x or higher
```

**macOS/Linux**:
```bash
python3 --version
# Should show: Python 3.11.x or higher
```

❌ **If Python not found or version < 3.11**:
- Download from https://www.python.org/downloads/
- During installation, check "Add Python to PATH"
- Restart terminal after installation

### Step 2: Verify Git Installation

```bash
git --version
# Should show: git version 2.x.x
```

❌ **If Git not found**:
- Download from https://git-scm.com/downloads
- Use default installation options

### Step 3: Create HuggingFace Account

1. **Sign up**: https://huggingface.co/join
2. **Verify email**: Check your inbox
3. **Create API token**:
   - Go to: https://huggingface.co/settings/tokens
   - Click "New token"
   - Name: `manufacturing-copilot`
   - Type: **Read**
   - Click "Generate"
   - **Copy token** (starts with `hf_...`)
   
4. **Accept Llama-2 license**:
   - Visit: https://huggingface.co/meta-llama/Llama-2-7b-chat-hf
   - Click "Agree and access repository"
   - Fill out the form
   - Wait for approval (usually instant)

✅ **Save your token somewhere safe!** You'll need it in Step 4.

---

## 🛠️ Installation Steps

### Step 1: Clone the Repository

**Windows (PowerShell)**:
```powershell
# Navigate to your projects folder
cd $HOME\Documents

# Clone repository
git clone https://github.com/abhayra12/Gen-AI-Roadmap.git

# Navigate to capstone project
cd Gen-AI-Roadmap\capstone_project
```

**macOS/Linux**:
```bash
# Navigate to your projects folder
cd ~/Documents

# Clone repository
git clone https://github.com/abhayra12/Gen-AI-Roadmap.git

# Navigate to capstone project
cd Gen-AI-Roadmap/capstone_project
```

### Step 2: Create Virtual Environment

**Windows (PowerShell)**:
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# If you get execution policy error:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

**macOS/Linux**:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

✅ **Verify activation**: Your terminal prompt should now show `(venv)` at the beginning.

### Step 3: Install Dependencies

```bash
# Upgrade pip (ensures latest package versions)
pip install --upgrade pip

# Install all dependencies (this may take 2-3 minutes)
pip install -r requirements.txt
```

✅ **Successful installation** shows:
```
Successfully installed langchain-0.x.x langchain-huggingface-0.0.1 ...
```

❌ **If installation fails**:
```bash
# Try installing dependencies one by one
pip install fastapi uvicorn pydantic python-dotenv
pip install langchain langchain-huggingface
pip install chromadb sentence-transformers
```

### Step 4: Configure Environment Variables

**Option A: Copy from template (Recommended)**

**Windows**:
```powershell
# Copy template
copy .env.example .env

# Open in Notepad
notepad .env
```

**macOS/Linux**:
```bash
# Copy template
cp .env.example .env

# Open in default editor
nano .env
# Or use: code .env (VS Code), vim .env, etc.
```

**Option B: Create manually**

Create a file named `.env` in the `capstone_project` folder with this content:

```bash
# Application Settings
APP_TITLE="Manufacturing Copilot API"
APP_VERSION="1.0.0"
LOG_LEVEL=INFO

# HuggingFace Configuration (REQUIRED)
HUGGINGFACE_TOKEN=hf_your_token_here  # ⬅️ REPLACE THIS

# Model Configuration
VLM_MODEL_ID=Salesforce/blip2-opt-2.7b
LLM_MODEL_ID=meta-llama/Llama-2-7b-chat-hf
EMBEDDING_MODEL_ID=sentence-transformers/all-MiniLM-L6-v2

# API Configuration
MAX_RETRIES=3
REQUEST_TIMEOUT=60
TEMPERATURE=0.7
MAX_TOKENS=512

# ChromaDB
CHROMA_PERSIST_DIR=./chroma_db

# Authentication
VALID_AUTH_TOKEN_PREFIX="Bearer technician-"
```

**⚠️ IMPORTANT**: Replace `hf_your_token_here` with your actual HuggingFace token from Step 3!

**Example**:
```bash
HUGGINGFACE_TOKEN=hf_AbCdEfGhIjKlMnOpQrStUvWxYz1234567890
```

✅ **Save the file** (Ctrl+S or Cmd+S)

### Step 5: Verify Setup

Run the automated verification script:

```bash
python scripts/test_setup.py
```

**Expected output**:
```
✅ Environment variables loaded successfully
✅ HuggingFace authentication successful
✅ Embeddings model accessible
✅ LLM endpoint responding
✅ ChromaDB initialized
✅ All systems ready!

Setup validation complete! You can now run the API server.
```

❌ **If you see errors**, see [Common Issues](#-common-issues--solutions) section below.

### Step 6: Start the API Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

**Expected output**:
```
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using StatReload
INFO:     Started server process [12346]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

🎉 **Success!** The API is now running at http://localhost:8080

---

## 🧪 Verification & Testing

### Test 1: Health Check

**Browser**:
- Open: http://localhost:8080/health

**Expected response**:
```json
{"status": "ok"}
```

**cURL (PowerShell)**:
```powershell
curl http://localhost:8080/health
```

**cURL (macOS/Linux)**:
```bash
curl http://localhost:8080/health
```

✅ **If you see `{"status": "ok"}`**, the server is running!

### Test 2: Interactive API Docs

1. **Open browser**: http://localhost:8080/docs
2. **You should see**: Swagger UI with API documentation
3. **Try the `/v1/diagnose` endpoint**:
   - Click "Try it out"
   - Fill in example data (or use defaults)
   - Click "Execute"
   - Wait 10-15 seconds for response

**Example request**:
```json
{
  "plant_id": "PUNE-IN",
  "equipment_id": "CNC-A-102",
  "problem_description": "Machine overheating during operation",
  "image_id": "test_img_001"
}
```

**Expected response** (partial):
```json
{
  "request_id": "uuid-here",
  "vision_analysis": {
    "defects_found": ["micro-fracture", "surface-roughness"],
    "confidence": 0.87
  },
  "rag_guidance": {
    "recommended_steps": [
      "1. Check coolant levels in the reservoir...",
      ...
    ]
  },
  "generated_report": "MANUFACTURING INCIDENT REPORT\n\n...",
  "confidence_score": 0.86
}
```

### Test 3: Command-Line Test

**PowerShell**:
```powershell
$headers = @{
    "X-Auth-Token" = "Bearer technician-test123"
    "Content-Type" = "application/json"
}

$body = @{
    plant_id = "PUNE-IN"
    equipment_id = "CNC-A-102"
    problem_description = "Machine overheating during operation"
    image_id = "test_img_001"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8080/v1/diagnose" `
    -Method POST `
    -Headers $headers `
    -Body $body
```

**Bash (macOS/Linux)**:
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

### Test 4: Python Client Test

Create a file `test_client.py`:

```python
import requests
import json

# API endpoint
url = "http://localhost:8080/v1/diagnose"

# Request headers
headers = {
    "X-Auth-Token": "Bearer technician-test123",
    "Content-Type": "application/json"
}

# Request body
data = {
    "plant_id": "PUNE-IN",
    "equipment_id": "CNC-A-102",
    "problem_description": "Machine overheating during operation",
    "image_id": "test_img_001"
}

# Send request
print("Sending diagnosis request...")
response = requests.post(url, headers=headers, json=data)

# Print results
print(f"\nStatus Code: {response.status_code}")
print(f"\nResponse:\n{json.dumps(response.json(), indent=2)}")
```

Run it:
```bash
python test_client.py
```

---

## 🔧 Common Issues & Solutions

### Issue 1: "HUGGINGFACE_TOKEN not found"

**Symptoms**:
```
KeyError: 'HUGGINGFACE_TOKEN'
```

**Solutions**:

1. **Check .env file exists**:
   ```bash
   # Windows
   dir .env
   
   # macOS/Linux
   ls -la .env
   ```

2. **Verify content**:
   ```bash
   # Windows
   type .env | findstr HUGGINGFACE_TOKEN
   
   # macOS/Linux
   cat .env | grep HUGGINGFACE_TOKEN
   ```

3. **Check for typos**:
   - ✅ Correct: `HUGGINGFACE_TOKEN=hf_abc123`
   - ❌ Wrong: `HUGGINGFACE_TOKEN = hf_abc123` (extra spaces)
   - ❌ Wrong: `HUGGING_FACE_TOKEN=hf_abc123` (underscore)

4. **Verify .env is in correct folder**:
   ```bash
   pwd  # Should show: .../capstone_project
   ```

### Issue 2: "Model loading timeout" / "Request timed out"

**Symptoms**:
```
TimeoutError: Request to HuggingFace API timed out
```

**Cause**: First API call to HuggingFace takes 30-60 seconds (cold start).

**Solutions**:

1. **Increase timeout in `.env`**:
   ```bash
   REQUEST_TIMEOUT=90  # Increase from 60 to 90 seconds
   ```

2. **Wait patiently**: First request is slowest. Subsequent requests are faster (5-10s).

3. **Try smaller model** (if issue persists):
   ```bash
   # Edit .env
   LLM_MODEL_ID=google/flan-t5-large
   ```

### Issue 3: "ChromaDB collection error"

**Symptoms**:
```
ValueError: Collection already exists
```

**Solution**: Delete and recreate ChromaDB:

**Windows**:
```powershell
Remove-Item -Recurse -Force .\chroma_db
```

**macOS/Linux**:
```bash
rm -rf ./chroma_db
```

Then restart the server.

### Issue 4: "Port 8080 already in use"

**Symptoms**:
```
ERROR: [Errno 48] Address already in use
```

**Solution A: Use different port**:
```bash
uvicorn app.main:app --reload --port 8000
# Then access at http://localhost:8000
```

**Solution B: Kill process on port 8080**:

**Windows**:
```powershell
# Find process
netstat -ano | findstr :8080

# Kill process (replace <PID> with actual process ID)
taskkill /PID <PID> /F
```

**macOS/Linux**:
```bash
# Kill process on port 8080
lsof -ti:8080 | xargs kill -9
```

### Issue 5: "Import Error: langchain_huggingface"

**Symptoms**:
```
ImportError: cannot import name 'HuggingFaceEndpoint' from 'langchain_huggingface'
```

**Solution**:
```bash
pip install langchain-huggingface --force-reinstall
```

### Issue 6: "Virtual environment not activating"

**Windows PowerShell - Execution Policy Error**:
```
cannot be loaded because running scripts is disabled
```

**Solution**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

**macOS/Linux - Permission Denied**:
```bash
chmod +x venv/bin/activate
source venv/bin/activate
```

### Issue 7: "Invalid authentication token"

**Symptoms**:
```json
{"detail": "Invalid authentication token"}
```

**Cause**: Wrong header format.

**Solution**: Ensure header follows this format:
```
X-Auth-Token: Bearer technician-<any_user_id>
```

**Examples**:
- ✅ `Bearer technician-john`
- ✅ `Bearer technician-test123`
- ❌ `technician-john` (missing "Bearer ")
- ❌ `Bearer john` (missing "technician-" prefix)

### Issue 8: "Rate limit exceeded"

**Symptoms**:
```
HuggingFace API rate limit exceeded
```

**Cause**: Too many requests in short time (free tier limit).

**Solutions**:

1. **Wait 1 minute** and try again
2. **Upgrade to HF Pro** ($9/month): https://huggingface.co/pricing
3. **Add retry delay** in code (already implemented in `app/agents.py`)

### Issue 9: Slow response times

**Symptoms**: Requests take >30 seconds.

**Normal Response Times**:
- First request: 30-60 seconds (cold start)
- Subsequent requests: 10-15 seconds

**Optimization tips**:

1. **Use smaller models** (edit `.env`):
   ```bash
   LLM_MODEL_ID=google/flan-t5-base
   ```

2. **Reduce max tokens** (edit `.env`):
   ```bash
   MAX_TOKENS=256  # Reduce from 512
   ```

3. **Enable caching** (already implemented in code)

---

## 🔄 Development Workflow

### Starting Development

```bash
# 1. Activate virtual environment
source venv/bin/activate  # macOS/Linux
.\venv\Scripts\Activate.ps1  # Windows

# 2. Start server in reload mode
uvicorn app.main:app --reload --port 8080

# Code changes auto-reload!
```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=app --cov-report=html

# Open coverage report
open htmlcov/index.html  # macOS
start htmlcov\index.html  # Windows
```

### Code Quality

```bash
# Format code
black app/

# Lint code
flake8 app/

# Type checking
mypy app/ --ignore-missing-imports
```

### Viewing Logs

Logs are printed to console. For structured logging:

```bash
# Redirect to file
uvicorn app.main:app --log-config logging.yaml > logs/app.log 2>&1
```

### Stopping the Server

**Terminal**: Press `Ctrl+C`

**Deactivate virtual environment**:
```bash
deactivate
```

---

## 🎯 Next Steps

### Learn More

1. **Read Implementation Guide**: [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)
   - Understand agent architecture
   - Learn how LangGraph orchestration works
   - Explore customization options

2. **Check Production Guide**: [PRODUCTION_READINESS.md](PRODUCTION_READINESS.md)
   - Production checklist (97/100 ready)
   - Deployment strategies
   - Monitoring and observability

3. **Explore Main README**: [README.md](README.md)
   - Full feature list
   - API documentation
   - Deployment options

### Customize the Project

1. **Add new SOPs**: Edit `app/agents.py` → `RAGAgent._populate_sample_docs()`
2. **Change models**: Edit `.env` → Update `LLM_MODEL_ID`
3. **Add new agents**: See [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md#add-a-new-agent)
4. **Modify prompts**: Edit `app/agents.py` → Prompt templates

### Deploy to Production

**Option 1: Docker**
```bash
docker build -t manufacturing-copilot:latest .
docker run -p 8080:8080 -e HUGGINGFACE_TOKEN=hf_... manufacturing-copilot
```

**Option 2: Google Cloud Run**
```bash
cd terraform
terraform init
terraform apply -var="project_id=your-gcp-project"
```

**Option 3: AWS/Azure**
- See deployment scripts in `scripts/deploy_cloud_run.py`
- Adapt for your cloud provider

---

## 📞 Getting Help

### Documentation

- **Setup Issues**: This guide (you're reading it!)
- **Code Questions**: [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)
- **API Reference**: http://localhost:8080/docs (when server running)
- **Course FAQ**: [../FAQ.md](../FAQ.md)

### Support Channels

1. **GitHub Issues**: https://github.com/abhayra12/Gen-AI-Roadmap/issues
2. **Course Discord**: (if applicable)
3. **Stack Overflow**: Tag with `langchain` `huggingface` `fastapi`

### Self-Help Checklist

Before asking for help, verify:
- [ ] Python 3.11+ installed (`python --version`)
- [ ] Virtual environment activated (see `(venv)` in terminal)
- [ ] Dependencies installed (`pip list | grep langchain`)
- [ ] .env file exists and has HF token
- [ ] Llama-2 license accepted on HuggingFace
- [ ] Internet connection working
- [ ] Ran `python scripts/test_setup.py` successfully

---

## 🎉 Congratulations!

You've successfully set up the Manufacturing Copilot on your local machine!

**What you've achieved**:
- ✅ Installed Python environment
- ✅ Configured HuggingFace API
- ✅ Initialized ChromaDB vector database
- ✅ Started FastAPI server
- ✅ Tested multi-agent workflow

**You now have**:
- 🤖 A production-ready AI agent system
- 🔍 Vision-Language Model for defect detection
- 🧠 RAG system with 5 manufacturing SOPs
- 📊 Automated report generation
- 🌐 RESTful API interface

**Ready to**:
- Learn how agents work ([IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md))
- Deploy to production ([PRODUCTION_READINESS.md](PRODUCTION_READINESS.md))
- Build your own agents (customize `app/agents.py`)
- Add to your portfolio (demo to recruiters!)

---

**Built with ❤️ for the Gen AI Masters Program**

Happy coding! 🚀
