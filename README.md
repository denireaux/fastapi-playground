# FastAPI Playground

A containerized full-stack environment for experimenting with **FastAPI**, **PostgreSQL**, and **Background Workers**. This project demonstrates microservice orchestration using Docker Compose and automated database initialization.

---

## Project Structure

```text
api-service/
├── docker/
│   ├── api.Dockerfile         # FastAPI application environment
│   └── heartbeat.Dockerfile   # Standalone Python worker
├── src/
│   ├── __init__.py            # Makes src a Python package
│   ├── main.py                # FastAPI entry point & DB logic
│   └── heartbeat_main.py      # Background heartbeat service
├── database/
│   └── init.sql               # Seed data (Songs table)
├── docker-compose.yaml        # Local orchestration
└── requirements.txt           # Shared Python dependencies
```

## Usage
```docker compose up --build```

## Database Schema
The database is pre-seeded via database/init.sql with a songs table containing:

    One by Metallica (Metal)
    Ethernal by HANA (Trance)
    To Hide to Shine to Cross by Bragolin (Post Punk)

## Accessing the services
    FastAPI Docs (Swagger): http://localhost:8000/docs
    API Endpoint: http://localhost:8000/songs
    Heartbeat Logs: Run docker compose logs -f heartbeat to see the background pulse.