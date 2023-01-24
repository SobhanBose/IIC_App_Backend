from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import datetime
from typing import List
from app import models
from app.utils import database
from app.about import responseModels, schemas

router = APIRouter()

@router.get("/aboutus")
def about_us():
    return {"data": "Lorem Ipsum"}