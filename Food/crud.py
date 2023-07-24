from sqlalchemy.orm import Session
from sqlalchemy.sql import func
import models
import schemas


def get_products(db: Session):
    products = db.query(models.Products).all()
    print(products)
    return products

def create_product(db: Session, object):
    print(object)
    product = models.Products(
        id=object.id,
        name=object.name,
        type=object.type,
        brand=object.brand,
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