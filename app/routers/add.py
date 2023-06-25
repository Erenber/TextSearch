from fastapi import APIRouter

from app.setup.DB_connection import session
from app.setup.ES_connection import es
from app.models.models import Docs, PyDoc


add_router = APIRouter(prefix="/add", tags=['Document addition'])

INDEX_NAME = "documents"

@add_router.post("/")
async def add_document(py_doc: PyDoc):
    doc = Docs(py_doc)
    session.add(doc)
    session.flush()
    session.commit()

    last_inserted_id = doc.id
    es.index(index=INDEX_NAME, body=doc.es_insert())

    return {"results": f"Документ успешно добавлен! {last_inserted_id}"}
