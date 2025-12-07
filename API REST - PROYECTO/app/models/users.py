from sqlalchemy import Column, Integer, String, Enum
from app.database import Base
import enum

class Role(str, enum.Enum):
    student = "student"
    teacher = "teacher"
    admin = "admin"
    cleaning = "cleaning"

class Status(str, enum.Enum):
    active = "active"
    inactive = "inactive"
    blocked = "blocked"

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(36))
    name = Column(String(100))
    lastname = Column(String(100))
    role = Column(Enum(Role))
    email = Column(String(150), unique=True)
    status = Column(Enum(Status), default=Status.active)
    card_uid = Column(String(36), unique=True)
    password = Column(String(255))
