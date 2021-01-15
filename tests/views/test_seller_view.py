import random


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

    result = client.post('/register', json=new_seller_json())
    assert result.status_code == 201


def test_login_seller(client):
    """loga com o novo seller criado e compara o status"""

    result = client.post('/login', json=new_seller_json())
    assert result.status_code == 200
