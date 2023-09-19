import uuid
from datetime import date

from pydantic import BaseModel


class ScheduleBase(BaseModel):
    date: date
    period: int


class ScheduleCreate(ScheduleBase):
    pass


class Schedule(ScheduleBase):
    id: uuid.UUID
    plan_id: uuid.UUID

    class Config:
        orm_mode = True
