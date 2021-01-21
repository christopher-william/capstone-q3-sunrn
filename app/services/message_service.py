from http import HTTPStatus

from app.models import Lead, Message, lead_schema, message_schema, messages_schema, simulations_schema
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


def get_message(lead_id, message_id):

    try:

        lead = Lead.query.get(lead_id)
        message = Message.query.get(message_id)


        lead_schema_rs = lead_schema.dump(lead)
        message_schema_rs = message_schema.dump(message)

        lead_schema_rs['simulation'] = simulations_schema.dump(lead_schema_rs['simulation'])

        lead_and_message = {
            "lead": lead_schema_rs,
            "message": message_schema_rs
        }

        return build_api_response(HTTPStatus.OK, lead_and_message)

    except:
        return build_api_response(HTTPStatus.BAD_REQUEST)
   


def get_lead_all_message(lead_id):

    try:
        
        lead = Lead.query.get(lead_id)
        messages = Message.query.filter_by(lead_id=lead_id)

        lead_schema_rs = lead_schema.dump(lead)
        messages_schema_rs = messages_schema.dump(messages)

        lead_schema_rs['simulation'] = simulations_schema.dump(lead_schema_rs['simulation'])

        lead_and_all_messages = {
            "lead": lead_schema_rs,
            "messages": messages_schema_rs
        }

        return build_api_response(HTTPStatus.OK, lead_and_all_messages)

    except:
        return build_api_response(HTTPStatus.BAD_REQUEST)