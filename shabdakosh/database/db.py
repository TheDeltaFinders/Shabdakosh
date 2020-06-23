from contextlib import contextmanager

from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sqlalchemy_utils

from . import settings
from . import models

DeclarativeBase = models.DeclarativeBase 

def create_connection(database_dict):
    database_url = URL(**database_dict)
    if not sqlalchemy_utils.database_exists(database_url):
        sqlalchemy_utils.create_database(database_url)
    engine = create_engine(database_url)
    session = sessionmaker(bind=engine)
    return engine, session


def delete_connection(database_dict):
    database_url = URL(**database_dict)
    if sqlalchemy_utils.database_exists(database_url):
        sqlalchemy_utils.drop_database(database_url)


def drop_tables(engine):
    DeclarativeBase.metadata.drop_all(engine)


def create_tables(engine):
    DeclarativeBase.metadata.create_all(engine)



@contextmanager
def session_scope(Session=None):
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as error:
        session.rollback()
        raise error
    finally:
        session.close()

def reset(engine):
    drop_tables(engine)
    create_tables(engine)
