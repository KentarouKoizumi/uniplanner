from abc import ABC, abstractmethod

from app.application.data_object.dto.plan.create_plan_dto import CreatePlanDto
from app.domain.models.plan import Plan


class ICreatePlanUseCase(ABC):
    @abstractmethod
    def execute(self, planDto: CreatePlanDto) -> Plan:
        pass
