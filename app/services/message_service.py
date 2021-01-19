from http import HTTPStatus

from app.models import (
    Lead, Message, lead_schema, message_schema,
    messages_schema)
from flask import current_app

from .http import build_api_response


def create_message(data):

    try:

        message = Message(
            classification=data['classification'],
            message=data['message'],
            lead_id=data['lead_id']
        )

        session = current_app.db.session
        session.add(message)
        session.commit()

        return build_api_response(HTTPStatus.CREATED, message_schema.dump(message))

    except:
        return build_api_response(HTTPStatus.BAD_REQUEST)


def get_lead_and_message(id):

    try:

        message = Message.query.get(id)
        lead = Lead.query.get(message.lead_id)

        lead_schema_rs = lead_schema.dump(lead)
        lead_schema_rs['messages'] = messages_schema.dump(
            lead_schema_rs['messages']
        )

        return build_api_response(HTTPStatus.OK, lead_schema_rs)

    except:
        return build_api_response(HTTPStatus.BAD_REQUEST)
