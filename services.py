from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load

from db.models import City


async def get_cities(session: AsyncSession):
    statement = select(City).options(
        Load(City).load_only(City.id, City.name),
    )
    result = await session.execute(statement)
    cities = result.scalars().all()
    return cities
