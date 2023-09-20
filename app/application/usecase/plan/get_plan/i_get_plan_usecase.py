from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.models.plan import Plan


class IGetPlanUseCase(ABC):
    @abstractmethod
    def execute(self, plan_id: UUID) -> Plan:
        pass
