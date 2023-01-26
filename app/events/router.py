from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import datetime
from typing import List
from app import models
from app.utils import database
from app.events import responseModels, schemas

router = APIRouter()

@router.post("/events", status_code=status.HTTP_201_CREATED, response_model=responseModels.ShowEvent)
def create_event(request: schemas.Event, db: Session = Depends(database.get_db)) -> responseModels.ShowEvent:
    new_event = models.Event(id=request.id, pic=request.pic, datetime=datetime.datetime.now(), heading=request.heading, text=request.text)
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event


@router.delete("/events/{id}", status_code=status.HTTP_200_OK)
def delete_event(id: int, db: Session = Depends(database.get_db)) -> dict:
    event = db.query(models.Event).filter(models.Event.id == id)
    if not event.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Event with id {id} not found")
    event.delete(synchronize_session=False)
    db.commit()
    return {"detail": "Event with id {id} was deleted"}


@router.put("/events/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_event(id: int, request: schemas.Event, db: Session = Depends(database.get_db)) -> dict:
    event = db.query(models.Event).filter(models.Event.id == id)
    if not event.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Event with id {id} was not found") 
    else:
        event.update(request, synchronize_session=False)
    db.commit()
    return {"detail": f"Event with id {id} was updated"}


@router.get("/events", status_code=status.HTTP_200_OK, response_model=List[responseModels.ShowEvent])
def get_events(db: Session = Depends(database.get_db)) -> List[responseModels.ShowEvent]:
    events = db.query(models.Event).all()
    return events


@router.get("/events/{id}", status_code=status.HTTP_200_OK, response_model=responseModels.ShowEvent)
def get_event_by_id(id: int, db: Session = Depends(database.get_db)) -> responseModels.ShowEvent:
    event = db.query(models.Event).filter(models.Event.id == id).first()
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Event with id {id} was not found")
    return event