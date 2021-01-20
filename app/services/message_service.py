from http import HTTPStatus

from app.models import Lead, Message, lead_schema, message_schema
from flask import current_app

from .http_service import build_api_response


def create_message(data):

    try:

        message = Message(
            classification=data['classification'],
            message=data['message'],
            lead_id=data['lead_id'],
            seller_id=data['seller_id']
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
        message_schema_rs = message_schema.dump(message)

        lead_schema_rs.pop('seller_id')

        message_and_lead_schema = {
            "lead": lead_schema_rs,
            "message": message_schema_rs
        }

        return build_api_response(HTTPStatus.OK, message_and_lead_schema)

    except:
        return build_api_response(HTTPStatus.BAD_REQUEST)
