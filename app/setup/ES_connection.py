from elasticsearch import Elasticsearch

from app.setup.config import ES_HOST, ES_PORT

es = Elasticsearch(f"http://{ES_HOST}:{ES_PORT}")
