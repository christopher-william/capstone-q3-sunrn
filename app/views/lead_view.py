from app.models.energy_data_model import EnergyData
from app.models.hsp_model import Hsp
from app.models.inverter_price_model import InverterPrice
from app.models.lead_model import Lead
from app.models.panel_price_model import PanelPrice
from app.models.simulation_model import Simulation
from app.services.calculate_roi_panel_service import roi_calc
from app.services.http_service import build_api_response
from app.services.lead_service import create_lead
from flask import current_app, request
from flask_restful import Resource
from app.models import energy_data_schema

class LeadView(Resource):

    def post(self):

        data = request.get_json()
        hsp = Hsp.query.filter_by(id=data["hsp_id"]).first()
        panel_list = PanelPrice.query.order_by(PanelPrice.power).all()
        inverter_list = InverterPrice.query.order_by(
            InverterPrice.power).all()

        energy_data = EnergyData(
            month_energy=data["month_energy"],
            month_value=data["month_value"]
        )

        

        simulation_data = roi_calc(
            energy_data, inverter_list,
            panel_list, hsp
        )

        energy_dict = energy_data_schema.dump(energy_data)

        lead = Lead(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            hsp_id=hsp.id,
            energy_id=energy_data.id
        )
        print("------------------------", energy_dict, lead.__dict__)

        simulation = Simulation(
            lead_id=lead.id,
            panel_id=simulation_data['panel']['id'],
            panel_quantity=simulation_data['panel']['quantity'],
            inversor_id=simulation_data['inversor']['id'],
            system_cost=simulation_data['system_cost'],
            energy_cost=simulation_data['energy_cost'],
            worker_cost=simulation_data['worker_cost'],
            project_cost=simulation_data['project_cost'],
            eletric_materials_cost=simulation_data['eletric_materials_cost'],
            maintanance_cost=simulation_data['maintanance_cost'],
            total_system_cost=simulation_data['total_system_cost'],
            roi_years=simulation_data['roi_years']
        )

        session = current_app.db.session
        session.add(energy_data)
        session.add(lead)
        session.add(simulation)
        session.commit()

        return simulation_data
