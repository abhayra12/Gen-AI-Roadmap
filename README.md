# 🚀 Gen AI Masters Program
### From Beginner to Production-Ready AI Engineer in 12 Weeks

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Codespaces](https://img.shields.io/badge/Codespace-Ready-success)](https://github.com/features/codespaces)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **A comprehensive, hands-on curriculum to master Generative AI, from foundational concepts to deploying production-grade, multi-agent systems.**

---

## 📚 Course Overview

Welcome to the Gen AI Masters Program! This repository contains a 12-week intensive course designed to transform you into a production-ready AI engineer. Through a series of hands-on notebooks and a portfolio-worthy capstone project, you will master the full lifecycle of building and deploying sophisticated Generative AI applications.

### 🎯 What You'll Build
- ✅ **15+ Jupyter Notebooks** covering every core Gen AI concept.
- ✅ **A Production-Grade Capstone Project:** A containerized, cloud-deployed, multi-agent system for the manufacturing domain.
- ✅ **Deep, practical understanding** of Transformers, RAG, Fine-tuning, and Agentic AI.
- ✅ **A standout portfolio** that demonstrates your ability to ship real-world AI products.

---

## 🗓️ 12-Week Learning Journey

The course is divided into five phases, each building upon the last, culminating in a comprehensive capstone project.

| Weeks   | Phase                               | Key Topics                                                              |
|---------|-------------------------------------|-------------------------------------------------------------------------|
| **1-2** | **Phase 1: Foundations**            | Python, ML Fundamentals, NumPy, Pandas                                  |
| **3-4** | **Phase 2: Deep Learning & NLP**    | Neural Networks, CNNs, RNNs, Transformers, Embeddings                   |
| **5-6** | **Phase 3: LLMs & RAG**             | Prompt Engineering, RAG Implementation, Vector Databases                |
| **7-8** | **Phase 4: Agents & Advanced RAG**  | LangChain, LangGraph, Multi-Agent Systems, Advanced RAG Patterns        |
| **9-10**| **Phase 5: Training & Fine-tuning** | Pre-training Concepts, PEFT, LoRA, QLoRA, Model Evaluation              |
| **11-12**| **Capstone: Production & Deployment**| MLOps, FastAPI, Docker, CI/CD, Terraform, GCP, Kubernetes              |

---

## 🏗️ Capstone Project: The Manufacturing Copilot

The final two weeks are dedicated to building and deploying the **Manufacturing Copilot**, a multi-agent AI system designed for the factory floor.

### Key Features
- 📸 **Visual Quality Inspection** using Vision-Language Models.
- 🔧 **Predictive Maintenance Q&A** using a sophisticated RAG system.
- 📝 **Automated, Multi-lingual Report Generation** using a fine-tuned model.
- 🤖 **Agentic Orchestration** with LangGraph to manage complex workflows.

### Tech Stack
- **Frameworks:** FastAPI, LangChain, LangGraph
- **Databases:** PostgreSQL, ChromaDB
- **Deployment:** Docker, Terraform, GitHub Actions
- **Cloud:** GCP (Cloud Run / GKE)
- **Monitoring:** Prometheus, Grafana

All code for the final project is located in the `capstone_project/` directory. The notebooks in `week-11-12` serve as conceptual guides for the implementation within the capstone.

---

## 🛠️ Getting Started

### Prerequisites
- Python 3.11+
- An active GitHub account
- **Recommended:** Use GitHub Codespaces for a seamless, pre-configured environment.

### Quick Start with GitHub Codespaces
1.  Click the **"Code"** button on the repository page.
2.  Select the **"Codespaces"** tab.
3.  Click **"Create codespace on main"**.
4.  The environment will build automatically. Once ready, open `00_environment_setup.ipynb` and begin your journey!

For a detailed local setup guide, see [GETTING_STARTED.md](./GETTING_STARTED.md).

---

## 📁 Repository Structure

The repository is organized into weekly modules and a final capstone project.

```
T_Tech/
├── capstone_project/          # All code for the final project
│   ├── app/                   # FastAPI application source
│   ├── tests/                 # Unit and integration tests
│   ├── .github/               # CI/CD workflows
│   ├── charts/                # Helm charts for Kubernetes
│   ├── scripts/               # Deployment scripts
│   └── terraform/             # Infrastructure as Code
│
├── week-01-02-python-ml-foundations/
├── week-03-04-deep-learning-nlp/
├── week-05-06-llms-rag/
├── week-07-08-langchain-agents/
├── week-09-10-training-finetuning/
├── week-11-12-production-capstone/ # Conceptual notebooks for the capstone
│
├── README.md                  # This file
├── GETTING_STARTED.md         # Detailed setup instructions
├── CAPSTONE_PROJECT.md        # The full capstone project guide
├── requirements.txt           # Python dependencies
└── ...
```

---

## 📜 License

This course is released under the MIT License. See [LICENSE](./LICENSE) for details.

---

## 🚀 Ready to Start?

1.  ⭐ **Star this repository** to bookmark your progress.
2.  📖 Read [GETTING_STARTED.md](./GETTING_STARTED.md).
3.  🔧 Launch a Codespace and complete `00_environment_setup.ipynb`.
4.  🎯 Begin with the `week-01-02` module.

**Let's begin your journey to becoming a Gen AI Master!** 🚀
