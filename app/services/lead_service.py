from http import HTTPStatus

from app.models.lead_model import Lead, lead_schema
from flask import current_app
from sqlalchemy.exc import IntegrityError

from .http_service import build_api_response


def create_lead(data):

    try:

        lead = Lead(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            hsp_id=data['hsp_id'],
            energy_id=data['energy_id']
        )

        session = current_app.db.session
        session.add(lead)
        session.commit()

        return build_api_response(HTTPStatus.CREATED, lead_schema.dump(lead))

    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)
