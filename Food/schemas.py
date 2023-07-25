from typing import List
from pydantic import BaseModel, Field
import datetime
from uuid import UUID

class Product(BaseModel):
    name: str
    type: str
    # brand_id: int
    count: int | None
    weight: float = Field(gt=0)
    protein: float = Field(ge=0)
    fat: float = Field(ge=0)
    сarbohydrate: float = Field(ge=0)
    kkal: float = Field(ge=0)
    shop: str
    date: datetime.date | None
    cost: float = Field(gt=0)

class ProductGet(Product):
    brand: str
    id: int

class ProductPost(Product):
    brand_id: int


class ProductsPost(BaseModel):
    products: List[ProductPost]

    class Config:
        from_attributes = True

class ProductsGet(BaseModel):
    products: List[ProductGet]

class Brand(BaseModel):
    name: str

class BrandGet(Brand):
    id: int

class Brands(BaseModel):
    brands: List[Brand]

class BrandsGet(BaseModel):
    brands: List[BrandGet]