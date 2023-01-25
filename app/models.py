from app.utils.database import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType


class User(Base):
    __tablename__ = 'users'

    username = Column(String, primary_key=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    email = Column(EmailType, unique=True, nullable=False)
    contact_no = Column(Integer, unique=True, nullable=False)
    pic = Column(String, nullable=True)

    team = relationship("Team", back_populates="user")


class Team(Base):
    __tablename__ = 'team'

    username = Column(String, ForeignKey("users.username"), primary_key=True)

    user = relationship("User", back_populates="team")


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    pic = Column(String, nullable=False)
    datetime = Column(DateTime, nullable=False)
    heading = Column(String, nullable=False)
    text = Column(String, nullable=False)



