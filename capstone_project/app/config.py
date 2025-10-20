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
    
    # HuggingFace Configuration (REQUIRED)
    HUGGINGFACE_TOKEN: str = Field(..., env="HUGGINGFACE_TOKEN")
    
    # Model Configuration - Using HuggingFace Inference Endpoints
    VLM_MODEL_ID: str = Field(default="Salesforce/blip2-opt-2.7b", env="VLM_MODEL_ID")
    LLM_MODEL_ID: str = Field(default="meta-llama/Llama-2-7b-chat-hf", env="LLM_MODEL_ID")
    EMBEDDING_MODEL_ID: str = Field(default="sentence-transformers/all-MiniLM-L6-v2", env="EMBEDDING_MODEL_ID")
    
    # API Configuration
    MAX_RETRIES: int = Field(default=3, env="MAX_RETRIES")
    REQUEST_TIMEOUT: int = Field(default=30, env="REQUEST_TIMEOUT")
    TEMPERATURE: float = Field(default=0.7, env="TEMPERATURE")
    MAX_TOKENS: int = Field(default=512, env="MAX_TOKENS")
    
    # ChromaDB Configuration
    CHROMA_HOST: str = Field(default="localhost", env="CHROMA_HOST")
    CHROMA_PORT: int = Field(default=8000, env="CHROMA_PORT")
    CHROMA_PERSIST_DIR: str = Field(default="./chroma_db", env="CHROMA_PERSIST_DIR")

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": False
    }

settings = Settings()
