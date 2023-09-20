from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.models.plan import Plan


class IPlanRepository(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_plan(self, plan_id: UUID) -> Plan | None:
        pass

    @abstractmethod
    def get_plans(self) -> list[Plan]:
        pass

    @abstractmethod
    def create_plan(self, plan: Plan) -> None:
        pass

    @abstractmethod
    def update_plan(self, plan: Plan) -> None:
        pass

    @abstractmethod
    def delete_plan(self, plan_id: UUID) -> None:
        pass
