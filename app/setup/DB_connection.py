from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.setup.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

try:
    engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True)

    marker = sessionmaker(bind=engine)
    session = marker()

except Exception as ex:
    print(f"DB connection error: {str(ex)}")
