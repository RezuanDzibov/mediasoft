from uuid import UUID
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import services
from db.base import get_session
from schemas import City, Street


router = APIRouter()


@router.get("/cities", response_model=List[City])
async def get_cities(session: AsyncSession = Depends(get_session)) -> List[City]:
    cities = await services.get_cities(session=session)
    return cities


@router.get("/cities/{city_id}/streets", response_model=List[Street])
async def get_city_streets(city_id: UUID, session: AsyncSession = Depends(get_session)) -> List[Street]:
    streets = await services.get_city_streets(session=session, city_id=str(city_id))
    return streets
