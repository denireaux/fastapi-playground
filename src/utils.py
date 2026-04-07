from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os
import logging


def database_init(database_url=None):
    if database_url is None:
        database_url = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/mydatabase")
        
    engine = create_engine(database_url)
    SessionLocal = sessionmaker(bind=engine) 
    
    return engine, SessionLocal

def get_db_conn():
    engine, SessionLocal = database_init()
    
    with engine.connect() as conn:
        yield conn

def get_logger():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    return logger
