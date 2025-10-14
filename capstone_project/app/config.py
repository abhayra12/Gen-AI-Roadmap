# app/config.py

import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    """Application configuration settings."""
    APP_TITLE: str = "Manufacturing Copilot API"
    APP_VERSION: str = "1.0.0"
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    # In a real app, this would be a more robust secret management strategy
    VALID_AUTH_TOKEN_PREFIX: str = "Bearer technician-"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
