from opensearchpy import OpenSearch

# Create a client instance
client = OpenSearch([{'host': 'localhost', 'port': 9200}])

# Define index settings and mappings
index_name = 'my_index'
def create_index():
    if not client.indices.exists(index=index_name):
        client.indices.create(index=index_name)
        print(f'Index {index_name} created.')
    else:
        print(f'Index {index_name} already exists.')

if __name__ == '__main__':
    create_index()