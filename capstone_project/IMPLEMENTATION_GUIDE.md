# 🛠️ Implementation Guide - Manufacturing Copilot

> **Deep dive into how the multi-agent system works, code architecture, and customization guide**

## 📋 Table of Contents

- [System Architecture](#-system-architecture)
- [Agent Implementation Details](#-agent-implementation-details)
- [LangGraph Orchestration](#-langgraph-orchestration)
- [HuggingFace Integration](#-huggingface-integration)
- [Code Walkthrough](#-code-walkthrough)
- [Customization Guide](#-customization-guide)
- [Performance Optimization](#-performance-optimization)
- [Error Handling Strategy](#-error-handling-strategy)
- [Production Deployment Architecture](#-production-deployment-architecture) ⭐ **NEW**

---

## 🏛️ System Architecture

### High-Level Design Pattern

This project implements the **Agent-as-a-Service** pattern using:

1. **FastAPI** - HTTP interface layer
2. **LangGraph** - Agent orchestration framework
3. **LangChain** - Agent building blocks
4. **HuggingFace** - Model inference backend
5. **ChromaDB** - Vector database for RAG

```
┌─────────────────────────────────────────────┐
│           Request Flow Architecture          │
└─────────────────────────────────────────────┘

1. HTTP Request
   ↓
2. FastAPI Endpoint Handler (main.py)
   ↓
3. Security Middleware (Bearer Token Validation)
   ↓
4. Pydantic Validation (models.py)
   ↓
5. LangGraph State Initialization
   ↓
6. Agent Execution Graph:
   ┌───────────┐
   │  Vision   │ → Analyzes image
   │   Agent   │    (BLIP-2 VLM)
   └─────┬─────┘
         │ vision_results
         ▼
   ┌───────────┐
   │    RAG    │ → Retrieves docs + generates guidance
   │   Agent   │    (Llama-2 + ChromaDB)
   └─────┬─────┘
         │ rag_guidance
         ▼
   ┌───────────┐
   │  Report   │ → Creates incident report
   │   Agent   │    (Llama-2)
   └─────┬─────┘
         │
         ▼
7. Response Aggregation
   ↓
8. JSON Response to Client
```

---

## 🤖 Agent Implementation Details

### 1. Vision Agent (VisionAgent)

**Purpose**: Analyze equipment images for visual defects using Vision-Language Models

**Model**: `Salesforce/blip2-opt-2.7b`
- **Type**: Vision-Language Model (VLM)
- **Capability**: Image captioning, visual Q&A, defect detection
- **Size**: 2.7B parameters

**Implementation** (`app/agents.py`):

```python
class VisionAgent:
    """Vision-based defect detection using BLIP-2 VLM"""
    
    def __init__(self):
        self.model_id = config.VLM_MODEL_ID  # "Salesforce/blip2-opt-2.7b"
        self.hf_token = config.HUGGINGFACE_TOKEN
        
    def analyze_image(self, image_id: str) -> Dict[str, Any]:
        """
        Analyzes image for manufacturing defects
        
        Args:
            image_id: Reference to image in storage system
            
        Returns:
            {
                "defects_found": ["micro-fracture", "surface-roughness"],
                "confidence": 0.87,
                "model_used": "Salesforce/blip2-opt-2.7b",
                "image_analyzed": "img_12345"
            }
        """
        # Current: Mock analysis (returns simulated defects)
        # TODO: Integrate actual HF Vision API call
        
        return {
            "defects_found": ["micro-fracture", "surface-roughness"],
            "confidence": 0.87,
            "model_used": self.model_id,
            "image_analyzed": image_id
        }
```

**How to Implement Real Vision Analysis**:

```python
from langchain_huggingface import HuggingFaceEndpoint

def analyze_image(self, image_id: str, image_bytes: bytes) -> Dict[str, Any]:
    """Real implementation with HF Vision API"""
    
    # 1. Initialize VLM endpoint
    vlm = HuggingFaceEndpoint(
        repo_id=self.model_id,
        huggingfacehub_api_token=self.hf_token,
        task="image-to-text",
        model_kwargs={
            "temperature": 0.3,  # Low temp for factual analysis
            "max_new_tokens": 200
        }
    )
    
    # 2. Create prompt for defect detection
    prompt = """Analyze this manufacturing equipment image.
    Identify any visible defects, damage, or quality issues.
    List each defect found with confidence level.
    
    Format: defect_name (confidence%)
    """
    
    # 3. Call VLM with image + prompt
    response = vlm.invoke(prompt, image=image_bytes)
    
    # 4. Parse defects from response
    defects = self._parse_defects(response)
    
    return {
        "defects_found": defects,
        "confidence": self._calculate_confidence(defects),
        "model_used": self.model_id,
        "image_analyzed": image_id,
        "raw_analysis": response
    }
```

---

### 2. RAG Agent (RAGAgent)

**Purpose**: Retrieve relevant technical documentation and generate maintenance guidance

**Components**:
- **LLM**: `meta-llama/Llama-2-7b-chat-hf` (7B parameters)
- **Embeddings**: `sentence-transformers/all-MiniLM-L6-v2` (384 dimensions)
- **Vector DB**: ChromaDB (persistent storage)

**Knowledge Base** (5 SOPs pre-populated):

| Doc ID | Title | Content Type |
|--------|-------|--------------|
| SOP-123 | CNC Machine Troubleshooting | Cooling systems, calibration |
| MAINT-GUIDE-V2 | Welding Equipment Maintenance | Electrode care, gas checks |
| SOP-456 | Assembly Line Quality Control | Torque specs, alignments |
| COATING-MANUAL-2024 | Surface Coating Guidelines | Temperature, thickness |
| SAFETY-SOP-001 | Emergency Response | Shutdowns, hazmat |

**Implementation** (`app/agents.py`):

```python
class RAGAgent:
    """RAG-powered maintenance guidance system"""
    
    def __init__(self):
        # 1. Initialize embeddings model
        self.embeddings = HuggingFaceEmbeddings(
            model_name=config.EMBEDDING_MODEL_ID,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True}
        )
        
        # 2. Initialize vector database
        self.vectorstore = Chroma(
            collection_name="manufacturing_sops",
            embedding_function=self.embeddings,
            persist_directory=config.CHROMA_PERSIST_DIR
        )
        
        # 3. Initialize LLM
        self.llm = HuggingFaceEndpoint(
            repo_id=config.LLM_MODEL_ID,
            huggingfacehub_api_token=config.HUGGINGFACE_TOKEN,
            temperature=config.TEMPERATURE,
            max_new_tokens=config.MAX_TOKENS
        )
        
        # 4. Create retrieval chain
        self.retrieval_chain = self._create_retrieval_chain()
        
        # 5. Populate knowledge base (first run only)
        self._populate_sample_docs()
    
    def _create_retrieval_chain(self):
        """Creates LangChain RAG pipeline"""
        
        # Retriever: Find top-k relevant documents
        retriever = self.vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 3}  # Retrieve 3 most relevant docs
        )
        
        # Prompt template for guidance generation
        template = """You are an expert manufacturing technician assistant.
        Use the following maintenance documentation to answer the question.
        
        Context from SOPs:
        {context}
        
        Question: {question}
        
        Provide step-by-step maintenance guidance based on the documentation.
        Cite the SOP document IDs you used.
        
        Guidance:"""
        
        prompt = PromptTemplate(
            template=template,
            input_variables=["context", "question"]
        )
        
        # Chain: Retrieve → Format → LLM → Parse
        chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | self.llm
            | StrOutputParser()
        )
        
        return chain
    
    def get_guidance(self, query: str) -> Dict[str, Any]:
        """
        Retrieves relevant docs and generates maintenance guidance
        
        Args:
            query: Problem description from technician
            
        Returns:
            {
                "recommended_steps": ["1. Check...", "2. Inspect..."],
                "cited_documents": ["SOP-123", "MAINT-GUIDE-V2"],
                "confidence": 0.85
            }
        """
        try:
            # Invoke RAG chain
            response = self.retrieval_chain.invoke(query)
            
            # Parse response
            steps = self._parse_steps(response)
            docs = self._extract_cited_docs(response)
            
            return {
                "recommended_steps": steps,
                "cited_documents": docs,
                "confidence": 0.85,
                "raw_response": response
            }
        except Exception as e:
            logger.error(f"RAG error: {e}")
            return self._fallback_guidance(query)
```

**How RAG Works**:

1. **User Query**: "CNC machine overheating"
2. **Embedding**: Query converted to 384-dim vector
3. **Similarity Search**: ChromaDB finds top-3 similar SOP chunks
4. **Context Building**: Retrieved docs formatted as context
5. **LLM Generation**: Llama-2 generates guidance using context
6. **Citation Extraction**: Parse doc IDs mentioned in response
7. **Response**: Structured guidance with sources

---

### 3. Report Agent (ReportAgent)

**Purpose**: Generate professional incident reports from diagnosis results

**Model**: `meta-llama/Llama-2-7b-chat-hf` (same as RAG agent)

**Implementation** (`app/agents.py`):

```python
class ReportAgent:
    """Automated incident report generation"""
    
    def __init__(self):
        self.llm = HuggingFaceEndpoint(
            repo_id=config.LLM_MODEL_ID,
            huggingfacehub_api_token=config.HUGGINGFACE_TOKEN,
            temperature=0.5,  # Slightly higher for natural writing
            max_new_tokens=700  # Longer for full report
        )
    
    def generate_report(self, state: Dict[str, Any]) -> str:
        """
        Creates incident report from diagnosis results
        
        Args:
            state: LangGraph state with vision + RAG results
            
        Returns:
            Formatted incident report (string)
        """
        # Build prompt with all context
        prompt = f"""Generate a professional manufacturing incident report.

INCIDENT DETAILS:
- Plant ID: {state['plant_id']}
- Equipment ID: {state['equipment_id']}
- Problem: {state['problem_description']}

VISUAL INSPECTION:
Defects Found: {', '.join(state['vision_analysis'].get('defects_found', []))}
Confidence: {state['vision_analysis'].get('confidence', 'N/A')}

TECHNICAL GUIDANCE:
{chr(10).join(state['rag_guidance'].get('recommended_steps', []))}

Documentation References: {', '.join(state['rag_guidance'].get('cited_documents', []))}

Create a structured report with:
1. SUMMARY (2-3 sentences)
2. DEFECTS IDENTIFIED (bullet points)
3. RECOMMENDED ACTIONS (numbered steps)
4. SAFETY NOTES
5. FOLLOW-UP REQUIRED

Format professionally for maintenance logs.

REPORT:"""

        # Generate report
        report = self.llm.invoke(prompt)
        
        return report.strip()
```

**Report Structure**:

```
MANUFACTURING INCIDENT REPORT

SUMMARY:
Equipment CNC-A-102 at PUNE-IN plant experienced overheating during 
operation. Visual inspection revealed micro-fractures and surface 
roughness. Immediate maintenance recommended.

DEFECTS IDENTIFIED:
• Micro-fracture (87% confidence)
• Surface roughness (87% confidence)

RECOMMENDED ACTIONS:
1. Check coolant levels in the reservoir
2. Inspect coolant lines for leaks or blockages
3. Verify coolant pump operation
4. Inspect spindle bearings for wear
5. Check cutting tool condition

SAFETY NOTES:
- Lock out/tag out before maintenance
- Wear appropriate PPE
- Allow equipment to cool before inspection

FOLLOW-UP REQUIRED:
- Maintenance team to execute corrective actions within 24 hours
- Re-inspect after repairs
- Update maintenance log in ERP system

Referenced SOPs: SOP-123, MAINT-GUIDE-V2
Report Generated: 2024-01-15 14:32:00 UTC
```

---

## 🔗 LangGraph Orchestration

**Why LangGraph?**
- **Sequential Execution**: Vision → RAG → Report (each depends on previous)
- **State Management**: Shared state across all agents
- **Error Handling**: Built-in retries and fallbacks
- **Observability**: Easy to trace execution flow

**Implementation** (`app/agents.py`):

```python
from langgraph.graph import StateGraph, END

# Define shared state schema
class AgentState(TypedDict):
    # Inputs
    plant_id: str
    equipment_id: str
    problem_description: str
    image_id: Optional[str]
    
    # Outputs from each agent
    vision_analysis: Optional[Dict[str, Any]]
    rag_guidance: Optional[Dict[str, Any]]
    generated_report: Optional[str]
    
    # Metadata
    request_id: str
    confidence_score: float

# Initialize agents
vision_agent = VisionAgent()
rag_agent = RAGAgent()
report_agent = ReportAgent()

# Define agent nodes
def vision_node(state: AgentState) -> AgentState:
    """Step 1: Analyze image for defects"""
    logger.info(f"[{state['request_id']}] Running vision analysis...")
    
    if state.get("image_id"):
        vision_results = vision_agent.analyze_image(state["image_id"])
    else:
        # No image provided
        vision_results = {"defects_found": [], "confidence": 0.0}
    
    state["vision_analysis"] = vision_results
    return state

def rag_node(state: AgentState) -> AgentState:
    """Step 2: Retrieve docs and generate guidance"""
    logger.info(f"[{state['request_id']}] Running RAG retrieval...")
    
    # Build enhanced query with vision context
    query = f"{state['problem_description']}"
    if state['vision_analysis'].get('defects_found'):
        query += f" Defects observed: {', '.join(state['vision_analysis']['defects_found'])}"
    
    rag_results = rag_agent.get_guidance(query)
    state["rag_guidance"] = rag_results
    return state

def report_node(state: AgentState) -> AgentState:
    """Step 3: Generate incident report"""
    logger.info(f"[{state['request_id']}] Generating report...")
    
    report = report_agent.generate_report(state)
    state["generated_report"] = report
    
    # Calculate overall confidence
    vision_conf = state['vision_analysis'].get('confidence', 0.0)
    rag_conf = state['rag_guidance'].get('confidence', 0.0)
    state["confidence_score"] = (vision_conf + rag_conf) / 2
    
    return state

# Build workflow graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("vision", vision_node)
workflow.add_node("rag", rag_node)
workflow.add_node("report", report_node)

# Define edges (execution order)
workflow.set_entry_point("vision")
workflow.add_edge("vision", "rag")
workflow.add_edge("rag", "report")
workflow.add_edge("report", END)

# Compile graph
agent_graph = workflow.compile()
```

**Execution Trace Example**:

```
[req-123] Running vision analysis...
  ↓ 2.3s
[req-123] Vision complete: 2 defects found (87% confidence)
  ↓
[req-123] Running RAG retrieval...
  ↓ 3.1s
[req-123] RAG complete: 5 steps, 2 docs cited (85% confidence)
  ↓
[req-123] Generating report...
  ↓ 4.7s
[req-123] Report complete (712 chars)
  ↓
[req-123] Total execution: 10.1s
```

---

## 🤗 HuggingFace Integration

### Why HuggingFace Inference API?

| Requirement | HF Solution |
|------------|-------------|
| No GPU available | Serverless inference endpoints |
| Cost-effective | Free tier + pay-per-use |
| Model variety | 200k+ models available |
| Production SLA | 99.9% uptime guarantee |
| Easy integration | LangChain native support |

### Model Selection Rationale

**LLM: Llama-2-7b-chat-hf**
- ✅ Good instruction following
- ✅ 7B size = fast inference
- ✅ Free on HF Inference API
- ✅ Strong factual accuracy
- ❌ Requires accepting Meta license

**VLM: BLIP-2 (opt-2.7b)**
- ✅ Strong visual understanding
- ✅ Can answer questions about images
- ✅ 2.7B = lightweight
- ✅ No license restrictions

**Embeddings: all-MiniLM-L6-v2**
- ✅ 384 dimensions (efficient)
- ✅ Fast encoding (10ms/doc)
- ✅ Good for technical content
- ✅ Widely adopted benchmark

### Configuration (`app/config.py`)

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # HuggingFace
    HUGGINGFACE_TOKEN: str
    VLM_MODEL_ID: str = "Salesforce/blip2-opt-2.7b"
    LLM_MODEL_ID: str = "meta-llama/Llama-2-7b-chat-hf"
    EMBEDDING_MODEL_ID: str = "sentence-transformers/all-MiniLM-L6-v2"
    
    # Inference settings
    TEMPERATURE: float = 0.7
    MAX_TOKENS: int = 512
    REQUEST_TIMEOUT: int = 60
    MAX_RETRIES: int = 3
    
    # ChromaDB
    CHROMA_PERSIST_DIR: str = "./chroma_db"
    
    class Config:
        env_file = ".env"

config = Settings()
```

### Error Handling for HF API

```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(config.MAX_RETRIES),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    reraise=True
)
def invoke_hf_endpoint(prompt: str, model_id: str) -> str:
    """
    Calls HF Inference API with retry logic
    
    Retries on:
    - Timeout errors
    - Rate limit errors (429)
    - Server errors (5xx)
    """
    llm = HuggingFaceEndpoint(
        repo_id=model_id,
        huggingfacehub_api_token=config.HUGGINGFACE_TOKEN,
        timeout=config.REQUEST_TIMEOUT
    )
    
    try:
        response = llm.invoke(prompt)
        return response
    except Exception as e:
        logger.error(f"HF API error: {e}")
        if "rate limit" in str(e).lower():
            logger.warning("Rate limited, retrying...")
            raise  # Retry
        elif "timeout" in str(e).lower():
            logger.warning("Timeout, retrying...")
            raise  # Retry
        else:
            # Non-retryable error
            return fallback_response(prompt)
```

---

## 📖 Code Walkthrough

### Request Lifecycle

**1. FastAPI Entry Point** (`app/main.py`)

```python
@app.post("/v1/diagnose", response_model=DiagnosisResponse)
async def diagnose(
    request: DiagnosisRequest,
    auth: str = Depends(verify_token)
) -> DiagnosisResponse:
    """
    Main endpoint for manufacturing diagnosis
    
    Flow:
    1. Validate auth token
    2. Validate request body (Pydantic)
    3. Initialize LangGraph state
    4. Execute agent workflow
    5. Return structured response
    """
    request_id = str(uuid.uuid4())
    logger.info(f"[{request_id}] New diagnosis request: {request.equipment_id}")
    
    # Initialize state
    initial_state = {
        "request_id": request_id,
        "plant_id": request.plant_id,
        "equipment_id": request.equipment_id,
        "problem_description": request.problem_description,
        "image_id": request.image_id
    }
    
    # Run agent graph
    final_state = agent_graph.invoke(initial_state)
    
    # Build response
    return DiagnosisResponse(
        request_id=request_id,
        vision_analysis=final_state["vision_analysis"],
        rag_guidance=final_state["rag_guidance"],
        generated_report=final_state["generated_report"],
        confidence_score=final_state["confidence_score"],
        safety_disclaimer="Always follow standard safety procedures."
    )
```

**2. Authentication** (`app/security.py`)

```python
async def verify_token(x_auth_token: str = Header(...)) -> str:
    """
    Validates bearer token
    
    Expected format: "Bearer technician-<user_id>"
    
    In production, replace with:
    - OAuth2/OIDC
    - API key management system
    - JWT validation
    """
    if not x_auth_token.startswith("Bearer technician-"):
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication token"
        )
    
    return x_auth_token
```

**3. Pydantic Models** (`app/models.py`)

```python
from pydantic import BaseModel, Field, validator

class DiagnosisRequest(BaseModel):
    """Request body validation"""
    
    plant_id: str = Field(
        ...,
        pattern=r"^[A-Z]{3,4}-\w{2,3}$",
        example="PUNE-IN"
    )
    equipment_id: str = Field(
        ...,
        min_length=4,
        example="CNC-A-102"
    )
    problem_description: str = Field(
        ...,
        min_length=10,
        max_length=500,
        example="Machine overheating during operation"
    )
    image_id: Optional[str] = Field(
        None,
        example="img_12345"
    )
    
    @validator("problem_description")
    def sanitize_description(cls, v):
        """Prevent injection attacks"""
        dangerous_chars = ["<", ">", "{", "}", ";"]
        for char in dangerous_chars:
            if char in v:
                raise ValueError(f"Invalid character: {char}")
        return v
```

---

## 🎨 Customization Guide

### Add a New Agent

**Example: Quality Score Agent**

```python
# 1. Define agent class
class QualityScoreAgent:
    """Calculates quality score from defect analysis"""
    
    def calculate_score(self, defects: List[str]) -> float:
        severity_map = {
            "micro-fracture": 0.3,
            "surface-roughness": 0.2,
            "corrosion": 0.5,
            "deformation": 0.6
        }
        
        if not defects:
            return 1.0
        
        penalties = [severity_map.get(d, 0.1) for d in defects]
        return max(0.0, 1.0 - sum(penalties))

# 2. Add to state
class AgentState(TypedDict):
    # ... existing fields
    quality_score: Optional[float]

# 3. Create node
def quality_node(state: AgentState) -> AgentState:
    defects = state['vision_analysis'].get('defects_found', [])
    score = quality_agent.calculate_score(defects)
    state['quality_score'] = score
    return state

# 4. Add to workflow
workflow.add_node("quality", quality_node)
workflow.add_edge("vision", "quality")  # After vision
workflow.add_edge("quality", "rag")     # Before RAG
```

### Use Different Models

**Switch to GPT-4 for LLM**:

```python
# .env
LLM_PROVIDER=openai
LLM_MODEL_ID=gpt-4-turbo-preview
OPENAI_API_KEY=sk-...

# app/agents.py
from langchain_openai import ChatOpenAI

if config.LLM_PROVIDER == "openai":
    llm = ChatOpenAI(
        model=config.LLM_MODEL_ID,
        api_key=config.OPENAI_API_KEY
    )
else:
    llm = HuggingFaceEndpoint(...)
```

### Add New SOP Documents

```python
# app/agents.py - RAGAgent class

def add_custom_sop(self, doc_id: str, title: str, content: str):
    """Add new SOP to knowledge base"""
    
    doc = Document(
        page_content=content,
        metadata={
            "doc_id": doc_id,
            "title": title,
            "type": "SOP",
            "added_date": datetime.now().isoformat()
        }
    )
    
    # Add to ChromaDB
    self.vectorstore.add_documents([doc])
    logger.info(f"Added SOP: {doc_id}")

# Usage
rag_agent.add_custom_sop(
    doc_id="SOP-789",
    title="Hydraulic System Maintenance",
    content="""
    HYDRAULIC SYSTEM TROUBLESHOOTING
    
    1. Pressure Issues:
       - Check hydraulic fluid level
       - Inspect pump for wear
       - Verify pressure relief valve setting
    
    2. Leak Detection:
       - Visual inspection of hoses
       - Check fitting torque
       - Replace damaged seals
    """
)
```

### Custom Prompt Templates

```python
# app/prompts.py

REPORT_PROMPT_TEMPLATE = """You are a senior maintenance engineer writing an incident report.

Context:
- Plant: {plant_id}
- Equipment: {equipment_id}
- Issue: {problem_description}

Analysis Results:
{analysis_summary}

Write a formal incident report following ISO 9001 standards.
Include root cause analysis and preventive measures.

REPORT:"""

# app/agents.py - ReportAgent

from app.prompts import REPORT_PROMPT_TEMPLATE

def generate_report(self, state: Dict[str, Any]) -> str:
    prompt = REPORT_PROMPT_TEMPLATE.format(
        plant_id=state['plant_id'],
        equipment_id=state['equipment_id'],
        problem_description=state['problem_description'],
        analysis_summary=self._build_summary(state)
    )
    
    return self.llm.invoke(prompt)
```

---

## ⚡ Performance Optimization

### 1. Caching LLM Responses

```python
from functools import lru_cache
import hashlib

@lru_cache(maxsize=100)
def cached_llm_invoke(prompt_hash: str, prompt: str) -> str:
    """Cache LLM responses for identical prompts"""
    return llm.invoke(prompt)

def invoke_with_cache(prompt: str) -> str:
    prompt_hash = hashlib.md5(prompt.encode()).hexdigest()
    return cached_llm_invoke(prompt_hash, prompt)
```

### 2. Parallel Agent Execution (If Independent)

```python
import asyncio

async def parallel_workflow(state: AgentState):
    """Run vision + metadata agents in parallel"""
    
    vision_task = asyncio.create_task(vision_agent.analyze_async(state))
    metadata_task = asyncio.create_task(metadata_agent.extract_async(state))
    
    vision_result, metadata_result = await asyncio.gather(
        vision_task,
        metadata_task
    )
    
    state['vision_analysis'] = vision_result
    state['metadata'] = metadata_result
    return state
```

### 3. ChromaDB Index Optimization

```python
# Increase batch size for faster embedding
self.vectorstore = Chroma(
    collection_name="manufacturing_sops",
    embedding_function=self.embeddings,
    persist_directory=config.CHROMA_PERSIST_DIR,
    collection_metadata={"hnsw:space": "cosine"}  # Faster similarity search
)

# Pre-warm collection on startup
def warmup_vectorstore():
    """Load index into memory"""
    _ = self.vectorstore.similarity_search("test query", k=1)
```

### 4. Request Batching

```python
@app.post("/v1/diagnose/batch")
async def diagnose_batch(requests: List[DiagnosisRequest]):
    """Process multiple diagnoses in parallel"""
    
    tasks = [
        asyncio.create_task(diagnose_single(req))
        for req in requests
    ]
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return {"results": results}
```

---

## 🛡️ Error Handling Strategy

### Three-Tier Fallback System

**Tier 1: Retry with Exponential Backoff**
```python
@retry(stop=stop_after_attempt(3), wait=wait_exponential())
def api_call():
    ...
```

**Tier 2: Graceful Degradation**
```python
def vision_node(state):
    try:
        result = vision_agent.analyze(state['image_id'])
    except Exception as e:
        logger.error(f"Vision agent failed: {e}")
        result = {
            "defects_found": [],
            "confidence": 0.0,
            "error": str(e)
        }
    state['vision_analysis'] = result
    return state
```

**Tier 3: Human Escalation**
```python
if final_state['confidence_score'] < 0.5:
    return {
        "status": "requires_manual_review",
        "message": "Confidence too low, escalating to human expert",
        "partial_results": final_state
    }
```

### Logging Strategy

```python
import structlog

logger = structlog.get_logger()

# Structured logging
logger.info(
    "agent_execution",
    agent="vision",
    request_id=state['request_id'],
    duration_ms=234,
    confidence=0.87,
    defects_count=2
)
```

---

## 🚢 Production Deployment Architecture

### Kubernetes Architecture

**Recommended for production deployments** with high availability and scalability requirements.

```
┌───────────────────────────────────────────────────────┐
│              Kubernetes Cluster (GKE/EKS/AKS)         │
│                                                       │
│  ┌─────────────────────────────────────────────┐    │
│  │            Ingress Controller                │    │
│  │  (NGINX / GKE Ingress / AWS ALB)            │    │
│  │  • TLS Termination                          │    │
│  │  • Rate Limiting                            │    │
│  │  • Path-based Routing                       │    │
│  └──────────────────┬──────────────────────────┘    │
│                     │                                │
│  ┌──────────────────▼──────────────────────────┐    │
│  │          Service (ClusterIP)                │    │
│  │  manufacturing-copilot:8080                 │    │
│  └──────────────────┬──────────────────────────┘    │
│                     │                                │
│  ┌──────────────────▼──────────────────────────┐    │
│  │      Horizontal Pod Autoscaler (HPA)        │    │
│  │  • Min: 2 replicas                          │    │
│  │  • Max: 10 replicas                         │    │
│  │  • Target: 70% CPU / 80% Memory             │    │
│  └──────────────────┬──────────────────────────┘    │
│                     │                                │
│  ┌──────────────────▼──────────────────────────┐    │
│  │        Deployment: manufacturing-copilot     │    │
│  │  ┌─────────────┐  ┌─────────────┐          │    │
│  │  │   Pod 1     │  │   Pod 2     │  ...     │    │
│  │  │ ┌─────────┐ │  │ ┌─────────┐ │          │    │
│  │  │ │FastAPI  │ │  │ │FastAPI  │ │          │    │
│  │  │ │Container│ │  │ │Container│ │          │    │
│  │  │ └─────────┘ │  │ └─────────┘ │          │    │
│  │  │ • CPU: 500m-2│  │ • CPU: 500m-2│         │    │
│  │  │ • Mem: 1-4Gi│  │ • Mem: 1-4Gi│          │    │
│  │  │ • Liveness  │  │ • Readiness │          │    │
│  │  │ • Startup   │  │   Probes    │          │    │
│  │  └─────────────┘  └─────────────┘          │    │
│  └─────────────────────────────────────────────┘    │
│                     │                                │
│  ┌──────────────────▼──────────────────────────┐    │
│  │   Persistent Volume (ChromaDB Storage)      │    │
│  │   • Size: 10Gi (SSD)                        │    │
│  │   • RWO (ReadWriteOnce)                     │    │
│  │   • StorageClass: pd-ssd/gp3/managed-premium│    │
│  └─────────────────────────────────────────────┘    │
│                                                       │
│  ┌─────────────────────────────────────────────┐    │
│  │         ConfigMap & Secrets                 │    │
│  │  • HUGGINGFACE_TOKEN (Secret)               │    │
│  │  • Model IDs (ConfigMap)                    │    │
│  │  • API Settings (ConfigMap)                 │    │
│  └─────────────────────────────────────────────┘    │
│                                                       │
│  ┌─────────────────────────────────────────────┐    │
│  │      Monitoring & Observability             │    │
│  │  • Prometheus (ServiceMonitor)              │    │
│  │  • Grafana Dashboards                       │    │
│  │  • Structured Logging (Fluentd)             │    │
│  └─────────────────────────────────────────────┘    │
│                                                       │
│  ┌─────────────────────────────────────────────┐    │
│  │         Network Policies                    │    │
│  │  • Ingress: From ingress-nginx only         │    │
│  │  • Egress: DNS + HTTPS (HuggingFace API)    │    │
│  └─────────────────────────────────────────────┘    │
│                                                       │
│  ┌─────────────────────────────────────────────┐    │
│  │      Pod Disruption Budget (PDB)            │    │
│  │  • minAvailable: 1                          │    │
│  │  • Ensures availability during updates      │    │
│  └─────────────────────────────────────────────┘    │
└───────────────────────────────────────────────────────┘
```

### Key Production Features

**1. High Availability**
- **Pod Disruption Budget**: Ensures at least 1 pod always running during voluntary disruptions
- **Anti-Affinity**: Spreads pods across nodes/zones
- **Health Probes**: Liveness, readiness, and startup probes prevent cascading failures

**2. Auto-Scaling**
- **Horizontal Pod Autoscaler**: Scales 2-10 replicas based on CPU/memory
- **Advanced Scaling Policies**: 
  - Scale up: Max 4 pods per minute, 100% increase
  - Scale down: 5 min stabilization window
- **Custom Metrics**: Can add HuggingFace API latency metrics

**3. Security**
- **NetworkPolicy**: Restricts pod-to-pod and external communication
- **SecurityContext**: Non-root user, read-only filesystem, dropped capabilities
- **Secrets Management**: Kubernetes Secrets with optional External Secrets Operator
- **RBAC**: Least-privilege ServiceAccount

**4. Observability**
- **Prometheus Integration**: ServiceMonitor for metrics scraping
- **Structured Logging**: JSON logs with request tracing
- **Request Tracing**: X-Request-Trace-ID header for distributed tracing

**5. Storage**
- **Persistent Volume**: SSD-backed storage for ChromaDB vector database
- **StatefulSet Option**: For multi-replica ChromaDB (future enhancement)

### Deployment Paths

**Path 1: Helm (Recommended)**
```bash
helm install copilot ./charts/manufacturing-copilot \
  --namespace manufacturing-copilot \
  --create-namespace \
  --values ./charts/manufacturing-copilot/values-prod.yaml \
  --set secrets.huggingfaceToken="hf_your_token"
```

**Path 2: kubectl**
```bash
kubectl apply -f kubernetes/ --namespace=manufacturing-copilot
```

**Path 3: GitOps (ArgoCD/Flux)**
- Helm chart or plain manifests tracked in Git
- Automatic sync on commit
- Rollback capability

### Multi-Cloud Support

| Cloud | Ingress Controller | Storage Class | Workload Identity |
|-------|-------------------|---------------|-------------------|
| **GKE** | gce | pd-ssd | iam.gke.io/gcp-service-account |
| **EKS** | alb | gp3 | eks.amazonaws.com/role-arn |
| **AKS** | nginx | managed-premium | azure.workload.identity/client-id |

**See [KUBERNETES_DEPLOYMENT.md](KUBERNETES_DEPLOYMENT.md) for complete guide.**

---

## 🎓 Further Customization Ideas

1. **Add Multi-Language Support**: Use `googletrans` for SOPs
2. **Implement Feedback Loop**: Store corrections to improve RAG
3. **Add Streaming Responses**: Use Server-Sent Events for real-time updates
4. **Image Upload**: Integrate blob storage (AWS S3, Azure Blob)
5. **Advanced RAG**: Implement Hyde, CoVe, or Self-Ask patterns
6. **Multi-Modal**: Combine audio (equipment sounds) + vision
7. **Predictive Maintenance**: Add time-series forecasting agent
8. **Knowledge Graph**: Use Neo4j for equipment relationships
9. **Kubernetes CronJobs**: Scheduled maintenance tasks (DB backups, model updates)
10. **Service Mesh**: Istio/Linkerd for advanced traffic management

---

**Questions? See [README.md](README.md), [KUBERNETES_DEPLOYMENT.md](KUBERNETES_DEPLOYMENT.md), or open an issue!**

**Built with ❤️ for the Gen AI Masters Program**
