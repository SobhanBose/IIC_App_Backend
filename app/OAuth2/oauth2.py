from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.user import schemas

from app.JWTtoken import token as jwttoken


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login/token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return jwttoken.verify_access_token(token, credentials_exception)


def get_current_active_user(current_user: schemas.User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
    
