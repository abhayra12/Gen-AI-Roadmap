# 📝 Homework Assignment - Week 5-6

**Module:** LLMs, Prompt Engineering & RAG  
**Due:** End of Week 6  
**Points:** 100

---

## 🎯 Assignment: Manufacturing Maintenance Q&A System

Build a RAG-powered question-answering system for manufacturing maintenance.

---

## 📊 Project Requirements

### Dataset
Use manufacturing equipment manuals, maintenance logs, and SOPs (Standard Operating Procedures).

### System Components
1. Document processing pipeline
2. Vector database (ChromaDB or FAISS)
3. Retrieval system
4. LLM integration via HuggingFace
5. Web interface

---

## 📋 Task Breakdown

### Part 1: Document Processing (25 points)
- Load 10+ PDF maintenance manuals
- Implement chunking strategy (500-1000 tokens)
- Extract metadata (equipment, date, section)
- Handle tables and images
- Quality validation

### Part 2: Vector Database Setup (20 points)
- Choose and justify embedding model
- Set up ChromaDB or FAISS
- Index all documents
- Implement efficient retrieval
- Test similarity search

### Part 3: RAG Pipeline (30 points)
- Query processing
- Retrieval with re-ranking
- Context assembly
- LLM generation
- Response formatting

### Part 4: Evaluation (15 points)
- Create test question set (50+ questions)
- Measure retrieval accuracy
- Evaluate response quality
- Compare with baseline
- Document findings

### Part 5: Demo Application (10 points)
- Build Streamlit or Gradio interface
- User-friendly query input
- Display sources
- Show confidence scores
- Deploy locally

---

## 🎯 Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Document Processing | 25 | Quality of chunking and metadata extraction |
| Vector Database | 20 | Efficient indexing and retrieval |
| RAG Pipeline | 30 | Accuracy and relevance of responses |
| Evaluation | 15 | Comprehensive testing and analysis |
| Demo | 10 | User experience and functionality |

---

## 💡 Implementation Guide

### Document Processing
```python
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = PyPDFLoader("manual.pdf")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(documents)
```

### Vector Database
```python
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)
```

### RAG Pipeline
```python
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub

llm = HuggingFaceHub(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    model_kwargs={"temperature": 0.7, "max_length": 512}
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3})
)
```

---

## 🚀 Bonus Challenges (+10 points each)

1. **Multi-lingual Support**: Handle Hindi maintenance manuals
2. **Advanced Retrieval**: Implement hybrid search (keyword + semantic)
3. **Citation**: Show exact source with page numbers
4. **Conversation Memory**: Multi-turn conversations
5. **Auto-evaluation**: Implement RAGAS metrics

---

## 📦 Submission Structure

```
homework/week-05-06/
├── README.md
├── rag_qa_system.ipynb
├── requirements.txt
├── data/
│   └── manuals/
├── chroma_db/
├── src/
│   ├── document_processor.py
│   ├── rag_pipeline.py
│   └── evaluation.py
├── app.py (Streamlit/Gradio)
└── reports/
    ├── evaluation_results.md
    └── demo_screenshots/
```

---

## ✅ Submission Checklist

- [ ] RAG pipeline functional
- [ ] 50+ test questions answered
- [ ] Evaluation report complete
- [ ] Demo app working
- [ ] Code documented
- [ ] README comprehensive
- [ ] Committed to GitHub

---

<div align="center">
Week 5-6 Homework | RAG Q&A System | Build intelligent search! 🔍
</div>
