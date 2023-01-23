from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import datetime
from typing import List
from app import models
from app.utils import database, hashing
from app.user import responseModels, schemas

router = APIRouter()

@router.post("/user", status_code=status.HTTP_201_CREATED, response_model=responseModels.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(username=request.username, password=hashing.hash_pswd(request.password), name=request.name, email=request.email, contact_no=request.contact_no, pic=request.pic)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.delete("/user/{username}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(username: str, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == username)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user{username} not found")
    user.delete(synchronize_session=False)
    db.commit()
    return {"detail": "user {username} was deleted"}


@router.put("/euser/{username}", status_code=status.HTTP_202_ACCEPTED)
def update_user(username: str, request: schemas.User, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == username)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {username} was not found") 
    else:
        user.update(request, synchronize_session=False)
    db.commit()
    return {"detail": f"User {username} was updated"}


@router.get("/user", status_code=status.HTTP_200_OK, response_model=List[responseModels.ShowUser])
def get_users(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users


@router.get("/users/{username}", status_code=status.HTTP_200_OK, response_model=responseModels.ShowUser)
def get_user_by_username(username: str, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user {username} not found")
    return user