from pydantic import BaseModel

class Event(BaseModel):
    id: str
    pic: str
    heading: str
    text: str