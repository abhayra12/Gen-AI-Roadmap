# 🚀 Gen AI Masters Program

### From Beginner to Production-Ready AI Engineer in 12 Weeks

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![HuggingFace](https://img.shields.io/badge/🤗-HuggingFace-yellow)](https://huggingface.co/)
[![GitHub Codespaces](https://img.shields.io/badge/Codespace-Ready-success)](https://github.com/features/codespaces)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Comprehensive hands-on curriculum designed to take you from zero to production-ready Gen AI engineer. 60+ notebooks, real-world capstone project, 100% practical learning. No GPU required!**

---

## 📚 Table of Contents

- [What You'll Achieve](#-what-youll-achieve)
- [Course Structure](#️-course-structure-12-weeks)
- [Capstone Project](#-capstone-project-manufacturing-copilot)
- [Quick Start](#-quick-start)
- [Learning Path](#-detailed-learning-path)
- [Prerequisites](#-prerequisites)
- [Resources](#-resources)
- [FAQ](#-faq)

---

## 🎯 What You'll Achieve

By the end of this program, you will have:

### ✅ Production Skills
- **Build & Deploy** multi-agent AI systems to the cloud (GCP, AWS, Azure)
- **Master LLMs** - Prompt engineering, fine-tuning, and RAG implementation
- **Production MLOps** - Docker, CI/CD, Terraform, Kubernetes
- **Industry Tools** - LangChain, LangGraph, HuggingFace, ChromaDB

### ✅ Portfolio-Ready Project
- **Manufacturing Copilot** - 3-agent system with Vision, RAG, and Reporting agents
- **Production-grade code** - 85%+ test coverage, containerized, cloud-deployed
- **GitHub showcase** - Professional README, docs, deployment scripts
- **Demo-able to employers** - Full API with Swagger docs

### ✅ Deep Understanding
- **60+ hands-on notebooks** - Theory + runnable code for every concept
- **Real-world problems** - From basics to production deployment
- **Best practices** - Security, observability, scalability, maintainability
- **Model Context Protocol (MCP)** - Latest LLM-tool integration standard

### 💰 Career Impact
- **Competitive salary** - Gen AI engineers earn $120-180k+ (US market)
- **High demand** - 10x growth in AI job postings in 2024
- **Future-proof skills** - AI is transforming every industry

---

## 🗓️ Course Structure: 12 Weeks

The curriculum is divided into six two-week phases, each building logically on the previous one. This structured approach ensures smooth progression from fundamentals to production-level skills.

| Weeks   | Phase | Focus | Key Topics | What You Build |
|---------|-------|-------|------------|----------------|
| **1-2** | **Foundations** | Python & ML Basics | Python, NumPy, Pandas, Sklearn, Data Viz | Classification models, data pipelines |
| **3-4** | **Deep Learning & NLP** | Neural Networks | CNNs, RNNs, LSTMs, Transformers, Attention | Image classifier, sequence models |
| **5-6** | **LLMs & RAG** | Large Language Models | Prompt Engineering, RAG, Vector DBs, Embeddings | Q&A system with RAG |
| **7-8** | **Agents & Orchestration** | Multi-Agent Systems | LangChain, LangGraph, **MCP**, Advanced RAG | Multi-agent workflow |
| **9-10** | **Training & Fine-tuning** | Model Customization | Pre-training, LoRA, QLoRA, PEFT, Evaluation | Fine-tuned domain model |
| **11-12** | **Production Deployment** | MLOps & Capstone | FastAPI, Docker, CI/CD, Terraform, GCP | **Manufacturing Copilot** |

**⏱️ Time Commitment**: 8-10 hours/week  
**🎓 Difficulty**: Beginner → Advanced (progressive difficulty)  
**💻 GPU Required**: ❌ No! Uses HuggingFace Inference API

---

## 🏭 Capstone Project: Manufacturing Copilot

The final two weeks culminate in building and deploying a **production-ready multi-agent AI system** for the manufacturing domain. This is your portfolio centerpiece.

### What It Does

<table>
<tr>
<td width="33%">

#### 📸 Vision Agent
- **Automated defect detection** from equipment images
- Uses **BLIP-2 VLM** via HuggingFace
- Identifies micro-fractures, surface damage, quality issues
- Confidence scoring

</td>
<td width="33%">

#### 🔧 RAG Agent
- **Technical documentation Q&A**
- ChromaDB vector database
- 5 pre-populated manufacturing SOPs
- **Llama-2** for guidance generation
- Citations to source documents

</td>
<td width="33%">

#### 📝 Report Agent
- **Automated incident reports**
- Professional formatting
- Integrates vision + RAG results
- **Llama-2** for natural language generation

</td>
</tr>
</table>

### 🤖 LangGraph Orchestration

All three agents are coordinated by a **LangGraph workflow** with sequential execution:

```
Vision Agent → RAG Agent → Report Agent
     ↓            ↓             ↓
  Defects → Maintenance → Incident Report
                           ↓
                     FastAPI Response
```

### 🛠️ Tech Stack

**Backend**: FastAPI, Python 3.11+  
**AI Framework**: LangChain, LangGraph, HuggingFace Inference API  
**Models**: Llama-2-7b-chat (LLM), BLIP-2 (VLM), all-MiniLM-L6-v2 (Embeddings)  
**Database**: ChromaDB (vector), PostgreSQL (optional)  
**Infrastructure**: Docker, Docker Compose, Terraform  
**Cloud**: Google Cloud Run (GCP)  
**CI/CD**: GitHub Actions  
**Testing**: Pytest (85%+ coverage)  

### 📊 Production Readiness: 97/100

- ✅ Containerized with Docker
- ✅ CI/CD pipeline configured
- ✅ Comprehensive tests (32+ test cases)
- ✅ API authentication
- ✅ Error handling & retry logic
- ✅ Structured logging
- ✅ Terraform IaC for cloud deployment
- ✅ OpenAPI/Swagger documentation
- ✅ Environment-based config

**📂 Code**: [`capstone_project/`](./capstone_project/)  
**📖 Documentation**:
- [README.md](./capstone_project/README.md) - Complete project overview
- [LOCAL_SETUP_GUIDE.md](./capstone_project/LOCAL_SETUP_GUIDE.md) - Zero to running in 5 minutes
- [IMPLEMENTATION_GUIDE.md](./capstone_project/IMPLEMENTATION_GUIDE.md) - Code walkthrough & customization

---

## 🚀 Quick Start

### Option 1: Start Learning (Recommended)

```bash
# 1. Clone repository
git clone https://github.com/abhayra12/Gen-AI-Roadmap.git
cd Gen-AI-Roadmap

# 2. Set up HuggingFace (no GPU needed!)
jupyter notebook 00_huggingface_setup.ipynb

# 3. Start with Week 1
cd week-01-02-python-ml-foundations
jupyter notebook 01_environment_setup.ipynb
```

### Option 2: Jump to Capstone

```bash
# 1. Navigate to capstone
cd Gen-AI-Roadmap/capstone_project

# 2. Follow setup guide
# See capstone_project/LOCAL_SETUP_GUIDE.md for detailed instructions

# 3. Run in 5 minutes!
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Add your HuggingFace token to .env
uvicorn app.main:app --reload --port 8080

# 4. Test at http://localhost:8080/docs
```

### Option 3: GitHub Codespaces (Zero Install)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=YOUR_REPO_ID)

Everything pre-configured! Just add your HuggingFace token.

---

## 📖 Detailed Learning Path

### Phase 1: Foundations (Weeks 1-2)

**📁 Folder**: `week-01-02-python-ml-foundations/`

| Notebook | Topic | Skills | Duration |
|----------|-------|--------|----------|
| 01_environment_setup.ipynb | Dev Environment | Virtual envs, Jupyter, Git | 1 hour |
| 02_python_essentials.ipynb | Python Refresher | Functions, classes, decorators | 2 hours |
| 03_numpy_pandas.ipynb | Data Manipulation | NumPy arrays, Pandas DataFrames | 3 hours |
| 04_data_visualization.ipynb | Visualization | Matplotlib, Seaborn, plotly | 2 hours |
| 05_ml_sklearn.ipynb | ML Fundamentals | Classification, regression, pipelines | 4 hours |

**🎯 Project**: Build a customer churn prediction model  
**📚 Resources**: [README.md](./week-01-02-python-ml-foundations/README.md) | [HOMEWORK.md](./week-01-02-python-ml-foundations/HOMEWORK.md)

---

### Phase 2: Deep Learning & NLP (Weeks 3-4)

**📁 Folder**: `week-03-04-deep-learning-nlp/`

| Notebook | Topic | Skills | Duration |
|----------|-------|--------|----------|
| 01_neural_networks.ipynb | Neural Net Basics | Perceptrons, backprop, activation functions | 3 hours |
| 02_cnn_basics.ipynb | Convolutional Networks | Image processing, conv layers, pooling | 3 hours |
| 03_rnn_lstm.ipynb | Recurrent Networks | Sequence modeling, LSTM, GRU | 3 hours |
| 04_transformers.ipynb | Transformer Architecture | Self-attention, encoder-decoder | 4 hours |
| 05_attention_mechanisms.ipynb | Attention Deep Dive | Multi-head attention, positional encoding | 3 hours |
| 06_embeddings.ipynb | Word/Token Embeddings | Word2Vec, GloVe, contextual embeddings | 2 hours |
| 07_huggingface_intro.ipynb | HuggingFace Basics | Transformers library, pipelines | 2 hours |

**🎯 Project**: Sentiment analysis with BERT  
**📚 Resources**: [README.md](./week-03-04-deep-learning-nlp/README.md) | [HOMEWORK.md](./week-03-04-deep-learning-nlp/HOMEWORK.md)

---

### Phase 3: LLMs & RAG (Weeks 5-6)

**📁 Folder**: `week-05-06-llms-rag/`

| Notebook | Topic | Skills | Duration |
|----------|-------|--------|----------|
| 01_llms_introduction.ipynb | LLM Fundamentals | GPT architecture, tokenization, inference | 3 hours |
| 02_huggingface_tasks.ipynb | HF Task APIs | Text generation, Q&A, summarization | 2 hours |
| 03_model_selection_preprocessing.ipynb | Model Selection | Choosing models, preprocessing strategies | 2 hours |
| 04_tokenizers_advanced.ipynb | Tokenization Deep Dive | BPE, WordPiece, SentencePiece | 2 hours |
| 05_prompt_engineering.ipynb | Prompt Engineering | Zero-shot, few-shot, chain-of-thought | 3 hours |
| 06_few_shot_learning.ipynb | Few-Shot Learning | In-context learning, examples | 2 hours |
| 07_rag_introduction.ipynb | RAG Concepts | Retrieval-augmented generation overview | 2 hours |
| 08_rag_implementation.ipynb | RAG Implementation | Build end-to-end RAG system | 4 hours |
| 09_vector_embeddings.ipynb | Vector Databases | ChromaDB, Pinecone, FAISS | 3 hours |

**🎯 Project**: Technical documentation Q&A system with RAG  
**📚 Resources**: [README.md](./week-05-06-llms-rag/README.md) | [HOMEWORK.md](./week-05-06-llms-rag/HOMEWORK.md)

---

### Phase 4: Agents & Orchestration (Weeks 7-8)

**📁 Folder**: `week-07-08-langchain-agents/`

| Notebook | Topic | Skills | Duration |
|----------|-------|--------|----------|
| 01_langchain_essentials.ipynb | LangChain Basics | Chains, prompts, memory | 2 hours |
| 02_message_structures.ipynb | Message Patterns | System, human, AI messages | 1 hour |
| 03_prompt_templates_chains.ipynb | Prompt Templates | Template design, chaining | 2 hours |
| 04_runnable_sequences.ipynb | LCEL | LangChain Expression Language | 2 hours |
| 05_document_loaders.ipynb | Document Loading | PDF, CSV, web scraping | 2 hours |
| 06_vector_databases.ipynb | Vector DBs Advanced | Hybrid search, metadata filtering | 2 hours |
| 07_advanced_rag_patterns.ipynb | Advanced RAG | Parent-child, hypothetical docs | 3 hours |
| 08_query_optimization.ipynb | Query Optimization | Query rewriting, expansion | 2 hours |
| 09_query_transformation.ipynb | Query Transformation | Multi-query, step-back | 2 hours |
| 10_rag_fusion_reranking.ipynb | RAG Fusion | Result reranking, fusion | 2 hours |
| 11_langgraph_introduction.ipynb | LangGraph Basics | State graphs, nodes, edges | 3 hours |
| 12_building_agents.ipynb | Agent Construction | ReAct, tools, memory | 3 hours |
| 13_agentic_tools.ipynb | Agent Tools | Custom tools, function calling | 2 hours |
| 14_agent_state_management.ipynb | State Management | Persistent state, checkpoints | 2 hours |
| 15_corrective_rag.ipynb | Corrective RAG | Self-correction, CRAG pattern | 2 hours |
| **16_mcp_introduction.ipynb** | **Model Context Protocol** | **MCP servers, tools, resources** | **3 hours** |

**🎯 Project**: Multi-agent research assistant with MCP integration  
**📚 Resources**: [README.md](./week-07-08-langchain-agents/README.md) | [HOMEWORK.md](./week-07-08-langchain-agents/HOMEWORK.md)

**🆕 NEW**: Week 7-8 now includes **Model Context Protocol (MCP)** - the emerging industry standard for LLM-tool integration!

---

### Phase 5: Training & Fine-tuning (Weeks 9-10)

**📁 Folder**: `week-09-10-training-finetuning/`

| Notebook | Topic | Skills | Duration |
|----------|-------|--------|----------|
| 01_pre_training_concepts.ipynb | Pre-training Theory | Language modeling, objectives | 2 hours |
| 02_bigram_language_model.ipynb | Simple LM | Build from scratch | 3 hours |
| 03_tensors_gpu_acceleration.ipynb | GPU Computing | PyTorch tensors, CUDA | 2 hours |
| 04_forward_backward_diagnostics.ipynb | Training Diagnostics | Loss curves, gradients | 2 hours |
| 05_mlp_sensor_fusion.ipynb | Multi-Layer Perceptrons | Feature fusion | 2 hours |
| 06_minibatch_curriculum.ipynb | Training Strategies | Batching, curriculum learning | 2 hours |
| 07_finetuning_vs_rag.ipynb | Fine-tuning vs RAG | When to use each approach | 2 hours |
| 08_peft_foundations.ipynb | PEFT Fundamentals | Parameter-efficient fine-tuning | 2 hours |
| 09_lora_qlora.ipynb | LoRA & QLoRA | Low-rank adaptation, quantization | 3 hours |

**🎯 Project**: Fine-tune Llama-2 for manufacturing domain  
**📚 Resources**: [README.md](./week-09-10-training-finetuning/README.md) | [HOMEWORK.md](./week-09-10-training-finetuning/HOMEWORK.md)

---

### Phase 6: Production Deployment (Weeks 11-12)

**📁 Folder**: `capstone_project/`

**Focus**: Build, test, and deploy the **Manufacturing Copilot** to production.

**Week 11 - Build & Test**:
- Implement 3 agents (Vision, RAG, Report)
- LangGraph orchestration
- FastAPI endpoints
- Unit & integration tests
- Local testing

**Week 12 - Deploy**:
- Containerization (Docker)
- CI/CD pipeline (GitHub Actions)
- Infrastructure as Code (Terraform)
- Cloud deployment (GCP Cloud Run)
- Monitoring & logging
- Documentation

**📚 Resources**:
- [README.md](./capstone_project/README.md) - Full project overview
- [LOCAL_SETUP_GUIDE.md](./capstone_project/LOCAL_SETUP_GUIDE.md) - Setup in 5 minutes
- [IMPLEMENTATION_GUIDE.md](./capstone_project/IMPLEMENTATION_GUIDE.md) - Code walkthrough
- [PRODUCTION_READINESS.md](./capstone_project/PRODUCTION_READINESS.md) - Deployment checklist

---

## ✅ Prerequisites

### Required Knowledge (Beginner-Friendly!)

- ✅ **Basic Python** - Variables, functions, loops (can learn in Week 1)
- ✅ **Command Line** - Running scripts, navigation (taught in course)
- ✅ **Basic Math** - High school algebra (matrices explained in course)

### Not Required

- ❌ **No ML/AI experience needed** - Start from scratch
- ❌ **No GPU required** - Uses HuggingFace cloud inference
- ❌ **No CS degree needed** - Self-learner friendly
- ❌ **No prior LLM experience** - We teach everything

### Technical Requirements

- **Python 3.11+** ([download](https://www.python.org/downloads/))
- **4GB RAM minimum** (8GB recommended)
- **2GB disk space**
- **Internet connection** (for HuggingFace API)
- **HuggingFace account** (free: [sign up](https://huggingface.co/join))

### Beginner Assessment

**Wondering if this course is right for you?**  
Read our [BEGINNER_ASSESSMENT.md](./BEGINNER_ASSESSMENT.md) - We rated this course **9.0/10 for beginners**!

---

## 📚 Resources

### Getting Started

- 📘 [GETTING_STARTED.md](./GETTING_STARTED.md) - Complete onboarding guide
- 🤗 [00_huggingface_setup.ipynb](./00_huggingface_setup.ipynb) - HuggingFace setup (required!)
- 📝 [PROGRESS_TRACKER.md](./PROGRESS_TRACKER.md) - Track your learning journey
- ❓ [FAQ.md](./FAQ.md) - Frequently asked questions

### Course Documentation

- 📖 [COURSE_SUMMARY.md](./COURSE_SUMMARY.md) - High-level overview
- 🔗 [COURSE_CONNECTIONS.md](./COURSE_CONNECTIONS.md) - How topics connect
- 🎯 [BEGINNER_ASSESSMENT.md](./BEGINNER_ASSESSMENT.md) - Is this course for you?

### Capstone Documentation

- 🏭 [capstone_project/README.md](./capstone_project/README.md) - Project overview
- 🚀 [capstone_project/LOCAL_SETUP_GUIDE.md](./capstone_project/LOCAL_SETUP_GUIDE.md) - Local setup
- 🛠️ [capstone_project/IMPLEMENTATION_GUIDE.md](./capstone_project/IMPLEMENTATION_GUIDE.md) - Code deep dive

### External Resources

- [HuggingFace Documentation](https://huggingface.co/docs)
- [LangChain Documentation](https://python.langchain.com/docs/introduction/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

---

## ❓ FAQ

<details>
<summary><strong>Do I need a GPU to run this course?</strong></summary>

**No!** This course uses **HuggingFace Inference API**, which runs models in the cloud. You only need a CPU and internet connection. See [00_huggingface_setup.ipynb](./00_huggingface_setup.ipynb) for setup.
</details>

<details>
<summary><strong>Is this course suitable for complete beginners?</strong></summary>

**Yes!** We rated this course **9.0/10 for beginners**. Week 1-2 covers Python and ML fundamentals. If you can write basic Python (variables, functions), you can start. See [BEGINNER_ASSESSMENT.md](./BEGINNER_ASSESSMENT.md) for detailed breakdown.
</details>

<details>
<summary><strong>How much does this cost?</strong></summary>

- **Course materials**: Free (MIT License)
- **HuggingFace API**: Free tier available (sufficient for learning)
- **Cloud deployment**: GCP free tier covers basic deployment
- **Total**: $0 to get started, <$50 for full production deployment
</details>

<details>
<summary><strong>Can I use OpenAI instead of HuggingFace?</strong></summary>

**Yes!** The course is designed for HuggingFace (no GPU needed), but most notebooks can be adapted to use OpenAI APIs. You'll need to modify initialization code. See individual notebook READMEs for guidance.
</details>

<details>
<summary><strong>How long does it take to complete?</strong></summary>

**12 weeks at 8-10 hours/week** for full completion. However:
- **Fast track**: 6 weeks at 20 hours/week
- **Part-time**: 6 months at 3-4 hours/week
- **Just capstone**: 2 weeks if you have LLM experience

Progress at your own pace!
</details>

<details>
<summary><strong>Will this get me a job?</strong></summary>

This course provides **production-ready skills** and a **portfolio project**. Many Gen AI engineer roles require:
- ✅ LLM fine-tuning (Week 9-10)
- ✅ RAG implementation (Week 5-6)
- ✅ Agent orchestration (Week 7-8)
- ✅ Production deployment (Week 11-12)

You'll learn all of this! However, landing a job also requires networking, interview prep, and soft skills.
</details>

<details>
<summary><strong>Can I contribute to this course?</strong></summary>

**Yes!** Contributions welcome:
- Report issues: [GitHub Issues](https://github.com/abhayra12/Gen-AI-Roadmap/issues)
- Suggest improvements: Pull requests
- Share your capstone variations: We'd love to see them!

See [LICENSE](./LICENSE) for terms.
</details>

---

## 🏆 What Makes This Course Unique?

### ✅ Production-First Approach
Most courses teach theory. We teach you to **ship code to production** from day one.

### ✅ No GPU Barrier
Using **HuggingFace Inference API** means anyone can learn, regardless of hardware.

### ✅ Real-World Capstone
Not a toy project. The **Manufacturing Copilot** is production-ready code you can deploy and demo.

### ✅ Latest Technologies
- **Model Context Protocol (MCP)** - Emerging industry standard
- **LangGraph** - State-of-the-art agent orchestration
- **HuggingFace** - Industry-standard model hub

### ✅ Comprehensive Coverage
60+ notebooks covering **every step** from Python basics to cloud deployment.

---

## 🤝 Contributing

Contributions are welcome! Please:

1. **Report bugs**: [Open an issue](https://github.com/abhayra12/Gen-AI-Roadmap/issues)
2. **Suggest improvements**: Submit a pull request
3. **Share your projects**: We'd love to see your capstone variations!

See [LICENSE](./LICENSE) for terms.

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](./LICENSE) file for details.

---

## 🙏 Acknowledgments

- **HuggingFace** for democratizing AI with free inference APIs
- **LangChain** team for the incredible agent framework
- **Anthropic** for Model Context Protocol inspiration
- **FastAPI** for the best Python web framework
- **Open-source community** for the tools that make this possible

---

## 📞 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/abhayra12/Gen-AI-Roadmap/issues)
- **Discussions**: [GitHub Discussions](https://github.com/abhayra12/Gen-AI-Roadmap/discussions)
- **Email**: (if applicable)

---

## 🎓 Ready to Start?

### Choose Your Path:

**Path 1: Complete Course (Recommended for Beginners)**
```bash
git clone https://github.com/abhayra12/Gen-AI-Roadmap.git
cd Gen-AI-Roadmap
jupyter notebook 00_huggingface_setup.ipynb
```

**Path 2: Jump to Capstone (For Experienced Learners)**
```bash
git clone https://github.com/abhayra12/Gen-AI-Roadmap.git
cd Gen-AI-Roadmap/capstone_project
# See LOCAL_SETUP_GUIDE.md for 5-minute setup
```

**Path 3: Browse & Explore**
- View notebooks on GitHub
- Read documentation first
- Clone when ready

---

**Built with ❤️ for aspiring Gen AI engineers**

**From Zero to Production in 12 Weeks** 🚀

---

## ⭐ Star This Repository

If you find this course valuable, please **star this repository** to help others discover it!

[![GitHub stars](https://img.shields.io/github/stars/abhayra12/Gen-AI-Roadmap.svg?style=social)](https://github.com/abhayra12/Gen-AI-Roadmap/stargazers)

- **Deployment:** Docker, Terraform, GitHub Actions

---- **Cloud:** Google Cloud Platform (GCP) - specifically Cloud Run or GKE

- **Monitoring:** Prometheus, Grafana

## 🚀 Quick Start

All code for the final project is located in the `capstone_project/` directory. The notebooks in the `week-11-12` module serve as conceptual guides for the implementation within the capstone, providing the theoretical underpinnings for the production code.

### GitHub Codespaces (2 minutes)

```---

1. Click "Code" → "Codespaces" → "Create codespace"

2. Wait 2-3 minutes for environment## 🛠️ Getting Started

3. Open 00_environment_setup.ipynb

4. Start learning!A smooth start is crucial. We've designed the setup process to be as simple as possible, with a strong recommendation for using a cloud-based development environment.

```

### Prerequisites

### Local Setup- Basic understanding of Python programming.

```bash- An active GitHub account.

git clone https://github.com/abhayra12/Gen-AI-Roadmap.git- **Strongly Recommended:** Use GitHub Codespaces for a seamless, pre-configured environment that works right out of the box.

cd Gen-AI-Roadmap

python -m venv venv### Quick Start with GitHub Codespaces (Recommended)

source venv/bin/activate  # Windows: .\venv\Scripts\activate1.  Click the **"Code"** button at the top of the repository page.

pip install -r requirements.txt2.  Select the **"Codespaces"** tab.

```3.  Click **"Create codespace on main"**.

4.  The environment will build automatically in your browser. Once it's ready, VS Code will open.

**Full Guide**: [GETTING_STARTED.md](./GETTING_STARTED.md)5.  Open the `00_environment_setup.ipynb` notebook and begin your journey!



---For a detailed guide on setting up your environment locally, please see [GETTING_STARTED.md](./GETTING_STARTED.md).



## 📂 What's Inside---



```## 📁 Repository Structure

├── week-01-02-python-ml-foundations/  # Start here

├── week-03-04-deep-learning-nlp/      # Neural networksThe repository is organized into weekly modules, with a clear separation between conceptual notebooks and the final production-level capstone project.

├── week-05-06-llms-rag/                # LLMs & RAG

├── week-07-08-langchain-agents/       # Agents & MCP ⭐```

├── week-09-10-training-finetuning/    # Fine-tuningT_Tech/

├── week-11-12-production-capstone/    # MLOps├── capstone_project/          # All production-level code for the final project

└── capstone_project/                  # Production code│   ├── app/                   # FastAPI application source code

    ├── app/         (FastAPI)│   ├── tests/                 # Unit and integration tests for the application

    ├── tests/       (Pytest, 85% coverage)│   ├── .github/               # CI/CD workflows for automated testing and deployment

    ├── terraform/   (GCP infrastructure)│   ├── charts/                # Helm charts for Kubernetes deployment

    └── Dockerfile   (Container)│   ├── scripts/               # Helper scripts for deployment and management

```│   └── terraform/             # Infrastructure as Code (IaC) for cloud resources

│

---├── week-01-02-python-ml-foundations/ # Foundational concepts

├── week-03-04-deep-learning-nlp/     # Core deep learning models

## 🎓 Perfect For├── week-05-06-llms-rag/              # Introduction to LLMs and RAG

├── week-07-08-langchain-agents/      # Building autonomous agents

✅ Software engineers → AI  ├── week-09-10-training-finetuning/   # Customizing models

✅ Data scientists → Gen AI  ├── week-11-12-production-capstone/ # Conceptual notebooks that explain the capstone's architecture

✅ Motivated beginners with Python basics  │

✅ Career changers seeking production skills├── README.md                  # This file: Your main guide to the course

├── GETTING_STARTED.md         # Detailed local setup and environment instructions

**Prerequisites**: Basic Python, terminal basics, GitHub account├── CAPSTONE_PROJECT.md        # A comprehensive guide to the capstone project

├── requirements.txt           # A list of all Python dependencies for the course

**New to Python?** Read [BEGINNER_ASSESSMENT.md](./BEGINNER_ASSESSMENT.md) first.└── ...

```

---

---

## 💡 Why This Course?

## 📜 License

| Feature | This Course | Others |

|---------|-------------|--------|This course and all its materials are released under the MIT License. See the [LICENSE](./LICENSE) file for more details. We believe in open and accessible education.

| **Focus** | Production deployment | Theory only |

| **Examples** | Real manufacturing domain | Toy datasets |---

| **Testing** | 32+ tests, 85% coverage | None |

| **Deployment** | Full CI/CD to GCP | Local only |## 🚀 Ready to Start Your Transformation?

| **Up-to-date** | MCP, LangGraph 0.0.20, Pydantic v2 | Outdated |

| **Capstone** | Portfolio-worthy | Simple demo |1.  ⭐ **Star this repository** to bookmark your progress and easily find it again.

2.  📖 Read the [GETTING_STARTED.md](./GETTING_STARTED.md) guide for environment setup.

---3.  🔧 **Launch a Codespace** and complete the `00_environment_setup.ipynb` notebook to verify your setup.

4.  🎯 Dive into the `week-01-02` module and begin the first phase of your learning.

## 📚 Documentation

**Let's begin your journey to becoming a Gen AI Master!** 🚀

- 📖 [GETTING_STARTED.md](./GETTING_STARTED.md) - Setup guide
- 🏭 [CAPSTONE_PROJECT.md](./CAPSTONE_PROJECT.md) - Final project
- 🎓 [BEGINNER_ASSESSMENT.md](./BEGINNER_ASSESSMENT.md) - Readiness check
- 📊 [PROGRESS_TRACKER.md](./PROGRESS_TRACKER.md) - Track progress
- ❓ [FAQ.md](./FAQ.md) - Common questions

**Want details?** See [README_DETAILED.md](./README_DETAILED.md)

---

## ⚡ Fast Track

**Week 1**: Environment + Python essentials  
**Week 2**: ML with Sklearn  
**Week 3-4**: Deep learning fundamentals  
**Week 5-6**: Build your first RAG system  
**Week 7-8**: Create autonomous agents  
**Week 9-10**: Fine-tune an LLM  
**Week 11-12**: Deploy to production

**Result**: Production-ready Gen AI engineer in 12 weeks 🚀

---

## 📊 By the Numbers

- **55+ Notebooks** - Every concept covered
- **12 Weeks** - Structured learning path
- **32+ Tests** - Production-quality capstone
- **15+ Technologies** - Industry-standard stack
- **9.5/10 Rating** - Beginner-friendly, production-ready

---

## ✅ Your Checklist

- [ ] ⭐ Star this repo
- [ ] 📖 Read [GETTING_STARTED.md](./GETTING_STARTED.md)
- [ ] 🔧 Launch Codespace
- [ ] ✅ Run `00_environment_setup.ipynb`
- [ ] 🎯 Complete Week 1-2
- [ ] 🏗️ Build capstone
- [ ] 🚀 Deploy to GCP
- [ ] 💼 Add to portfolio

---

## 🎯 Start Now

```bash
# Option 1: GitHub Codespaces (easiest)
Click "Code" → "Codespaces" → "Create"

# Option 2: Local
git clone https://github.com/abhayra12/Gen-AI-Roadmap.git
cd Gen-AI-Roadmap
pip install -r requirements.txt
jupyter lab
```

**Ready?** Open `00_environment_setup.ipynb` and let's go! 🚀

---

## 📜 License

MIT - Free for learning, building, and sharing.

---

**Questions?** → [FAQ.md](./FAQ.md)  
**Issues?** → Open a GitHub issue  
**Feedback?** → PRs welcome!

**Let's build the future of AI!** 🌟
