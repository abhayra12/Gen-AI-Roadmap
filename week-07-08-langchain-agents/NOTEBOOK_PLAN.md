# Week 07-08 · LangChain, Agents & Advanced RAG — Notebook Plan

This roadmap keeps continuity with the manufacturing maintenance copilot narrative developed in Weeks 05-06 and the training focus from Weeks 09-10.

## Shared Scenario
Arvind Manufacturing is piloting a second-generation GenAI assistant. The assistant must:
- Parse SOP manuals, maintenance tickets, and IoT summaries.
- Route questions to the right plant knowledge base.
- Trigger contextual automations (spare-part lookup, downtime reports) via tools.
- Provide regulatory-safe responses with citations and bilingual support (English/Spanish).

Each notebook embeds governance checkpoints, performance expectations, and lab work to prepare the capstone deployment.

---

## Notebook Breakdown

### 01_langchain_essentials.ipynb — LangChain Framework Fundamentals
- Objectives: Introduce core components, pipelines, and manufacturing scenario.
- Sections: ecosystem overview, loaders, prompt templates, chains, manufacturing quickstart.
- Lab: Connect to synthetic SOP dataset and build first chain.

### 02_message_structures.ipynb — Conversational Context Management
- Objectives: Use `AIMessage`, `HumanMessage`, `SystemMessage`, multi-lingual prompts.
- Sections: message object anatomy, translation guardrails, batch messaging.
- Lab: Design bilingual system instruction for EHS inspections.

### 03_prompt_templates_chains.ipynb — Prompt Engineering with LCEL
- Objectives: Build templated prompts, Jinja expressions, dynamic variables.
- Sections: templating patterns, plant-specific context injection, template testing harness.
- Lab: Compose chain linking safety policy + technician question.

### 04_runnable_sequences.ipynb — Orchestrating Workflows
- Objectives: Compose sequential/parallel runnables, error handling, retries.
- Sections: runnables overview, router vs map, fallback strategies.
- Lab: Implement fallback to bilingual template when translation confidence < threshold.

### 05_document_loaders.ipynb — Data Ingestion Playbook
- Objectives: Demonstrate PDF, CSV, HTML, and custom loader for maintenance logs.
- Sections: loader catalog, metadata enrichment, compliance filtering.
- Lab: Build loader that redacts PII before ingestion.

### 06_vector_databases.ipynb — Embedding Stores Comparison
- Objectives: Evaluate Chroma vs FAISS vs pgvector for plant data.
- Sections: evaluation metrics, ingestion pipeline, cost/performance table.
- Lab: Populate both stores and benchmark query latency.

### 07_advanced_rag_patterns.ipynb — Multi-Stage Retrieval Strategies
- Objectives: Multi-query expansion, hierarchical retrieval, domain-specific heuristics.
- Sections: multi-query generation, context weighting, manufacturing heuristics.
- Lab: Implement hierarchical retrieval pipeline for SOP sections.

### 08_query_optimization.ipynb — Routing & Transformation Logic
- Objectives: Connect routers, classification, and conditional pipelines.
- Sections: query classifiers, router chains, plant escalation logic.
- Lab: Build router that directs Spanish queries to translated knowledge base.

### 09_query_transformation.ipynb — Decomposition & Rewrite
- Objectives: Use transformers to break down tasks and rephrase queries.
- Sections: question decomposition, follow-up question synthesis, audit logging.
- Lab: Implement `HypotheticalDocumentEmbedder` for synthetic answers.

### 10_rag_fusion_reranking.ipynb — Scoring & Rerankers
- Objectives: Score fusion, cross-encoder rerankers, evaluation harness.
- Sections: reciprocal rank fusion, Cohere/Transformers rerankers, calibration.
- Lab: Compare reranking uplift using maintenance question set.

### 11_langgraph_introduction.ipynb — State Graph Basics
- Objectives: Build LangGraph state machine for maintenance triage.
- Sections: LangGraph fundamentals, nodes/edges, state persistence.
- Lab: Create base graph with ingestion, reasoning, and response nodes.

### 12_building_agents.ipynb — ReAct & Tool Use
- Objectives: Implement ReAct agent with manufacturing toolset.
- Sections: tool design, memory integration, guardrails.
- Lab: Connect to spare-part lookup API mock and demonstrate reasoning trace.

### 13_agentic_tools.ipynb — Custom Tooling & Multi-Tool Agents
- Objectives: Register custom async tools, manage dependencies, retries.
- Sections: tool wrappers, concurrency, failure handling.
- Lab: Build observation logging tool writing to governance dashboard.

### 14_agent_state_management.ipynb — Session Persistence
- Objectives: Manage agent memory, checkpointing, multi-agent coordination.
- Sections: memory strategies, vectorstore-backed memory, cross-shift handover.
- Lab: Persist agent scratchpad to Redis mock and restore session.

### 15_corrective_rag.ipynb — Self-Checking & CRAG Patterns
- Objectives: Implement grading, self-correction, and escalation flows.
- Sections: grader chains, CRAG loops, audit log integration.
- Lab: Add automatic SME escalation when confidence < policy threshold.

---

## Shared Assets to Reuse
- Synthetic manufacturing datasets from Weeks 05-06 and 09-10 (`data/` folder expected).
- Governance utilities (PII filters, audit log writers) to keep compliance narrative.
- Plant configuration YAMLs for environment-specific toggles.

## Deliverables
- 15 notebooks (`01_…` through `15_…`) under `week-07-08-langchain-agents/`.
- Each notebook includes scenario, objectives, code, governance tables, lab assignment, checklist, references.
- Ensure bilingual (English/Spanish) examples appear in conversation-focused notebooks.
