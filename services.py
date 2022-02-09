from typing import List
from uuid import UUID


from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load, joinedload, contains_eager, load_only

from db.models import City, Shop, Street
from schemas import ShopCreateIn, ShopQueryParameters


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


async def insert_shop(session: AsyncSession, item: ShopCreateIn) -> UUID:
    statement = insert(Shop).values(**item.dict()).returning(Shop.id)
    result = await session.execute(statement)
    await session.commit()
    shop_id = result.scalar()
    return shop_id


async def get_shops(session: AsyncSession, query_parameters: ShopQueryParameters):
    statement = select(Shop).options(
        Load(Shop).load_only(
                Shop.id,
                Shop.name,
                Shop.building,
                Shop.open_time,
                Shop.close_time,
            ),
        joinedload(Shop.street).load_only(Street.id, Street.name).joinedload(Street.city).load_only(City.id, City.name),
    ).join(Shop.street).join(Street.city)
    if query_parameters.street_id:
        statement = statement.filter(Street.id == query_parameters.street_id)
    if query_parameters.city_id:
        statement = statement.filter(City.id == query_parameters.city_id)
    result = await session.execute(statement)
    shops = result.scalars().all()
    return shops
