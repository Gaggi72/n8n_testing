from opensearchpy import OpenSearch

# Create a client instance
client = OpenSearch([{'host': 'localhost', 'port': 9200}])

# Define index name and document ID
index_name = 'my_index'
document_id = '1'

# Define the document update
update_body = {'doc': {'field': 'value'}}
def update_document():
    client.update(index=index_name, id=document_id, body=update_body)
    print(f'Document {document_id} updated in index {index_name}.')

if __name__ == '__main__':
    update_document()