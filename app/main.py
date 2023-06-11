from fastapi import FastAPI
from datetime import datetime


def get_date():
    time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return tuple(time.split())


app = FastAPI()
documents = [
    {"id": 1, "rubricks": "Ne znaiu shto eto...", "text": "Artik is cool", "created_data": get_date()},
    {"id": 2, "rubricks": "Ne znaiu shto eto...", "text": "EEEEE", "created_data": get_date()},
    {"id": 3, "rubricks": "Ne znaiu shto eto...", "text": "Dima bro", "created_data": get_date()},
    {"id": 4, "rubricks": "Ne znaiu shto eto...", "text": "Modsen modsen", "created_data": get_date()},
]


@app.get("/documents/{text}")
def search(text):
    return [doc for doc in documents if text in doc["text"]]


@app.get("/")
def main_page():
    return 'Main page. .documents to look through the documents. documents/... to look through the documents containing...    '


@app.get("/documents")
def get_documents():
    return documents
