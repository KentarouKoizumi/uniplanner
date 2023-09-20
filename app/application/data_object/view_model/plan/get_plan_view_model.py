from uuid import UUID

from pydantic import BaseModel

from app.application.data_object.view_model.schedule.get_schedule_view_model import (
    GetScheduleViewModel,
)
from app.domain.models.plan import Plan


class GetPlanViewModel(BaseModel):
    def __init__(self, plan: Plan):
        super().__init__(**plan.__dict__)

    id: UUID
    name: str
    description: str
    is_weekly: bool
    schedules: list[GetScheduleViewModel]
