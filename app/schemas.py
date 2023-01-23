from pydantic import BaseModel

class Event(BaseModel):
    id: str
    pic: str
    heading: str
    text: str

class ShowEvent(Event):
    class Config():
        orm_mode = True