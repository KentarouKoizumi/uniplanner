from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel


class GetScheduleViewModel(BaseModel):
    id: UUID
    plan_id: UUID
    date: date
    period: int
    created_at: datetime
