import uuid
from datetime import datetime

from pydantic import BaseModel

from app.schemas.schedule import Schedule, ScheduleCreate
from app.schemas.user import User


class PlanBase(BaseModel):
    name: str
    description: str
    is_weekly: bool


class PlanCreate(PlanBase):
    schedules: list[ScheduleCreate]


class Plan(PlanBase):
    id: uuid.UUID
    created_at: datetime
    users: list[User] = []
    schedules: list[Schedule] = []

    class Config:
        orm_mode = True
