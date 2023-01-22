from .database import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy_utils import EmailType


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(EmailType, unique=True, nullable=False)
    contact_no = Column(Integer, unique=True, nullable=False)
    pic = Column(String)


class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True)


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    pic = Column(String, nullable=False)
    datetime = Column(DateTime, nullable=False)
    heading = Column(String, nullable=False)
    text = Column(String, nullable=False)



