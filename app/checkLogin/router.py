from fastapi import APIRouter, status, Depends
from app.OAuth2 import oauth2
from app.user import schemas


router = APIRouter()

@router.get("/checkLogin", status_code=status.HTTP_200_OK)
def check_login(current_user: schemas.User = Depends(oauth2.get_current_user)):
    return {"data": "you are logged in"}