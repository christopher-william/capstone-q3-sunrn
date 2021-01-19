from . import db


class Simulation(db.Model):
    __tablename__ = "simulation"

    id = db.Column(db.Integer, primary_key=True)
    lead_id = db.Column(db.Integer, db.ForeignKey('lead.id'))
    panel_id = db.Column(db.Integer, db.ForeignKey('panel.id'))
    inversor_id = db.Column(db.Integer, db.ForeignKey('inversor.id'))
    system_cost = db.Column(db.Integer)
    energy_cost = db.Column(db.Integer)
    worker_cost = db.Column(db.Integer)
    project_cost = db.Column(db.integer)
    eletric_materials_cost = db.Column(db.Integer)
    maintanance_cost = db.Column(db.Integer)
    total_system_cost = db.Column(db.Integer)
    roi_years = db.Column(db.Integer)
