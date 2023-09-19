import uuid

from pydantic import BaseModel


class AnswerBase(BaseModel):
    answer: int


class AnswerCreate(AnswerBase):
    pass


class Answer(AnswerBase):
    id: uuid.UUID
    schedule_id: uuid.UUID
    user_id: uuid.UUID

    class Config:
        orm_mode = True
