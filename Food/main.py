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


@app.get("/products", response_model=schemas.Products)
def read_objects(db: Session = Depends(get_db)):
    products = crud.get_products(db=db)
    return {"products": products}

@app.post("/products", response_model=schemas.Products)
def create_products(products: schemas.Products, db: Session = Depends(get_db)):
    for product in products.products:
        crud.create_product(db=db, object=product)
    # return "sucsess"
    return {"products": products.products}