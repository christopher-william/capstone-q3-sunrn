from app.services.post_lead_service import post_lead
from flask import request
from flask_restful import Resource


class LeadView(Resource):

    def post(self):
        data = request.get_json()

        response = post_lead(data)
        return response
