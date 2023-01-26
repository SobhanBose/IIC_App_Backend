from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import datetime
from typing import List
from app import models
from app.utils import database
from app.about import responseModels, schemas

router = APIRouter()

@router.get("/aboutus", status_code=status.HTTP_200_OK)
def about_us() -> dict:
    return {"data": "Lorem Ipsum"}