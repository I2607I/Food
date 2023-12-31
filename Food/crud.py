from sqlalchemy.orm import Session
from sqlalchemy.sql import func, text
import models
import schemas


def get_products(db: Session):
    products = db.query(models.Products, models.Brands).join(models.Brands).filter(models.Brands.id == models.Products.brand_id).all()
    for item in products:
        item[0].__dict__["brand"] = item[1].name
        print(item[0].__dict__)
        print(item[1].__dict__)
    return products

def get_products_sort(db: Session, param: str, limit: int, offset: int):
    products = db.query(models.Products).order_by(text(f'products.{param}')).offset(offset).limit(limit)
    return products

def get_brands(db: Session):
    brands = db.query(models.Brands).all()
    return brands

def create_product(db: Session, object):
    print(object)
    product = models.Products(
        name=object.name,
        type=object.type,
        brand_id=object.brand_id,
        count=object.count,
        weight=object.weight,
        protein=object.protein,
        fat=object.fat,
        сarbohydrate=object.сarbohydrate,
        kkal=object.kkal,
        shop=object.shop,
        date=object.date,
        cost=object.cost)
    db.add(product)
    db.commit()
    db.refresh(product)

def create_brand(db: Session, object):
    brand = models.Brands(
        name=object.name
    )
    db.add(brand)
    db.commit()
    db.refresh(brand)