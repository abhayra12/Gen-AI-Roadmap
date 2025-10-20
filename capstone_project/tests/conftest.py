"""Pytest configuration and shared fixtures."""

import pytest
import sys
from pathlib import Path

# Add the app directory to the Python path
app_dir = Path(__file__).parent.parent / "app"
sys.path.insert(0, str(app_dir))


@pytest.fixture
def sample_diagnosis_request():
    """Provide a sample diagnosis request payload."""
    return {
        "plant_id": "PUNE-IN",
        "equipment_id": "CNC-A-102",
        "problem_description": "Machine overheating during operation",
        "image_id": "img_12345"
    }


@pytest.fixture
def sample_vision_output():
    """Provide sample vision agent output."""
    return {
        "defects_found": ["micro-fracture", "surface-discoloration"],
        "confidence": 0.85,
    }


@pytest.fixture
def sample_rag_output():
    """Provide sample RAG agent output."""
    return {
        "recommended_steps": [
            "1. Inspect the primary coolant line for leaks.",
            "2. Verify torque settings on mounting bolts (Ref: SOP-123, Sec 4.2).",
            "3. Escalate to Level-2 maintenance if vibration exceeds 5mm/s.",
        ],
        "cited_documents": ["SOP-123", "MAINT-GUIDE-V2"],
    }
