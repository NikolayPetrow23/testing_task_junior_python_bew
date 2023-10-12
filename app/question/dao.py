from sqlalchemy import select

from app.dao.dao import BaseDAO
from app.database import async_session_maker
from app.question.models import Question


class QuestionDAO(BaseDAO):
    model = Question

    @classmethod
    async def find_by_question(cls, text_questions: list[str]):
        async with async_session_maker() as session:
            query = select(cls.model).filter(cls.model.text_question.in_(text_questions))
            result = await session.execute(query)
            existing_questions = [row for row in result.scalars()]

        return existing_questions

    @classmethod
    async def last_item(cls):
        async with async_session_maker() as session:
            query = select(cls.model).order_by(cls.model.id.desc()).limit(1)
            result = await session.execute(query)
            row = result.fetchone()
            if row is not None:
                return row._asdict()
            else:
                return {}
