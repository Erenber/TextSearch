#!/bin/sh

cd Alembic
alembic revision --autogenerate -m "DB creation"
alembic upgrade head
cd ..
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000