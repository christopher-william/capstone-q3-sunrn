from app.services.post_lead_service import get_lead_all_message, post_lead
from flask import request
from flask_restful import Resource


class LeadView(Resource):

    def post(self):
        data = request.get_json()

        response = post_lead(data)
        return response


class LeadMessages(Resource):

    def get(self, lead_id):

        request = get_lead_all_message(lead_id)
        return request
