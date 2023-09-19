from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import BaseModel


class UserModel(BaseModel):
    __tablename__ = "users"

    name = Column(String, nullable=False)
    plan_id = Column(UUID(as_uuid=True), ForeignKey("plans.id"))

    plan = relationship(
        "PlanModel", back_populates="users", cascade="save-update, delete"
    )
    answers = relationship(
        "AnswerModel", back_populates="user", cascade="save-update, delete"
    )
