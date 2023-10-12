# Репозиторий тестового задания на вакансию junior python-разработчик.

## Требования к окружению

- **Python - 3.9**
- **FastAPI - 0.103.2**
- **Aiohttp - 3.8.6**
- **Pydantic - 1.10.8**
- **PostgreSQL - 13.3**
- **Docker - 4.19**
- **docker-compose - 3.8**

## Установка и запуск

```bash
# Установка репозитория
git clone git@github.com:NikolayPetrow23/testing_task_junior_python_bew.git
```

### Запустить данный проект можно двумя способами:
1. Запуск с помощью Docker
2. Обычный запуск проекта


### Запуск проекта с помощью Docker:
```bash
# Собираем образ контейнера приложения app.
docker compose build
```
```bash
# Запуск проекта с утановкой всех зависимостей.
docker compose up
```

### Запуск проекта в ручную:
```bash
# Установке зависимостей
pip install -r requirements.txt
```

```bash
# Поднятие базы данных с помощью Dokcer
docker run -p 5432:5432 --name "Имя вашей БД" -e POSTGRES_USER="Введите пользователя для БД" -e POSTGRES_PASSWORD="Введите пароль для БД" -e POSTGRES_DB="Имя вашей БД" -d postgres:13.3
```

```bash
# Выполните миграции
alembic upgrade head
```

```bash
# Запуск проекта
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Пример запросов и ответов API

### Запрос на запись случайного вопроса и ответа из стороннего API
```
# Endpoint
POST    /question
```

#### Пример запроса
```
/question?question_num=1
```

#### Пример ответа
```
{
  "Question": {
    "text_question": "As the Vietnam War raged & men were drafted who couldn't vote, the 26th amendment made the voting age this",
    "text_answer": "18",
    "created_at": "2022-12-30",
    "id": 1
  }
}
```

### Swagger (документация проекта)
```
GET     /docs#/Вопрос/question_question_post
```


## Автор
Николай Петров - [GitHub](https://github.com/NikolayPetrow23)