from fastapi import FastAPI, Depends
from sqlalchemy import text
from src.utils import get_logger, database_init, get_db_conn

log = get_logger()
app = FastAPI()
engine, SessionLocal = database_init()

@app.on_event("startup")
def startup_event():
    log.info("API started. Songs will be queried every 5 seconds.")

@app.get("/songs")
def get_songs(conn = Depends(get_db_conn), limit: int = 50):
    result = conn.execute(text("SELECT * FROM songs LIMIT :l"), {"l": limit})
    return [dict(row._mapping) for row in result]

@app.get("/heartbeat-query")
def query_songs_loop(conn = Depends(get_db_conn)):
    result = conn.execute(text("SELECT title FROM songs ORDER BY RANDOM() LIMIT 1;"))
    song = result.fetchone()
    return {"current_vibe": song[0] if song else "No songs found"}
