from opensearchpy import OpenSearch

# Create a client instance
client = OpenSearch([{'host': 'localhost', 'port': 9200}])

# Define index name
index_name = 'my_index'
def delete_index():
    if client.indices.exists(index=index_name):
        client.indices.delete(index=index_name)
        print(f'Index {index_name} deleted.')
    else:
        print(f'Index {index_name} does not exist.')

if __name__ == '__main__':
    delete_index()