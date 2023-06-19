from fastapi import FastAPI
from fastapi.responses import FileResponse

from app.routers.search import search_router
from app.routers.add import add_router
from app.routers.delete import delete_router

app = FastAPI()

app.include_router(search_router)
app.include_router(add_router)
app.include_router(delete_router)


@app.get("/")
async def root():
    return FileResponse("app/templates/app/main.html")
