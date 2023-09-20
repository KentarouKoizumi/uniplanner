from uuid import UUID

from fastapi import Depends, HTTPException

from app.application.usecase.plan.get_plan.i_get_plan_usecase import (
    IGetPlanUseCase,
)
from app.domain.interfaces.repository.planRepositoryBase import IPlanRepository
from app.domain.models.plan import Plan
from app.infrastructure.dataAccess.repository.planRepository import (
    PlanRepository,
)


class GetPlanUseCase(IGetPlanUseCase):
    planRepository: IPlanRepository

    def __init__(self, planRepository: IPlanRepository = Depends(PlanRepository)):
        self.planRepository = planRepository

    def execute(self, plan_id: UUID) -> Plan:
        plan = self.planRepository.get_plan(plan_id)
        if plan is None:
            raise HTTPException(status_code=404, detail="Plan not found")
        return plan
