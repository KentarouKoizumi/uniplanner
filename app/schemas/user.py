import uuid

from pydantic import BaseModel

from . import answer


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: uuid.UUID
    plan_id: uuid.UUID
    answers: list[answer.Answer]

    class Config:
        orm_mode = True
