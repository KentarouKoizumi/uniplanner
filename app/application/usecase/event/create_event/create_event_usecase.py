from fastapi import Depends

from app.application.data_object.dto.event.create_event_dto import CreateEventDto
from app.application.usecase.event.create_event.i_create_event_usecase import ICreateEventUseCase
from app.domain.interfaces.repository.eventRepositoryBase import IEventRepository
from app.domain.models.event import Event
from app.domain.models.schedule import Schedule
from app.infrastructure.dataAccess.repository.eventRepository import EventRepository


class CreateEventUseCase(ICreateEventUseCase):
    eventRepository: IEventRepository

    def __init__(self, eventRepository: IEventRepository = Depends(EventRepository)):
        self.eventRepository = eventRepository

    def execute(self, eventDto: CreateEventDto) -> Event:
        event: Event = Event(
            name=eventDto.name,
            description=eventDto.description,
            is_weekly=eventDto.is_weekly,
            schedules=[Schedule(**schedule.model_dump()) for schedule in eventDto.schedules],
        )
        self.eventRepository.create_event(event)
        return event
