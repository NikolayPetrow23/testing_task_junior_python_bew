from sqlalchemy import insert

from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def add_bulk_data(cls, data_list):
        async with async_session_maker() as session:
            insert_stmt = insert(cls.model)
            insert_values = [data for data in data_list]
            await session.execute(insert_stmt.values(insert_values))
            await session.commit()
