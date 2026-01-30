from opensearchpy import OpenSearch

# Create a client instance
client = OpenSearch([{'host': 'localhost', 'port': 9200}])

# Define index name
index_name = 'my_index'

def bulk_insert(docs):
    client.bulk(index=index_name, body=docs)
    print('Bulk insert completed.')

if __name__ == '__main__':
    documents = [{'index': {}}]  # Your documents here
    bulk_insert(documents)