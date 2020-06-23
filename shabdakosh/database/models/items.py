from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Column

from .. import db

Base = declarative_base()

class Items(db.DeclarativeBase):
    """
    Item
    """

    __tablename__ = "Items"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sku = Column(String)

