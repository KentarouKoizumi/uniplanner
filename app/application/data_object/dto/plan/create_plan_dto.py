from pydantic import BaseModel

from app.application.data_object.dto.schedule.create_schedule_dto import (
    CreateScheduleDto,
)


class CreatePlanDto(BaseModel):
    name: str
    description: str
    is_weekly: bool
    schedules: list[CreateScheduleDto]
