from uuid import UUID

from fastapi import Depends, HTTPException

from app.application.usecase.event.get_event.i_get_event_usecase import IGetEventUseCase
from app.domain.interfaces.repository.eventRepositoryBase import IEventRepository
from app.domain.models.event import Event
from app.infrastructure.dataAccess.repository.eventRepository import EventRepository


class GetEventUseCase(IGetEventUseCase):
    eventRepository: IEventRepository

    def __init__(self, eventRepository: IEventRepository = Depends(EventRepository)):
        self.eventRepository = eventRepository

    def execute(self, event_id: UUID) -> Event:
        event = self.eventRepository.get_event(event_id)
        if event is None:
            raise HTTPException(status_code=404, detail="Event not found")
        return event
