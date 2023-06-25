from elasticsearch import Elasticsearch

from config import ES_HOST


MAPPING = {
            "properties": {
                "iD": {
                    "type": "long",
                },
                "text": {
                    "type": "text"
                }
            },
        }


def create_indexes():
    elastic_client: Elasticsearch = Elasticsearch(f"http://{ES_HOST}:9200")
    elastic_client.indices.create(index="documents", mappings=MAPPING)


if __name__ == "__main__":
    create_indexes()
