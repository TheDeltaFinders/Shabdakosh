from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Column

DeclarativeBase = declarative_base()

class Base(DeclarativeBase):
    __abstract__ = True


class BaseWord(Base):
    __tablename__ = "words"
    word_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

class  SubWord(Base):
    __tablename__ = 'sub_words'
    sub_word_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

