import requests

def test_get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
