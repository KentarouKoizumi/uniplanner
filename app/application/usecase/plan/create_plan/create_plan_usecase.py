from fastapi import Depends

from app.application.data_object.dto.plan.create_plan_dto import CreatePlanDto
from app.application.usecase.plan.create_plan.i_create_plan_usecase import (
    ICreatePlanUseCase,
)
from app.domain.interfaces.repository.planRepositoryBase import IPlanRepository
from app.domain.models.plan import Plan
from app.domain.models.schedule import Schedule
from app.infrastructure.dataAccess.repository.planRepository import (
    PlanRepository,
)


class CreatePlanUseCase(ICreatePlanUseCase):
    planRepository: IPlanRepository

    def __init__(
        self, planRepository: IPlanRepository = Depends(PlanRepository)
    ):
        self.planRepository = planRepository

    def execute(self, planDto: CreatePlanDto) -> Plan:
        plan: Plan = Plan(
            name=planDto.name,
            description=planDto.description,
            is_weekly=planDto.is_weekly,
            schedules=[
                Schedule(**schedule.model_dump())
                for schedule in planDto.schedules
            ],
        )
        self.planRepository.create_plan(plan)
        return plan
