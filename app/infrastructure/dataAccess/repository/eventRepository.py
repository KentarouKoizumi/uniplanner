from uuid import UUID

from fastapi import Depends
from sqlalchemy.orm import Session

from app.domain.interfaces.repository.eventRepositoryBase import IEventRepository
from app.domain.models.event import Event
from app.infrastructure.dataAccess.database.settings import get_session


class EventRepository(IEventRepository):
    session: Session

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_event(self, event_id: UUID):
        return self.session.query(Event).filter(Event.id == event_id).first()

    def get_events(self):
        return self.session.query(Event).all()

    def create_event(self, event: Event):
        self.session.add(event)
        self.session.commit()

    def update_event(self, event: Event):
        self.session.add(event)
        self.session.commit()

    def delete_event(self, event_id: UUID):
        self.session.query(Event).filter(Event.id == event_id).delete()
        self.session.commit()
