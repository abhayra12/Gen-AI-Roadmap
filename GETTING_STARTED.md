# 🚀 Getting Started - 2 Minute Setup

Choose your path: **Codespaces (recommended)** or **Local**

---

## ⚡ Option 1: GitHub Codespaces (Easiest)

**Time**: 2-3 minutes  
**Difficulty**: ⭐ Beginner-friendly  
**Cost**: Free (60 hours/month on free tier)

### Steps:
1. **Click "Code" button** (top right, green button)
2. **Select "Codespaces" tab**
3. **Click "Create codespace on main"**
4. **Wait 2-3 minutes** for environment to build
5. **Open `00_environment_setup.ipynb`**
6. **Run all cells** to verify setup

✅ Done! Everything is pre-configured.

### Add Your API Keys (Optional)
For notebooks using HuggingFace or OpenAI:

1. Go to **Repository Settings** → **Secrets** → **Codespaces**
2. Add secrets:
   - `HUGGINGFACE_TOKEN` ([get it here](https://huggingface.co/settings/tokens))
   - `OPENAI_API_KEY` (if using OpenAI models)
3. Restart Codespace

---

## 💻 Option 2: Local Setup

**Time**: 10-15 minutes  
**Difficulty**: ⭐⭐ Requires some technical knowledge  
**Cost**: Free

### Prerequisites
- Python 3.11+ ([download](https://www.python.org/downloads/))
- Git ([download](https://git-scm.com/downloads))
- VS Code ([download](https://code.visualstudio.com/)) - recommended

### Steps:

#### 1. Clone Repository
```bash
git clone https://github.com/abhayra12/Gen-AI-Roadmap.git
cd Gen-AI-Roadmap
```

#### 2. Create Virtual Environment
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

#### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 4. Set Environment Variables
Create `.env` file in project root:
```bash
# .env file
HUGGINGFACE_TOKEN=hf_your_token_here
OPENAI_API_KEY=sk-your_key_here  # Optional
```

**Important**: Never commit `.env` to Git (already in `.gitignore`)

#### 5. Verify Setup
```bash
jupyter lab
# Open 00_environment_setup.ipynb
# Run all cells
```

✅ If all cells run without errors, you're ready!

---

## 🔧 Troubleshooting

### Common Issues

**"Python not found"**
```bash
# Check Python version
python --version  # Should be 3.11+

# If not installed, download from python.org
```

**"pip install fails"**
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Try again
pip install -r requirements.txt
```

**"Cannot activate venv" (Windows)**
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Try activating again
.\venv\Scripts\Activate.ps1
```

**"ImportError: No module named..."**
```bash
# Make sure venv is activated (you should see (venv) in prompt)
# Reinstall dependencies
pip install -r requirements.txt
```

**"CUDA/GPU not available"**
- Don't worry! Course works fine on CPU
- Most notebooks use small models
- For larger models, use Google Colab (free GPU)

### Still Stuck?

1. Check [FAQ.md](./FAQ.md)
2. Search existing [GitHub Issues](https://github.com/abhayra12/Gen-AI-Roadmap/issues)
3. Open a new issue with:
   - Your OS and Python version
   - Error message (full traceback)
   - Steps you've tried

---

## 📚 What's Next?

### Beginner Track:
1. ✅ **Week 0** (if new to Python): Review [BEGINNER_ASSESSMENT.md](./BEGINNER_ASSESSMENT.md)
2. 📓 **Week 1**: `week-01-02-python-ml-foundations/01_environment_setup.ipynb`
3. 🐍 **Week 1**: `02_python_essentials.ipynb`
4. 📊 **Week 2**: `03_numpy_pandas.ipynb`

### Experienced Track:
1. 📓 Scan Week 1-2 (review if needed)
2. 🧠 Start Week 3-4 (Deep Learning)
3. 🚀 Focus on Week 5+ (LLMs, Agents)

### Everyone:
- 📖 Read module READMEs before starting each week
- ✍️ Do the homework assignments
- 🏗️ Start thinking about capstone project ideas

---

## 🎯 Recommended Setup

### Essential Extensions (VS Code):
- **Python** (Microsoft)
- **Jupyter** (Microsoft)
- **GitHub Copilot** (optional, helpful)

### Helpful Tools:
- **Terminal**: Integrated terminal in VS Code
- **Git GUI**: GitHub Desktop (if you prefer GUI)
- **Notes**: Keep a learning journal

### Organization:
```
my-gen-ai-journey/
├── Gen-AI-Roadmap/        # This repo
├── my-projects/           # Your experiments
│   ├── week1-practice/
│   ├── week2-homework/
│   └── ...
└── notes/                 # Learning notes
```

---

## ⏱️ Time Estimates

| Activity | First Time | Subsequent |
|----------|-----------|------------|
| Codespace setup | 3 min | 30 sec |
| Local setup | 15 min | - |
| Per notebook | 30-90 min | - |
| Homework | 2-4 hours | - |
| Weekly total | 8-10 hours | - |

**Tip**: Set aside 1-2 hour blocks for focused learning.

---

## 🔑 API Keys Guide

### HuggingFace Token (Required)
1. Go to https://huggingface.co/settings/tokens
2. Click "New token"
3. Name: "gen-ai-course"
4. Type: "Read"
5. Copy token

### OpenAI API Key (Optional)
- Only needed for Week 5-6 and 7-8 OpenAI examples
- Alternative: Use open models (Llama, Mistral) - free
- Get key: https://platform.openai.com/api-keys

### Anthropic API Key (Optional)
- For Claude examples in Week 7-8
- Alternative: Use OpenAI or open models
- Get key: https://console.anthropic.com/

**Budget Tip**: Most notebooks work with free HuggingFace models!

---

## ✅ Setup Verification Checklist

Run this to verify everything:

```python
# In 00_environment_setup.ipynb

import sys
import torch
import transformers
import langchain
import pandas as pd
import numpy as np

print(f"✅ Python: {sys.version}")
print(f"✅ PyTorch: {torch.__version__}")
print(f"✅ Transformers: {transformers.__version__}")
print(f"✅ LangChain: {langchain.__version__}")
print(f"✅ Pandas: {pd.__version__}")
print(f"✅ NumPy: {np.__version__}")
```

All packages should print versions without errors.

---

## 🎓 Ready to Learn!

Everything set up? **Great!** 

**Next Steps**:
1. Open `week-01-02-python-ml-foundations/README.md`
2. Start with `01_environment_setup.ipynb`
3. Follow the notebooks in order
4. Join the learning journey!

**Need more details?** See [GETTING_STARTED_DETAILED.md](./GETTING_STARTED_DETAILED.md)

---

**Happy Learning!** 🚀

_Having issues? Open a [GitHub Issue](https://github.com/abhayra12/Gen-AI-Roadmap/issues) and we'll help!_
