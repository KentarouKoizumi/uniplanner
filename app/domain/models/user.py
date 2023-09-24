from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    name = Column(String, nullable=False)
    event_id = Column(UUID(as_uuid=True), ForeignKey("events.id"))

    event = relationship("Event", back_populates="users", cascade="save-update, delete")
    answers = relationship("Answer", back_populates="user", cascade="save-update, delete")
