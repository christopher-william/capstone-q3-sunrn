from app.services.post_lead_service import (get_lead_all_message, get_leads,
                                            post_lead)
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

class LeadView(Resource):

    def post(self):
        data = request.get_json()

        response = post_lead(data)
        return response
    
    @jwt_required
    def get(self, lead_id=None):

        if lead_id:
            request = get_lead_all_message(lead_id)
        else:
            request = get_leads()

        return request
