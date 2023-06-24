from elasticsearch import Elasticsearch

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
    elastic_client: Elasticsearch = Elasticsearch("http://elastic:9200")    elastic_client.indices.create(index="documents", mappings=MAPPING)


if __name__ == "__main__":
    create_indexes()
