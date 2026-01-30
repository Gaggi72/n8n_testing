from opensearchpy import OpenSearch

# Create a client instance
client = OpenSearch([{'host': 'localhost', 'port': 9200}])

# Define index name and settings
index_name = 'my_index'
settings = {
    'settings': {'number_of_shards': 1, 'number_of_replicas': 0},
    'mappings': {'properties': {'field': {'type': 'text'}}}
}
def create_index_with_settings():
    if not client.indices.exists(index=index_name):
        client.indices.create(index=index_name, body=settings)
        print(f'Index {index_name} with settings created.')
    else:
        print(f'Index {index_name} already exists.')

if __name__ == '__main__':
    create_index_with_settings()