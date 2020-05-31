
import requests


BASE_URL = 'http://localhost:5000/'
BAD_URL = 'http://localhost:5000/random'

def test_get_request():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

def test_invalid_request():
    response = requests.get(BAD_URL)
    assert response.status_code == 404

def test_get_request_with_valid_accept_header():
    response = requests.get(BASE_URL,headers={'Accept':'application/json'})
    assert response.json() == {'message': "Hello, World"}

def test_get_request_with_invalid_accept_header():
    response = requests.get(BASE_URL,headers={'Accept':'text/html'})
    assert response.text == "<p> Hello, World </p>"
