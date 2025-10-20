# 🚀 Gen AI Masters Program
### From Beginner to Production-Ready AI Engineer in 12 Weeks

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Codespaces](https://img.shields.io/badge/Codespace-Ready-success)](https://github.com/features/codespaces)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Welcome! This repository hosts a comprehensive, hands-on curriculum designed to guide you from foundational concepts to deploying sophisticated, production-grade Generative AI systems. Your journey to becoming a Gen AI specialist starts here.**

---

## 📚 Course Overview

The Gen AI Masters Program is a 12-week intensive course structured to make you a production-ready AI engineer. Through a series of detailed, hands-on Jupyter notebooks and a portfolio-worthy capstone project, you will master the complete lifecycle of building and deploying advanced Generative AI applications.

### 🎯 What You'll Build & Master
- ✅ **15+ Hands-On Notebooks:** Each notebook is a deep dive into a core Gen AI concept, packed with theoretical explanations and practical code.
- ✅ **A Production-Grade Capstone Project:** You will build and deploy a containerized, cloud-native, multi-agent system tailored for the manufacturing domain.
- ✅ **Deep, Practical Understanding:** Gain mastery over Transformers, Retrieval-Augmented Generation (RAG), model fine-tuning, and agentic AI workflows.
- ✅ **A Standout Portfolio:** Finish the course with a project that showcases your ability to design, build, and ship real-world AI products.

---

## 🗓️ Your 12-Week Learning Journey

The curriculum is meticulously divided into six two-week phases, each building logically on the last. This structured path ensures a smooth learning curve as you progress from fundamentals to advanced, production-level topics.

| Weeks   | Phase                               | Key Topics                                                              | Core Skills Gained                                                     |
|---------|-------------------------------------|-------------------------------------------------------------------------|------------------------------------------------------------------------|
| **1-2** | **Phase 1: Foundations**            | Python, ML Fundamentals, NumPy, Pandas, Data Visualization              | Manipulating data and understanding core machine learning principles.  |
| **3-4** | **Phase 2: Deep Learning & NLP**    | Neural Networks, CNNs, RNNs, Transformers, Embeddings                   | Building deep learning models and processing sequential text data.     |
| **5-6** | **Phase 3: LLMs & RAG**             | Prompt Engineering, RAG Implementation, Vector Databases (ChromaDB)     | Leveraging large language models and augmenting them with external data. |
| **7-8** | **Phase 4: Agents & Advanced RAG**  | LangChain, LangGraph, Multi-Agent Systems, Advanced RAG Patterns        | Building autonomous agents that can reason, plan, and execute tasks.   |
| **9-10**| **Phase 5: Training & Fine-tuning** | Pre-training Concepts, PEFT, LoRA, QLoRA, Model Evaluation              | Customizing and optimizing LLMs for specific, domain-oriented tasks.   |
| **11-12**| **Capstone: Production & Deployment**| MLOps, FastAPI, Docker, CI/CD, Terraform, GCP, Kubernetes              | Shipping robust, scalable AI applications to the cloud.                |

---

## 🏗️ Capstone Project: The Manufacturing Copilot

The final two weeks are dedicated to the capstone: building and deploying the **Manufacturing Copilot**, a multi-agent AI system designed to solve real-world problems on the factory floor. This project is your opportunity to integrate everything you've learned into a single, impressive portfolio piece.

### Key Features
- 📸 **Visual Quality Inspection:** Use Vision-Language Models (VLMs) to automatically detect product defects from images.
- 🔧 **Predictive Maintenance Q&A:** Implement a sophisticated RAG system that allows engineers to query maintenance logs and technical manuals.
- 📝 **Automated, Multi-lingual Report Generation:** Fine-tune a model to generate daily production summaries in multiple languages.
- 🤖 **Agentic Orchestration:** Use LangGraph to create a master agent that delegates tasks to specialized sub-agents, managing complex, multi-step workflows.

### Tech Stack
- **Frameworks:** FastAPI, LangChain, LangGraph
- **Databases:** PostgreSQL, ChromaDB
- **Deployment:** Docker, Terraform, GitHub Actions
- **Cloud:** Google Cloud Platform (GCP) - specifically Cloud Run or GKE
- **Monitoring:** Prometheus, Grafana

All code for the final project is located in the `capstone_project/` directory. The notebooks in the `week-11-12` module serve as conceptual guides for the implementation within the capstone, providing the theoretical underpinnings for the production code.

---

## 🛠️ Getting Started

A smooth start is crucial. We've designed the setup process to be as simple as possible, with a strong recommendation for using a cloud-based development environment.

### Prerequisites
- Basic understanding of Python programming.
- An active GitHub account.
- **Strongly Recommended:** Use GitHub Codespaces for a seamless, pre-configured environment that works right out of the box.

### Quick Start with GitHub Codespaces (Recommended)
1.  Click the **"Code"** button at the top of the repository page.
2.  Select the **"Codespaces"** tab.
3.  Click **"Create codespace on main"**.
4.  The environment will build automatically in your browser. Once it's ready, VS Code will open.
5.  Open the `00_environment_setup.ipynb` notebook and begin your journey!

For a detailed guide on setting up your environment locally, please see [GETTING_STARTED.md](./GETTING_STARTED.md).

---

## 📁 Repository Structure

The repository is organized into weekly modules, with a clear separation between conceptual notebooks and the final production-level capstone project.

```
T_Tech/
├── capstone_project/          # All production-level code for the final project
│   ├── app/                   # FastAPI application source code
│   ├── tests/                 # Unit and integration tests for the application
│   ├── .github/               # CI/CD workflows for automated testing and deployment
│   ├── charts/                # Helm charts for Kubernetes deployment
│   ├── scripts/               # Helper scripts for deployment and management
│   └── terraform/             # Infrastructure as Code (IaC) for cloud resources
│
├── week-01-02-python-ml-foundations/ # Foundational concepts
├── week-03-04-deep-learning-nlp/     # Core deep learning models
├── week-05-06-llms-rag/              # Introduction to LLMs and RAG
├── week-07-08-langchain-agents/      # Building autonomous agents
├── week-09-10-training-finetuning/   # Customizing models
├── week-11-12-production-capstone/ # Conceptual notebooks that explain the capstone's architecture
│
├── README.md                  # This file: Your main guide to the course
├── GETTING_STARTED.md         # Detailed local setup and environment instructions
├── CAPSTONE_PROJECT.md        # A comprehensive guide to the capstone project
├── requirements.txt           # A list of all Python dependencies for the course
└── ...
```

---

## 📜 License

This course and all its materials are released under the MIT License. See the [LICENSE](./LICENSE) file for more details. We believe in open and accessible education.

---

## 🚀 Ready to Start Your Transformation?

1.  ⭐ **Star this repository** to bookmark your progress and easily find it again.
2.  📖 Read the [GETTING_STARTED.md](./GETTING_STARTED.md) guide for environment setup.
3.  🔧 **Launch a Codespace** and complete the `00_environment_setup.ipynb` notebook to verify your setup.
4.  🎯 Dive into the `week-01-02` module and begin the first phase of your learning.

**Let's begin your journey to becoming a Gen AI Master!** 🚀
