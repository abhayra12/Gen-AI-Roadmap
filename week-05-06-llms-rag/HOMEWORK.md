# 📝 Homework Assignment - Week 5-6: Build the Copilot's Brain

**Module:** LLMs, Prompt Engineering & RAG  
**Project:** Build the Knowledge Core for the Manufacturing Copilot  
**Due:** End of Week 6  
**Points:** 100

---

## 🎯 Your Mission: Forge the "Brain" of the Manufacturing Copilot

Your mission, should you choose to accept it, is to build the single most critical component of our Manufacturing Copilot: its **knowledge core**. This is not just another Q&A bot. You are creating a domain-specific expert system that can empower a factory floor technician to get instant, accurate answers from complex technical manuals.

You will construct a complete, end-to-end Retrieval-Augmented Generation (RAG) pipeline. This system will ingest a dense technical manual for a CNC machine, understand its contents, and provide precise, source-cited answers to natural language questions. Success here means transforming a static, hard-to-search document into a dynamic, interactive knowledge source.

---

## 📊 The Scenario: A Technician's Assistant

Imagine a technician on the factory floor facing a machine malfunction. Instead of spending 30 minutes searching through a 500-page PDF manual, they can simply ask the Copilot:

> *"What's the recommended pressure for the hydraulic system during a cycle?"*

Your system will instantly retrieve the relevant section from the manual and provide a clear, concise answer, complete with the page number for verification. This is the power you are about to build.

---

## 📋 Core Requirements

You will build your system around a provided technical manual for a "Haas VF-2" CNC machine. This document is representative of the complex, dense information common in industrial settings.

Your final submission must include:

1.  **Document Processing Pipeline:** A script that can load, parse, and intelligently chunk the provided PDF manual.
2.  **Vector Database:** A persistent `ChromaDB` or `FAISS` vector store that serves as the long-term memory of your system.
3.  **RAG Chain:** An end-to-end LangChain pipeline that connects a user query to the vector store and a generative LLM.
4.  **Evaluation Suite:** A clear and repeatable method for evaluating the quality of both your retriever and your generator.
5.  **Interactive Web Interface:** A simple but effective `Streamlit` or `Gradio` application that allows for live interaction and, most importantly, **cites its sources**.

---

## ✅ Task Breakdown & Step-by-Step Guide

### Part 1: The Foundation - Document Ingestion & Processing (25 points)

This is the most critical step. Garbage in, garbage out.

-   **Load the Data:** Use a robust PDF loader (like `PyPDFLoader` from LangChain) to ingest the sample manual.
-   **Chunking Strategy:** Don't just split randomly. Technical manuals have structure (headings, tables, lists).
    -   **Implement `RecursiveCharacterTextSplitter`**. Start with a `chunk_size` of `1000` and a `chunk_overlap` of `200`.
    -   **Justify your choices.** In your `README.md`, explain *why* you chose your chunking parameters. How do they balance context preservation with the LLM's token limit?
-   **Metadata is King:** For each chunk, you *must* extract and store the page number (`metadata={'page': ...}`). This is non-negotiable for source citation.
-   **Validation:** Write a small script to print out a few sample chunks and their metadata to ensure your pipeline is working correctly.

### Part 2: The Memory - Vector Database and Embeddings (20 points)

-   **Choose Your Embedding Model:** The choice of embedding model has a huge impact on retrieval quality.
    -   **Select a model.** Good candidates for technical text include `BAAI/bge-small-en-v1.5` or the classic `sentence-transformers/all-mpnet-base-v2`.
    -   **Justify your choice.** Why is this model a good fit for technical jargon compared to a more generic model?
-   **Build the Vector Store:**
    -   Set up and populate a `ChromaDB` vector store.
    -   **Make it persistent.** Save the database to disk so you don't have to re-process the PDF every time you run your app.
-   **Test Retrieval:** Write a simple test function to perform a similarity search on a few sample queries (e.g., "how to change the coolant?"). Does it retrieve relevant-looking chunks?

### Part 3: The Brain - The RAG Pipeline (30 points)

-   **Build the `RetrievalQA` Chain:** Use LangChain to construct the end-to-end pipeline.
-   **Design a Powerful Prompt:** This is where you control the LLM's personality and behavior. Your prompt must explicitly instruct the LLM to:
    1.  Act as an expert assistant.
    2.  Answer the question based *only* on the provided context.
    3.  If the answer is not in the context, state that clearly and do not hallucinate.
-   **Select a Generator Model:** `google/flan-t5-base` is a good, efficient choice.
-   **Enable Source Citation:** Ensure your `RetrievalQA` chain is configured with `return_source_documents=True`.

### Part 4: The Report Card - Evaluation (15 points)

How do you know if your system is any good? You test it.

-   **Create an Evaluation Set:** Based on the manual, create a CSV or JSON file with at least 10 realistic question/ground-truth answer pairs.
-   **Measure Retrieval Accuracy:** For each question, programmatically check if the retrieved documents contain the information needed to answer it. Calculate a "hit rate."
-   **Measure Generation Quality:** Manually review the LLM's generated answers. Are they:
    -   **Faithful?** (Do they stick to the source material?)
    -   **Accurate?** (Are they correct?)
    -   **Concise?** (Do they get to the point?)
-   **Document Your Findings:** Write a short `evaluation_report.md` summarizing your results, including what worked well and what could be improved.

### Part 5: The Interface - Interactive Demo (10 points)

-   **Build a simple `Streamlit` or `Gradio` interface.**
-   The UI must have:
    -   A text box for the user to enter their question.
    -   A button to submit the query.
    -   A clear display area for the generated answer.
    -   A **"Sources" section** that displays the `page_content` and `page` number of the source documents the LLM used. This is the most important part of the UI.

---

##  Grading Rubric

| Component | Points | Criteria |
|---|---|---|
| **Document Processing** | 25 | Justification of chunking strategy, correct metadata extraction. |
| **Vector Database** | 20 | Justification of embedding model choice, persistent and efficient indexing. |
| **RAG Pipeline** | 30 | Quality of the prompt, faithfulness and accuracy of the generated answers. |
| **Evaluation** | 15 | Thoroughness of the test set, insightful analysis in the report. |
| **Demo & Citation** | 10 | A functional and intuitive UI with **clear and accurate source citation**. |

---

## 🚀 Bonus Challenges (+10 points each)

1.  **Advanced Retrieval: Hybrid Search:** Combine your dense vector search with a sparse, keyword-based search (like `BM25`) to improve retrieval for specific part numbers or error codes that semantic search might miss.
2.  **Conversational Memory:** Use LangChain's `ConversationBufferMemory` to allow your app to remember the context of the conversation and answer follow-up questions.
3.  **Automated Evaluation with RAGAS:** Integrate the `RAGAS` library to automatically score your pipeline on metrics like `faithfulness`, `answer_relevancy`, and `context_recall`.
4.  **Handling Tables:** Technical manuals are full of tables. Research and implement a strategy to parse tables from the PDF and represent them in a way that your RAG system can effectively use (e.g., convert them to markdown or a structured string).

---

## 📦 Recommended Project Structure

```
homework/week-05-06/
├── README.md                # Your main project write-up
├── app.py                   # Your Streamlit/Gradio application
├── rag_pipeline.ipynb       # Your development notebook
├── requirements.txt
├── data/
│   └── haas_vf2_manual.pdf  # The provided technical manual
└── evaluation/
    ├── test_suite.csv       # Your question-answer evaluation set
    └── evaluation_report.md # Your analysis of the system's performance
```

---

<div align="center">
<h3>This is your chance to build a truly useful AI tool. Good luck!</h3>
</div>
