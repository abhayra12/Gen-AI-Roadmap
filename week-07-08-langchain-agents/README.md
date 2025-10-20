# 📖 Week 7-8: LangChain, Agents, & Advanced RAG

**Phase 4: Agents & Advanced RAG**  
**Goal:** Build complex, multi-step AI applications and autonomous agents using high-level frameworks like LangChain and LangGraph.

---

## 📚 Module Overview

This module is about orchestration. You will move beyond single-shot Q&A to build sophisticated applications that can reason, plan, and use tools to accomplish complex tasks. You will master LangChain for rapid application development and LangGraph for creating robust, stateful, and even multi-agent systems.

### Learning Objectives
By the end of this module, you will be able to:
- ✅ Compose complex AI workflows using the LangChain Expression Language (LCEL).
- ✅ Implement advanced RAG patterns like query transformation, routing, and re-ranking.
- ✅ Understand and build with LangGraph to create cyclical, stateful AI graphs.
- ✅ Design and implement AI agents that can use tools (e.g., search, code execution) to solve problems.
- ✅ Build a multi-agent system where different agents collaborate to achieve a goal.
- ✅ Implement cutting-edge techniques like Corrective RAG (CRAG) for self-improving systems.

---

## 📓 Notebooks & Concepts

This module contains an extensive set of 16 notebooks covering LangChain, advanced RAG, and agentic AI with LangGraph:

| Area                  | Notebooks                               | Key Concepts                                       |
|-----------------------|-----------------------------------------|----------------------------------------------------|
| **LangChain Core**    | `01` - `04`                             | LCEL, Prompt Templates, Chains, Runnables          |
| **Advanced RAG**      | `05` - `10`                             | Document Loaders, Vector DBs, Query Transformation, RAG Fusion, Re-ranking |
| **Agentic AI**        | `11` - `16`                             | LangGraph, State Management, Tool Use, MCP, Multi-Agent Systems, CRAG |

**NEW**: Notebook `16` introduces **Model Context Protocol (MCP)**, Anthropic's standard for connecting LLMs to external tools and data sources in a production-ready, reusable way.

---

## 📝 Homework: Multi-Agent Data Analysis System

**Objective:** Build a collaborative multi-agent system to perform data analysis.

**Task:**
Create a system with at least two agents (e.g., a "Data Analyst Agent" and a "Visualization Agent") that work together. The system should be able to take a dataset and a high-level user query, perform analysis, and generate both textual insights and a data visualization.

- **Instructions:** See the `HOMEWORK.md` file in this directory for detailed instructions.

---

## 🎯 What's Next?

You've learned to build intelligent systems that can retrieve knowledge and take action. Now it's time to learn how to create and customize the models themselves in **Week 9-10: Training & Fine-Tuning**. You will dive deep into the mechanics of model training and learn how to adapt pre-trained models to your specific needs.

**Let's build autonomous agents!** 🤖
