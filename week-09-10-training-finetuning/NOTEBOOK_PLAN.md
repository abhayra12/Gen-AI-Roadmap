# Week 09-10 Notebook Blueprint · Model Training & Fine-tuning

**Audience:** Manufacturing AI engineers moving from prompt-centric workflows (Weeks 05-08) to custom model adaptation.

**Theme:** Every notebook anchors on a discrete scenario from the factory floor (maintenance, quality, supply chain, or EHS). Each delivers:
- Learning objectives + success criteria
- Manufacturing narrative + dataset guidance
- Code walkthroughs with checkpoints
- Evaluation and governance hooks (safety, cost, compliance)
- Lab assignment or takeaway worksheet

---

## Notebook 01 · Pre-Training Concepts for Manufacturing Corpora
- **Objectives:** Explain masked LM vs. causal LM; curate multi-source manufacturing corpora; quantify data quality.
- **Scenario:** Aggregating 5 years of shift logs, NCRs, and SOP updates to assess readiness for pre-training a maintenance co-pilot.
- **Key Sections:**
  - Data audit checklist (PII, safety-sensitive text, export controls)
  - Token statistics dashboard using `pandas` & `matplotlib`
  - Curriculum design for domain-specific pre-training (core vs. edge cases)
  - Risk register: hallucinations, stale procedures, regulatory leakage
- **Hands-on:** Build a profiling notebook that scores document freshness and coverage vs. critical equipment categories.

## Notebook 02 · Bigram Language Model with Maintenance Logs
- **Objectives:** Implement a bigram LM from scratch; connect n-gram intuition to transformer pre-training.
- **Scenario:** Predictive typing for maintenance technicians entering work orders on a tablet.
- **Key Sections:**
  - Text normalization for units & acronyms ("psi", "℃", "OEE")
  - PyTorch bigram implementation with perplexity tracking
  - Error analysis on jargon-heavy vs. plain-language entries
  - Manufacturing-specific smoothing heuristics (e.g., part numbers)
- **Hands-on:** Students extend the model to trigram, compare perplexity, and document failure modes.

## Notebook 03 · Tensors & GPU Acceleration in Edge Plants
- **Objectives:** Master tensor operations, broadcasting, and efficient GPU usage under constrained hardware.
- **Scenario:** Deploying a fine-tuning job on an on-prem A100 vs. shared RTX 6000 for a tier-2 supplier.
- **Key Sections:**
  - Torch tensor kitchen tour (dtype, device, stride)
  - Mixed precision experiments (FP32 vs. bfloat16) on sample workloads
  - Memory profiling with `torch.cuda.memory_summary()`
  - Downtime mitigation checklist for edge compute in plants
- **Hands-on:** Optimize a matrix multiplication benchmark and report throughput gains + energy savings.

## Notebook 04 · Forward & Backward Pass Diagnostics
- **Objectives:** Visualize gradients, spot vanishing/exploding issues, and tie to control-floor reliability.
- **Scenario:** Fine-tuning a classifier to flag safety incidents; gradients destabilize due to class imbalance.
- **Key Sections:**
  - Manual gradient computation on toy network (pandas trace table)
  - Autograd hooks to log layer-wise gradient norms
  - Exploding gradient remediation (gradient clipping, layer norm)
  - Quality gate: gradient health dashboards before each training shift
- **Hands-on:** Implement callbacks that halt training if gradient variance crosses thresholds.

## Notebook 05 · MLP Implementation for Sensor Fusion
- **Objectives:** Build an MLP in PyTorch; integrate tabular sensor data with textual incident labels.
- **Scenario:** Predicting potential downtime from combined vibration readings and shift notes.
- **Key Sections:**
  - Data loaders blending CSV sensor streams and labeled text embeddings
  - Custom loss functions (weighted BCE) reflecting production costs
  - Feature importance analysis vs. maintenance prioritization
  - Governance: documenting model card for cross-functional review
- **Hands-on:** Students experiment with activation functions and regularization, logging results in MLflow.

## Notebook 06 · Mini-batch Training & Curriculum Scheduling
- **Objectives:** Implement batching, shuffling, and curriculum learning tailored to manufacturing data skew.
- **Scenario:** Few high-severity incidents among many routine logs; need curriculum to stabilize training.
- **Key Sections:**
  - Streaming data loaders for large PDF+CSV corpora
  - Curriculum phases (routine → abnormal → crisis reports)
  - Batch size vs. throughput vs. GPU memory trade-off table
  - Shift hand-off checklist for monitoring training jobs in 24/7 plants
- **Hands-on:** Run ablations swapping curriculum strategies; capture convergence charts.

## Notebook 07 · Fine-tuning vs. RAG Decision Matrix
- **Objectives:** Provide a quantitative framework for choosing adaptation method per use case.
- **Scenario:** PM must decide between RAG upgrade or fine-tuning for warranty-claim automation.
- **Key Sections:**
  - Cost/benefit calculator (data size, latency, compliance risk)
  - Case study comparisons referencing Weeks 05-08 RAG builds
  - Hybrid strategies (fine-tune small adapter + RAG for long-tail knowledge)
  - Stakeholder alignment worksheet (IT, Compliance, Operations)
- **Hands-on:** Students populate decision matrix with their plant data and present recommendation.

## Notebook 08 · PEFT Foundations with PEFT Library
- **Objectives:** Explain adapters, prompt tuning, and their trade-offs; implement PEFT adapters.
- **Scenario:** Upgrading a multilingual maintenance assistant while keeping GPU budget flat.
- **Key Sections:**
  - Overview of PEFT methods (prefix, prompt, adapters) with selection rubric
  - HuggingFace PEFT integration on domain dataset (CSV + context prompts)
  - Latency & memory benchmarking pre/post adapters
  - Change-management checklist for model updates during maintenance freeze periods
- **Hands-on:** Train adapters on bilingual maintenance FAQs and evaluate cross-language accuracy.

## Notebook 09 · LoRA & QLoRA for Cost-Efficient Fine-tuning
- **Objectives:** Dive deep into low-rank adaptation, quantization (4-bit), and manufacturing deployment constraints.
- **Scenario:** Supplier wants LoRA-tuned assistant that runs on a single T4 GPU for remote plants.
- **Key Sections:**
  - LoRA math recap + manufacturing-specific prompt templates
  - QLoRA setup with bitsandbytes, checking quantization error on technical terms
  - Throughput benchmarking before/after quantization
  - Safety gates: ensure torque specs or SOP steps aren’t quantized away
- **Hands-on:** Tune a LoRA adapter on shift reports; deliver latency & accuracy report vs. baseline.

## Notebook 10 · End-to-End Fine-tuning Pipeline (Supervised Instruction Tuning)
- **Objectives:** Build a production-ready pipeline covering data prep, training, evaluation, and packaging.
- **Scenario:** Instruction-tuning a base model to follow plant SOP query formats, with approval workflow.
- **Key Sections:**
  - Data governance: QA checklist, red-teaming prompts, escalation paths
  - Training orchestration (Accelerate/DeepSpeed, gradient accumulation) with config-driven approach
  - Evaluation suite: BLEU, Rouge, exact match, and human-in-loop scoring for safety-critical responses
  - Model packaging (Safetensors, HuggingFace Hub, internal registry)
- **Hands-on:** Students run a scaled-down training job (Zephyr-7B on sample data) and publish artifacts with version tags.

## Notebook 11 · Post-Tuning Evaluation, Monitoring & Drift Management
- **Objectives:** Operationalize continuous evaluation, drift detection, and rollback strategies.
- **Scenario:** Fine-tuned assistant deployed across 4 plants; must monitor performance and regulatory compliance.
- **Key Sections:**
  - Evaluation harness integrating RAGAS-style metrics + human review forms
  - Canary testing using shadow traffic from live maintenance chat logs
  - Embedding drift dashboards + anomaly alerts (cosine distance over time)
  - SOP for emergency rollback and change log sign-off
- **Hands-on:** Build a monitoring notebook that ingests inference logs, flags anomalies, and generates a weekly governance report.

---

## Cross-Notebook Integration
- **Data Backbone:** Provide synthetic yet realistic maintenance/quality datasets (CSV + PDF) shared across notebooks for continuity.
- **Code Reuse:** Establish `/common` Python utilities (data loaders, evaluation helpers) imported via relative paths.
- **Governance Thread:** Each notebook ends with a safety/compliance checklist aligned with ISO 9001 & OSHA guidance.
- **Capstone Alignment:** Outputs feed directly into Week 11-12 deployment notebooks (model registry, monitoring dashboards).

---

## Deliverables for Notebook Authors
1. Draft markdown outlines per notebook using the above skeleton.
2. Identify required datasets/artifacts and note gaps for data generation.
3. Flag any new dependencies beyond `requirements.txt` (e.g., `bitsandbytes`, `peft`, `accelerate`).
4. Provide ETA and owner for each notebook in project tracker.

---

**Next Steps:**
- Validate this blueprint with curriculum lead.
- Spin up shared datasets + utilities repo for reuse.
- Begin authoring Notebook 01 with data profiling code and manufacturing context.
