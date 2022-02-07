from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import services
from db.base import get_session
from schemas import City


router = APIRouter()


@router.get('/cities', response_model=List[City])
async def get_cities(session: AsyncSession = Depends(get_session)) -> List[City]:
    cities = await services.get_cities(session=session)
    return cities
