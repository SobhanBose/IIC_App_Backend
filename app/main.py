from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.utils import database
from . import models

from app.events import router as events_router
from app.user import router as user_router
from app.team import router as team_router
from app.about import router as about_router


app = FastAPI()

models.Base.metadata.create_all(database.engine)

app.include_router(events_router.router, tags=["Events"])
app.include_router(user_router.router, tags=["User"])
app.include_router(team_router.router, tags=["Team"])
app.include_router(about_router.router, tags=["About Us"])
