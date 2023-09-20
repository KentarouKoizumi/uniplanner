from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import BaseModel


class Answer(BaseModel):
    __tablename__ = "answers"

    answer = Column(
        Integer, CheckConstraint("answer in (0,1,2)"), nullable=False
    )
    user_id = Column(
        UUID(as_uuid=True), ForeignKey("users.id"), nullable=False
    )
    schedule_id = Column(
        UUID(as_uuid=True), ForeignKey("schedules.id"), nullable=False
    )

    user = relationship(
        "User", back_populates="answers", cascade="save-update, delete"
    )
    schedule = relationship(
        "Schedule",
        back_populates="answers",
        cascade="save-update, delete",
    )
