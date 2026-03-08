from fastapi import APIRouter, Depends
from typing import Any

from app.dependencies.auth import get_current_user

router = APIRouter()


@router.get("/me")
async def get_current_user_profile(user_auth: Any = Depends(get_current_user)) -> dict:
    """
    Example protected route testing Clerk authentication.
    Returns the user's ID and token details from the verified Clerk session.
    """
    return {
        "message": "You are authenticated securely via Clerk!",
        "user_id": user_auth.user_id,
        "session_id": user_auth.session_id,
    }
