from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from .base import BaseModel


class PlanModel(BaseModel):
    __tablename__ = "plans"

    name = Column(String)
    description = Column(String)
    is_weekly = Column(Boolean, nullable=False)

    users = relationship(
        "UserModel", back_populates="plan", cascade="save-update, delete"
    )
    schedules = relationship(
        "ScheduleModel", back_populates="plan", cascade="save-update, delete"
    )
