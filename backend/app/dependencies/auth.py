from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from clerk_backend_api import Clerk
from clerk_backend_api.jwks_helpers import AuthenticateRequestOptions

from app.config import settings

bearer_scheme = HTTPBearer()

# Initialize Clerk client
clerk_client = Clerk(bearer_auth=settings.CLERK_SECRET_KEY)

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    """
    Dependency to verify the Clerk JWT token and return user details.
    """
    token = credentials.credentials
    
    try:
        # Authenticate the request using the token
        request_state = clerk_client.authenticate_request(
            AuthenticateRequestOptions(
                secret_key=settings.CLERK_SECRET_KEY,
                token=token
            )
        )
        
        if not request_state.is_signed_in:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authenticated",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
        # Optional: You can fetch full user details if needed using request_state.to_auth().user_id
        # user = clerk_client.users.get(request_state.to_auth().user_id)
        
        return request_state.to_auth()
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication credentials: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )
