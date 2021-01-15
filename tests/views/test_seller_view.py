
def test_create_seller(client):

    new_seller = {
        'name': "Christopher",
        'email': "christopherk@gmail.com",
        'password': "121314"
    }
    result = client.post('/register', json=new_seller)

    assert result == 201


def test_login_seller(client):

    seller = {
        'email': "christopherk@gmail.com",
        'password': "121314"
    }
    result = client.post('/login', json=seller)

    assert result == 200


def test_clear_database():
    pass
