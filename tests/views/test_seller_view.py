import ast
import random

from flask import json
from app.services.decode_service import decode_password
from app.services.encode_service import encode_password

def generated_email(max):
    return ''.join([random.choice("abcde") for _ in range(max)]) + '@gmail.com'


random_email = generated_email(20)


def new_seller_json():
    """retorna um json com as informações no novo seller"""

    return {
        'name': "Christopher",
        'email': random_email,
        'password': "121314"
    }


def test_create_seller(client):
    """cria um novo seller e compara o status"""
    json_data = new_seller_json()
    response = client.post('/register', json=json_data)
    token = json.loads(response.data)['data'].get('auth_token')
    
    key = json_data['password']
    print(key)
    encoded_data = encode_password(json_data)
    result = decode_password(encoded_data, key).get('user')['email']
    print(result)
    expected = json_data['email']
    
    assert token == result 
    assert response.status_code == 201


def test_login_seller(client):
    """loga com o novo seller criado e compara o status"""

    response = client.post('/login', json=new_seller_json())
    assert response.status_code == 200
    
