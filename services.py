from uuid import UUID
from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load

from db.models import City, Street


async def get_cities(session: AsyncSession) -> List[City]:
    statement = select(City).options(
        Load(City).load_only(City.id, City.name),
    )
    result = await session.execute(statement)
    cities = result.scalars().all()
    return cities


async def get_city_streets(session: AsyncSession, city_id: str) -> List[Street]:
    statement = select(Street).where(Street.city_id == city_id).options(
        Load(Street).load_only(Street.id, Street.name),
    )
    result = await session.execute(statement)
    streets = result.scalars().all()
    return streets
