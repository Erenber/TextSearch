from fastapi import APIRouter, Body

from app.setup.DB_connection import session
from app.models.models import Docs

delete_router = APIRouter(prefix="/delete", tags=['Deleting documents'])


@delete_router.delete("/")
async def delete_by_id(data=Body()):
    delete_id = int(data["id"])
    if delete_id == -1:
        result = session.query(Docs).delete()
    else:
        result = session.query(Docs).filter(Docs.id == delete_id).delete()
    session.commit()
    return result
