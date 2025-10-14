# Week 11-12 Notebook Blueprint · Production Deployment & Capstone

**Audience:** Manufacturing AI engineers ready to ship their GenAI copilots to production across multi-plant operations.

**Guiding Theme:** Every notebook mirrors the steps of taking the Week 09-10 tuned models + Week 05-08 RAG stack into production with enterprise-grade governance.

Each notebook must include:
- Learning objectives + business impact summary
- Factory narrative (specific plant, stakeholders, constraints)
- Hands-on code blocks (prefer FastAPI, Terraform, GitHub Actions, monitoring libraries)
- Operational checklists (security, compliance, change management)
- Lab assignment tied to capstone deliverables
- References to prior weeks & external docs

---

## Notebook 01 · MLOps Fundamentals for GenAI in Manufacturing
- **Scenario:** A global manufacturing conglomerate standardizes the ML lifecycle for its "Manufacturing Copilot" across multiple plants.
- **Key Sections:**
  - End-to-end lifecycle diagram: Data Ingestion → Model Tuning → Deployment → Monitoring.
  - Versioning strategy for code (Git), data (DVC), and models (MLflow/Vertex AI Model Registry).
  - Audit-readiness checklist for manufacturing standards (e.g., ISO 9001), capturing metadata for each release.
  - Tooling stack comparison: MLflow vs. Vertex AI vs. Azure ML, with a focus on manufacturing constraints.
  - Hands-on: Build an MLflow experiment, log parameters and metrics, and register a model tagged by plant and production line.
- **Lab:** Generate an MLOps readiness scorecard for the capstone project.

## Notebook 02 · FastAPI Serving for RAG & Vision Agents
- **Scenario:** Expose a unified "Manufacturing Copilot" API, serving both the maintenance RAG and quality control vision agents.
- **Key Sections:**
  - API design contract using OpenAPI for text-based RAG, vision classification, and health checks.
  - Dependency injection for asynchronous data retrieval and GPU-bound model inference.
  - Input validation with Pydantic models to enforce plant-level Role-Based Access Control (RBAC).
  - Streaming responses for long-running analyses using Server-Sent Events (SSE).
  - Integration testing with `httpx.AsyncClient`.
- **Lab:** Extend the API with an audit trail middleware that logs user ID, equipment ID, and request latency.

## Notebook 03 · Dockerizing GenAI Pipelines
- **Scenario:** Containerize the FastAPI service and its associated workers for deployment at the plant edge, accounting for intermittent network connectivity.
- **Key Sections:**
  - Multi-stage Dockerfile (base image, dependencies, runtime) including vulnerability scanning steps.
  - Secure handling of environment variables using secrets mounts, config files, and `.env`.
  - Build variants for CPU vs. GPU deployments, with notes on the NVIDIA Container Toolkit.
  - Local development setup using a `docker-compose.yml` file to wire the API, worker, Redis, and Postgres.
  - Image hardening checklist: non-root user, read-only filesystem, and health checks.
- **Lab:** Create a `docker-compose.override.yml` for staging vs. production environments.

## Notebook 04 · Monitoring & Logging for Production Copilots
- **Scenario:** Deploy a monitoring stack with Prometheus, Grafana, and structured logging to track model performance (e.g., hallucinations), latency, and operational costs.
- **Key Sections:**
  - Metrics taxonomy covering business KPIs, model metrics (accuracy, drift), and infrastructure metrics (CPU/GPU usage).
  - Prometheus instrumentation using FastAPI middleware to export latency and custom business metrics.
  - Structured JSON logging to an ELK/OpenSearch stack with correlation IDs for traceability.
  - Alerting rules configured to notify via PagerDuty or Microsoft Teams for error spikes or performance degradation.
  - A pre-built Grafana dashboard template for visualizing plant-level metrics.
- **Lab:** Implement a synthetic alert scenario and create a corresponding incident runbook entry.

## Notebook 05 · CI/CD with GitHub Actions & Quality Gates
- **Scenario:** Automate testing, security scanning, and staged deployments for the "Manufacturing Copilot" services.
- **Key Sections:**
  - GitHub Actions workflow (`.github/workflows/main.yml`) with jobs for linting, testing, building images, security scanning (Trivy), and deploying to a staging environment.
  - Matrix testing for different Python versions (3.10, 3.11) and client operating systems.
  - Branch protection rules and approval processes for regulated plant environments.
  - Secrets management using GitHub OIDC to securely connect to GCP Secret Manager.
  - Evidence collection for audits by uploading test summaries and other artifacts.
- **Lab:** Build a pull request checklist that requires updates to the model card and runbook.

## Notebook 06 · GCP Deployment (Cloud Run & Cloud Storage)
- **Scenario:** Deploy the "Manufacturing Copilot" API and background workers to GCP Cloud Run, integrating with Cloud Storage for documents and embeddings.
- **Key Sections:**
  - Infrastructure diagram showing the architecture: VPC, Cloud SQL, Cloud Storage, and Cloud Run.
  - Deployment commands using `gcloud`, with a focus on IAM roles and service accounts.
  - Secrets and key management using Google Secret Manager and Customer-Managed Encryption Keys (CMEK) for storage.
  - Traffic splitting for canary releases using Cloud Run revisions.
  - Budget monitoring and cost optimization strategies for GPU/TPU resources.
- **Lab:** Write a deployment runbook that includes a rollback plan and smoke test procedures.

## Notebook 07 · Terraform Infrastructure as Code
- **Scenario:** Provision multi-region infrastructure for the "Manufacturing Copilot" to ensure high availability for plants in different geographical regions (e.g., APAC and EMEA).
- **Key Sections:**
  - Terraform project structure: `providers.tf`, `main.tf`, `variables.tf`, `outputs.tf`.
  - Reusable modules for Cloud Run, Pub/Sub, Cloud SQL, and Cloud Storage.
  - State management using a GCS backend or Terraform Cloud.
  - Policy as Code (PaC) with Open Policy Agent (OPA)/Conftest to enforce naming conventions and tagging for cost allocation.
  - Drift detection workflow using `terraform plan` in a CI pipeline with manual approvals.
- **Lab:** Implement a skeleton Terraform module and run `terraform plan` to capture the estimated cost.

## Notebook 08 · Kubernetes Orchestration & Autoscaling
- **Scenario:** Deploy the "Manufacturing Copilot" to a GKE/AKS cluster with GPU nodes for plants that require on-premise or specialized hardware.
- **Key Sections:**
  - Kubernetes manifests: Deployment, Service, Ingress, Horizontal Pod Autoscaler (HPA), and PodDisruptionBudget.
  - Helm chart for templating configurations across different environments (staging, production).
  - Autoscaling strategies: HPA on custom metrics and KEDA for scaling based on queue depth.
  - Service mesh considerations (e.g., Istio) for implementing zero-trust security and mutual TLS.
  - Disaster recovery playbook for backing up and restoring the vector store and application configuration.
- **Lab:** Configure a blue/green deployment YAML and simulate a rollout status check.

---

## Cross-Notebook Integration
- Reuse common utilities from a `/common` directory for logging, evaluation, and configuration management.
- Maintain consistent dataset references (e.g., maintenance logs, inspection images) stored in a `data/` directory.
- Each notebook updates a central progress tracker (e.g., `capstone-progress.csv`) with its key outputs.
- Provide connectors to the fine-tuned models and adapters from Week 09-10 for inference.

---

## Dependencies & Tooling
- **Python Packages:** `fastapi`, `uvicorn`, `httpx`, `prometheus-client`, `structlog`, `python-json-logger`, `google-cloud-run`, `google-cloud-storage`, `google-cloud-secret-manager`, `apache-beam` (optional), `paramiko` (for on-prem automation), `python-terraform`.
- **CLI Tools:** `docker`, `gcloud`, `terraform`, `kubectl`, `helm`. Ensure installation instructions and version placeholders are documented.

---

## Deliverables & Next Steps
1.  Validate this blueprint with the curriculum lead and capstone mentors.
2.  Generate shared assets: Grafana dashboard templates, Terraform modules, and CI workflow skeletons.
3.  Begin drafting Notebook 01 with the MLflow lifecycle walkthrough and readiness scorecard.
4.  Track open questions (e.g., GPU quotas, secret naming conventions) in `PROGRESS_TRACKER.md`.
