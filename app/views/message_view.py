from app.services.message_service import create_message, get_lead_all_message, get_message
from flask import request
from flask_restful import Resource
from http import HTTPStatus


class Message(Resource):

    def get(self, lead_id=None, message_id=None):

        request = 'Dont Have Lead or Message id', HTTPStatus.BAD_REQUEST

        if lead_id and message_id:
            request = get_message(lead_id, message_id)

        if lead_id and not message_id:
            request = get_lead_all_message(lead_id)

        
        return request

    def post(self):
        data = request.get_json()

        response = create_message(data)
        return response
