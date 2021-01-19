
from app.services.lead_service import create_lead
from flask import request
from flask import current_app
from flask_restful import Resource
from models.lead_model import Lead
from models.hsp_model import Hsp
from models.energy_data_model import Energy_data
from models.simulation_model import Simulation
from models.panel_price_model import Panel_price
from models.inverter_price_model import Inverter_price

from services.calculate_roi_panel_service import roi_calc


class Lead(Resource):

    def post(self):

        data = request.get_json()

        hsp = Hsp.query.filter_by(id=data["hsp_id"]).first()
        panel_list = Panel_price.query.order_by(Panel_price.power).all()
        inverter_list = Inverter_price.query.order_by(
            Inverter_price.power).all()

        energy_data = Energy_data(data["month_energy"], data["month_value"])
        simulation_data = roi_calc(energy_data, inverter_list, panel_list, hsp)

        lead = Lead(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            hsp_id=hsp.id,
            energy_id=energy_data.id
        )

        simulation = Simulation(
            lead_id=lead.id,
            panel_id=simulation['panel'][0].id,
            inverter_id=simulation['inversor'].id,
            system_cost=simulation['system_cost'],
            worker_cost=simulation['energy_cost'],
            project_cost=simulation['worker_cost'],
            eletric_materials_cost=simulation['eletric_materials_cost'],
            maintanance_cost=simulation['maintanance_cost'],
            total_system_cost=simulation['total_system_cost'],
            roi_years=simulation['roi_years']
        )

        session = current_app.db.session
        session.add(lead)
        session.add(simulation)
        session.commit()

        return simulation_data
