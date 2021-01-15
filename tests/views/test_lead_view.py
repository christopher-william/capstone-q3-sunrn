

def new_lead_json():
    """retorna um json do novo lead"""

    return {
        "name": "chritopher william buscoski sanocki",
        "email": "christopher@gmail.com",
        "phone": 40028922,
        "hsp_id": 1,
        "energy_id": 1,
    }


def test_create_new_lead(client):
    """cria novo lead e verifica o retorno do post e o status"""

    new_lead = new_lead_json()

    response = client.post('/lead', json=new_lead)

    data = response.data
    status = response.status_code

    expected = {"data": new_lead}

    # assert data == expected
    # assert status == 201
