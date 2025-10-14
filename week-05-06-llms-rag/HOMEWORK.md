# 📝 Homework Assignment - Week 5-6

**Module:** LLMs, Prompt Engineering & RAG  
**Project:** Build the Knowledge Core for the Manufacturing Copilot  
**Due:** End of Week 6  
**Points:** 100

---

## 🎯 Assignment: Build a Q&A System for a CNC Machine Technical Manual

Your mission is to build the "brain" of our Manufacturing Copilot. This will be a Retrieval-Augmented Generation (RAG) system that allows a factory floor technician to ask questions in natural language about a specific piece of equipment and get accurate answers sourced directly from its technical manuals.

This is a critical component that turns our Copilot from a general assistant into a domain-specific expert.

---

## 📊 Project Requirements

### Dataset
You will use a provided technical manual for a "Haas VF-2" CNC machine. This document contains complex information about operations, maintenance, and troubleshooting. You can also supplement this with any provided maintenance logs or Standard Operating Procedures (SOPs).

### System Components
1.  **Document Ingestion & Processing Pipeline:** A robust script to load, parse, and chunk the PDF manual.
2.  **Vector Database:** A FAISS or ChromaDB vector store to house the knowledge.
3.  **Retrieval System:** An efficient retriever that finds the most relevant document chunks for a given query.
4.  **LLM Integration:** A generation component using a powerful LLM from HuggingFace to synthesize answers.
5.  **Web Interface:** A simple but effective Gradio or Streamlit interface for live interaction.

---

## 📋 Task Breakdown

### Part 1: Document Processing & Ingestion (25 points)
-   Load a sample PDF document (you can create a short, 2-3 page PDF with mock technical data).
-   Implement a smart chunking strategy. **Justify your choice of `chunk_size` and `chunk_overlap`**. Is `RecursiveCharacterTextSplitter` the best choice for technical manuals?
-   Extract relevant metadata for each chunk (e.g., page number, source document). This is crucial for citation.
-   Write a script to validate the quality of your chunks.

### Part 2: Vector Database and Embeddings (20 points)
-   **Select and justify your choice of embedding model**. Consider models like `BAAI/bge-small-en-v1.5` or `sentence-transformers/all-mpnet-base-v2`. Why is it suitable for technical text?
-   Set up and populate a ChromaDB or FAISS vector store.
-   Implement a function to perform similarity search and test its effectiveness on sample queries (e.g., "how to change the coolant?").

### Part 3: The RAG Pipeline (30 points)
-   Build the end-to-end RAG chain using LangChain.
-   **Query Processing:** How will you handle user queries? Any pre-processing needed?
-   **Retrieval & Re-ranking (Optional but encouraged):** Retrieve the top-k most relevant chunks. Consider adding a re-ranking step to improve relevance.
-   **Context Assembly & Prompting:** Create a robust prompt template that combines the user's question with the retrieved context. Your prompt should guide the LLM to answer based *only* on the provided information.
-   **Generation:** Use a model like `google/flan-t5-base` or another suitable model for generation.

### Part 4: Evaluation (15 points)
-   Create a test set of at least 10 question-answer pairs based on your mock manual.
-   Measure the retrieval accuracy (e.g., Hit Rate, MRR). Did your retriever find the correct source chunk?
-   Evaluate the quality of the generated responses. Are they accurate? Concise? Do they avoid making things up (hallucination)?
-   Document your findings in a short report.

### Part 5: Interactive Demo (10 points)
-   Build a simple but functional Streamlit or Gradio interface.
-   The interface should allow a user to type a question.
-   The application should display the generated answer.
-   **Crucially, it must also cite the source**, showing the page number or the retrieved text chunk, so the user can verify the information.

---

## 🎯 Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Document Processing | 25 | Quality & justification of chunking, metadata extraction. |
| Vector Database | 20 | Justification of embedding model, efficient indexing. |
| RAG Pipeline | 30 | Accuracy, relevance, and faithfulness of responses. Quality of the prompt. |
| Evaluation | 15 | Comprehensive testing, insightful analysis of results. |
| Demo & Citation | 10 | UX, functionality, and proper source citation. |

---

## 💡 Implementation Guide

The code snippets from the notebook `08_rag_implementation.ipynb` are a great starting point. Refer to them for using `TextLoader`, `Chroma`, and `RetrievalQA`.

### Key Challenge: Prompting for Factual Grounding
Your prompt is critical. A good starting point:

```
"Use the following pieces of context to answer the user's question. If you don't know the answer, just say that you don't know, don't try to make up an answer. Provide the answer and then include the page number from the source document."

Context:
{context}

Question:
{question}

Helpful Answer:
```

---

## 🚀 Bonus Challenges (+10 points each)

1.  **Advanced Retrieval:** Implement a hybrid search that combines keyword-based search (like BM25) with your semantic search to improve retrieval for part numbers or specific error codes.
2.  **Conversational Memory:** Extend your app to handle follow-up questions using `ConversationBufferMemory`.
3.  **Auto-Evaluation with RAGAS:** Use the `RAGAS` library to automatically evaluate your pipeline's performance on metrics like `faithfulness`, `answer_relevancy`, and `context_recall`.
4.  **Handling Tables:** Many manuals contain tables. Implement a strategy to parse and represent tabular data effectively for the RAG system.

---

## 📦 Submission Structure

Organize your project clearly. A recommended structure:
```
homework/week-05-06/
├── README.md
├── rag_app.py         # Your Streamlit/Gradio app
├── rag_pipeline.ipynb # Notebook for development
├── requirements.txt
├── data/
│   └── sample_manual.pdf
└── evaluation/
    ├── test_qna.csv
    └── evaluation_report.md
```

---

## ✅ Submission Checklist

- [ ] RAG pipeline is fully functional and answers questions about the sample manual.
- [ ] Evaluation report is complete with metrics and analysis.
- [ ] The demo app works and correctly cites sources.
- [ ] Your code is well-documented and follows best practices.
- [ ] The main `README.md` for your submission is comprehensive.
- [ ] All code is committed to your GitHub repository.

---

<div align="center">
Week 5-6 Homework | Building the Brain of the Manufacturing Copilot 🧠
</div>
