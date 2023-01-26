from fastapi import APIRouter, status, Depends
from app.OAuth2 import oauth2
from app.user import schemas, responseModels


router = APIRouter()

@router.get("/checkLogin", status_code=status.HTTP_200_OK, response_model=responseModels.ShowUser)
def check_login(current_user: schemas.User = Depends(oauth2.get_current_user)) -> responseModels.ShowUser:
    return current_user