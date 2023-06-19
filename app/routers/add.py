from fastapi import APIRouter

from app.setup.DB_connection import session
from app.models.models import Docs, PyDoc


add_router = APIRouter(prefix="/add", tags=['Document addition'])


@add_router.post("/")
def add_document(py_doc: PyDoc):
    # if data["rubrics"] == "" or data["doc_text"] == "":
    #     return {"message": f"Error: Null parameter"}
    doc = Docs(py_doc)
    session.add(doc)
    session.commit()
    return {"results": f"Document added successfully!"}
