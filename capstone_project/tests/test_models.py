"""Unit tests for the Manufacturing Copilot API models."""

import pytest
from uuid import UUID
from pydantic import ValidationError
from app.models import DiagnosisRequest, DiagnosisResponse, HealthStatus


class TestDiagnosisRequest:
    """Test cases for DiagnosisRequest model."""

    def test_valid_diagnosis_request(self):
        """Test creation of a valid diagnosis request."""
        request = DiagnosisRequest(
            plant_id="PUNE-IN",
            equipment_id="CNC-A-102",
            problem_description="Machine overheating during operation",
            image_id="img_12345"
        )
        assert request.plant_id == "PUNE-IN"
        assert request.equipment_id == "CNC-A-102"
        assert request.problem_description == "Machine overheating during operation"
        assert request.image_id == "img_12345"

    def test_valid_request_without_image(self):
        """Test creation of a valid request without an image."""
        request = DiagnosisRequest(
            plant_id="MEX-GTO",
            equipment_id="PUMP-B-05",
            problem_description="Unusual vibration detected"
        )
        assert request.image_id is None

    def test_invalid_plant_id_format(self):
        """Test that invalid plant ID formats are rejected."""
        with pytest.raises(ValidationError) as exc_info:
            DiagnosisRequest(
                plant_id="invalid-format",
                equipment_id="CNC-A-102",
                problem_description="Test"
            )
        errors = exc_info.value.errors()
        assert any("plant_id" in str(error) for error in errors)

    def test_equipment_id_too_short(self):
        """Test that equipment ID must be at least 4 characters."""
        with pytest.raises(ValidationError) as exc_info:
            DiagnosisRequest(
                plant_id="PUNE-IN",
                equipment_id="ABC",  # Too short
                problem_description="Test"
            )
        errors = exc_info.value.errors()
        assert any("equipment_id" in str(error) for error in errors)

    def test_missing_required_fields(self):
        """Test that required fields must be provided."""
        with pytest.raises(ValidationError):
            DiagnosisRequest()


class TestDiagnosisResponse:
    """Test cases for DiagnosisResponse model."""

    def test_valid_diagnosis_response(self):
        """Test creation of a valid diagnosis response."""
        response = DiagnosisResponse(
            request_id=UUID("12345678-1234-5678-1234-567812345678"),
            vision_analysis={"defects": ["crack", "rust"]},
            rag_guidance={"steps": ["Step 1", "Step 2"]},
            generated_report="Test report",
            confidence_score=0.85
        )
        assert isinstance(response.request_id, UUID)
        assert response.confidence_score == 0.85
        assert "Always follow standard safety procedures" in response.safety_disclaimer

    def test_confidence_score_validation(self):
        """Test that confidence score must be between 0 and 1."""
        with pytest.raises(ValidationError) as exc_info:
            DiagnosisResponse(
                request_id=UUID("12345678-1234-5678-1234-567812345678"),
                vision_analysis={},
                rag_guidance={},
                generated_report="Test",
                confidence_score=1.5  # Invalid: > 1.0
            )
        errors = exc_info.value.errors()
        assert any("confidence_score" in str(error) for error in errors)

    def test_default_safety_disclaimer(self):
        """Test that safety disclaimer has a default value."""
        response = DiagnosisResponse(
            request_id=UUID("12345678-1234-5678-1234-567812345678"),
            vision_analysis={},
            rag_guidance={},
            generated_report="Test",
            confidence_score=0.9
        )
        assert response.safety_disclaimer is not None
        assert len(response.safety_disclaimer) > 0


class TestHealthStatus:
    """Test cases for HealthStatus model."""

    def test_health_status_default(self):
        """Test default health status."""
        health = HealthStatus()
        assert health.status == "ok"

    def test_health_status_custom(self):
        """Test custom health status."""
        health = HealthStatus(status="degraded")
        assert health.status == "degraded"
