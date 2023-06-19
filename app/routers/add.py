from fastapi import APIRouter

from app.setup.DB_connection import session
from app.models.models import Docs, PyDoc


add_router = APIRouter(prefix="/add", tags=['Document addition'])


@add_router.post("/")
async def add_document(py_doc: PyDoc):
    doc = Docs(py_doc)
    session.add(doc)
    session.commit()
    return {"results": f"Document added successfully!"}
