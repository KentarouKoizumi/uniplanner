from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.schemas.plan import Plan, PlanCreate

from . import crud
from .database.settings import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/plans/", response_model=Plan)
def create_plan(plan: PlanCreate, db: Session = Depends(get_db)):
    return crud.create_plan(db=db, plan=plan)
