from abc import ABC, abstractmethod

from app.application.data_object.dto.event.create_event_dto import CreateEventDto
from app.domain.models.event import Event


class ICreateEventUseCase(ABC):
    @abstractmethod
    def execute(self, eventDto: CreateEventDto) -> Event:
        pass
