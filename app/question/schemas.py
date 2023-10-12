from datetime import date

from pydantic import BaseModel


class SQuestion(BaseModel):
    id: int
    text_question: str
    text_answer: str
    date_to: date


class SNewQuestion(BaseModel):
    pass
