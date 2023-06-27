from elasticsearch import Elasticsearch

from app.setup.config import ES_HOST, ES_PORT


INDEX_NAME = "documents"

try:
    es = Elasticsearch(f"http://{ES_HOST}:{ES_PORT}")
except Exception as ex:
    print(f"DB connection error: {str(ex)}")

