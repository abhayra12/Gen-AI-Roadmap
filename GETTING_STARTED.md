# 🚀 Getting Started with Gen AI Masters Program

Welcome to your Gen AI journey! This guide will help you set up your development environment and get started with the course.

---

## 📋 Prerequisites

### Required
- ✅ **GitHub Account** (for Codespaces)
- ✅ **HuggingFace Account** (free tier) - [Sign up here](https://huggingface.co/join)
- ✅ **Basic Python knowledge** (don't worry, we'll cover this in Week 1-2)
- ✅ **Internet connection** (for cloud-based development)

### Optional (for local development)
- Python 3.10 or higher
- 8GB RAM minimum (16GB recommended)
- Git installed locally

---

## 🌐 Setup Option 1: GitHub Codespaces (Recommended)

**Why Codespaces?**
- ✅ Zero installation required
- ✅ Pre-configured environment
- ✅ Works on any device (even tablets!)
- ✅ 60 hours/month free for personal accounts
- ✅ Consistent environment across devices

### Step-by-Step Setup

#### 1. Fork/Clone This Repository

```bash
# If you have your own copy
git clone <your-repo-url>

# Or fork on GitHub and then open in Codespaces
```

#### 2. Create a Codespace

1. Navigate to your repository on GitHub
2. Click the green **"Code"** button
3. Select **"Codespaces"** tab
4. Click **"Create codespace on main"**
5. Wait 2-3 minutes for environment to build

#### 3. Verify Installation

Once your Codespace is ready, open a terminal and run:

```bash
# Check Python version
python --version  # Should be 3.10+

# Check installed packages
pip list | grep -E "transformers|langchain|torch"

# Verify Jupyter
jupyter --version
```

#### 4. Set Up HuggingFace Token

1. Get your token from: https://huggingface.co/settings/tokens
2. Create a **Read** token (not Write for security)
3. Set as environment variable:

```bash
# In your Codespace terminal
echo 'export HUGGINGFACE_TOKEN="your_token_here"' >> ~/.bashrc
source ~/.bashrc

# Verify
echo $HUGGINGFACE_TOKEN
```

**Better approach:** Use GitHub Secrets
1. Go to repository **Settings** → **Secrets and variables** → **Codespaces**
2. Add new secret: `HUGGINGFACE_TOKEN`
3. Restart Codespace

#### 5. Launch Jupyter Lab

```bash
# Option 1: Jupyter Lab (Recommended)
jupyter lab

# Option 2: Jupyter Notebook (Classic)
jupyter notebook

# Option 3: VSCode Jupyter Extension (Already available in Codespaces)
# Just open any .ipynb file!
```

#### 6. Test Your Setup

Open `00_environment_setup.ipynb` and run all cells. This will:
- ✅ Verify all packages are installed
- ✅ Test HuggingFace connection
- ✅ Download a small test model
- ✅ Run a simple inference

---

## 💻 Setup Option 2: Local Development

### For Windows

#### 1. Install Python

```powershell
# Check if Python is installed
python --version

# If not, download from: https://www.python.org/downloads/
# Or use winget
winget install Python.Python.3.11
```

#### 2. Create Virtual Environment

```powershell
# Navigate to course directory
cd "C:\Users\abhay.ahirkar\OneDrive - TRIDIAGONAL.AI PRIVATE LIMITED\learning\Gen AI\T_Tech"

# Create virtual environment
python -m venv venv

# Activate
.\venv\Scripts\Activate.ps1

# If you get execution policy error
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### 3. Install Dependencies

```powershell
# Upgrade pip
python -m pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# This may take 5-10 minutes
```

#### 4. Set Environment Variables

```powershell
# Temporary (current session)
$env:HUGGINGFACE_TOKEN="your_token_here"

# Permanent (using System Properties)
# Or create a .env file (recommended)
```

Create `.env` file in root:
```bash
HUGGINGFACE_TOKEN=your_token_here
```

#### 5. Launch Jupyter

```powershell
# Make sure virtual environment is activated
jupyter lab
```

### For Linux/Mac

#### 1. Install Python

```bash
# Check Python version
python3 --version

# Install if needed (Ubuntu/Debian)
sudo apt update
sudo apt install python3.10 python3.10-venv python3-pip

# For Mac (using Homebrew)
brew install python@3.10
```

#### 2. Create Virtual Environment

```bash
# Navigate to course directory
cd ~/T_Tech

# Create virtual environment
python3 -m venv venv

# Activate
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt
```

#### 4. Set Environment Variables

```bash
# Add to ~/.bashrc or ~/.zshrc
echo 'export HUGGINGFACE_TOKEN="your_token_here"' >> ~/.bashrc
source ~/.bashrc

# Or use .env file (recommended)
```

#### 5. Launch Jupyter

```bash
jupyter lab
```

---

## 🔧 Configuration Files

### 1. `.devcontainer/devcontainer.json`

Already configured for GitHub Codespaces with:
- Python 3.10
- Jupyter extensions
- Git configuration
- Port forwarding for Jupyter

### 2. `requirements.txt`

Core dependencies:
```txt
# Core ML & Data Science
numpy>=1.24.0
pandas>=2.0.0
matplotlib>=3.7.0
seaborn>=0.12.0
scikit-learn>=1.3.0

# Deep Learning
torch>=2.0.0
torchvision>=0.15.0

# Transformers & NLP
transformers>=4.35.0
tokenizers>=0.15.0
datasets>=2.14.0
evaluate>=0.4.0
accelerate>=0.24.0

# LangChain Ecosystem
langchain>=0.1.0
langchain-community>=0.0.10
langchain-core>=0.1.0
langgraph>=0.0.20
langsmith>=0.0.60

# Vector Databases
chromadb>=0.4.18
faiss-cpu>=1.7.4

# RAG & Document Processing
pypdf>=3.17.0
python-docx>=1.1.0
unstructured>=0.10.0

# LLM Fine-tuning
peft>=0.7.0
bitsandbytes>=0.41.0
trl>=0.7.0

# API & Serving
fastapi>=0.104.0
uvicorn>=0.24.0
pydantic>=2.5.0

# Utilities
python-dotenv>=1.0.0
tqdm>=4.66.0
requests>=2.31.0

# Jupyter
jupyter>=1.0.0
jupyterlab>=4.0.0
ipywidgets>=8.1.0

# Visualization
plotly>=5.18.0
```

### 3. `.env.example`

```bash
# HuggingFace
HUGGINGFACE_TOKEN=your_token_here

# LangSmith (Optional for advanced tracking)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_key

# For production (later weeks)
GCP_PROJECT_ID=your_project_id
GCP_REGION=us-central1
```

---

## ✅ Verification Checklist

Run through this checklist to ensure everything is set up correctly:

### Environment Check
```bash
# Python version
python --version  # Should show 3.10+

# Pip packages
pip list | grep transformers  # Should show transformers package
pip list | grep langchain     # Should show langchain package
pip list | grep torch         # Should show torch package
```

### HuggingFace Check
```python
# Run in Python/Jupyter
from huggingface_hub import login
from transformers import pipeline

# This should work without errors
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
result = classifier("I love learning Gen AI!")
print(result)
```

### GPU Check (Optional - not needed for HuggingFace endpoints)
```python
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version: {torch.version.cuda if torch.cuda.is_available() else 'N/A'}")
```

---

## 🗂️ Workspace Organization

Organize your work:

```
T_Tech/
├── notebooks/           # Your working notebooks
│   ├── week-01/
│   ├── week-02/
│   └── ...
├── homework/            # Your homework submissions
│   ├── week-01/
│   └── ...
├── datasets/            # Downloaded datasets
├── models/              # Saved models (add to .gitignore)
└── outputs/             # Generated outputs
```

Create these directories:
```bash
mkdir -p notebooks/week-{01..12}
mkdir -p homework/week-{01..12}
mkdir -p datasets outputs
```

---

## 📚 Quick Start Tutorial

### Your First Gen AI Application (5 minutes)

1. **Open** `00_environment_setup.ipynb`
2. **Run** the verification cells
3. **Test** HuggingFace integration:

```python
from transformers import pipeline

# Load a sentiment analysis model
classifier = pipeline("sentiment-analysis")

# Test it
result = classifier("I'm excited to learn Gen AI!")
print(result)
# Output: [{'label': 'POSITIVE', 'score': 0.9998}]
```

4. **Congratulations!** You've just run your first Gen AI model! 🎉

---

## 🆘 Troubleshooting

### Common Issues

#### Issue 1: Package Installation Fails

```bash
# Solution 1: Upgrade pip
pip install --upgrade pip setuptools wheel

# Solution 2: Install one by one
pip install transformers
pip install langchain
# ... etc

# Solution 3: Use conda (if available)
conda install -c conda-forge transformers
```

#### Issue 2: HuggingFace Token Not Working

```bash
# Verify token is set
echo $HUGGINGFACE_TOKEN  # Linux/Mac
echo $env:HUGGINGFACE_TOKEN  # Windows PowerShell

# Re-login
python -c "from huggingface_hub import login; login()"
```

#### Issue 3: Out of Memory Error

```python
# Use smaller models or HuggingFace endpoints
# We'll use endpoints for most of the course to avoid this

# For local models, use quantization
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained(
    "model_name",
    load_in_8bit=True,  # Reduces memory usage
    device_map="auto"
)
```

#### Issue 4: Jupyter Kernel Dies

```bash
# Increase memory limit (if local)
# Or use HuggingFace Inference API instead of loading models locally

# Restart kernel
# Runtime → Restart Kernel
```

#### Issue 5: Slow Package Installation

```bash
# Use a mirror (for pip)
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# Or install essential packages only first
pip install transformers datasets torch
```

---

## 🎯 Next Steps

Now that your environment is ready:

1. ✅ **Complete** `00_environment_setup.ipynb`
2. 📖 **Read** the Week 1-2 README in `week-01-02-python-ml-foundations/`
3. 🚀 **Start** with `01_environment_setup.ipynb` in Week 1 folder
4. 📊 **Track** your progress in [PROGRESS_TRACKER.md](./PROGRESS_TRACKER.md)

---

## 💡 Pro Tips

1. **Use Codespaces** for hassle-free setup
2. **Commit regularly** to track your progress
3. **Use .env files** for secrets (never commit them!)
4. **Create branches** for experiments
5. **Save notebooks** with outputs for reference
6. **Use GPU** in later weeks (we'll show you how)

---

## 📞 Need Help?

- 📧 **Email:** [Your Support Email]
- 💬 **Discord:** [Community Link]
- 🐛 **GitHub Issues:** Report technical problems
- 📖 **FAQ:** Check [FAQ.md](./FAQ.md)

---

## ✅ Setup Complete!

If you've made it this far, congratulations! 🎉

You're now ready to start your Gen AI Masters journey. Let's build amazing things together!

**Next:** Open `week-01-02-python-ml-foundations/README.md`

---

<div align="center">
Happy Learning! 🚀 | Questions? Open an Issue!
</div>
