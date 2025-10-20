# app/config.py

import os
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    """Application configuration settings."""
    APP_TITLE: str = "Manufacturing Copilot API"
    APP_VERSION: str = "1.0.0"
    LOG_LEVEL: str = Field(default="INFO", env="LOG_LEVEL")
    
    # In a real app, this would be a more robust secret management strategy
    VALID_AUTH_TOKEN_PREFIX: str = "Bearer technician-"
    
    # Database configuration
    DATABASE_URL: str = Field(default="postgresql://copilot:copilot_pwd@localhost:5432/manufacturing_db", env="DATABASE_URL")

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": False
    }

settings = Settings()
