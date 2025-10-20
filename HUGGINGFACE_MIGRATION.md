# 🔄 Course Notebooks - HuggingFace Migration Guide

## Overview

All course notebooks have been updated to use **HuggingFace Inference Endpoints** instead of OpenAI or local models.

## ✅ What Changed

### Environment Setup
- **New File**: `.env` in project root with `HUGGINGFACE_TOKEN`
- **New Notebook**: `00_huggingface_setup.ipynb` - Complete HF setup guide

### Import Changes

**Before** (OpenAI):
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)
```

**After** (HuggingFace):
```python
from langchain_huggingface import HuggingFaceEndpoint
import os
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-2-7b-chat-hf",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_TOKEN"),
    temperature=0.7,
    max_new_tokens=512
)
```

## 📋 Updated Notebooks

### Week 7-8: LangChain & Agents (12 notebooks)

All notebooks using `ChatOpenAI` have been updated to `HuggingFaceEndpoint`:

1. ✅ `01_langchain_essentials.ipynb`
2. ✅ `02_message_structures.ipynb`
3. ✅ `03_prompt_templates_chains.ipynb`
4. ✅ `04_runnable_sequences.ipynb`
5. ✅ `07_advanced_rag_patterns.ipynb`
6. ✅ `08_query_optimization.ipynb`
7. ✅ `09_query_transformation.ipynb`
8. ✅ `11_langgraph_introduction.ipynb`
9. ✅ `12_building_agents.ipynb`
10. ✅ `14_agent_state_management.ipynb`
11. ✅ `15_corrective_rag.ipynb`
12. ✅ `16_mcp_introduction.ipynb` (already uses HF)

### Week 5-6: LLMs & RAG
- Notebooks use HuggingFace Transformers library (already compatible)
- Added examples using HuggingFace Inference API

### Week 9-10: Training & Fine-tuning
- Fine-tuning notebooks remain as-is (they teach actual model training)
- Inference examples updated to use HF endpoints

## 🔧 Installation Requirements

Update `requirements.txt` in project root:

```txt
# Add these packages
langchain-huggingface==0.0.1
python-dotenv==1.0.0

# Keep existing packages
langchain==0.1.0
langchain-community==0.0.10
langgraph==0.0.20
transformers==4.35.2
sentence-transformers==2.2.2
chromadb==0.4.18
```

## 🚀 Quick Start for Students

### 1. Get HuggingFace Token
1. Create account: https://huggingface.co/join
2. Create token: https://huggingface.co/settings/tokens
3. Copy the token (starts with `hf_`)

### 2. Configure Environment
Create `.env` file in project root:
```bash
HUGGINGFACE_TOKEN=hf_your_token_here
HF_LLM_MODEL=meta-llama/Llama-2-7b-chat-hf
```

### 3. Accept Model Terms
For Llama-2, visit: https://huggingface.co/meta-llama/Llama-2-7b-chat-hf
Click "Agree and access repository"

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Start Learning!
Open `00_huggingface_setup.ipynb` first to verify setup.

## 📚 Recommended Models

### For LangChain & Agents (Week 7-8):

1. **Llama-2-7b-chat-hf** (Default, Best Quality)
   - Repo: `meta-llama/Llama-2-7b-chat-hf`
   - Requires: Agreeing to terms
   - Use for: General Q&A, conversation

2. **Mistral-7B-Instruct-v0.2** (Fast, No Special Access)
   - Repo: `mistralai/Mistral-7B-Instruct-v0.2`
   - Use for: Quick responses, coding

3. **Flan-T5-Large** (Lightweight)
   - Repo: `google/flan-t5-large`
   - Use for: Testing, simple tasks

### For Embeddings (RAG):

1. **all-MiniLM-L6-v2** (Default)
   - Fast and accurate
   - Works on CPU
   - Great for semantic search

## 🎯 Benefits of HuggingFace Approach

| Aspect | Local Models | OpenAI | HuggingFace Inference |
|--------|-------------|--------|----------------------|
| **GPU Required** | ✅ Yes | ❌ No | ❌ No |
| **Setup Complexity** | High | Low | Low |
| **Cost** | Free (if you have GPU) | Pay per token | Free tier + pay |
| **Model Choice** | Any | GPT models only | 1000s of models |
| **Privacy** | Best | Sends to OpenAI | Sends to HF |
| **Learning Value** | High | Medium | High |

✅ **HuggingFace = Best for Learning** - No GPU needed, many models, great for portfolios!

## 🔄 Migration Checklist

For each notebook using LLMs:

- [ ] Add `from dotenv import load_dotenv` and `load_dotenv()` at top
- [ ] Replace `from langchain_openai import ChatOpenAI` with `from langchain_huggingface import HuggingFaceEndpoint`
- [ ] Update LLM initialization:
  - Change `ChatOpenAI` → `HuggingFaceEndpoint`
  - Change `model` → `repo_id`
  - Change `openai_api_key` → `huggingfacehub_api_token`
  - Add `max_new_tokens` parameter
- [ ] Update token retrieval: `os.getenv("OPENAI_API_KEY")` → `os.getenv("HUGGINGFACE_TOKEN")`
- [ ] Test the notebook

## 📖 Additional Resources

- **HuggingFace Hub**: https://huggingface.co/models
- **Inference API Docs**: https://huggingface.co/docs/api-inference
- **LangChain HF Integration**: https://python.langchain.com/docs/integrations/llms/huggingface_endpoint
- **Setup Guide Notebook**: `00_huggingface_setup.ipynb`

## ⚠️ Important Notes

1. **First run may be slow** (30-60 seconds) as models "wake up"
2. **Free tier has rate limits** - Reasonable for learning
3. **Some models require access** - Just click "Agree" on model page
4. **Token is sensitive** - Never commit `.env` to Git (already in `.gitignore`)

## 🎓 For Instructors

When teaching:
1. Share your HuggingFace token approach (students get their own)
2. Start with `00_huggingface_setup.ipynb` 
3. Recommend `mistralai/Mistral-7B-Instruct-v0.2` for fast iteration
4. Use `meta-llama/Llama-2-7b-chat-hf` for quality responses

---

**Updated**: Course now 100% compatible with machines without GPUs! 🎉
