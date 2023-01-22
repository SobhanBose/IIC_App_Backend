from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from . import schemas, models
from . import database
import datetime

app = FastAPI()

models.Base.metadata.create_all(database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


#ABOUT US
@app.get("/aboutus")
def home():
    return {"data": "Lorem Ipsum"}



#TEAM
@app.post("/team")
def add_team():
    return {"data": "data"}

@app.delete("/teams")
def delete_team():
    return {"data": "data"}

@app.put("/teams")
def update_team():
    return {"data": "data"}

@app.get("/team")
def team():
    return {"data": "data"}



#EVENTS
@app.post("/events", status_code=status.HTTP_201_CREATED)
def create_event(request: schemas.Event, db: Session = Depends(get_db)):
    new_event = models.Event(id=request.id, pic=request.pic, datetime=datetime.datetime.now(), heading=request.heading, text=request.text)
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event


@app.delete("/events/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_event(id: int, db: Session = Depends(get_db)):
    event = db.query(models.Event).filter(models.Event.id == id)
    if not event.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Event with id {id} not found")
    event.delete(synchronize_session=False)
    db.commit()
    return {"detail": "Event with id {id} was deleted"}


@app.put("/events/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_event(id: int, request: schemas.Event, db: Session = Depends(get_db)):
    event = db.query(models.Event).filter(models.Event.id == id)
    if not event.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Event with id {id} was not found") 
    else:
        event.update(request, synchronize_session=False)
    db.commit()
    return {"detail": f"Event with id {id} was updated"}


@app.get("/events", status_code=status.HTTP_200_OK)
def get_events(db: Session = Depends(get_db)):
    events = db.query(models.Event).all()
    return events


@app.get("/events/{id}")
def get_event_by_id(id: int, db: Session = Depends(get_db)):
    event = db.query(models.Event).filter(models.Event.id == id).first()
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Event with id {id} was not found")
    return event        