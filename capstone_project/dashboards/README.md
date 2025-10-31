# Dashboards

Monitoring and visualization dashboards for the Manufacturing Copilot system.

## Planned Dashboards

### 1. API Performance Dashboard
- Request latency metrics
- Throughput (requests/second)
- Error rates
- Response time distribution

### 2. Agent Execution Metrics
- Vision Agent performance
- RAG Agent retrieval times
- Report Agent generation times
- LangGraph orchestration metrics

### 3. System Health Dashboard
- Service availability
- Resource usage (CPU, Memory)
- Database connections
- Queue depths

### 4. ML Model Metrics
- Prediction accuracy
- Model inference time
- Feature importance
- Drift detection

## Implementation

Dashboards will be implemented using:
- **Grafana** for visualization
- **Prometheus** for metrics collection
- **Loki** for log aggregation

## Setup

```bash
# Start monitoring stack
docker-compose -f docker-compose-full.yml up -d

# Access Grafana
open http://localhost:3000
# Default credentials: admin/admin
```

## Dashboard Templates

Pre-built dashboard templates will be added here for:
- FastAPI applications
- LangChain agents
- ML model monitoring
- Kafka streaming metrics

## Coming Soon

- [ ] API Performance Dashboard JSON
- [ ] Agent Metrics Dashboard JSON
- [ ] System Health Dashboard JSON
- [ ] ML Model Monitoring Dashboard JSON
