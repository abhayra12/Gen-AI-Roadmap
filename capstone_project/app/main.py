# app/main.py

import time
import logging
from uuid import uuid4

from fastapi import FastAPI, Request, Depends
from .config import settings
from .models import DiagnosisRequest, DiagnosisResponse, HealthStatus
from .security import authorize_request
from .agents import run_copilot_inference

# --- Application Setup ---
app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION,
    description="API for interacting with the Manufacturing Copilot agents.",
)

# --- Logging Configuration ---
# In a real app, you might use a more advanced logging setup (e.g., Loguru)
# and configure it to output structured JSON logs.
logging.basicConfig(
    level=settings.LOG_LEVEL.upper(),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("manufacturing_copilot_api")


# --- Middleware for Observability ---
@app.middleware("http")
async def add_observability_headers(request: Request, call_next):
    """
    Middleware to add custom headers for timing and tracing.
    This is crucial for monitoring and debugging in a production environment.
    """
    trace_id = str(uuid4())
    request.state.trace_id = trace_id
    
    start_time = time.perf_counter()
    
    # Process the request
    response = await call_next(request)
    
    # Calculate duration
    duration_ms = (time.perf_counter() - start_time) * 1000
    
    # Add custom headers to the response
    response.headers["X-Request-Trace-ID"] = trace_id
    response.headers["X-Response-Time-ms"] = f"{duration_ms:.2f}"
    
    logger.info(
        f"Request {request.method} {request.url.path} completed in {duration_ms:.2f}ms",
        extra={"trace_id": trace_id, "duration_ms": duration_ms, "path": request.url.path}
    )
    
    # Warn if latency exceeds our SLA (Service Level Agreement)
    if duration_ms > 500:
        logger.warning(
            f"High latency detected: {duration_ms:.2f}ms on path {request.url.path}",
            extra={"trace_id": trace_id}
        )
        
    return response


# --- API Endpoints ---

@app.get("/health", response_model=HealthStatus, tags=["Monitoring"])
async def health_check():
    """
    Health check endpoint to verify that the service is running.
    This is used by load balancers and monitoring systems.
    """
    return HealthStatus(status="ok")


@app.post("/v1/diagnose", response_model=DiagnosisResponse, tags=["Copilot"])
async def diagnose_problem(
    payload: DiagnosisRequest,
    user_id: str = Depends(authorize_request)
):
    """
    Main endpoint to diagnose a manufacturing problem.
    
    This endpoint orchestrates all agents (Vision, RAG, Report, ML, Analytics) 
    to provide a comprehensive analysis and recommendation. 
    Requires a valid technician auth token.
    """
    logger.info(
        f"Received diagnosis request from user '{user_id}' for plant '{payload.plant_id}'.",
        extra={"trace_id": getattr(payload, 'trace_id', None)}
    )
    
    # Call LangGraph orchestrator which runs all agents
    response = await run_copilot_inference(payload)
    
    return response


@app.post("/v1/predict", tags=["ML Agent"])
async def predict_failure(
    equipment_id: str,
    sensor_data: dict,
    user_id: str = Depends(authorize_request)
):
    """
    Predict equipment failure using ML models.
    
    This endpoint provides predictive maintenance insights using trained ML models.
    Returns failure probability, risk level, and maintenance recommendations.
    """
    try:
        from .ml_agent import ml_agent
        result = await ml_agent.predict_failure(equipment_id, sensor_data)
        return result
    except ImportError:
        return {
            "error": "ML Agent not available. Train the model first: python ml_models/predictive_maintenance/train_model.py",
            "equipment_id": equipment_id
        }
    except Exception as e:
        logger.error(f"ML prediction error: {e}")
        return {"error": str(e), "equipment_id": equipment_id}


@app.get("/v1/analytics/{equipment_id}", tags=["Analytics Agent"])
async def get_analytics(
    equipment_id: str,
    time_range: str = "last_30_days",
    user_id: str = Depends(authorize_request)
):
    """
    Get historical performance analytics for equipment.
    
    Returns performance trends, KPIs, and data-driven insights.
    Time range options: last_7_days, last_30_days, last_90_days
    """
    try:
        from .analytics_agent import analytics_agent
        result = await analytics_agent.analyze_performance_trend(equipment_id, time_range)
        return result
    except ImportError:
        return {
            "error": "Analytics Agent not available",
            "equipment_id": equipment_id,
            "note": "Running in mock mode. Connect BigQuery for real data."
        }
    except Exception as e:
        logger.error(f"Analytics error: {e}")
        return {"error": str(e), "equipment_id": equipment_id}
