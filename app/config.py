import os
from dotenv import load_dotenv

load_dotenv()


DB_HOST: str = os.getenv("DB_HOST")
DB_PORT: int = os.getenv("DB_PORT")
DB_USER: str = os.getenv("DB_USER")
DB_PASS: str = os.getenv("DB_PASS")
DB_NAME: str = os.getenv("DB_NAME")

URL_API: str = os.getenv("URL_API")


def database_url():
    user = f"{DB_USER}:{DB_PASS}"
    database = f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
    return f"postgresql+asyncpg://{user}@{database}"
