from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
import datetime
import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/products", response_model=schemas.ProductsGet)
def read_products(db: Session = Depends(get_db)):
    products = crud.get_products(db=db)
    # res = []
    # for item in products:
        # print(item[0].__dict__ + item[1].__dict__)
        # a = dict(list(item[0].__dict__.items()) + list(item[1].__dict__.items()))
        # res.append(a)
    # for item in res:
    #     print(item)
    res = []
    for item in products:
        res.append(item[0])
    return {"products": res}

@app.get("/brands", response_model=schemas.BrandsGet)
def read_brands(db: Session = Depends(get_db)):
    brands = crud.get_brands(db=db)
    return {"brands": brands}

@app.post("/products", response_model=schemas.ProductsPost)
def create_products(products: schemas.ProductsPost, db: Session = Depends(get_db)):
    for product in products.products:
        crud.create_product(db=db, object=product)
    # return "sucsess"
    return products
    return {"products": products.products}

@app.post("/brands", response_model=schemas.Brands)
def create_brands(brands: schemas.Brands, db: Session = Depends(get_db)):
    for brand in brands.brands:
        crud.create_brand(db=db, object=brand)
    return brands
