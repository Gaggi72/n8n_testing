from opensearchpy import OpenSearch

# Create a client instance
client = OpenSearch([{'host': 'localhost', 'port': 9200}])

# Define index name
index_name = 'my_index'

def search_query(query):
    response = client.search(index=index_name, body={'query': {'match': {'field': query}}})
    return response['hits']['hits']

if __name__ == '__main__':
    result = search_query('value')
    print(result)