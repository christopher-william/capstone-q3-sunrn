
from app.services.lead_service import create_lead
from flask import request
from flask_restful import Resource


class Lead(Resource):

    def post(self):

        data = request.get_json()

        response = create_lead()

        # faser calculos de lead
        # EXP: response = calculos_de_lead()

        return response
