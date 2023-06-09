from fastapi import APIRouter, Body
from starlette.responses import JSONResponse

from app.setup.DB_connection import session
from app.setup.ES_connection import es, INDEX_NAME
from app.models.models import Docs


delete_router = APIRouter(prefix="/delete", tags=['Deleting documents'])


@delete_router.delete("/")
async def delete_by_id(data=Body()):
    try:
        delete_id = int(data["id"])
        if delete_id == -1:
            result = session.query(Docs).delete()
            es.delete_by_query(index=INDEX_NAME, body={
                                                        "query": {
                                                            "match_all": {}
                                                        }
                                                      }
                               )
        else:
            result = session.query(Docs).filter(Docs.id == delete_id).delete()
            es.delete_by_query(index=INDEX_NAME, body={
                                                        "query": {
                                                            "match": {
                                                                "id": delete_id
                                                            }
                                                        }
                                                      }
                               )
        session.commit()
        return result

    except Exception as ex:
        return JSONResponse(
            status_code=500,
            content={"error": str(ex)},
        )
