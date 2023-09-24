from uuid import UUID

from fastapi import APIRouter, Depends

from app.application.data_object.dto.event.create_event_dto import CreateEventDto
from app.application.data_object.view_model.event.get_event_view_model import GetEventViewModel
from app.application.usecase.event.create_event.create_event_usecase import CreateEventUseCase
from app.application.usecase.event.create_event.i_create_event_usecase import ICreateEventUseCase
from app.application.usecase.event.get_event.get_event_usecase import GetEventUseCase
from app.application.usecase.event.get_event.i_get_event_usecase import IGetEventUseCase

router = APIRouter()


@router.get("/")
def get_events():
    return {"Hello": "World"}


@router.get("/{event_id}", response_model=GetEventViewModel)
def get_event(
    event_id: UUID,
    usecase: IGetEventUseCase = Depends(GetEventUseCase),
):
    return usecase.execute(event_id)


@router.post("/", response_model=GetEventViewModel)
def create_event(
    eventDto: CreateEventDto,
    usecase: ICreateEventUseCase = Depends(CreateEventUseCase),
):
    return usecase.execute(eventDto)
