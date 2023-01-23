from pydantic import BaseModel

#EVENT Schemas
class Event(BaseModel):
    id: int
    pic: str
    heading: str
    text: str