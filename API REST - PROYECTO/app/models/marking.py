from sqlalchemy import Column, Integer, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class Action(str, enum.Enum):
    entry = "entry"
    exit = "exit"

class Marking(Base):
    __tablename__ = "marking"

    marking_id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(TIMESTAMP)
    action = Column(Enum(Action))
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User")
