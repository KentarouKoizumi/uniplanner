from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from .base import BaseModel


class Plan(BaseModel):
    __tablename__ = "plans"

    name = Column(String)
    description = Column(String)
    is_weekly = Column(Boolean, nullable=False)

    users = relationship(
        "User", back_populates="plan", cascade="save-update, delete"
    )
    schedules = relationship(
        "Schedule", back_populates="plan", cascade="save-update, delete"
    )
