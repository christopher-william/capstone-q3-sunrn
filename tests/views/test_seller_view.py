import random


def generated_email(max):
    return ''.join([random.choice("abcde") for _ in range(max)])


random_word = generated_email(20)


def new_seller_json():
    """retorna um json com as informações no novo seller"""

    return {
        'name': "Christopher",
        'email': f"{random_word}@gmail.com",
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
