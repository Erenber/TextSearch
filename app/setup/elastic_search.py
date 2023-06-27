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
    try:
        elastic_client: Elasticsearch = Elasticsearch(f"http://{ES_HOST}:{ES_PORT}")
        elastic_client.indices.create(index="documents", mappings=MAPPING)
    except Exception as ex:
        print(f"Ошибка при подключении к базе данных: {str(ex)}")


if __name__ == "__main__":
    create_indexes()
