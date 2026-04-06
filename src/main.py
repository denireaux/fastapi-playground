import time
import logging
from fastapi import FastAPI
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Database connection URL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/mydatabase")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autobind=engine)

@app.on_event("startup")
def startup_event():
    logger.info("API started. Songs will be queried every 5 seconds.")

@app.get("/songs")
def get_songs():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM songs;"))
        return [dict(row._mapping) for row in result]

# Heartbeat Query
@app.get("/heartbeat-query")
def query_songs_loop():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT title FROM songs ORDER BY RANDOM() LIMIT 1;"))
        song = result.fetchone()
        return {"current_vibe": song[0] if song else "No songs found"}
