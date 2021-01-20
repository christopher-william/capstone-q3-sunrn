from flask import json
from tests.database_connection import execute_sql_comand_in_database


def new_message_json():
    """retorna o json com as informações da nova menssagem"""

    return {
        "lead_id": "2",
        "seller_id": "1",
        "classification": "5",
        "message": "O lead quer uma proposta formalizada por email."
    }


def test_dict_create_message_with_status_201(client):
    """cria uma nova messagem e verifica as informações do json sem o id"""

    new_message = new_message_json()

    response = client.post('/message', json=new_message)

    status_result = response.status_code
    data_result = json.loads(response.data)

    status_expected = 201
    assert status_result == status_expected

    data_expected = new_message.copy()

    assert int(data_result['id']) > 0
    assert type(data_result['id']) is int

    last_message_id = execute_sql_comand_in_database(
        """SELECT id FROM message ORDER BY ID DESC LIMIT 1""")[0][0]

    data_expected.update({'id': last_message_id})

    assert sorted(data_result.keys()) == sorted(data_expected.keys())
    assert sorted([str(i) for i in data_result.values()]) == sorted(
        [str(i) for i in data_expected.values()])


def test_dict_of_get_lead_and_message_with_status_200(client):
    """pega o lead e as messagens e verifica o status"""
    response = client.get(f'/message/{2}')

    status_result = response.status_code
    data_result = json.loads(response.data)

    status_expected = 200
    assert status_result == status_expected

    lead_messages_result = data_result['messages'].copy()

    data_expected = execute_sql_comand_in_database(
        """SELECT * FROM lead WHERE lead.id = 1""")[0]
    lead_messages_expected = execute_sql_comand_in_database(
        """SELECT * FROM message WHERE message.lead_id = 1""")

    assert int(data_result['id']) == int(data_expected[0])
    assert len(lead_messages_result) == len(lead_messages_expected)
