# Репозиторий тестового задания на вакансию junir python-разработчик.

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


## Автор
Николай Петров - [GitHub](https://github.com/NikolayPetrow23)