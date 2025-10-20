# 📖 Week 3-4: Deep Learning & Natural Language Processing (NLP) Foundations

**Phase 2: From Classical Machine Learning to Deep Learning**  
**Goal:** This module marks a pivotal transition from the foundational concepts of classical machine learning to the core of modern AI: **deep learning**. Our primary objective is to build a strong theoretical and practical understanding of neural networks, culminating in a deep dive into the **Transformer architecture**—the engine that powers today's Large Language Models (LLMs).

---

## 📚 Module Overview

In this module, you will move beyond the structured, tabular data of the previous weeks and into the realm of unstructured data like text and images. You will learn the theory behind what makes deep learning so powerful and gain hands-on experience with the fundamental architectures that have revolutionized fields like computer vision (CNNs), sequence modeling (RNNs), and, most importantly, natural language processing (Transformers).

### Core Learning Objectives
By the end of this two-week module, you will be able to:
- ✅ **Build and Train Neural Networks**: Understand the mechanics of a neural network, including layers, activation functions, loss functions, and the backpropagation algorithm. You will implement and train your first neural networks using **PyTorch**.
- ✅ **Implement Convolutional Neural Networks (CNNs)**: Grasp the concepts of convolutions and pooling layers and understand why CNNs are so effective for image-based tasks.
- ✅ **Understand Recurrent Neural Networks (RNNs)**: Learn the architecture of RNNs and their variants (LSTMs, GRUs), which were the state-of-the-art for handling sequence data before the Transformer era.
- ✅ **Master the Transformer Architecture**: Deconstruct the revolutionary Transformer model, paying close attention to its core innovation: the **self-attention mechanism**. You will build a Transformer from scratch to solidify your understanding.
- ✅ **Grasp Embeddings and Tokenization**: Understand how we represent words and sentences as numbers that a neural network can process, covering techniques from Word2Vec to modern subword tokenization like BPE.
- ✅ **Leverage the Hugging Face Ecosystem**: Get hands-on with the `transformers` library, learning how to use `pipeline`, `AutoModel`, and `AutoTokenizer` to download, use, and experiment with thousands of powerful pre-trained models from the Hugging Face Hub.

---

## 📓 Notebooks & Key Concepts

This module is structured into seven comprehensive notebooks that build upon each other:

| Order | Notebook                            | Key Concepts Covered                                       |
|-------|-------------------------------------|------------------------------------------------------------|
| 1.    | `01_neural_networks.ipynb`          | **PyTorch Tensors, Automatic Differentiation, Backpropagation, Loss Functions, Optimizers.** |
| 2.    | `02_cnn_basics.ipynb`               | **Convolutions, Pooling Layers, Filters, Image Classification, Transfer Learning.** |
| 3.    | `03_rnn_lstm.ipynb`                 | **Handling Sequences, Hidden States, LSTMs, GRUs, Sequence-to-Sequence Models.** |
| 4.    | `04_transformers.ipynb`             | **The Encoder-Decoder Structure, Positional Encodings, Scaled Dot-Product Attention.** |
| 5.    | `05_attention_mechanisms.ipynb`     | **Self-Attention (Query, Key, Value), Multi-Head Attention, Masking.** |
| 6.    | `06_embeddings.ipynb`               | **Word2Vec, GloVe, and the need for Contextual Embeddings.** |
| 7.    | `07_huggingface_intro.ipynb`        | **Using `pipeline`, `AutoModel`, `AutoTokenizer`, and interacting with the Hugging Face Hub.** |

---

## 📝 Homework: Building a Text Classifier with Transformers

**Objective:** Apply your knowledge of the Transformer architecture and the Hugging Face library to build, fine-tune, and evaluate a high-performance text classifier.

**Task:**
You will select a pre-trained Transformer model (like `distilbert-base-uncased`), fine-tune it on a custom dataset for a practical classification task (e.g., sentiment analysis of customer reviews or classifying news articles by topic), and rigorously evaluate its performance. This project will be your first taste of applying state-of-the-art NLP models to a real-world problem.

- **Detailed Instructions:** Please refer to the `HOMEWORK.md` file located in this directory for the full assignment details.

---

## 🎯 What's Next?

With a strong, foundational understanding of the Transformer architecture, you will be perfectly positioned for the next module, **Week 5-6: LLMs & Retrieval-Augmented Generation (RAG)**. In that module, you will move from training models to *using* very large, pre-trained models and building sophisticated systems that can reason over external knowledge bases.

**This module is where you truly start building at the cutting edge of AI. Let's dive in!** 🧠