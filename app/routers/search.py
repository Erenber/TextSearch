from fastapi import APIRouter

from app.setup.DB_connection import session
from app.setup.ES_connection import es, INDEX_NAME
from app.models.models import Docs

search_router = APIRouter(prefix="/search", tags=['Document search'])


@search_router.get("/all")
async def return_all():
    try:
        return [doc for doc in session.query(Docs)]
    except Exception as ex:
        return {"results": str(ex)}


@search_router.get("/{text}")
async def search_text(text: str):
    try:
        es_docs = es.search(index=INDEX_NAME, source={"includes": ["id"]},
                            query={
                                "query_string": {
                                    "query": f"*{text.lower()}*",
                                    "fields": ["text"],
                                    "default_operator": "AND"
                                }
                            }
                            , size=1000)
        document_ids = [document["_source"]["id"] for document in es_docs.body["hits"]["hits"]]

        result = session.query(Docs) \
            .filter(Docs.id.in_(document_ids)) \
            .order_by(Docs.created_date.desc()) \
            .limit(20)

        return [doc for doc in result]

    except Exception as ex:
        return {"results": str(ex)}
