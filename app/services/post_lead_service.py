from http import HTTPStatus

from app.models import (EnergyData, Hsp, HspLead, InverterPrice, Lead,
                        PanelPrice, Simulation, energy_data_schema,
                        simulation_schema)
from app.models.lead_model import Lead, lead_schema
from app.services.calculate_roi_panel_service import roi_calc
from app.services.http_service import build_api_response
from flask import current_app, request
from sqlalchemy.exc import IntegrityError

from .http_service import build_api_response


def post_lead(data):

    try:

        session = current_app.db.session

        panel_list = PanelPrice.query.order_by(PanelPrice.power).all()

        inverter_list = InverterPrice.query.order_by(
            InverterPrice.power).all()
        hsp = Hsp.query.filter_by(id=data["hsp_id"]).first()

        energy_data = EnergyData(
            month_energy=data["month_energy"],
            month_value=data["month_value"]
        )

        print(energy_data.__dict__)

        # session.add(energy_data)
        # session.commit()

        print(energy_data.__dict__)

        simulation_data = roi_calc(
            energy_data, inverter_list,
            panel_list, hsp
        )

        lead = Lead(
            name=data['name'], email=data['email'],
            phone=data['phone'], energy_id=energy_data.id
        )

        hsplead = HspLead(
            hsp_id=hsp.id, lead_id=lead.id
        )

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

        # session.add(energy_data)
        # session.add(simulation)
        # session.add(lead)
        # session.add(hsplead)
        # session.commit()

        data = simulation_schema.dump(simulation)
        print(data, simulation_data)

        return build_api_response(HTTPStatus.CREATED, simulation_data)

    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)
