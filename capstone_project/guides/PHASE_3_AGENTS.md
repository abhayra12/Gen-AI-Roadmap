# Phase 3: GenAI Agents Implementation

## Step 3: Build the Agents (Continued)

Create `app/agents.py`:

```python
# app/agents.py

import os
import logging
from typing import TypedDict, List, Dict, Any, Optional
from uuid import uuid4

from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.schema import SystemMessage, HumanMessage
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langgraph.graph import StateGraph, END

from app.config import settings

# Configure logging
logger = logging.getLogger(__name__)

# =============================================================================
# AGENT STATE
# =============================================================================

class AgentState(TypedDict):
    """Shared state across all agents in the graph."""
    request_id: str
    plant_id: str
    equipment_id: str
    problem_description: str
    image_id: Optional[str]
    
    # Agent outputs
    vision_analysis: Optional[Dict[str, Any]]
    rag_guidance: Optional[Dict[str, Any]]
    generated_report: Optional[str]
    confidence_score: float


# =============================================================================
# VISION AGENT
# =============================================================================

class VisionAgent:
    """
    Agent that analyzes images of equipment using Vision-Language Models.
    
    Responsibilities:
    - Process equipment images
    - Identify visual defects
    - Extract visual features
    """
    
    def __init__(self):
        """Initialize the Vision Agent with BLIP-2 model."""
        self.model_id = settings.VLM_MODEL_ID
        logger.info(f"Initializing VisionAgent with model: {self.model_id}")
        
    def analyze_image(self, image_id: str, equipment_id: str) -> Dict[str, Any]:
        """
        Analyze an equipment image.
        
        Args:
            image_id: Identifier for the image
            equipment_id: Equipment being analyzed
            
        Returns:
            Dictionary with visual analysis results
        """
        logger.info(f"Analyzing image {image_id} for equipment {equipment_id}")
        
        # In production, this would:
        # 1. Load image from storage (S3, Azure Blob, etc.)
        # 2. Send to BLIP-2 model via HuggingFace Inference API
        # 3. Parse and return results
        
        # Mock response for demonstration
        return {
            "detected_issue": "rust_corrosion",
            "severity": "moderate",
            "affected_components": ["gear_assembly", "bearing_housing"],
            "confidence": 0.85,
            "visual_description": "Visible rust on metal surfaces, particularly around bearing housing"
        }
    
    def node_function(self, state: AgentState) -> AgentState:
        """
        LangGraph node function for Vision Agent.
        
        Args:
            state: Current agent state
            
        Returns:
            Updated state with vision_analysis
        """
        logger.info("VisionAgent node executing...")
        
        if state.get("image_id"):
            analysis = self.analyze_image(state["image_id"], state["equipment_id"])
            state["vision_analysis"] = analysis
            logger.info(f"Vision analysis complete: {analysis}")
        else:
            state["vision_analysis"] = {
                "message": "No image provided for analysis"
            }
            logger.info("No image provided, skipping visual analysis")
        
        return state


# =============================================================================
# RAG AGENT
# =============================================================================

class RAGAgent:
    """
    Agent that retrieves relevant information from SOPs and manuals.
    
    Responsibilities:
    - Query vector database
    - Retrieve relevant documentation
    - Generate contextual guidance
    """
    
    def __init__(self):
        """Initialize the RAG Agent with ChromaDB and Llama-2."""
        logger.info("Initializing RAGAgent...")
        
        # Initialize embeddings
        self.embeddings = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL_ID,
            model_kwargs={'device': 'cpu'}
        )
        
        # Initialize vector store
        self.vectorstore = self._initialize_vectorstore()
        
        # Initialize LLM
        self.llm = HuggingFaceEndpoint(
            repo_id=settings.LLM_MODEL_ID,
            huggingfacehub_api_token=settings.HUGGINGFACE_TOKEN,
            temperature=settings.TEMPERATURE,
            max_new_tokens=settings.MAX_TOKENS,
        )
        
        # Create RAG prompt
        self.prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""You are a manufacturing equipment expert. Use the following context to answer the question.

Context: {context}

Question: {question}

Provide a structured answer with:
1. Root cause analysis
2. Recommended actions
3. Safety precautions
4. Expected resolution time

Answer:"""
        )
        
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)
        
    def _initialize_vectorstore(self) -> Chroma:
        """Initialize or load ChromaDB vector store."""
        persist_dir = settings.CHROMA_PERSIST_DIR
        
        if os.path.exists(persist_dir):
            logger.info(f"Loading existing vector store from {persist_dir}")
            return Chroma(
                persist_directory=persist_dir,
                embedding_function=self.embeddings,
                collection_name="manufacturing_docs"
            )
        else:
            logger.warning(f"Vector store not found at {persist_dir}, creating new one")
            # In production, you'd populate this with actual documents
            vectorstore = Chroma(
                persist_directory=persist_dir,
                embedding_function=self.embeddings,
                collection_name="manufacturing_docs"
            )
            
            # Add sample documents
            sample_docs = [
                "CNC machines require regular lubrication of moving parts every 200 operating hours.",
                "Rust on metal surfaces indicates moisture exposure. Clean with wire brush and apply rust inhibitor.",
                "Bearing noise often indicates lack of lubrication or worn bearings. Replace if excessive play detected.",
                "Hydraulic system pressure drops may be caused by leaking seals or low fluid levels.",
                "Electrical panel overheating: Check for loose connections and ensure adequate ventilation."
            ]
            
            vectorstore.add_texts(
                texts=sample_docs,
                metadatas=[{"source": "maintenance_manual", "section": f"Section {i+1}"} for i in range(len(sample_docs))]
            )
            
            vectorstore.persist()
            logger.info("Sample documents added to vector store")
            
            return vectorstore
    
    def retrieve_guidance(self, query: str, equipment_id: str) -> Dict[str, Any]:
        """
        Retrieve and generate guidance from documentation.
        
        Args:
            query: The problem description
            equipment_id: Equipment being diagnosed
            
        Returns:
            Dictionary with RAG guidance
        """
        logger.info(f"Retrieving guidance for: {query}")
        
        # Retrieve relevant documents
        docs = self.vectorstore.similarity_search(query, k=3)
        context = "\n\n".join([doc.page_content for doc in docs])
        
        # Generate response using LLM
        response = self.chain.run(context=context, question=query)
        
        return {
            "guidance": response,
            "sources": [doc.metadata.get("source", "unknown") for doc in docs],
            "confidence": 0.8
        }
    
    def node_function(self, state: AgentState) -> AgentState:
        """
        LangGraph node function for RAG Agent.
        
        Args:
            state: Current agent state
            
        Returns:
            Updated state with rag_guidance
        """
        logger.info("RAGAgent node executing...")
        
        # Build query from problem description and vision analysis
        query = state["problem_description"]
        
        if state.get("vision_analysis") and "detected_issue" in state["vision_analysis"]:
            query += f" Visual analysis detected: {state['vision_analysis']['detected_issue']}"
        
        guidance = self.retrieve_guidance(query, state["equipment_id"])
        state["rag_guidance"] = guidance
        
        logger.info(f"RAG guidance generated: {guidance}")
        
        return state


# =============================================================================
# REPORT AGENT
# =============================================================================

class ReportAgent:
    """
    Agent that generates structured maintenance reports.
    
    Responsibilities:
    - Synthesize outputs from other agents
    - Generate structured reports
    - Calculate confidence scores
    """
    
    def __init__(self):
        """Initialize the Report Agent."""
        logger.info("Initializing ReportAgent...")
        
        self.llm = HuggingFaceEndpoint(
            repo_id=settings.LLM_MODEL_ID,
            huggingfacehub_api_token=settings.HUGGINGFACE_TOKEN,
            temperature=0.5,  # Lower temperature for more structured output
            max_new_tokens=512,
        )
        
        self.prompt = PromptTemplate(
            input_variables=["plant_id", "equipment_id", "problem", "vision", "guidance"],
            template="""Generate a structured maintenance report for the following:

Plant: {plant_id}
Equipment: {equipment_id}
Problem: {problem}

Visual Analysis: {vision}

Expert Guidance: {guidance}

Generate a comprehensive report with the following sections:
1. SUMMARY
2. ROOT CAUSE ANALYSIS
3. RECOMMENDED ACTIONS (numbered list)
4. PARTS REQUIRED
5. ESTIMATED TIME
6. SAFETY NOTES

Report:"""
        )
        
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)
    
    def generate_report(
        self,
        plant_id: str,
        equipment_id: str,
        problem: str,
        vision_analysis: Dict[str, Any],
        rag_guidance: Dict[str, Any]
    ) -> tuple[str, float]:
        """
        Generate maintenance report.
        
        Returns:
            Tuple of (report_text, confidence_score)
        """
        logger.info("Generating maintenance report...")
        
        # Format inputs
        vision_text = str(vision_analysis) if vision_analysis else "No visual data"
        guidance_text = rag_guidance.get("guidance", "No guidance available")
        
        # Generate report
        report = self.chain.run(
            plant_id=plant_id,
            equipment_id=equipment_id,
            problem=problem,
            vision=vision_text,
            guidance=guidance_text
        )
        
        # Calculate overall confidence
        vision_conf = vision_analysis.get("confidence", 0) if vision_analysis else 0
        rag_conf = rag_guidance.get("confidence", 0) if rag_guidance else 0
        confidence = (vision_conf + rag_conf) / 2 if (vision_conf and rag_conf) else max(vision_conf, rag_conf)
        
        logger.info(f"Report generated with confidence: {confidence}")
        
        return report, confidence
    
    def node_function(self, state: AgentState) -> AgentState:
        """
        LangGraph node function for Report Agent.
        
        Args:
            state: Current agent state
            
        Returns:
            Updated state with generated_report and confidence_score
        """
        logger.info("ReportAgent node executing...")
        
        report, confidence = self.generate_report(
            plant_id=state["plant_id"],
            equipment_id=state["equipment_id"],
            problem=state["problem_description"],
            vision_analysis=state.get("vision_analysis"),
            rag_guidance=state.get("rag_guidance")
        )
        
        state["generated_report"] = report
        state["confidence_score"] = confidence
        
        logger.info("Report generation complete")
        
        return state


# =============================================================================
# LANGGRAPH ORCHESTRATOR
# =============================================================================

class DiagnosticOrchestrator:
    """
    Orchestrates multiple agents using LangGraph.
    
    The graph flows:
    START → Vision Agent → RAG Agent → Report Agent → END
    """
    
    def __init__(self):
        """Initialize the orchestrator and build the graph."""
        logger.info("Initializing DiagnosticOrchestrator...")
        
        # Initialize agents
        self.vision_agent = VisionAgent()
        self.rag_agent = RAGAgent()
        self.report_agent = ReportAgent()
        
        # Build graph
        self.graph = self._build_graph()
        
        logger.info("Orchestrator initialized successfully")
    
    def _build_graph(self) -> StateGraph:
        """Build the LangGraph workflow."""
        workflow = StateGraph(AgentState)
        
        # Add nodes
        workflow.add_node("vision", self.vision_agent.node_function)
        workflow.add_node("rag", self.rag_agent.node_function)
        workflow.add_node("report", self.report_agent.node_function)
        
        # Add edges (defines flow)
        workflow.set_entry_point("vision")
        workflow.add_edge("vision", "rag")
        workflow.add_edge("rag", "report")
        workflow.add_edge("report", END)
        
        return workflow.compile()
    
    def diagnose(
        self,
        plant_id: str,
        equipment_id: str,
        problem_description: str,
        image_id: Optional[str] = None
    ) -> AgentState:
        """
        Run the full diagnostic workflow.
        
        Args:
            plant_id: Plant identifier
            equipment_id: Equipment identifier
            problem_description: Problem description
            image_id: Optional image identifier
            
        Returns:
            Final agent state with all outputs
        """
        logger.info(f"Starting diagnosis for equipment {equipment_id}")
        
        # Initialize state
        initial_state: AgentState = {
            "request_id": str(uuid4()),
            "plant_id": plant_id,
            "equipment_id": equipment_id,
            "problem_description": problem_description,
            "image_id": image_id,
            "vision_analysis": None,
            "rag_guidance": None,
            "generated_report": None,
            "confidence_score": 0.0
        }
        
        # Run graph
        final_state = self.graph.invoke(initial_state)
        
        logger.info(f"Diagnosis complete for request {final_state['request_id']}")
        
        return final_state


# =============================================================================
# SINGLETON INSTANCE
# =============================================================================

# Create single instance to reuse across requests
orchestrator = DiagnosticOrchestrator()
```

## Understanding the Code

### 1. Agent State (`AgentState`)

**What**: A shared dictionary that passes through all agents

**Why**: LangGraph requires a shared state to coordinate agents

**When**: State is created at start, updated by each agent, and returned at end

**Example Flow**:
```
Initial State:
{
  "request_id": "123",
  "equipment_id": "CNC-A-102",
  "problem_description": "Strange noise",
  "vision_analysis": None,  # Will be filled by Vision Agent
  "rag_guidance": None,     # Will be filled by RAG Agent
  "generated_report": None  # Will be filled by Report Agent
}

After Vision Agent:
{
  "vision_analysis": {"detected_issue": "worn_bearing", ...},
  ...
}

After RAG Agent:
{
  "rag_guidance": {"guidance": "Replace bearing...", ...},
  ...
}

After Report Agent:
{
  "generated_report": "MAINTENANCE REPORT\n...",
  "confidence_score": 0.85
}
```

### 2. Vision Agent

**What**: Analyzes images of equipment

**Why**: Visual inspection is crucial for diagnosing mechanical issues

**When**: First agent in the pipeline (if image is provided)

**How It Works**:
1. Receives image_id from state
2. Loads image (mock in our implementation)
3. Sends to BLIP-2 model (Vision-Language Model)
4. Parses response
5. Updates state with vision_analysis

**Production Implementation**:
```python
# Real implementation would look like:
def analyze_image(self, image_id: str, equipment_id: str):
    # 1. Load image from storage
    image_path = f"s3://bucket/images/{image_id}.jpg"
    image = load_image(image_path)
    
    # 2. Call HuggingFace Inference API
    from huggingface_hub import InferenceClient
    client = InferenceClient(token=settings.HUGGINGFACE_TOKEN)
    
    result = client.image_to_text(
        image,
        model=settings.VLM_MODEL_ID
    )
    
    # 3. Parse and return
    return parse_vision_result(result)
```

### 3. RAG Agent

**What**: Retrieves relevant information from SOPs and manuals using RAG

**Why**: Combines knowledge base with LLM generation

**When**: Second agent in the pipeline

**How RAG Works**:
```
User Query: "CNC machine making noise"
     ↓
1. Convert to vector using embeddings
     ↓
2. Search ChromaDB for similar documents
     ↓
3. Retrieve top 3 most relevant docs
     ↓
4. Combine docs into context
     ↓
5. Send context + query to Llama-2
     ↓
6. LLM generates answer based on context
     ↓
Result: "Based on maintenance manual section 4.2..."
```

**Key Components**:
- **Embeddings**: Convert text to vectors for similarity search
- **Vector Store (ChromaDB)**: Stores document embeddings
- **LLM (Llama-2)**: Generates contextual answers
- **Prompt Template**: Structures the LLM input

### 4. Report Agent

**What**: Synthesizes all information into a structured report

**Why**: Provides actionable, formatted output for technicians

**When**: Final agent in the pipeline

**How It Works**:
1. Receives outputs from Vision and RAG agents
2. Formats inputs into a comprehensive prompt
3. Sends to Llama-2 for report generation
4. Calculates overall confidence score
5. Returns structured report

### 5. Diagnostic Orchestrator

**What**: Coordinates all agents using LangGraph

**Why**: Manages complex workflows with multiple agents

**When**: Entry point for all diagnosis requests

**LangGraph Benefits**:
- **State Management**: Automatic state passing
- **Error Handling**: Graceful failures
- **Observability**: Track agent execution
- **Flexibility**: Easy to add/remove agents

**Graph Visualization**:
```
  ┌─────┐
  │START│
  └──┬──┘
     │
     ▼
  ┌──────────┐
  │ Vision   │
  │ Agent    │
  └──┬───────┘
     │
     ▼
  ┌──────────┐
  │ RAG      │
  │ Agent    │
  └──┬───────┘
     │
     ▼
  ┌──────────┐
  │ Report   │
  │ Agent    │
  └──┬───────┘
     │
     ▼
   ┌───┐
   │END│
   └───┘
```

## Testing the Agents

Create `tests/test_agents.py`:

```python
# tests/test_agents.py

import pytest
from app.agents import VisionAgent, RAGAgent, ReportAgent, DiagnosticOrchestrator, AgentState

def test_vision_agent():
    """Test Vision Agent initialization and analysis."""
    agent = VisionAgent()
    
    result = agent.analyze_image("IMG_001", "CNC-A-102")
    
    assert "detected_issue" in result
    assert "confidence" in result
    assert isinstance(result["confidence"], float)

def test_rag_agent():
    """Test RAG Agent retrieval and generation."""
    agent = RAGAgent()
    
    result = agent.retrieve_guidance("Machine making noise", "CNC-A-102")
    
    assert "guidance" in result
    assert "sources" in result
    assert "confidence" in result

def test_report_agent():
    """Test Report Agent report generation."""
    agent = ReportAgent()
    
    vision = {"detected_issue": "rust", "confidence": 0.85}
    rag = {"guidance": "Clean and apply rust inhibitor", "confidence": 0.8}
    
    report, confidence = agent.generate_report(
        plant_id="PUNE-IN",
        equipment_id="CNC-A-102",
        problem="Rust on surface",
        vision_analysis=vision,
        rag_guidance=rag
    )
    
    assert isinstance(report, str)
    assert len(report) > 50
    assert 0 <= confidence <= 1

def test_full_orchestration():
    """Test full diagnostic workflow."""
    orchestrator = DiagnosticOrchestrator()
    
    result = orchestrator.diagnose(
        plant_id="PUNE-IN",
        equipment_id="CNC-A-102",
        problem_description="Machine making strange noise",
        image_id="IMG_001"
    )
    
    assert "request_id" in result
    assert result["vision_analysis"] is not None
    assert result["rag_guidance"] is not None
    assert result["generated_report"] is not None
    assert 0 <= result["confidence_score"] <= 1
```

Run tests:
```powershell
# Install pytest
pip install pytest

# Run tests
pytest tests/test_agents.py -v
```

## Common Issues & Solutions

### Issue 1: HuggingFace API Rate Limits

**Error**: `RateLimitError: Rate limit reached`

**Solution**:
```python
# Add retry logic with exponential backoff
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def call_hf_api(self, prompt):
    return self.llm.invoke(prompt)
```

### Issue 2: ChromaDB Persistence Issues

**Error**: `sqlite3.OperationalError: database is locked`

**Solution**:
```python
# Use different collection names or separate directories
vectorstore = Chroma(
    persist_directory=f"./chroma_db_{uuid4()}",
    ...
)
```

### Issue 3: Memory Issues with Large Documents

**Error**: `MemoryError: Out of memory`

**Solution**:
```python
# Chunk large documents before adding to vector store
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)
vectorstore.add_documents(chunks)
```

## ✅ Phase 3 Checkpoint

You should now have:
- [ ] `app/config.py` - Configuration management
- [ ] `app/models.py` - Pydantic models
- [ ] `app/agents.py` - All three agents + orchestrator
- [ ] `tests/test_agents.py` - Agent tests
- [ ] All tests passing
- [ ] ChromaDB initialized with sample documents

**Next**: Phase 4 - Building the FastAPI Backend

