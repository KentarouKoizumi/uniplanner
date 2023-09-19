from uuid import UUID

from sqlalchemy.orm import Session

from app.models.plan import PlanModel
from app.models.schedule import ScheduleModel
from app.models.user import UserModel
from app.schemas.plan import PlanCreate
from app.schemas.user import UserCreate


def get_plan(db: Session, plan_id: UUID):
    return db.query(PlanModel).filter(PlanModel.id == plan_id).first()


def create_plan(db: Session, plan: PlanCreate):
    new_plan = PlanModel(
        name=plan.name,
        description=plan.description,
        is_weekly=plan.is_weekly,
        schedules=[
            ScheduleModel(**schedule.model_dump())
            for schedule in plan.schedules
        ],
    )
    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)
    return new_plan


def create_user(db: Session, user: UserCreate, plan_id: UUID):
    new_user = UserModel(**user.model_dump(), plan_id=plan_id)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
