from flask import request
from flask_restful import Resource
from app.services.post_lead_service import post_lead


class LeadView(Resource):

    def post(self):
        data = request.get_json()
        response = post_lead(data)
        
        return response
