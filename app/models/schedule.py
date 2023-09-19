from sqlalchemy import Column, Date, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import BaseModel


class ScheduleModel(BaseModel):
    __tablename__ = "schedules"

    date = Column(Date, nullable=False)
    period = Column(Integer, nullable=False)
    plan_id = Column(
        UUID(as_uuid=True), ForeignKey("plans.id"), nullable=False
    )

    plan = relationship(
        "PlanModel", back_populates="schedules", cascade="save-update, delete"
    )
    answers = relationship(
        "AnswerModel", back_populates="schedule", cascade="save-update, delete"
    )
