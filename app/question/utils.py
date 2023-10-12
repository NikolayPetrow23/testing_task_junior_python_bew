import datetime

import aiohttp
from dateutil import parser

from app.config import URL_API
from app.question.dao import QuestionDAO


def date_format(date: str) -> datetime:
    created_at: datetime = parser.parse(date)
    created_at_date: datetime = created_at.date()
    return created_at_date


async def check_unique_question(data: list[dict]):
    questions = []
    for item in data:
        question = item.get("text_question")
        questions.append(question)
    results = await QuestionDAO.find_by_question(questions)
    return results


def unpacking_answers(json: dict) -> list[dict]:
    data = []

    for key in range(len(json)):
        data.append({
            "text_question": json[key].get("question"),
            "text_answer": json[key].get("answer"),
            "created_at": datetime.datetime.now()
        })
    return data


async def request_question(count):
    url = f"{URL_API}{count}"

    async with aiohttp.ClientSession() as session:
        while True:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    unpacked_answers = unpacking_answers(data)
                    res = await check_unique_question(unpacked_answers)
                    if res == []:
                        return unpacked_answers
                else:
                    return None
