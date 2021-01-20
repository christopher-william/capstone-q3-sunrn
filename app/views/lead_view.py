from flask import request
from flask_restful import Resource


class LeadView(Resource):

    def post(self):
        data = request.get_json()

        return simulation_data
