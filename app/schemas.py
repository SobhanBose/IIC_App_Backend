from pydantic import BaseModel

#EVENT Schemas
class Event(BaseModel):
    id: str
    pic: str
    heading: str
    text: str


class ShowEvent(Event):
    class Config():
        orm_mode = True


#USER Schemas
class User(BaseModel):
    id: int
    username: str
    password: str
    name: str
    email: str
    contact_no: int
    pic: str