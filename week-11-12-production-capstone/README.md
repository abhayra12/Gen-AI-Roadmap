# 📖 Week 11-12: Production & Deployment

**Capstone: Production & Deployment**  
**Goal:** Take everything you've learned and build a single, production-grade, end-to-end AI application.

---

## 📚 Module Overview

This is the final module, where you transition from a student to a builder. You will take all the individual skills you've acquired—from RAG to fine-tuning to agentic design—and integrate them into a single, cohesive, deployed application. The notebooks in this module are conceptual guides; the actual implementation happens in the `capstone_project` directory.

### Learning Objectives
By the end of this module, you will have hands-on experience with:
- ✅ The complete MLOps lifecycle, from development to production.
- ✅ Serving your AI application via a robust FastAPI backend.
- ✅ Containerizing your application with Docker for portability.
- ✅ Implementing a full CI/CD pipeline with GitHub Actions for automated testing and deployment.
- ✅ Defining and managing your cloud infrastructure as code using Terraform.
- ✅ Deploying your application to a scalable cloud service like GCP Cloud Run.
- ✅ Orchestrating complex applications with Kubernetes and Helm (Advanced).

---

## 📓 Conceptual Notebooks & The Capstone Project

The eight notebooks in this module serve as **conceptual guides** for the tasks you will perform to build and deploy the final capstone project. All the code you write will be part of the final project located in the top-level `capstone_project/` directory.

| Notebook                            | Concept Covered                     | Corresponding Capstone Component | Status |
|-------------------------------------|-------------------------------------|----------------------------------|--------|
| `01_mlops_fundamentals.ipynb`       | MLOps Principles                    | Entire `capstone_project`        | ✅     |
| `02_fastapi_ml_serving.ipynb`       | API Development                     | `capstone_project/app/`          | ✅     |
| `03_docker_containerization.ipynb`  | Containerization                    | `capstone_project/Dockerfile`    | ✅     |
| `04_monitoring_logging.ipynb`       | Observability                       | `capstone_project/app/monitoring`| ✅     |
| `05_cicd_github_actions.ipynb`      | CI/CD Automation                    | `capstone_project/.github/`      | ✅     |
| `06_gcp_deployment.ipynb`           | Cloud Deployment                    | `capstone_project/scripts/`      | ✅     |
| `07_terraform_iac.ipynb`            | Infrastructure as Code              | `capstone_project/terraform/`    | ✅     |
| `08_kubernetes_orchestration.ipynb` | Orchestration (Advanced) ⭐         | `capstone_project/charts/` + `kubernetes/` | ✅ **Production-Ready** |

> ⭐ **NEW**: The capstone project now includes **complete production-ready Kubernetes deployment**!
> - 📦 Helm charts in `capstone_project/charts/manufacturing-copilot/`
> - 📋 Plain manifests in `capstone_project/kubernetes/`
> - 🚀 Deployment scripts: `deploy-k8s.sh` and `deploy-k8s.ps1`
> - 📖 Full guide: `capstone_project/KUBERNETES_DEPLOYMENT.md`

---

## 🚀 The Capstone Project: Manufacturing Copilot

This is the culmination of the entire course. You will build a multi-agent AI system for the manufacturing domain, integrating all the techniques you have learned.

- **For the full project brief, architecture, and requirements, see the main `CAPSTONE_PROJECT.md` file in the root directory.**

---

## 🎓 Final Assessment

Your work will be assessed based on the final state of your `capstone_project` and a live presentation. This includes the functionality of the deployed application, the quality of your code, the robustness of your infrastructure, and your documentation.

**Congratulations on making it to the final module. It's time to build and ship!** 🚀
