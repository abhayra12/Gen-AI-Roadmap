"""Unit tests for security and authentication."""

import pytest
from fastapi import HTTPException
from app.security import authorize_request
from app.config import settings


class TestAuthorization:
    """Test cases for the authorization dependency."""

    @pytest.mark.asyncio
    async def test_valid_auth_token(self):
        """Test that a valid token is accepted."""
        valid_token = f"{settings.VALID_AUTH_TOKEN_PREFIX}user123"
        user_id = await authorize_request(x_auth_token=valid_token)
        assert user_id == "user123"

    @pytest.mark.asyncio
    async def test_invalid_token_prefix(self):
        """Test that tokens with invalid prefix are rejected."""
        invalid_token = "InvalidPrefix user123"
        with pytest.raises(HTTPException) as exc_info:
            await authorize_request(x_auth_token=invalid_token)
        assert exc_info.value.status_code == 401
        assert "Invalid or missing authentication token" in str(exc_info.value.detail)

    @pytest.mark.asyncio
    async def test_empty_user_id(self):
        """Test that token with empty user ID is rejected."""
        empty_user_token = settings.VALID_AUTH_TOKEN_PREFIX  # Just the prefix, no user ID
        with pytest.raises(HTTPException) as exc_info:
            await authorize_request(x_auth_token=empty_user_token)
        assert exc_info.value.status_code == 401
        assert "User ID missing in token" in str(exc_info.value.detail)

    @pytest.mark.asyncio
    async def test_token_extraction(self):
        """Test correct extraction of user ID from token."""
        token = f"{settings.VALID_AUTH_TOKEN_PREFIX}technician-abc-xyz-123"
        user_id = await authorize_request(x_auth_token=token)
        assert user_id == "technician-abc-xyz-123"
