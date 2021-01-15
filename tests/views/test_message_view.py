
def test_create_message(client):

    new_message = {
        "lead_id": 1,
        "classification": 5,
        "message": "O lead quer uma proposta formalizada por email."
    }
    response = client.post('/message', json=new_message)

    assert response == 201


def test_get_lead_by_message(client):

    id = 2

    response = client.get(f'/message/{id}')
    assert response == 200
