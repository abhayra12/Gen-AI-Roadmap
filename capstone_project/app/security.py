# app/security.py

from fastapi import Header, HTTPException
from .config import settings

async def authorize_request(x_auth_token: str = Header(...)):
    """
    Dependency to check for a valid authentication token in the request header.
    
    Raises:
        HTTPException: 401 if the token is missing or invalid.
    
    Returns:
        str: The user ID extracted from the token.
    """
    if not x_auth_token.startswith(settings.VALID_AUTH_TOKEN_PREFIX):
        raise HTTPException(
            status_code=401, 
            detail="Invalid or missing authentication token."
        )
    # Extract user ID from "Bearer technician-<user_id>"
    user_id = x_auth_token.removeprefix(settings.VALID_AUTH_TOKEN_PREFIX)
    if not user_id:
        raise HTTPException(status_code=401, detail="User ID missing in token.")
    return user_id
