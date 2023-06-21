#!/usr/bin/env bash

cd Alembic
alembic upgrade head
cd ..
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]