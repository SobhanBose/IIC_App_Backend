from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models
from app.utils import database
from app.team import responseModels, schemas

router = APIRouter()

@router.post("/team")
def add_team():
    return {"data": "data"}

@router.delete("/team")
def delete_team():
    return {"data": "data"}

@router.put("/team")
def update_team():
    return {"data": "data"}

@router.get("/team")
def team():
    return {"data": "data"}