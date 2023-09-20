from uuid import UUID

from fastapi import APIRouter, Depends

from app.application.data_object.dto.plan.create_plan_dto import CreatePlanDto
from app.application.data_object.view_model.plan.get_plan_view_model import (
    GetPlanViewModel,
)
from app.application.usecase.plan.create_plan.create_plan_usecase import (
    CreatePlanUseCase,
)
from app.application.usecase.plan.create_plan.i_create_plan_usecase import (
    ICreatePlanUseCase,
)
from app.application.usecase.plan.get_plan.get_plan_usecase import (
    GetPlanUseCase,
)
from app.application.usecase.plan.get_plan.i_get_plan_usecase import (
    IGetPlanUseCase,
)

router = APIRouter()


@router.get("/")
def get_plans():
    return {"Hello": "World"}


@router.get("/{plan_id}", response_model=GetPlanViewModel)
def get_plan(
    plan_id: UUID,
    usecase: IGetPlanUseCase = Depends(GetPlanUseCase),
):
    return usecase.execute(plan_id)


@router.post("/")
def create_plan(
    planDto: CreatePlanDto,
    usecase: ICreatePlanUseCase = Depends(CreatePlanUseCase),
):
    return usecase.execute(planDto)
