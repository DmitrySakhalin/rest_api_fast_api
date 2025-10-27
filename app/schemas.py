from datetime import datetime
from pydantic import BaseModel, Field


class AdvertisementCreate(BaseModel):
    title: str = Field(..., max_length=100)
    description: str
    price: float
    author: str


class AdvertisementUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    price: float | None = None


class AdvertisementResponse(BaseModel):
    id: int
    title: str
    description: str
    price: float
    author: str
    created_at: datetime

    class Config:
        orm_mode = True
