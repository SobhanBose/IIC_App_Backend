from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models
from app.utils import database
from app.team import responseModels, schemas

router = APIRouter()

@router.post("/team/", status_code=status.HTTP_201_CREATED, response_model=responseModels.ShowTeam)
def add_team(request: schemas.Team, db: Session = Depends(database.get_db)) -> responseModels.ShowTeam:
    new_team_member = models.Team(username=request.username)
    db.add(new_team_member)
    db.commit()
    db.refresh(new_team_member)
    return new_team_member


@router.delete("/team/{username}", status_code=status.HTTP_200_OK)
def delete_team(username: str, db: Session = Depends(database.get_db)) -> dict:
    team_member = db.query(models.Team).filter(models.Team.username==username)
    if not team_member.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"team member {username} not found")
    team_member.delete(synchronize_session=False)
    db.commit()
    return {"detail": f"team member {username} was deleted"}


@router.get("/team", status_code=status.HTTP_302_FOUND, response_model=List[responseModels.ShowTeam])
def get_team(db: Session = Depends(database.get_db)) -> responseModels.ShowTeam:
    team_members = db.query(models.Team).all()
    return team_members