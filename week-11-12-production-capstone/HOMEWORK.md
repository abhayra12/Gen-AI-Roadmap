# 📝 Homework Assignment - Week 11-12: The Manufacturing Copilot Capstone

**Module:** Production Deployment & Capstone Project  
**Due:** End of Week 12  
**Points:** 200 (This is your final project and grade)

---

## 🎯 Assignment: Build and Deploy the Manufacturing Copilot

This is your final assignment: to build, test, and deploy a production-grade version of the **Manufacturing Copilot**. You will integrate all the skills you've learned throughout this course—from MLOps and FastAPI to Docker, Terraform, and Kubernetes—into a single, comprehensive application.

Refer to the main **[CAPSTONE_PROJECT.md](../CAPSTONE_PROJECT.md)** file for the complete, detailed implementation guide.

---

## 🏭 Project Overview

**Title:** The Manufacturing Copilot

**Description:** A multi-agent AI system designed for the factory floor that:
-   Performs **visual quality inspection** on parts using a vision model.
-   Provides **maintenance Q&A** by retrieving information from technical documents (RAG).
-   Generates **structured reports** in multiple languages using a fine-tuned model.
-   **Orchestrates** these skills into complex workflows using LangGraph.

**Real-World Impact:** This tool is designed to reduce manufacturing defects, decrease machine downtime, and provide critical support for factory floor technicians.

---

## 📊 Project Requirements

### Core Application Features (Must-Have)
1.  **Vision Agent:** Detects defects in images of manufactured parts.
2.  **RAG Agent:** Answers questions based on a knowledge base of SOPs and manuals.
3.  **Report Generation Agent:** Creates multi-lingual summaries and reports.
4.  **Agent Orchestration:** A LangGraph workflow that routes tasks to the correct agent.
5.  **REST API:** A robust FastAPI application to expose the copilot's functionality.
6.  **Database:** PostgreSQL for structured data and ChromaDB for vector storage.

### Production & MLOps Features (Must-Have)
1.  **Docker:** A multi-stage `Dockerfile` for containerizing the FastAPI application.
2.  **Infrastructure as Code (IaC):** Terraform scripts to provision all necessary GCP resources.
3.  **CI/CD Pipeline:** A GitHub Actions workflow that automatically tests and deploys the application.
4.  **Cloud Deployment:** The application must be live and accessible on GCP Cloud Run.
5.  **Monitoring & Logging:** Prometheus metrics and structured logs to monitor application health.
6.  **Testing:** A suite of unit and integration tests with good coverage.

---

## 📋 High-Level Implementation Plan

This is a two-week intensive project. Manage your time carefully.

### Week 11: Core Application Development
-   **Days 1-2: Foundation & Architecture:** Set up your project structure, database schemas, and overall application design.
-   **Days 3-4: RAG Agent Implementation:** Build the document processing pipeline, set up the vector database, and create the Q&A agent.
-   **Days 5-6: Vision & Report Agents:** Integrate the vision model for defect detection and the fine-tuned model for report generation.
-   **Day 7: Agent Orchestration:** Build the main LangGraph workflow that connects all the agents.

### Week 12: Deployment & Productionalization
-   **Days 8-9: API Development & Containerization:** Build the FastAPI endpoints and create the `Dockerfile`.
-   **Days 10-11: Infrastructure as Code:** Write the Terraform scripts to define your GCP infrastructure.
-   **Day 12: CI/CD Pipeline:** Create the GitHub Actions workflow for automated testing and deployment.
-   **Day 13: Deployment & Monitoring:** Deploy the application to GCP, set up monitoring dashboards, and conduct load testing.
-   **Day 14: Final Touches & Presentation Prep:** Finalize your documentation, record your demo video, and prepare for your presentation.

---

## 🎯 Grading Rubric (200 points)

### Functionality (60 points)
-   **Vision Agent (15 pts):** Accurately detects defects.
-   **RAG Agent (15 pts):** Retrieves relevant, correct information.
-   **Report Agent (10 pts):** Generates accurate, multi-lingual reports.
-   **Orchestration (20 pts):** The LangGraph workflow correctly routes tasks and manages state.

### Code & Architecture Quality (40 points)
-   **Architecture (10 pts):** Clean, modular, and scalable design.
-   **Code Style (10 pts):** Follows best practices (PEP8, type hints, docstrings).
-   **Testing (10 pts):** High test coverage for critical components.
-   **Documentation (10 pts):** Thorough `README.md`, API docs, and code comments.

### Production Readiness (50 points)
-   **Docker (10 pts):** Optimized, multi-stage Dockerfile.
-   **CI/CD (10 pts):** Reliable, automated pipeline in GitHub Actions.
-   **Cloud Deployment (15 pts):** Application is successfully deployed and running on GCP.
-   **Monitoring (10 pts):** Dashboards and alerts are configured.
-   **Security (5 pts):** Secrets are managed securely, not hardcoded.

### Innovation & Problem Solving (20 points)
-   Creative solutions to domain-specific challenges.
-   Thoughtful implementation of extra features or optimizations.

### Final Presentation & Demo (30 points)
-   **Live Demo (15 pts):** A clear, end-to-end demonstration of the working application.
-   **Documentation (10 pts):** The project is well-documented and easy to understand.
-   **Q&A (5 pts):** Ability to confidently answer questions about your project.

---

## 📦 Submission Requirements

1.  **GitHub Repository:** A public repository containing all your source code, configuration files, tests, and documentation.
2.  **Live Deployment URL:** A publicly accessible URL for your deployed Manufacturing Copilot application on GCP.
3.  **Demo Video:** A 5-10 minute video that walks through your application's features, architecture, and code.

---

## ✅ Final Checklist

-   [ ] All core features of the Manufacturing Copilot are implemented and working.
-   [ ] The application is fully containerized with Docker.
-   [ ] The infrastructure is defined in Terraform.
-   [ ] The CI/CD pipeline in GitHub Actions is passing.
-   [ ] The application is deployed and accessible on GCP.
-   [ ] Monitoring is active and capturing metrics.
-   [ ] The project is thoroughly documented.
-   [ ] The demo video is recorded and ready for submission.

---

**This capstone is your opportunity to build a project that showcases the full range of your Generative AI engineering skills. Good luck, and build something amazing!** 🚀

---

<div align="center">

**Week 11-12 Capstone** | The Manufacturing Copilot | From Concept to Production

[📖 View Full Capstone Guide](../CAPSTONE_PROJECT.md) | [🏠 Return to Course Home](../README.md)

</div>
