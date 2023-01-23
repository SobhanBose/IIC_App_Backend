from pydantic import BaseModel
from app.events.schemas import Event

#EVENT Response Model
class ShowEvent(Event):
    class Config():
        orm_mode = True