import uvicorn
from fastapi import FastAPI

from app.question.router import router as router_question


app = FastAPI(
    title="testing_task"
)

app.include_router(router_question)
