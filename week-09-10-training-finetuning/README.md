# 📖 Week 9-10: Training & Fine-Tuning

**Phase 5: Training & Fine-tuning**  
**Goal:** Learn to train, fine-tune, and evaluate LLMs to adapt them for specialized tasks.

---

## 📚 Module Overview

In this module, you will go under the hood of LLMs to understand how they are trained and how you can customize them. You will start by building a simple language model from scratch to grasp the core mechanics. Then, you will master powerful and efficient fine-tuning techniques (PEFT, LoRA, QLoRA) to specialize pre-trained models for domain-specific tasks without the need for massive computational resources.

### Learning Objectives
By the end of this module, you will be able to:
- ✅ Understand the fundamental concepts of model pre-training.
- ✅ Build a simple language model and its training loop from scratch using PyTorch.
- ✅ Know when to use fine-tuning versus RAG for a given problem.
- ✅ Implement Parameter-Efficient Fine-Tuning (PEFT) techniques like LoRA and QLoRA.
- ✅ Fine-tune a powerful open-source LLM on a custom dataset.
- ✅ Establish a robust framework for evaluating the performance of your fine-tuned model.

---

## 📓 Notebooks & Concepts

This module is split into two parts: training fundamentals and advanced fine-tuning, covered across 11 notebooks:

| Area                  | Notebooks       | Key Concepts                                       |
|-----------------------|-----------------|----------------------------------------------------|
| **Training from Scratch** | `01` - `06`     | Pre-training, Bigram Model, Forward/Backward Pass, MLP, Mini-batching |
| **Fine-Tuning**       | `07` - `11`     | Fine-tuning vs. RAG, PEFT, LoRA, QLoRA, Evaluation Metrics |

---

## 📝 Homework: Fine-Tune for Maintenance Ticket Classification

**Objective:** Specialize an LLM to understand and classify maintenance requests.

**Task:**
You will use a provided dataset of maintenance tickets to fine-tune a pre-trained LLM. The goal is to create a model that can accurately classify new tickets into categories like `Mechanical`, `Electrical`, or `Software`, enabling automated routing.

- **Instructions:** See the `HOMEWORK.md` file in this directory for detailed instructions.

---

## 🎯 What's Next?

You have now covered the full spectrum of creating and customizing AI models. You are ready for the final and most critical phase: **Week 11-12: Production & Deployment**. In this capstone module, you will take everything you've learned and build a single, production-grade, end-to-end AI application.

**Time to forge your own models!** 🔥
