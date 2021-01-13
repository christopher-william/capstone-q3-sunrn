from app.services.seller_services import create_seller
from flask import Flask, request
from flask_restful import Api, Resource


class SellerRoute(Resource):

    def post(self):

        data = request.get_json()

        response = create_seller(data)
        return response
