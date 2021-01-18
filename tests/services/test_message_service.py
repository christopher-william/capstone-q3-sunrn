from http import HTTPStatus

from app.services.message_service import create_message, get_lead_and_message


def new_message_json():
    return {
        "lead_id": 1,
        "message": "[TEST]: nova message de test",
        "classification": 2
    }


def test_dict_create_message_with_status_201():
    """Testa o dicionario e o status retornado pela função create_message"""

    data = new_message_json()

    data_result, status_result = create_message(data)

    data_expected = data.copy()

    assert data_result['id'] > 0
    assert type(data_result['id']) is int

    # para que o data_expected acompanhe a mudança do id no database
    data_expected.update({'id': data_result['id']})
    status_expected = HTTPStatus.CREATED

    assert sorted(data_result.keys()) == sorted(data_expected.keys())
    assert sorted(data_result.values()) == sorted(data_expected.values())
    assert status_result == status_expected

    # TODO --> testar a data no database


def test_dict_of_get_lead_and_message_with_status_200():
    """Testa o dicionario e o status retornado pela função get_lead_and_message"""

    message_id = 1

    data_result, status_result = get_lead_and_message(message_id)

    lead_messages_result = data_result['messages'].copy()

    data_expected = dict('criar um expected data')
    lead_messages_expected = dict('criar um expected lead_message')
    status_expected = HTTPStatus.OK

    assert sorted(data_result.keys()) == sorted(data_expected.keys())
    assert sorted(data_result.values()) == sorted(data_expected.values())
    assert sorted(lead_messages_result) == sorted(lead_messages_expected)

    assert status_result == status_expected
