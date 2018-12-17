from app import create_app

'''Want to make sure the test configuration gets passed'''
def test_config():
	assert not create_app().testing
	assert create_app({'TESTING': True}).testing


'''Make sure the '/hello' route works properly'''
def test_hello(client):
	response = client.get('/hello')
	assert response.data == b'Hello World!'