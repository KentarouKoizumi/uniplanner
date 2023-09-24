from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.models.event import Event


class IEventRepository(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_event(self, event_id: UUID) -> Event | None:
        pass

    @abstractmethod
    def get_events(self) -> list[Event]:
        pass

    @abstractmethod
    def create_event(self, event: Event) -> None:
        pass

    @abstractmethod
    def update_event(self, event: Event) -> None:
        pass

    @abstractmethod
    def delete_event(self, event_id: UUID) -> None:
        pass
