# 🏭 Capstone Project: The Manufacturing Copilot
### A Production-Grade, Multi-Agent AI System for Smart Manufacturing

---

## 🎯 Project Overview

This capstone project is the culmination of the Gen AI Masters Program, where you will apply every skill you've learned to build and deploy a **Manufacturing Copilot**. This is an intelligent, multi-agent system designed to solve high-value problems in a smart factory environment: improving quality control, streamlining maintenance, and automating reporting.

### Core Features You Will Build:
- **Visual Quality Inspection Agent:** An agent that leverages a Vision-Language Model (VLM) to analyze images of products on an assembly line and automatically identify manufacturing defects.
- **RAG-Powered Maintenance Agent:** An agent that acts as an expert assistant for factory technicians. It answers complex technical questions by retrieving information from a knowledge base of maintenance manuals, technical schematics, and standard operating procedures (SOPs).
- **Automated Reporting Agent:** An agent that uses a fine-tuned language model to generate structured, multi-lingual daily production reports, summarizing key metrics and incidents.
- **Agentic Orchestrator:** A central "brain" built with LangGraph that manages the entire workflow. It intelligently routes tasks to the appropriate agent, manages state, and orchestrates complex sequences of operations to fulfill a user's request.

### Why This Project is a Career-Defining Portfolio Piece:
- **Industry-Relevant:** It solves real-world, high-impact challenges in the rapidly growing smart manufacturing sector.
- **Portfolio-Defining:** It demonstrates a complete, end-to-end skill set, from initial data processing and model fine-tuning to robust cloud deployment and monitoring.
- **Production-Grade:** The final application is not just a demo. It is a containerized, monitored, and fully deployed system managed by a professional CI/CD pipeline, showcasing your ability to ship real-world AI products.

---

## 🛠️ Technical Architecture

The system is designed using a modular, microservices-oriented architecture. A central LangGraph-based orchestrator manages the flow of information and tasks between specialized agents, all exposed via a secure FastAPI backend.

### High-Level System Diagram
```
┌─────────────────────────────────────────────────────────────┐
│                   User Interface / API Client                │
│              (e.g., Streamlit, Postman, cURL)                │
└───────────────────────┬─────────────────────────────────────┘
                        │ (Secure HTTP Requests)
┌───────────────────────▼─────────────────────────────────────┐
│                FastAPI Backend (`capstone_project/app`)      │
│  (API Gateway, Authentication, Request/Response Handling)    │
└───────────────────────┬─────────────────────────────────────┘
                        │ (Internal Python Function Calls)
┌───────────────────────▼─────────────────────────────────────┐
│          Agent Orchestrator (`app/agents.py` w/ LangGraph)   │
│ (Manages State, Routes Tasks, Coordinates Agent Execution)   │
└───────────────────────┬─────────────────────────────────────┘
                        │ (Delegates to Specialized Agents)
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Vision Agent │ │   RAG Agent  │ │ Report Agent │
│ (Uses VLM)   │ │ (Uses LLM)   │ │ (Uses LLM)   │
└──────────────┘ └──────────────┘ └──────────────┘
        │               │               │
        └───────────────┼───────────────┘
                        │ (Interacts with External Models/Services)
        ┌───────────────▼───────────────┐
        │      External Services & Data Stores        │
        │ ┌───────────────────────────┐ │
        │ │   HuggingFace Models      │ │
        │ ├───────────────────────────┤ │
        │ │   Vector DB (ChromaDB)    │ │
        │ ├───────────────────────────┤ │
        │ │   PostgreSQL (Logging)    │ │
        │ └───────────────────────────┘ │
        └───────────────────────────────┘
```

### Core Components Explained:
- **FastAPI Backend:** Serves as the robust, asynchronous main entry point for the application. It handles all incoming API requests, performs data validation using Pydantic, and manages security.
- **LangGraph Orchestrator:** This is the "brain" of the system. It's a stateful graph that receives requests from the API layer and intelligently routes them to the appropriate agent or sequence of agents based on the task.
- **Specialized Agents:** Each agent is a self-contained Python class responsible for a specific capability (vision, RAG, reporting). They are designed to be modular and are called by the orchestrator.
- **External Services:** The agents interact with a suite of external services, including HuggingFace for accessing pre-trained and fine-tuned models, ChromaDB for efficient vector storage and retrieval, and PostgreSQL for structured data logging and monitoring.

---

## 🚀 Development & Deployment Lifecycle (MLOps in Practice)

This project is built and deployed using modern MLOps best practices, ensuring that the final product is robust, scalable, and maintainable. The notebooks in the `week-11-12` module serve as detailed conceptual guides for each of these critical steps.

### 1. API Development (`capstone_project/app`)
- A high-performance, asynchronous FastAPI application serves as the backend.
- Pydantic models are used extensively for strict data validation and to auto-generate API documentation.
- Clear API endpoints are defined for each core feature: `/inspect` (for visual inspection), `/query` (for the RAG agent), and `/generate-report`.

### 2. Containerization (`capstone_project/Dockerfile`)
- The entire application, including all its dependencies, is packaged into a lightweight Docker container.
- A multi-stage `Dockerfile` is used to create a lean, optimized, and secure production image.
- A `docker-compose.yml` file is provided for easy local development and testing of the full stack, including the API, database, and other services.

### 3. Infrastructure as Code (IaC) (`capstone_project/terraform`)
- All required cloud infrastructure (e.g., GCP Cloud Run for serving, Secret Manager for secrets, and Google Cloud Storage for artifacts) is defined declaratively using Terraform.
- This ensures that your infrastructure is reproducible, version-controlled, and can be managed as code.
- The Terraform configuration is highly modular, with separate modules for different services, promoting reusability and maintainability.

### 4. CI/CD (`capstone_project/.github/workflows`)
- GitHub Actions are used to create a complete Continuous Integration and Continuous Deployment pipeline.
- **CI (`ci.yml`):** On every push or pull request to the repository, the CI pipeline automatically runs linters, static analysis, and a full suite of unit and integration tests.
- **CD (`deploy.yml`):** On a push to the `main` branch, the CD pipeline automatically builds the production Docker image, pushes it to a container registry (like Google Artifact Registry), and deploys the new version to the cloud with zero downtime.

### 5. Orchestration & Scalability (`capstone_project/charts`)
- For advanced, large-scale deployments, a Helm chart is provided.
- This allows the application to be easily deployed, managed, and scaled on a Kubernetes cluster (like Google Kubernetes Engine - GKE).

---

## 🧪 A Robust Testing Strategy

A comprehensive testing strategy is crucial for ensuring the reliability and correctness of the application.

- **Unit Tests (`capstone_project/tests`):** Each function, class, and agent is tested in isolation to verify its logic.
- **Integration Tests:** The interactions between different components (e.g., the API layer and the agent orchestrator) are tested to ensure they work together as expected.
- **Static Analysis & Linting:** Code quality and security are maintained using tools like CodeQL and linters, which are integrated directly into the CI pipeline to catch issues early.

---

## 🎯 The Final Goal

The final deliverable of this program is not just a collection of experimental notebooks, but a **single, cohesive, and fully deployed application** located in the `capstone_project` directory. This project serves as definitive proof of your ability to go beyond theory and experimentation to design, build, and ship production-ready Generative AI solutions.
