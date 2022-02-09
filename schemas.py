from datetime import datetime, time
from enum import Enum
from typing import Optional

from pydantic import BaseModel, UUID4, validator


class City(BaseModel):
    id: UUID4
    name: str

    class Config:
        orm_mode = True
        allow_mutation = True


class Street(BaseModel):
    id: UUID4
    name: str

    class Config:
        orm_mode = True
        allow_mutation = True


class ShopCreateIn(BaseModel):
    name: str
    building: str
    open_time: time
    close_time: time
    street_id: UUID4


class ShopCreateOut(BaseModel):
    id: UUID4


class ShopIsOpenEnum(Enum):
    is_closed = 0
    is_open = 1


class ShopQueryParameters(BaseModel):
    street_id: Optional[UUID4]
    city_id: Optional[UUID4]


class ShopRetrieveStreet(Street):
    city: City


class ShopRetrive(BaseModel):
    id: UUID4
    name: str
    open_time: time
    close_time: time
    is_open: int = None
    street: ShopRetrieveStreet

    class Config:
        orm_mode = True
        json_encoders = {time: lambda v: v.strftime("%H:%M")}

    @validator("is_open", always=True, pre=True, check_fields=False)
    def set_is_open(cls, v, values, **kwargs) -> int:
        now = time(*map(int, datetime.now().strftime("%H:%M").split(":")))
        shop_is_open: int
        if now > values.get("open_time") and now < values.get("close_time"):
            shop_is_open = 1
        else:
            shop_is_open = 0
        return shop_is_open
