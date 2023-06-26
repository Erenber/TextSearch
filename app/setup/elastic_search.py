from elasticsearch import Elasticsearch

from config import ES_HOST, ES_PORT


MAPPING = {
            "properties": {
                "id": {
                    "type": "long",
                },
                "text": {
                    "type": "text"
                }
            },
        }


def create_indexes():
    elastic_client: Elasticsearch = Elasticsearch(f"http://{ES_HOST}:{ES_PORT}")
    elastic_client.indices.create(index="documents", mappings=MAPPING)


if __name__ == "__main__":
    create_indexes()
