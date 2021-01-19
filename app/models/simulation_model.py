from . import db


class Simulation(db.Model):
    __tablename__ = "simulation"

    id = db.Column(db.Integer, primary_key=True)
    system_cost = db.Column(db.Integer, nullable=False)
    energy_cost = db.Column(db.Integer, nullable=False)
    worker_cost = db.Column(db.Integer, nullable=False)
    project_cost = db.Column(db.integer, nullable=False)
    eletric_materials_cost = db.Column(db.Integer, nullable=False)
    maintanance_cost = db.Column(db.Integer, nullable=False)
    total_system_cost = db.Column(db.Integer, nullable=False)
    roi_years = db.Column(db.Integer, nullable=False)
    panel_quantity = db.Column(db.Integer, nullable=False)

    lead_id = db.Column(db.Integer, nullable=False, db.ForeignKey('lead.id'))    
    panel_id = db.Column(db.Integer, nullable=False, db.ForeignKey('panel.id'))
    inversor_id = db.Column(
        db.Integer, nullable=False, db.ForeignKey('inverter_price.id'))