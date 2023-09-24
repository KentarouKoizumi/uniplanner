from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.models.event import Event


class IGetEventUseCase(ABC):
    @abstractmethod
    def execute(self, event_id: UUID) -> Event:
        pass
