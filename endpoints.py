from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import services
from db.base import get_session
from schemas import City, ShopCreateIn, ShopCreateOut, Street


router = APIRouter()


@router.get("/cities", response_model=List[City])
async def get_cities(session: AsyncSession = Depends(get_session)) -> List[City]:
    cities = await services.get_cities(session=session)
    return cities


@router.get("/cities/{city_id}/streets", response_model=List[Street])
async def get_city_streets(city_id: UUID, session: AsyncSession = Depends(get_session)) -> List[Street]:
    streets = await services.get_city_streets(session=session, city_id=str(city_id))
    return streets


@router.post("/shops", response_model=ShopCreateOut)
async def create_shop(item: ShopCreateIn, session: AsyncSession = Depends(get_session)) -> ShopCreateOut:
    shop_id = await services.insert_shop(session=session, item=item)
    return ShopCreateOut(id=shop_id)
