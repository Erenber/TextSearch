from fastapi import APIRouter

#from DB_connection import session
from app.setup.DB_connection import session
from app.models.models import Docs


search_router = APIRouter(prefix="/search", tags=['Document surch'])


@search_router.get("/all")
async def return_all():
    return [doc for doc in session.query(Docs)]


@search_router.get("/{text}")
async def search_text(text: str):
    result = session.query(Docs).filter(Docs.doc_text.like(f"%{text}%")).order_by(Docs.created_date.desc())
    return [doc for doc in result]
