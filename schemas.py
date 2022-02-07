from pydantic import BaseModel, UUID4


class City(BaseModel):
    id: UUID4
    name: str

    class Config:
        orm_mode = True
