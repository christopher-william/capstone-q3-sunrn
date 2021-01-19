import random

from flask import json
from tests.database_connection import execute_sql_comand_in_database


def email_generator(max):
    return ''.join([
        random.choice("abcdefghijqlimnopkrstuvxwyz")
        for _ in range(max)
    ]) + '@gmail.com'


random_email = email_generator(10)


def new_seller_json():
    """retorna um json com as informações no novo seller"""

    return {
        'name': "[TEST] Example Name",
        'email': random_email,
        'password': "121314"
    }


def test_create_seller(client):
    """cria um novo seller e compara o status"""

    json_data = new_seller_json()
    response = client.post('/register', json=json_data)

    data_result = json.loads(response.data)

    status_result = response.status_code
    assert status_result == 201

    id, name, email = execute_sql_comand_in_database(
        """SELECT id, name, email FROM seller"""
    )[-1]

    last_seller = {"id": id, "name": name, "email": email}

    assert sorted(data_result['user'].keys()) == sorted(last_seller.keys())
    assert sorted(data_result['user'].values()) == sorted(last_seller.values())

    assert type(data_result['auth_token']) is str
    assert len(data_result['auth_token']) > 15


def test_login_seller(client):
    """loga com o novo seller criado e compara o status"""

    json_data = new_seller_json()
    response = client.post('/login', json=json_data)

    data_result = json.loads(response.data)

    status_result = response.status_code
    assert status_result == 200

    id, name, email = execute_sql_comand_in_database(
        f"""SELECT id, name , email FROM seller WHERE seller.email = '{json_data['email']}'"""
    )[0]

    lead_logged = {"id": id, "name": name, "email": email}

    assert data_result['user'] == lead_logged

    assert type(data_result['auth_token']) is str
    assert len(data_result['auth_token']) > 15
