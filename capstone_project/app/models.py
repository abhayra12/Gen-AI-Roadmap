# app/models.py

from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, Field

class DiagnosisRequest(BaseModel):
    """Request model for the main diagnosis endpoint."""
    plant_id: str = Field(
        ...,
        pattern=r"^[A-Z]{3,4}-\w{2,3}$",
        description="Unique plant identifier, e.g., 'PUNE-IN' or 'MEX-GTO'.",
        examples=["PUNE-IN"],
    )
    equipment_id: str = Field(
        ..., min_length=4, description="Tag or ID of the equipment.", examples=["CNC-A-102"]
    )
    problem_description: str = Field(
        ..., description="Technician's description of the issue."
    )
    image_id: Optional[str] = Field(
        None, description="ID of the uploaded image for visual inspection."
    )

class DiagnosisResponse(BaseModel):
    """Response model containing the combined output from all agents."""
    request_id: UUID
    vision_analysis: dict
    rag_guidance: dict
    generated_report: str
    confidence_score: float = Field(
        ..., ge=0.0, le=1.0, description="Overall confidence in the recommendation."
    )
    # New ML and Analytics insights (optional, will be added if available)
    ml_prediction: Optional[dict] = Field(None, description="ML Agent prediction results")
    analytics_insights: Optional[dict] = Field(None, description="Analytics Agent insights")
    safety_disclaimer: str = "Always follow standard safety procedures and consult a supervisor if unsure."

class HealthStatus(BaseModel):
    """Response model for the health check endpoint."""
    status: str = "ok"
