from app.models import Message, Lead, lead_schema, message_schema, messages_schema
from sqlalchemy.exc import IntegrityError
from http import HTTPStatus
from .http import build_api_response
from flask import current_app


def create_message(data):

    message = Message(
        classification=data['classification'],
        message=data['message'],
        lead_id=data['lead_id']
    )

    try:
        session = current_app.db.session
        session.add(message)
        session.commit()
        return build_api_response(HTTPStatus.CREATED, message_schema.dump(message))

    except IntegrityError:
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

    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)
