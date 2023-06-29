from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.setup.DB_connection import session
from app.setup.ES_connection import es, INDEX_NAME
from app.models.models import Docs, PyDoc

add_router = APIRouter(prefix="/add", tags=['Document addition'])


@add_router.post("/")
async def add_document(py_doc: PyDoc):
    try:
        doc = Docs(py_doc)
        session.add(doc)
        session.flush()
        session.commit()

        last_inserted_id = doc.id
        es.index(index=INDEX_NAME, body=doc.es_insert())

        return {"results": f"Документ №{last_inserted_id} успешно добавлен!"}

    except Exception as ex:
        return JSONResponse(
            status_code=500,
            content={"error": str(ex)},
        )
