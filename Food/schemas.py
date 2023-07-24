from typing import List
from pydantic import BaseModel
import datetime
from uuid import UUID


class Product(BaseModel):
    id: int
    name: str
    type: str
    brand: str
    count: int | None
    weight: float
    protein: float
    fat: float
    сarbohydrate: float
    kkal: float
    shop: str
    date: datetime.date | None
    cost: float

class Products(BaseModel):
    products: List[Product]

    class Config:
        from_attributes = True