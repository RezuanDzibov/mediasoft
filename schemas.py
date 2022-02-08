from datetime import time

from pydantic import BaseModel, UUID4


class City(BaseModel):
    id: UUID4
    name: str

    class Config:
        orm_mode = True


class Street(BaseModel):
    id: UUID4
    name: str

    class Config:
        orm_mode = True


class ShopCreateIn(BaseModel):
    name: str
    building: str
    open_time: time
    close_time: time
    street_id: UUID4


class ShopCreateOut(BaseModel):
    id: UUID4
