from pydantic import BaseModel
from enum import Enum

class Role(str, Enum):
    student = "student"
    teacher = "teacher"
    admin = "admin"
    cleaning = "cleaning"

class Status(str, Enum):
    active = "active"
    inactive = "inactive"
    blocked = "blocked"

class UserBase(BaseModel):
    id: int
    name: str
    lastname: str
    email: str
    card_uid: str | None

    class Config:
        orm_mode = True
