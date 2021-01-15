import ast


def new_message_json():
    """retorna o json com as informações da nova menssagem"""

    return {
        "lead_id": 1,
        "classification": 5,
        "message": "O lead quer uma proposta formalizada por email."
    }


def decode_data(response):
    dict_str = response.decode("UTF-8")
    return ast.literal_eval(dict_str)


def test_create_message(client):
    """cria uma nova messagem e verifica as informações do json sem o id"""

    new_message = new_message_json()

    response = client.post('/message', json=new_message)

    status = response.status_code
    data = decode_data(response.data)['data']
    data.pop('id')
    expected = new_message.copy()

    assert status == 201
    assert data == expected
    assert sorted(data.keys()) == sorted(expected.keys())


def test_get_lead_by_message(client):
    """pega o lead e as messagens e verifica o status"""
    response = client.get(f'/message/{1}')
    assert response == 200
