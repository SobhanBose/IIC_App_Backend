from pydantic import BaseModel
from app.schemas import Event, User

#EVENT Response Model
class ShowEvent(Event):
    class Config():
        orm_mode = True


#USER Response Model
class ShowUser(BaseModel):
    username: str
    name: str
    email: str
    contact_no: int
    pic: str

    class Config():
        orm_mode = True