from sqlalchemy import Column, ForeignKey, Integer, String, Date, Table, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    brand = Column(String)
    count = Column(Integer)
    weight = Column(Float)
    protein = Column(Float)
    fat = Column(Float)
    сarbohydrate = Column(Float)
    kkal = Column(Float)
    shop = Column(String)
    date = Column(Date)
    cost = Column(Float)
    # numbers = relationship("Numbers_mobile")