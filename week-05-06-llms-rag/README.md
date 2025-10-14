# 📖 Week 5-6: LLMs & Retrieval-Augmented Generation (RAG)

**Phase 3: LLMs & RAG**  
**Goal:** Master Large Language Models, prompt engineering, and build a powerful RAG system to answer questions from a custom knowledge base.

---

## 📚 Module Overview

This module focuses on the practical application of LLMs. You will learn how to effectively communicate with these models through advanced prompting techniques and then build a complete Retrieval-Augmented Generation (RAG) system from scratch. This is a cornerstone skill for creating AI that can reason about private or domain-specific data.

### Learning Objectives
By the end of this module, you will be able to:
- ✅ Select the right LLM for a given task based on performance, cost, and latency.
- ✅ Engineer sophisticated prompts (e.g., Chain-of-Thought, Few-Shot) to control LLM output.
- ✅ Understand the complete RAG pipeline: Load, Split, Embed, Retrieve, Generate.
- ✅ Build a functional RAG system that uses a vector database to find relevant information.
- ✅ Implement semantic search using sentence transformers to go beyond keyword matching.
- ✅ Grasp the trade-offs between RAG and fine-tuning for knowledge-intensive tasks.

---

## 📓 Notebooks & Concepts

This module's nine notebooks guide you from basic LLM usage to building a full RAG system:

| Order | Notebook                            | Key Concepts                                       |
|-------|-------------------------------------|----------------------------------------------------|
| 1.    | `01_llms_introduction.ipynb`        | LLM landscape, model selection, inference endpoints|
| 2.    | `02_huggingface_tasks.ipynb`        | Sentiment, Summarization, Q&A with `pipeline`      |
| 3.    | `03_model_selection_preprocessing.ipynb`| `AutoTokenizer`, data cleaning, post-processing    |
| 4.    | `04_tokenizers_advanced.ipynb`      | BPE/WordPiece, training custom tokenizers          |
| 5.    | `05_prompt_engineering.ipynb`       | Zero-shot, Few-shot, Chain-of-Thought prompting    |
| 6.    | `06_few_shot_learning.ipynb`        | In-context learning, example selection strategies  |
| 7.    | `07_rag_introduction.ipynb`         | RAG theory, architecture, and use cases            |
| 8.    | `08_rag_implementation.ipynb`       | Document loading, chunking, retrieval, generation  |
| 9.    | `09_vector_embeddings.ipynb`        | Sentence transformers, semantic search, similarity |

---

## 📝 Homework: Q&A System for a Technical Manual

**Objective:** Build a complete RAG system to answer questions about a specific document.

**Task:**
You will create a Q&A system that ingests a technical PDF, stores its content in a vector database, and uses an LLM to answer user questions based on the retrieved information.

- **Instructions:** See the `HOMEWORK.md` file in this directory for detailed instructions.

---

## 🎯 What's Next?

Now that you can build systems that retrieve knowledge, you're ready for **Week 7-8: LangChain, Agents, & Advanced RAG**. You will learn to use powerful frameworks like LangChain and LangGraph to build complex, multi-step applications and intelligent agents that can take actions.

**Let's make models knowledgeable!** 💡
