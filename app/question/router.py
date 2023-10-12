from fastapi import APIRouter, status

from app.question.dao import QuestionDAO
from app.question.schemas import SQuestion
from app.question.utils import request_question

router = APIRouter(
    prefix="/question",
    tags=["Вопрос"],
)


@router.post("", status_code=status.HTTP_201_CREATED)
async def question(question_num: int) -> list[SQuestion]:
    data: list[dict] = await request_question(question_num)
    last_item = await QuestionDAO.last_item()
    await QuestionDAO.add_bulk_data(data)
    return last_item
