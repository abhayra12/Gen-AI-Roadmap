# 🏭 Manufacturing Copilot: Data Engineering + ML Integration

> **Complete End-to-End Platform**: GenAI Agents + Data Engineering + Machine Learning

---

## 📋 Table of Contents

1. [Overview](#-overview)
2. [Architecture](#-architecture)
3. [Components](#-components)
4. [Data Flow](#-data-flow)
5. [ML Models](#-ml-models)
6. [Tech Stack](#-tech-stack)
7. [Implementation Guide](#-implementation-guide)

---

## 🎯 Overview

### What's New?

This integration transforms the Manufacturing Copilot from a pure GenAI application into a **complete data-driven AI platform** by adding:

1. **Real-Time Data Streaming** - Kafka-based IoT sensor data ingestion
2. **Batch Data Processing** - Spark jobs for historical analysis
3. **Data Warehouse** - BigQuery for analytics and BI
4. **ML Models** - Predictive maintenance, anomaly detection, quality forecasting
5. **Data Orchestration** - Airflow DAGs for workflow management
6. **Data Transformations** - dbt models for business logic
7. **Analytics Dashboards** - Metabase for visualization
8. **Enhanced AI Agents** - ML Agent, Analytics Agent, Forecasting Agent

### Architecture Evolution

**Before (Pure GenAI):**
```
User → FastAPI → LangGraph → [Vision, RAG, Report] → HuggingFace API
```

**After (Hybrid: GenAI + Data Engineering + ML):**
```
IoT Sensors → Kafka → Spark → BigQuery → ML Models ↘
                                                    ↘
User → FastAPI → LangGraph → [Vision, RAG, Report, ML, Analytics, Forecast] 
                            ↗
    HuggingFace API + Trained ML Models + Data Analytics
```

---

## 🏗️ Architecture

### System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                       Data Sources Layer                         │
├─────────────────────────────────────────────────────────────────┤
│ • IoT Sensors (Temperature, Vibration, Pressure, etc.)          │
│ • Equipment Logs (Machine states, error codes)                  │
│ • Production Data (Quality metrics, throughput)                 │
│ • Images (Product defects, visual inspection)                   │
│ • Historical Data (Maintenance records, failure logs)           │
└───────────────────────┬─────────────────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────────────────┐
│                   Data Ingestion Layer                           │
├─────────────────────────────────────────────────────────────────┤
│  STREAMING                    │  BATCH                           │
│  • Apache Kafka               │  • Manual Uploads                │
│  • Schema Registry            │  • Database Exports              │
│  • Real-time producers        │  • API Integrations              │
└───────────┬─────────────────────────────┬───────────────────────┘
            │                             │
┌───────────▼─────────────────────────────▼───────────────────────┐
│                  Data Processing Layer                           │
├─────────────────────────────────────────────────────────────────┤
│  STREAMING JOBS          │  BATCH JOBS                           │
│  • Kafka Consumers       │  • Apache Spark                       │
│  • Data Validation       │  • Data Cleansing                     │
│  • Real-time Alerts      │  • Feature Engineering                │
│  • Stream Analytics      │  • Aggregations                       │
└───────────┬─────────────────────────────┬───────────────────────┘
            │                             │
            └──────────────┬──────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────────┐
│                    Storage Layer                                 │
├─────────────────────────────────────────────────────────────────┤
│  • Google Cloud Storage (Data Lake)                              │
│  • BigQuery (Data Warehouse - OLAP)                              │
│  • PostgreSQL (Operational DB - OLTP)                            │
│  • ChromaDB (Vector Store for RAG)                               │
└──────────────────────────┬──────────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────────┐
│               Transformation Layer (dbt)                         │
├─────────────────────────────────────────────────────────────────┤
│  • Staging Models (raw → cleaned)                                │
│  • Intermediate Models (business logic)                          │
│  • Mart Models (analytics-ready)                                 │
│  • Data Quality Tests                                            │
│  • Documentation & Lineage                                       │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                 ┌─────────┴─────────┐
                 │                   │
┌────────────────▼────────┐  ┌──────▼──────────────────────────┐
│   ML Training Layer     │  │  Analytics & BI Layer           │
├─────────────────────────┤  ├─────────────────────────────────┤
│ • Predictive Models     │  │ • Metabase Dashboards           │
│ • Anomaly Detection     │  │ • KPI Tracking                  │
│ • Quality Forecasting   │  │ • Trend Analysis                │
│ • Model Registry        │  │ • Executive Reports             │
│ • Experiment Tracking   │  │ • Real-time Monitoring          │
└─────────────┬───────────┘  └─────────────────────────────────┘
              │
┌─────────────▼───────────────────────────────────────────────────┐
│              AI Agents Layer (LangGraph)                         │
├─────────────────────────────────────────────────────────────────┤
│  EXISTING AGENTS         │  NEW AGENTS                          │
│  1. Vision Agent         │  4. ML Agent (Predictive Models)     │
│  2. RAG Agent            │  5. Analytics Agent (Data Insights)  │
│  3. Report Agent         │  6. Forecasting Agent (Predictions)  │
└─────────────┬───────────────────────────────────────────────────┘
              │
┌─────────────▼───────────────────────────────────────────────────┐
│                   API Layer (FastAPI)                            │
├─────────────────────────────────────────────────────────────────┤
│  • /v1/diagnose          • /v1/predict                           │
│  • /v1/analytics         • /v1/forecast                          │
│  • /v1/stream-data       • /health                               │
└─────────────┬───────────────────────────────────────────────────┘
              │
┌─────────────▼───────────────────────────────────────────────────┐
│                  Orchestration Layer                             │
├─────────────────────────────────────────────────────────────────┤
│  • Apache Airflow (Workflow orchestration)                       │
│  • DAGs for: ETL, ML Training, Data Quality, Reports             │
│  • Monitoring & Alerting                                         │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Components

### 1. Streaming Pipeline (Real-Time)

**Purpose**: Ingest real-time sensor data from manufacturing equipment

**Components**:
- **Kafka Producers**: Simulate IoT sensors sending data
- **Kafka Topics**: 
  - `equipment-sensors` (temperature, vibration, pressure)
  - `equipment-status` (running, idle, error)
  - `quality-metrics` (defect rates, throughput)
- **Schema Registry**: Avro schemas for data validation
- **Kafka Consumers**: Process and store data

**Data Flow**:
```
Equipment Sensors → Kafka Producer → Kafka Broker → Kafka Consumer → GCS/BigQuery
```

### 2. Batch Pipeline (Historical Analysis)

**Purpose**: Process historical data for ML training and analytics

**Components**:
- **Apache Spark**: Distributed data processing
- **PySpark Jobs**:
  - Data cleansing (handle nulls, outliers)
  - Feature engineering (rolling averages, time-based features)
  - Aggregations (daily/weekly summaries)
- **Export to BigQuery**: Load processed data

**Data Flow**:
```
Raw Data (GCS/DB) → Spark Jobs → Processed Data → BigQuery Tables
```

### 3. Data Warehouse (BigQuery)

**Purpose**: Centralized analytics repository

**Schema Design**:

**Fact Tables**:
- `fact_sensor_readings` (time-series sensor data)
- `fact_equipment_events` (maintenance, failures, alerts)
- `fact_quality_inspections` (defect data, inspection results)
- `fact_production_metrics` (throughput, downtime, efficiency)

**Dimension Tables**:
- `dim_equipment` (equipment metadata)
- `dim_plant` (plant/facility information)
- `dim_date` (date dimension for time-based analysis)
- `dim_defect_types` (defect classification)

**Mart Tables** (dbt-generated):
- `mart_equipment_health` (current equipment status)
- `mart_predictive_maintenance` (failure predictions)
- `mart_quality_dashboard` (quality KPIs)

### 4. Machine Learning Models

#### A. Predictive Maintenance Model

**Type**: Binary Classification (Will Fail / Won't Fail)

**Algorithm**: Random Forest / XGBoost

**Features**:
- Temperature trends (rolling mean, std)
- Vibration patterns
- Operating hours since last maintenance
- Historical failure count
- Equipment age
- Seasonal factors

**Target**: `failure_within_7_days` (0/1)

**Evaluation Metrics**:
- Precision (minimize false alarms)
- Recall (catch all real failures)
- F1-Score
- ROC-AUC

#### B. Anomaly Detection Model

**Type**: Unsupervised Learning

**Algorithm**: Isolation Forest / Autoencoder

**Purpose**: Detect unusual sensor patterns that indicate issues

**Features**:
- Multi-variate sensor readings
- Statistical features (mean, std, skewness)
- Time-based features (hour of day, day of week)

**Output**: Anomaly score (0-1)

#### C. Quality Prediction Model

**Type**: Multi-class Classification

**Algorithm**: Gradient Boosting

**Classes**: 
- `Good Quality`
- `Minor Defect`
- `Major Defect`
- `Reject`

**Features**:
- Equipment parameters during production
- Material properties
- Environmental conditions
- Operator experience level

#### D. Time-Series Forecasting

**Type**: Time Series Prediction

**Algorithm**: LSTM / Prophet

**Purpose**: Forecast equipment metrics (temperature, vibration)

**Use Case**: Predict when thresholds will be exceeded

### 5. dbt Transformations

**Directory Structure**:
```
dbt_transformations/
├── models/
│   ├── staging/
│   │   ├── stg_sensor_readings.sql
│   │   ├── stg_equipment_events.sql
│   │   └── stg_quality_inspections.sql
│   ├── intermediate/
│   │   ├── int_equipment_metrics_hourly.sql
│   │   ├── int_failure_labels.sql
│   │   └── int_quality_aggregates.sql
│   └── marts/
│       ├── mart_equipment_health.sql
│       ├── mart_predictive_maintenance.sql
│       └── mart_quality_dashboard.sql
├── tests/
│   ├── generic_tests.yml
│   └── custom_tests/
└── dbt_project.yml
```

**Example Model** (`mart_equipment_health.sql`):
```sql
WITH latest_sensors AS (
  SELECT
    equipment_id,
    MAX(timestamp) as last_reading_time,
    AVG(temperature) as avg_temp_24h,
    AVG(vibration) as avg_vibration_24h,
    MAX(temperature) as max_temp_24h
  FROM {{ ref('stg_sensor_readings') }}
  WHERE timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 24 HOUR)
  GROUP BY equipment_id
),
failure_predictions AS (
  SELECT
    equipment_id,
    predicted_failure_prob,
    prediction_timestamp
  FROM {{ ref('ml_predictions') }}
  WHERE prediction_date = CURRENT_DATE()
)
SELECT
  e.equipment_id,
  e.equipment_name,
  e.plant_id,
  s.last_reading_time,
  s.avg_temp_24h,
  s.avg_vibration_24h,
  s.max_temp_24h,
  f.predicted_failure_prob,
  CASE
    WHEN f.predicted_failure_prob > 0.8 THEN 'Critical'
    WHEN f.predicted_failure_prob > 0.5 THEN 'Warning'
    ELSE 'Normal'
  END as health_status
FROM {{ ref('dim_equipment') }} e
LEFT JOIN latest_sensors s ON e.equipment_id = s.equipment_id
LEFT JOIN failure_predictions f ON e.equipment_id = f.equipment_id
```

### 6. Apache Airflow DAGs

**DAG 1: Streaming to Batch ETL**
```python
# airflow_dags/streaming_to_batch_dag.py
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'data-eng',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'streaming_to_batch_etl',
    default_args=default_args,
    schedule_interval='@hourly',
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:
    
    # Consume Kafka → GCS
    kafka_to_gcs = BashOperator(
        task_id='kafka_to_gcs',
        bash_command='python /opt/airflow/dags/scripts/kafka_consumer.py',
    )
    
    # Spark Processing
    spark_processing = BashOperator(
        task_id='spark_processing',
        bash_command='spark-submit /opt/airflow/dags/spark_jobs/process_sensor_data.py',
    )
    
    # Load to BigQuery
    load_to_bq = BigQueryInsertJobOperator(
        task_id='load_to_bigquery',
        configuration={
            "load": {
                "sourceUris": ["gs://manufacturing-data/processed/*.parquet"],
                "destinationTable": {
                    "projectId": "{{ var.value.gcp_project }}",
                    "datasetId": "manufacturing",
                    "tableId": "sensor_readings",
                },
                "sourceFormat": "PARQUET",
                "writeDisposition": "WRITE_APPEND",
            }
        },
    )
    
    kafka_to_gcs >> spark_processing >> load_to_bq
```

**DAG 2: ML Model Training**
```python
# airflow_dags/ml_training_dag.py
with DAG(
    'ml_model_training',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2025, 1, 1),
) as dag:
    
    # Extract training data
    extract_data = BigQueryInsertJobOperator(...)
    
    # Train model
    train_model = BashOperator(
        task_id='train_predictive_model',
        bash_command='python /opt/ml/training_pipelines/train_predictive_maintenance.py',
    )
    
    # Evaluate model
    evaluate_model = BashOperator(...)
    
    # Register model (MLflow/Vertex AI)
    register_model = BashOperator(...)
    
    # Deploy if metrics pass threshold
    deploy_model = BashOperator(...)
    
    extract_data >> train_model >> evaluate_model >> register_model >> deploy_model
```

**DAG 3: dbt Transformations**
```python
with DAG('dbt_transformations', ...) as dag:
    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='cd /opt/dbt && dbt run --models marts',
    )
    
    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='cd /opt/dbt && dbt test',
    )
    
    dbt_run >> dbt_test
```

### 7. Analytics Dashboards (Metabase)

**Dashboards**:

1. **Equipment Health Dashboard**
   - Real-time sensor readings
   - Equipment status (running, idle, error)
   - Anomaly alerts

2. **Predictive Maintenance Dashboard**
   - Failure probability scores
   - Maintenance recommendations
   - Historical failure trends

3. **Quality Analytics Dashboard**
   - Defect rates by equipment
   - Quality trends over time
   - Root cause analysis

4. **Production KPIs**
   - Overall Equipment Effectiveness (OEE)
   - Throughput metrics
   - Downtime analysis

---

## 📊 Data Flow

### Complete End-to-End Flow

```
1. DATA COLLECTION
   IoT Sensor → Kafka Producer → Kafka Broker
                                       ↓
2. REAL-TIME PROCESSING
   Kafka Consumer → Validation → GCS (Raw Data Lake)
                                       ↓
3. BATCH PROCESSING (Every Hour)
   Airflow Trigger → Spark Job → Feature Engineering
                                       ↓
4. DATA WAREHOUSE
   Load to BigQuery → Partitioned Tables
                                       ↓
5. TRANSFORMATIONS (dbt)
   Staging → Intermediate → Marts
                                       ↓
6. ML & ANALYTICS (Parallel)
   ├─→ ML Models (Predictions) → Model Predictions Table
   └─→ Metabase (Dashboards) → Visualizations
                                       ↓
7. AI AGENTS (Real-time Inference)
   User Query → FastAPI → LangGraph
                    ↓
   ┌───────────────┴────────────────┐
   │                                │
   ▼                                ▼
Vision Agent (HF)              ML Agent (Trained Models)
RAG Agent (Vector DB)          Analytics Agent (BigQuery)
Report Agent (LLM)             Forecast Agent (Time Series)
   │                                │
   └───────────────┬────────────────┘
                   ▼
            Unified Response
```

---

## 🤖 Enhanced AI Agents

### Agent 4: ML Agent (Predictive Models)

**Purpose**: Provide ML-based predictions using trained models

**Capabilities**:
- Predict equipment failure probability
- Detect anomalies in sensor data
- Forecast quality metrics
- Recommend maintenance schedules

**Example Request**:
```json
{
  "equipment_id": "CNC-A-102",
  "prediction_type": "failure_risk",
  "time_horizon": "7_days"
}
```

**Example Response**:
```json
{
  "failure_probability": 0.73,
  "risk_level": "High",
  "contributing_factors": [
    "Elevated vibration (12% above normal)",
    "Temperature trending upward",
    "45 days since last maintenance"
  ],
  "recommended_action": "Schedule maintenance within 3 days"
}
```

### Agent 5: Analytics Agent (Data Insights)

**Purpose**: Query BigQuery and provide data-driven insights

**Capabilities**:
- Historical trend analysis
- Comparative analysis (equipment, plants, time periods)
- Root cause analysis using data
- KPI calculations

**Example Request**:
```json
{
  "equipment_id": "CNC-A-102",
  "analysis_type": "performance_trend",
  "time_range": "last_30_days"
}
```

**Example Response**:
```json
{
  "metrics": {
    "avg_uptime": "92.3%",
    "avg_temperature": "67.2°C",
    "defect_rate": "2.1%"
  },
  "trends": {
    "uptime": "↓ 3.2% vs previous month",
    "temperature": "↑ 5.1% vs previous month",
    "defect_rate": "↑ 0.8% vs previous month"
  },
  "insights": [
    "Equipment showing signs of degradation",
    "Temperature increase correlates with defect rate increase",
    "Recommend inspection of cooling system"
  ]
}
```

### Agent 6: Forecasting Agent (Time Series Predictions)

**Purpose**: Forecast future equipment metrics

**Capabilities**:
- Predict sensor values (temperature, vibration, pressure)
- Forecast production metrics
- Predict when thresholds will be exceeded
- Multi-step ahead forecasting

**Example Request**:
```json
{
  "equipment_id": "CNC-A-102",
  "metric": "temperature",
  "forecast_horizon": "24_hours"
}
```

**Example Response**:
```json
{
  "forecasted_values": [
    {"timestamp": "2025-11-01T10:00:00Z", "value": 68.3, "confidence_interval": [66.1, 70.5]},
    {"timestamp": "2025-11-01T11:00:00Z", "value": 69.1, "confidence_interval": [66.8, 71.4]},
    ...
  ],
  "threshold_violations": [
    {
      "timestamp": "2025-11-01T15:00:00Z",
      "predicted_value": 75.2,
      "threshold": 70.0,
      "severity": "Warning"
    }
  ],
  "recommendation": "Monitor temperature closely. Predicted to exceed warning threshold at 15:00"
}
```

---

## 🛠️ Tech Stack

### Data Engineering
| Component | Technology | Purpose |
|-----------|-----------|---------|
| Streaming | Apache Kafka + Schema Registry | Real-time data ingestion |
| Batch Processing | Apache Spark (PySpark) | Large-scale data processing |
| Data Warehouse | Google BigQuery | Analytics & BI |
| Data Lake | Google Cloud Storage | Raw data storage |
| Orchestration | Apache Airflow | Workflow management |
| Transformations | dbt (data build tool) | SQL-based transformations |
| Visualization | Metabase | Dashboards & reports |

### Machine Learning
| Component | Technology | Purpose |
|-----------|-----------|---------|
| ML Framework | scikit-learn, XGBoost | Traditional ML models |
| Deep Learning | TensorFlow/PyTorch | Neural networks (LSTM, Autoencoder) |
| Time Series | Prophet, ARIMA | Forecasting |
| Experiment Tracking | MLflow / Weights & Biases | Model versioning |
| Model Registry | MLflow / Vertex AI | Model deployment |
| Feature Store | Feast (optional) | Feature management |

### GenAI (Existing)
| Component | Technology | Purpose |
|-----------|-----------|---------|
| LLM | HuggingFace (Llama-2, BLIP-2) | Language & vision models |
| Orchestration | LangGraph | Multi-agent workflows |
| Vector DB | ChromaDB | RAG document store |
| API | FastAPI | REST API backend |

### Infrastructure
| Component | Technology | Purpose |
|-----------|-----------|---------|
| Containerization | Docker, Docker Compose | Development environment |
| Orchestration | Kubernetes (GKE/EKS/AKS) | Production deployment |
| IaC | Terraform | Infrastructure provisioning |
| CI/CD | GitHub Actions | Automated deployment |
| Monitoring | Prometheus + Grafana | System monitoring |
| Logging | ELK Stack | Centralized logging |

---

## 📖 Implementation Guide

### Phase 1: Data Engineering Foundation (Week 1-2)

**Day 1-2: Streaming Pipeline**
- [ ] Set up Kafka cluster (Docker Compose)
- [ ] Create Kafka topics
- [ ] Implement data producer (simulate sensors)
- [ ] Implement data consumer
- [ ] Set up Schema Registry

**Day 3-4: Batch Processing**
- [ ] Set up Apache Spark
- [ ] Create PySpark jobs for data cleansing
- [ ] Implement feature engineering
- [ ] Test Spark jobs locally

**Day 5-6: Data Warehouse**
- [ ] Set up BigQuery project
- [ ] Design schema (fact & dimension tables)
- [ ] Create tables with partitioning/clustering
- [ ] Implement data loading scripts

**Day 7: Orchestration**
- [ ] Set up Apache Airflow
- [ ] Create ETL DAGs
- [ ] Test DAG execution
- [ ] Set up monitoring

### Phase 2: dbt Transformations (Week 2-3)

**Day 8-9: dbt Setup**
- [ ] Initialize dbt project
- [ ] Configure BigQuery connection
- [ ] Create staging models
- [ ] Write data quality tests

**Day 10-11: Business Logic**
- [ ] Create intermediate models
- [ ] Create mart models
- [ ] Document models
- [ ] Generate dbt docs

### Phase 3: Machine Learning (Week 3-4)

**Day 12-13: Predictive Maintenance Model**
- [ ] Prepare training data
- [ ] Feature engineering
- [ ] Train Random Forest/XGBoost model
- [ ] Evaluate and tune
- [ ] Save model

**Day 14: Anomaly Detection Model**
- [ ] Implement Isolation Forest
- [ ] Train on normal data
- [ ] Test anomaly detection
- [ ] Set thresholds

**Day 15: Quality Prediction Model**
- [ ] Prepare labeled quality data
- [ ] Train classification model
- [ ] Evaluate metrics
- [ ] Deploy model

**Day 16: Time Series Forecasting**
- [ ] Implement LSTM/Prophet model
- [ ] Train on historical sensor data
- [ ] Test forecasting accuracy
- [ ] Deploy forecasting service

### Phase 4: Enhanced AI Agents (Week 4-5)

**Day 17-18: ML Agent**
- [ ] Create `ml_agent.py`
- [ ] Integrate trained models
- [ ] Implement prediction logic
- [ ] Add to LangGraph workflow

**Day 19: Analytics Agent**
- [ ] Create `analytics_agent.py`
- [ ] Integrate BigQuery client
- [ ] Implement query templates
- [ ] Add to LangGraph workflow

**Day 20: Forecasting Agent**
- [ ] Create `forecasting_agent.py`
- [ ] Integrate time series models
- [ ] Implement forecast logic
- [ ] Add to LangGraph workflow

**Day 21: API Endpoints**
- [ ] Add `/v1/predict` endpoint
- [ ] Add `/v1/analytics` endpoint
- [ ] Add `/v1/forecast` endpoint
- [ ] Update API documentation

### Phase 5: Dashboards & Monitoring (Week 5-6)

**Day 22-23: Metabase Setup**
- [ ] Set up Metabase
- [ ] Connect to BigQuery
- [ ] Create equipment health dashboard
- [ ] Create predictive maintenance dashboard

**Day 24-25: Advanced Dashboards**
- [ ] Create quality analytics dashboard
- [ ] Create production KPIs dashboard
- [ ] Set up email alerts
- [ ] Share dashboards with team

**Day 26: End-to-End Testing**
- [ ] Test complete data flow
- [ ] Test all agents
- [ ] Load testing
- [ ] Fix bugs

**Day 27: Documentation**
- [ ] Update README
- [ ] Create architecture diagrams
- [ ] Write deployment guide
- [ ] Record demo video

### Phase 6: Production Deployment (Week 6)

**Day 28-30: Production Setup**
- [ ] Update Terraform configs
- [ ] Deploy to Kubernetes
- [ ] Set up monitoring (Prometheus/Grafana)
- [ ] Configure CI/CD
- [ ] Production testing

---

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.11+
- GCP account (for BigQuery)
- HuggingFace API token

### Installation

```bash
# 1. Clone and navigate
cd capstone_project

# 2. Start all services with Docker Compose
docker-compose -f docker-compose-full.yml up -d

# This starts:
# - Kafka + Zookeeper
# - Schema Registry
# - Spark Master + Worker
# - Airflow Webserver + Scheduler
# - PostgreSQL
# - Metabase
# - FastAPI Backend
# - Prometheus + Grafana

# 3. Initialize Airflow
docker-compose exec airflow-webserver airflow db init
docker-compose exec airflow-webserver airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin

# 4. Access UIs
# - FastAPI: http://localhost:8080/docs
# - Airflow: http://localhost:8081 (admin/admin)
# - Metabase: http://localhost:3010
# - Kafka Control Center: http://localhost:9021
# - Spark Master: http://localhost:8082
# - Grafana: http://localhost:3000

# 5. Start data generation
python data_engineering/streaming_pipeline/kafka_producer.py
```

---

## 📊 Success Metrics

### Data Engineering KPIs
- ✅ **Data Latency**: <5 minutes for streaming, <1 hour for batch
- ✅ **Data Quality**: >99% data validation pass rate
- ✅ **Pipeline Uptime**: >99.5% availability
- ✅ **Processing Throughput**: 10K+ events/second

### ML Model KPIs
- ✅ **Predictive Maintenance**: Precision >80%, Recall >90%
- ✅ **Anomaly Detection**: False Positive Rate <5%
- ✅ **Quality Prediction**: Accuracy >85%
- ✅ **Forecast Accuracy**: MAPE <10%

### System KPIs
- ✅ **API Response Time**: <2 seconds (p95)
- ✅ **Agent Accuracy**: >80% user satisfaction
- ✅ **Dashboard Load Time**: <3 seconds
- ✅ **System Uptime**: >99.9%

---

## 🎓 Learning Outcomes

By completing this integration, you'll master:

1. **Data Engineering**:
   - Real-time streaming with Kafka
   - Batch processing with Spark
   - Data warehousing with BigQuery
   - Orchestration with Airflow
   - Data modeling with dbt

2. **Machine Learning**:
   - Predictive maintenance models
   - Anomaly detection
   - Time series forecasting
   - MLOps (training, deployment, monitoring)

3. **GenAI**:
   - Multi-agent systems with LangGraph
   - RAG implementation
   - Production LLM deployment

4. **System Design**:
   - End-to-end data platform architecture
   - Microservices design
   - Scalable infrastructure

---

**This is a COMPLETE Data + AI platform!** 🚀

You're combining the best of:
- **Data Engineering** (your agri pipeline)
- **Machine Learning** (predictive models)
- **Generative AI** (intelligent agents)

**Next Steps**: Follow the Implementation Guide phase by phase!
