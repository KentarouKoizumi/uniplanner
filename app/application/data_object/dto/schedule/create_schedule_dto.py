from datetime import date

from pydantic import BaseModel


class CreateScheduleDto(BaseModel):
    date: date
    period: int
