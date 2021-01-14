from http import HTTPStatus
from flask import current_app

from app.models import db
from app.models.seller_model import Seller, seller_schema
from sqlalchemy.exc import IntegrityError
from .http import build_api_response
from app.services.encode_service import encode_password

def login_seller(data):
    try:
        encoded_password = encode_password(data)

        seller = Seller.query.filter_by(
            email=data['email'], password=encode_password).first()

        if not seller:
            return build_api_response(HTTPStatus.NOT_FOUND)

        return build_api_response(HTTPStatus.OK, seller_schema.dump(seller))

    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)


def create_seller(data):
    encoded_password = encode_password(data)
    seller = Seller(
        name=data['name'],
        email=data['email'],
        password=encoded_password
    )

    try:
        session = current_app.db.session
        session.add(seller)
        session.commit()
        return build_api_response(HTTPStatus.CREATED, seller_schema.dump(seller))
    
    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)
