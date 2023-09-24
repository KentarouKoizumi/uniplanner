from sqlalchemy import Column, Date, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import BaseModel


class Schedule(BaseModel):
    __tablename__ = "schedules"

    date = Column(Date, nullable=False)
    period = Column(Integer, nullable=False)
    event_id = Column(UUID(as_uuid=True), ForeignKey("events.id"), nullable=False)

    event = relationship("Event", back_populates="schedules", cascade="save-update, delete")
    answers = relationship("Answer", back_populates="schedule", cascade="save-update, delete")
