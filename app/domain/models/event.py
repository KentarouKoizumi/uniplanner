from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from .base import BaseModel


class Event(BaseModel):
    __tablename__ = "events"

    name = Column(String)
    description = Column(String)
    is_weekly = Column(Boolean, nullable=False)

    users = relationship("User", back_populates="event", cascade="save-update, delete")
    schedules = relationship("Schedule", back_populates="event", cascade="save-update, delete")
