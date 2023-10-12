from sqlalchemy import Column, Date, Integer, String

from app.database import Base


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    text_question = Column(String, nullable=False)
    text_answer = Column(String, nullable=False)
    created_at = Column(Date, nullable=False)
