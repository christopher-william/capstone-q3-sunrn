from flask_restful import Resource
from app.services.message_service import get_lead_and_message


class Message(Resource):

    def get(self, id):

        request = get_lead_and_message(id)
        return request

    def post(self):
        pass
