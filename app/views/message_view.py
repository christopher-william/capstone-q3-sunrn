from flask_restful import Resource
from app.services.message_service import get_lead_and_message, create_message
from flask import request


class Message(Resource):

    def get(self, id):
        print(id)

        request = get_lead_and_message(id)
        return request

    def post(self):
        data = request.get_json()

        response = create_message(data)
        return response
