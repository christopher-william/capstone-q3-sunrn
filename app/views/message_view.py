from app.services.message_service import create_message, get_lead_and_message
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

class Message(Resource):
    @jwt_required
    def get(self, id):
        request = get_lead_and_message(id)
        return request

    @jwt_required
    def post(self):
        data = request.get_json()

        response = create_message(data)
        return response
