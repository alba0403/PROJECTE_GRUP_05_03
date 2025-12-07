from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class Action(str, Enum):
    entry = "entry"
    exit = "exit"

class MarkingBase(BaseModel):
    marking_id: int
    timestamp: datetime
    action: Action
    user_id: int

    #alchemy
    class Config:
        orm_mode = True
