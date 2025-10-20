"""Integration tests for the Manufacturing Copilot API."""

import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI application."""
    return TestClient(app)


@pytest.fixture
def valid_auth_token():
    """Provide a valid authentication token for tests."""
    return "Bearer technician-test-user-123"


class TestHealthEndpoint:
    """Test cases for the health check endpoint."""

    def test_health_check_success(self, client):
        """Test that health check endpoint returns 200 OK."""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

    def test_health_check_response_headers(self, client):
        """Test that health check includes observability headers."""
        response = client.get("/health")
        assert "X-Request-Trace-ID" in response.headers
        assert "X-Response-Time-ms" in response.headers


class TestDiagnoseEndpoint:
    """Test cases for the main diagnosis endpoint."""

    def test_diagnose_without_auth(self, client):
        """Test that diagnosis endpoint requires authentication."""
        payload = {
            "plant_id": "PUNE-IN",
            "equipment_id": "CNC-A-102",
            "problem_description": "Machine overheating"
        }
        response = client.post("/v1/diagnose", json=payload)
        assert response.status_code == 422  # Missing auth header

    def test_diagnose_with_invalid_auth(self, client):
        """Test that invalid auth token is rejected."""
        payload = {
            "plant_id": "PUNE-IN",
            "equipment_id": "CNC-A-102",
            "problem_description": "Machine overheating"
        }
        headers = {"X-Auth-Token": "InvalidToken"}
        response = client.post("/v1/diagnose", json=payload, headers=headers)
        assert response.status_code == 401

    def test_diagnose_with_valid_auth(self, client, valid_auth_token):
        """Test successful diagnosis with valid authentication."""
        payload = {
            "plant_id": "PUNE-IN",
            "equipment_id": "CNC-A-102",
            "problem_description": "Machine overheating during operation"
        }
        headers = {"X-Auth-Token": valid_auth_token}
        response = client.post("/v1/diagnose", json=payload, headers=headers)
        assert response.status_code == 200
        
        data = response.json()
        assert "request_id" in data
        assert "vision_analysis" in data
        assert "rag_guidance" in data
        assert "generated_report" in data
        assert "confidence_score" in data
        assert "safety_disclaimer" in data

    def test_diagnose_with_image(self, client, valid_auth_token):
        """Test diagnosis endpoint with an image ID."""
        payload = {
            "plant_id": "MEX-GTO",
            "equipment_id": "PUMP-B-05",
            "problem_description": "Unusual vibration",
            "image_id": "img_test_123"
        }
        headers = {"X-Auth-Token": valid_auth_token}
        response = client.post("/v1/diagnose", json=payload, headers=headers)
        assert response.status_code == 200

    def test_diagnose_invalid_plant_id(self, client, valid_auth_token):
        """Test that invalid plant ID format is rejected."""
        payload = {
            "plant_id": "invalid",
            "equipment_id": "CNC-A-102",
            "problem_description": "Test"
        }
        headers = {"X-Auth-Token": valid_auth_token}
        response = client.post("/v1/diagnose", json=payload, headers=headers)
        assert response.status_code == 422  # Validation error

    def test_diagnose_response_structure(self, client, valid_auth_token):
        """Test the structure of a successful diagnosis response."""
        payload = {
            "plant_id": "PUNE-IN",
            "equipment_id": "CNC-A-102",
            "problem_description": "Machine overheating"
        }
        headers = {"X-Auth-Token": valid_auth_token}
        response = client.post("/v1/diagnose", json=payload, headers=headers)
        
        data = response.json()
        
        # Verify vision analysis structure
        assert isinstance(data["vision_analysis"], dict)
        assert "defects_found" in data["vision_analysis"]
        assert "confidence" in data["vision_analysis"]
        
        # Verify RAG guidance structure
        assert isinstance(data["rag_guidance"], dict)
        assert "recommended_steps" in data["rag_guidance"]
        assert "cited_documents" in data["rag_guidance"]
        
        # Verify report is a string
        assert isinstance(data["generated_report"], str)
        
        # Verify confidence score is a float between 0 and 1
        assert 0.0 <= data["confidence_score"] <= 1.0


class TestObservabilityMiddleware:
    """Test cases for observability middleware."""

    def test_trace_id_header_added(self, client):
        """Test that every response includes a trace ID."""
        response = client.get("/health")
        assert "X-Request-Trace-ID" in response.headers
        trace_id = response.headers["X-Request-Trace-ID"]
        assert len(trace_id) > 0

    def test_response_time_header_added(self, client):
        """Test that every response includes response time."""
        response = client.get("/health")
        assert "X-Response-Time-ms" in response.headers
        response_time = float(response.headers["X-Response-Time-ms"])
        assert response_time >= 0

    def test_different_requests_have_different_trace_ids(self, client):
        """Test that different requests get different trace IDs."""
        response1 = client.get("/health")
        response2 = client.get("/health")
        
        trace_id1 = response1.headers["X-Request-Trace-ID"]
        trace_id2 = response2.headers["X-Request-Trace-ID"]
        
        assert trace_id1 != trace_id2
