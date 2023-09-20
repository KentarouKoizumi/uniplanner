from uuid import UUID

from fastapi import Depends
from sqlalchemy.orm import Session

from app.domain.interfaces.repository.planRepositoryBase import IPlanRepository
from app.domain.models.plan import Plan
from app.infrastructure.dataAccess.database.settings import get_session


class PlanRepository(IPlanRepository):
    session: Session

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_plan(self, plan_id: UUID):
        return self.session.query(Plan).filter(Plan.id == plan_id).first()

    def get_plans(self):
        return self.session.query(Plan).all()

    def create_plan(self, plan: Plan):
        self.session.add(plan)
        self.session.commit()

    def update_plan(self, plan: Plan):
        self.session.add(plan)
        self.session.commit()

    def delete_plan(self, plan_id: UUID):
        self.session.query(Plan).filter(Plan.id == plan_id).delete()
        self.session.commit()
