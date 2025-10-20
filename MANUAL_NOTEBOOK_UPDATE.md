# 📝 Manual Notebook Update Instructions

Due to encoding complexities, here's a manual guide to update notebooks from ChatOpenAI to HuggingFace endpoints.

## 🔄 Step-by-Step for Each Notebook

### Week 7-8 Notebooks Using ChatOpenAI (12 notebooks)

For each notebook listed below, make these changes:

1. `01_langchain_essentials.ipynb`
2. `02_message_structures.ipynb`
3. `03_prompt_templates_chains.ipynb`
4. `04_runnable_sequences.ipynb`
5. `07_advanced_rag_patterns.ipynb`
6. `08_query_optimization.ipynb`
7. `09_query_transformation.ipynb`
8. `11_langgraph_introduction.ipynb`
9. `12_building_agents.ipynb`
10. `14_agent_state_management.ipynb`
11. `15_corrective_rag.ipynb`
12. `16_mcp_introduction.ipynb` (already correct - uses simulated responses)

---

## 🛠️ Changes to Make in Each Notebook

### 1. Add Setup Cell (at the beginning, after imports)

Add a new code cell:

```python
# ⚙️ Setup: Load HuggingFace Token
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file from project root

HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
if not HF_TOKEN:
    raise ValueError(
        "❌ HUGGINGFACE_TOKEN not found!\\n"
        "Please ensure .env file exists in project root with:\\n"
        "HUGGINGFACE_TOKEN=hf_your_token_here\\n"
        "See 00_huggingface_setup.ipynb for setup instructions."
    )

print("✅ HuggingFace token loaded!")
```

### 2. Add Info Markdown Cell (before first LLM usage)

```markdown
**📝 Note**: This notebook uses **HuggingFace Inference Endpoints** instead of OpenAI.

- ✅ **No local GPU required**
- ✅ **Free tier available**  
- ✅ **Setup guide**: See `00_huggingface_setup.ipynb`

**Quick Setup**:
1. Get token from https://huggingface.co/settings/tokens
2. Add to `.env` file: `HUGGINGFACE_TOKEN=hf_your_token_here`
3. Run this notebook!
```

### 3. Replace Import Statement

**Find**:
```python
from langchain_openai import ChatOpenAI
```

**Replace with**:
```python
from langchain_huggingface import HuggingFaceEndpoint
```

### 4. Replace LLM Initialization

**Find** (example):
```python
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)
```

**Replace with**:
```python
llm = HuggingFaceEndpoint(
    repo_id=os.getenv("HF_LLM_MODEL", "meta-llama/Llama-2-7b-chat-hf"),
    huggingfacehub_api_token=HF_TOKEN,
    temperature=0.7,
    max_new_tokens=512,
    timeout=60
)
```

### Parameter Mapping:

| ChatOpenAI | HuggingFaceEndpoint |
|------------|---------------------|
| `model=` | `repo_id=` |
| `openai_api_key=` | `huggingfacehub_api_token=` |
| (none) | `max_new_tokens=` (required) |
| (none) | `timeout=` (optional but recommended) |

### Common Model Values:

| OpenAI | HuggingFace Equivalent |
|--------|------------------------|
| `gpt-3.5-turbo` | `meta-llama/Llama-2-7b-chat-hf` or `mistralai/Mistral-7B-Instruct-v0.2` |
| `gpt-4` | `meta-llama/Llama-2-7b-chat-hf` (no exact equivalent) |

---

## ⚡ Quick Find & Replace Guide

### 1. Imports
- Find: `from langchain_openai import ChatOpenAI`
- Replace: `from langchain_huggingface import HuggingFaceEndpoint`

### 2. Class Names
- Find: `ChatOpenAI(`
- Replace: `HuggingFaceEndpoint(`

### 3. Parameters
- Find: `model=`
- Replace: `repo_id=`

- Find: `openai_api_key=os.getenv("OPENAI_API_KEY")`
- Replace: `huggingfacehub_api_token=HF_TOKEN`

- Find: `model="gpt-3.5-turbo"`
- Replace: `repo_id=os.getenv("HF_LLM_MODEL", "meta-llama/Llama-2-7b-chat-hf")`

### 4. Add New Parameters
After `temperature=X.X,` add:
```python
max_new_tokens=512,
timeout=60
```

---

## 📋 Verification Checklist

For each updated notebook:

- [ ] Added setup cell with `load_dotenv()` and `HF_TOKEN`
- [ ] Added info markdown cell about HuggingFace
- [ ] Replaced `ChatOpenAI` → `HuggingFaceEndpoint`
- [ ] Replaced `model=` → `repo_id=`
- [ ] Replaced `openai_api_key=` → `huggingfacehub_api_token=HF_TOKEN`
- [ ] Added `max_new_tokens=512`
- [ ] Added `timeout=60`
- [ ] Tested the notebook runs without errors

---

## 🎯 Alternative: Simple Wrapper Approach

If you prefer minimal changes, add this at the top of each notebook:

```python
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint

load_dotenv()

# Create a ChatOpenAI-compatible wrapper
def ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7, **kwargs):
    """Wrapper to use HuggingFace instead of OpenAI"""
    return HuggingFaceEndpoint(
        repo_id=os.getenv("HF_LLM_MODEL", "meta-llama/Llama-2-7b-chat-hf"),
        huggingfacehub_api_token=os.getenv("HUGGINGFACE_TOKEN"),
        temperature=temperature,
        max_new_tokens=512,
        timeout=60,
        **kwargs
    )

print("✅ Using HuggingFace endpoints (ChatOpenAI wrapper)")
```

Then you don't need to change the rest of the notebook! Just add this cell at the beginning.

---

## 📚 Resources

- **Setup Guide**: `00_huggingface_setup.ipynb`
- **Migration Guide**: `HUGGINGFACE_MIGRATION.md`
- **HuggingFace Token**: https://huggingface.co/settings/tokens
- **Model Hub**: https://huggingface.co/models

---

## ⏱️ Time Estimate

- Per notebook: ~5 minutes
- All 12 notebooks: ~1 hour
- **OR** use wrapper approach: ~5 minutes total

---

## 🎓 For Students

**Recommended Order**:
1. Read `00_huggingface_setup.ipynb`
2. Set up `.env` file with your token
3. Start with Week 7-8 notebooks (they'll automatically use HuggingFace)
4. Enjoy learning without needing a GPU! 🚀

