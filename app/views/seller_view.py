from app.services.seller_services import create_seller, login_seller
from flask import request
from flask_restful import Resource


class SellerRegister(Resource):

    def post(self):

        data = request.get_json()

        response = create_seller(data)
        return response


class SellerLogin(Resource):

    def post(self):

        data = request.get_json()

        response = login_seller(data)
        return response
