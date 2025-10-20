# 🏭 Manufacturing Copilot - Capstone Project

A production-grade, multi-agent AI system for smart manufacturing that leverages Vision-Language Models, RAG, and LangGraph to solve real-world factory challenges.

## 🎯 Project Overview

The Manufacturing Copilot is an intelligent system that combines three specialized AI agents:

- **Vision Agent**: Analyzes product images to identify manufacturing defects
- **RAG Agent**: Provides expert maintenance guidance from technical documentation
- **Report Agent**: Generates structured, multi-lingual production reports

These agents are orchestrated by a central LangGraph-based system and exposed via a secure FastAPI backend.

## 🏗️ Architecture

```
┌─────────────────┐
│  FastAPI Backend│
└────────┬────────┘
         │
┌────────▼────────────────┐
│ LangGraph Orchestrator  │
└─┬──────┬────────┬────────┘
  │      │        │
  ▼      ▼        ▼
┌────┐ ┌───┐  ┌──────┐
│VLM │ │RAG│  │Report│
└────┘ └───┘  └──────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Docker & Docker Compose
- PostgreSQL 15+
- ChromaDB (for vector storage)

### Local Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/abhayra12/Gen-AI-Roadmap.git
   cd Gen-AI-Roadmap/capstone_project
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements-dev.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run with Docker Compose**:
   ```bash
   docker-compose up --build
   ```

6. **Access the API**:
   - API: http://localhost:8080
   - API Docs: http://localhost:8080/docs
   - Health Check: http://localhost:8080/health

## 📝 API Endpoints

### Health Check
```bash
GET /health
```

### Diagnose Manufacturing Issue
```bash
POST /v1/diagnose
Headers:
  X-Auth-Token: Bearer technician-<user_id>
  Content-Type: application/json

Body:
{
  "plant_id": "PUNE-IN",
  "equipment_id": "CNC-A-102",
  "problem_description": "Machine overheating during operation",
  "image_id": "img_12345"
}
```

## 🧪 Testing

### Run all tests:
```bash
pytest tests/ -v
```

### Run with coverage:
```bash
pytest tests/ --cov=app --cov-report=html
```

### Run specific test file:
```bash
pytest tests/test_api.py -v
```

## 🐳 Docker Deployment

### Build the Docker image:
```bash
docker build -t manufacturing-copilot:latest .
```

### Run the container:
```bash
docker run -p 8080:8080 \
  -e LOG_LEVEL=INFO \
  -e DATABASE_URL=postgresql://... \
  manufacturing-copilot:latest
```

## ☁️ Cloud Deployment (GCP)

### Using Terraform:

1. **Navigate to terraform directory**:
   ```bash
   cd terraform
   ```

2. **Initialize Terraform**:
   ```bash
   terraform init
   ```

3. **Plan the deployment**:
   ```bash
   terraform plan -var="project_id=your-gcp-project"
   ```

4. **Apply the configuration**:
   ```bash
   terraform apply -var="project_id=your-gcp-project"
   ```

### Using the deployment script:
```bash
python scripts/deploy_cloud_run.py \
  --project your-gcp-project \
  --region us-central1 \
  --service-name manufacturing-copilot
```

## 🔐 Security

- **Authentication**: Bearer token authentication for all diagnosis endpoints
- **Input Validation**: Pydantic models with strict validation rules
- **Rate Limiting**: (TODO: Implement rate limiting middleware)
- **Secrets Management**: Environment variables and GCP Secret Manager

## 📊 Monitoring & Observability

Every request includes:
- **X-Request-Trace-ID**: Unique identifier for request tracing
- **X-Response-Time-ms**: Response time in milliseconds

High latency warnings (>500ms) are automatically logged.

## 🛠️ Development

### Code Quality Tools:

```bash
# Lint code
flake8 app

# Format code
black app

# Type checking
mypy app --ignore-missing-imports

# Sort imports
isort app
```

### Pre-commit hooks:
```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run manually
pre-commit run --all-files
```

## 📦 Project Structure

```
capstone_project/
├── app/                    # Application code
│   ├── main.py            # FastAPI application
│   ├── agents.py          # Agent orchestration logic
│   ├── models.py          # Pydantic models
│   ├── config.py          # Configuration settings
│   ├── security.py        # Authentication logic
│   └── functions/         # Cloud functions
├── tests/                 # Test suite
│   ├── test_api.py        # API integration tests
│   ├── test_models.py     # Model unit tests
│   └── test_security.py   # Security tests
├── terraform/             # Infrastructure as Code
│   ├── main.tf           # Main Terraform config
│   └── modules/          # Terraform modules
├── .github/workflows/     # CI/CD pipelines
│   ├── ci.yml            # Continuous Integration
│   └── deploy.yml        # Continuous Deployment
├── scripts/              # Deployment and utility scripts
├── Dockerfile            # Container definition
├── docker-compose.yml    # Local development stack
├── requirements.txt      # Production dependencies
└── requirements-dev.txt  # Development dependencies
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is part of the Gen AI Masters Program curriculum.

## 🙏 Acknowledgments

- HuggingFace for Transformers library
- LangChain team for the agent framework
- FastAPI for the excellent web framework

## 📞 Support

For questions or issues, please:
- Open an issue in the repository
- Check the main course [FAQ](../FAQ.md)
- Review the [Getting Started Guide](../GETTING_STARTED.md)

---

Built with ❤️ for the Gen AI Masters Program
