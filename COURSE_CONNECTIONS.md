# 🔄 Course Connections: Building an Integrated Learning Path

This document outlines how concepts build across the course modules and how the notebooks connect with each other, helping you see the progression toward the capstone project.

## 📊 Module Progression Overview

```
Week 1-2: Python & ML Foundations 
  ↓
Week 3-4: Deep Learning & NLP Foundations
  ↓ 
Week 5-6: LLMs & RAG
  ↓
Week 7-8: LangChain & Agents
  ↓
Week 9-10: Model Training & Fine-tuning
  ↓
Week 11-12: Production Deployment & Capstone
```

## 🔗 Cross-Module Connections

### Week 1-2 → Week 3-4
- **Data preprocessing** techniques from Week 1-2 are directly applied to **prepare text data** for transformer models in Week 3-4
- **NumPy array manipulation** knowledge supports understanding **tensor operations** in neural networks
- **Visualization skills** extend to plotting **attention maps** and **embedding spaces**

### Week 3-4 → Week 5-6
- **Transformer architecture** knowledge enables better understanding of **LLM internals**
- **Tokenization** concepts are reapplied when working with **prompt engineering**
- **Embedding techniques** form the foundation for **vector-based retrieval**

### Week 5-6 → Week 7-8
- **RAG patterns** are enhanced with **LangChain abstractions**
- **Vector database** knowledge is applied to **agent memory** implementations
- **Prompt engineering** skills are leveraged in **agent system prompts**

### Week 7-8 → Week 9-10
- **Governance patterns** from agent systems inform **evaluation metrics** for fine-tuned models
- **Domain-specific tools** created for agents identify **areas for model specialization**
- **Error handling** approaches guide **training data cleaning** techniques

### Week 9-10 → Week 11-12
- **Fine-tuned models** are deployed as part of the **production system**
- **Performance metrics** guide **monitoring dashboards**
- **Training pipelines** are integrated into **CI/CD workflows**

## 📚 Notebook Dependencies Map

### Week 1-2: Python & ML Foundations
1. `01_environment_setup.ipynb` → Sets up tools used throughout course
2. `02_python_essentials.ipynb` → Core programming used in all future notebooks
3. `03_numpy_pandas.ipynb` → Data manipulation used in all ML/DL notebooks
4. `04_data_preprocessing.ipynb` → Techniques reused in Week 3-4, 5-6, 9-10
5. `05_ml_foundations.ipynb` → Concepts extended in deep learning notebooks

### Week 3-4: Deep Learning & NLP
1. `01_neural_networks.ipynb` → Foundation for all deep learning concepts
2. `02_cnn_basics.ipynb` → Visual processing concepts used in multimodal AI
3. `03_rnn_lstm.ipynb` → Sequence models leading to transformers
4. `04_transformers.ipynb` → **KEY NOTEBOOK**: Core architecture of modern LLMs
5. `05_attention_mechanisms.ipynb` → Critical concept used in all LLM work
6. `06_embeddings.ipynb` → **KEY NOTEBOOK**: Foundation for all vector search
7. `07_huggingface_intro.ipynb` → Platform used extensively in later weeks

### Week 5-6: LLMs & RAG
1. `01_llm_foundations.ipynb` → Core concepts for rest of the course
2. `02_prompt_engineering.ipynb` → Techniques used in all LLM interactions
3. `03_in_context_learning.ipynb` → Methods applied throughout agent notebooks
4. `04_evaluation_metrics.ipynb` → **KEY NOTEBOOK**: Used in all future LLM work
5. `05_document_processing.ipynb` → Data prep for Week 7-8 retrieval systems
6. `06_vector_search.ipynb` → **KEY NOTEBOOK**: Core RAG functionality
7. `07_retrieval_augmentation.ipynb` → **KEY NOTEBOOK**: Foundation for Week 7-8
8. `08_rag_evaluation.ipynb` → Metrics reused in Week 7-8, 11-12

### Week 7-8: LangChain & Agents
1. `01_langchain_essentials.ipynb` → **KEY NOTEBOOK**: Framework for remaining notebooks
2. `02_message_structures.ipynb` → Message patterns used in all agent notebooks
3. `03_prompt_templates_chains.ipynb` → Templates used in notebooks 4-15
4. `04_runnable_sequences.ipynb` → Orchestration patterns used in notebooks 7-15
5. `05_document_loaders.ipynb` → Data ingest used in RAG notebooks (7-10, 15)
6. `06_vector_databases.ipynb` → Storage used in RAG & memory notebooks (7-10, 14)
7. `07_advanced_rag_patterns.ipynb` → Enhanced retrieval for notebooks 8-10
8. `08_query_optimization.ipynb` → Techniques used in notebooks 9-10
9. `09_query_transformation.ipynb` → Methods used in notebooks 10, 15
10. `10_rag_fusion_reranking.ipynb` → Advanced techniques for notebook 15
11. `11_langgraph_introduction.ipynb` → **KEY NOTEBOOK**: Foundation for notebooks 12-14
12. `12_building_agents.ipynb` → **KEY NOTEBOOK**: Core agent design
13. `13_agentic_tools.ipynb` → Tools used in notebooks 12, 14
14. `14_agent_state_management.ipynb` → Memory persistence for Week 11-12
15. `15_corrective_rag.ipynb` → Self-evaluation for Week 11-12

### Week 9-10: Model Training & Fine-tuning
1. `01_pre_training_concepts.ipynb` → Foundation for understanding model adaptations
2. `02_bigram_language_model.ipynb` → Simple implementation for concept mastery
3. `03_tensors_gpu_acceleration.ipynb` → Optimization techniques for training
4. `04_forward_backward_diagnostics.ipynb` → Debugging techniques for custom models
5. `05_mlp_sensor_fusion.ipynb` → Manufacturing-specific model extensions
6. `06_minibatch_curriculum.ipynb` → Advanced training techniques
7. `07_finetuning_vs_rag.ipynb` → **KEY NOTEBOOK**: Decision framework for approach
8. `08_peft_foundations.ipynb` → Core efficient fine-tuning methods
9. `09_lora_qlora.ipynb` → **KEY NOTEBOOK**: Primary fine-tuning technique
10. `10_finetuning_pipeline.ipynb` → End-to-end workflow for custom models
11. `11_post_tuning_monitoring.ipynb` → Evaluation framework for Week 11-12

### Week 11-12: Production & Capstone
1. `01_production_fundamentals.ipynb` → Deployment concepts used throughout module
2. `02_model_serving.ipynb` → **KEY NOTEBOOK**: API creation for models
3. `03_api_development.ipynb` → Framework for all services
4. `04_logging_monitoring.ipynb` → Observability for production systems
5. `05_container_orchestration.ipynb` → Deployment infrastructure
6. `06_ci_cd_pipelines.ipynb` → Automation for model updates
7. `07_cost_optimization.ipynb` → Efficiency techniques for production
8. `08_governance_compliance.ipynb` → Enterprise readiness requirements
9. `09_capstone_planning.ipynb` → Integration of all course concepts
10. `10_capstone_implementation.ipynb` → Final application of learned skills

## 🔑 Key Integration Points for Capstone

1. **Manufacturing Scenario Consistency**
   - Week 1-2: Manufacturing quality dataset analysis
   - Week 3-4: Text classification of maintenance reports
   - Week 5-6: RAG on manufacturing SOPs and manuals
   - Week 7-8: Maintenance agent with safety compliance
   - Week 9-10: Fine-tuning for manufacturing terminology
   - Week 11-12: Production-ready manufacturing assistant

2. **Data Flow Continuity**
   - Week 1-2: Data cleaning and preprocessing
   - Week 3-4: Feature extraction and embeddings
   - Week 5-6: Vector storage and retrieval
   - Week 7-8: Agent memory and state management
   - Week 9-10: Training data creation and augmentation
   - Week 11-12: Production data pipelines and monitoring

3. **Governance & Compliance Thread**
   - Week 1-2: Data validation and documentation
   - Week 3-4: Model validation techniques
   - Week 5-6: Citation and source tracking
   - Week 7-8: Audit logging and traceability
   - Week 9-10: Model cards and bias evaluation
   - Week 11-12: Complete governance framework

4. **Multilingual Support Evolution**
   - Week 3-4: Basic multilingual embeddings
   - Week 5-6: Cross-lingual retrieval
   - Week 7-8: Bilingual agent responses
   - Week 9-10: Language-specific tuning
   - Week 11-12: Full multilingual production system

## 📈 Skills Progression Map

```
Python Basics → NumPy/Pandas → Neural Networks → Transformers → 
Embeddings → Vector Search → RAG → LangChain Chains → 
LangGraph → Agents → Fine-tuning → Production Deployment
```

Each module builds on the previous one, with practical applications that reinforce earlier concepts while adding new capabilities. The manufacturing theme provides a consistent domain context that grows in complexity and realism.

## 🏆 Capstone Project Integration

The capstone project in Weeks 11-12 represents the culmination of all previous modules:

1. Uses **Python & ML foundations** for data processing
2. Applies **Deep Learning & NLP** for understanding user queries
3. Implements **RAG patterns** for knowledge retrieval
4. Orchestrates multiple **LangChain agents** for complex tasks
5. Incorporates **fine-tuned models** for domain specialization
6. Delivers a **production-ready system** with monitoring and governance

This integration ensures that students experience a complete learning journey from basic principles to production-ready implementation, with each module's skills directly contributing to the final capstone achievement.