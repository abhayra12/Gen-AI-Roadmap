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
- **Scenario:** Global manufacturing conglomerate standardizes ML lifecycle for maintenance copilots across 6 plants.
- **Key Sections:**
  - Lifecycle diagram aligning data → model → deployment → monitoring
  - Versioning strategy: Git, DVC, model registry (Weights & Biases / MLflow)
  - Audit-readiness checklist (SOX, ISO 9001) capturing metadata per release
  - Tooling stack comparison table (MLflow vs. Vertex AI vs. Azure ML) with manufacturing constraints
  - Hands-on: Build MLflow experiment, log params/metrics, register model tagged by plant
- **Lab:** Generate an MLOps readiness scorecard for the capstone team.

## Notebook 02 · FastAPI Serving for RAG & Vision Agents
- **Scenario:** Expose a unified maintenance + quality assistant via FastAPI with multilingual endpoints.
- **Key Sections:**
  - API design contract (OpenAPI snippet) covering text RAG, vision classification, health checks
  - Dependency injection for async retrieval and GPU-bound inference
  - Input validation (Pydantic models) enforcing plant-level RBAC metadata
  - Streaming responses for long-running analyses (Server-Sent Events)
  - Integration tests using `httpx.AsyncClient`
- **Lab:** Extend API with audit trail middleware logging user ID, equipment ID, latency.

## Notebook 03 · Dockerizing GenAI Pipelines
- **Scenario:** Containerize the FastAPI service + worker for plant edge deployments with flaky connectivity.
- **Key Sections:**
  - Multi-stage Dockerfile (base image, deps, runtime) with vulnerability scan steps
  - Environment variable handling (secrets mount, config files, .env)
  - GPU vs. CPU build variants (nvidia container toolkit hints)
  - Local compose file wiring API + worker + Redis + Postgres for caching/logging
  - Image hardening checklist (non-root user, read-only FS, healthcheck)
- **Lab:** Create a docker-compose override for staging vs. production.

## Notebook 04 · Monitoring & Logging for Production Copilots
- **Scenario:** Deploy monitoring stack combining Prometheus, Grafana, and structured logging to track hallucinations, latency, and cost.
- **Key Sections:**
  - Metrics taxonomy (business KPIs, model metrics, infra metrics)
  - Prometheus instrumentation example (FastAPI middleware exporting latency/accuracy)
  - Structured JSON logging to ELK/OpenSearch with correlation IDs
  - Alerting rules (PagerDuty/Teams) for error spikes or drift warnings
  - Observability dashboard template (Grafana JSON) highlighting plant-level metrics
- **Lab:** Implement a synthetic alert scenario and generate incident runbook entry.

## Notebook 05 · CI/CD with GitHub Actions & Quality Gates
- **Scenario:** Automate testing, security scanning, and staged deployments for the GenAI services.
- **Key Sections:**
  - Workflow YAML with jobs: lint/test, build image, security scan (Trivy), deploy to staging
  - Matrix testing for Python 3.10/3.11 and Windows/Linux clients
  - Branch protection + approval process for regulated plants
  - Secrets management best practices (GitHub OIDC to GCP secrets)
  - Evidence collection for audits (upload artifacts, test summaries)
- **Lab:** Build a PR checklist requiring model card update and runbook changes.

## Notebook 06 · GCP Deployment (Cloud Run & Cloud Storage)
- **Scenario:** Deploy API + background workers to GCP Cloud Run, integrate with Cloud Storage for embedding documents.
- **Key Sections:**
  - Infrastructure diagram bridging VPC, Cloud SQL, Cloud Storage, Cloud Run
  - `gcloud` deployment commands (use placeholders, focus on IAM roles, service accounts)
  - Secrets + key management (Secret Manager, CMEK for storage)
  - Traffic splitting for canary releases (Cloud Run revisions)
  - Budget monitoring + cost optimization tips for GPU/TPU resources
- **Lab:** Write a deployment runbook with rollback plan and smoke test steps.

## Notebook 07 · Terraform Infrastructure as Code
- **Scenario:** Provision multi-region infrastructure for redundancy (APAC + EMEA plants).
- **Key Sections:**
  - Terraform project structure (`providers.tf`, `main.tf`, `variables.tf`, `outputs.tf`)
  - Modules for Cloud Run, Pub/Sub, Cloud SQL, Cloud Storage
  - State management with Terraform Cloud or GCS backend
  - Policy as code (OPA/Conftest) enforcing naming conventions and tagging for plants
  - Drift detection workflow (terraform plan in CI + approvals)
- **Lab:** Implement a Terraform module skeleton and run `terraform plan` (mock output) capturing cost estimation.

## Notebook 08 · Kubernetes Orchestration & Autoscaling
- **Scenario:** For plants requiring on-prem clusters, deploy the assistant on GKE / AKS with GPU nodes.
- **Key Sections:**
  - Kubernetes manifests: Deployment, Service, Ingress, HPA, PodDisruptionBudget
  - Helm chart snippet with values for stage/prod (resource requests, secrets)
  - Autoscaling strategies (HPA on custom metrics, KEDA with queue depth)
  - Service mesh considerations (Istio) for zero-trust and mutual TLS
  - Disaster recovery playbook: backup/restore of vector store + config
- **Lab:** Configure a blue/green deployment YAML and simulate a rollout status check.

---

## Cross-Notebook Integration
- Reuse `/common` utilities for logging, evaluation metrics, config management.
- Maintain consistent dataset references (maintenance logs, inspection images stored in `data/`)
- Each notebook updates the capstone tracker (e.g., `capstone-progress.csv`) with its outputs.
- Provide connectors to existing Week 09-10 artifacts (model weights, adapters) for inferencing.

---

## Dependencies & Tooling
- New Python packages likely required: `fastapi`, `uvicorn`, `httpx`, `prometheus-client`, `structlog`, `python-json-logger`, `google-cloud-run`, `google-cloud-storage`, `google-cloud-secret-manager`, `apache-beam` (optional), `paramiko` (for on-prem automation), `python-terraform` (if scripting).
- CLI tools referenced: `docker`, `gcloud`, `terraform`, `kubectl`, `helm` (document installation instructions and placeholders).

---

## Deliverables & Next Steps
1. Validate this blueprint with curriculum lead / capstone mentors.
2. Generate shared assets: Grafana dashboards, Terraform module templates, CI workflow skeletons.
3. Begin drafting Notebook 01 with MLflow lifecycle walkthrough + readiness scorecard.
4. Track open questions (GPU quotas, secret naming conventions) in `PROGRESS_TRACKER.md`.
