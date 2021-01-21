from marshmallow import fields

from . import db, ma


class Simulation(db.Model):
    __tablename__ = "simulation"

    id = db.Column(db.Integer, primary_key=True)
    system_cost = db.Column(db.Numeric, nullable=False)
    energy_cost = db.Column(db.Numeric, nullable=False)
    worker_cost = db.Column(db.Numeric, nullable=False)
    project_cost = db.Column(db.Numeric, nullable=False)
    eletric_materials_cost = db.Column(db.Numeric, nullable=False)
    maintanance_cost = db.Column(db.Numeric, nullable=False)
    total_system_cost = db.Column(db.Numeric, nullable=False)
    roi_years = db.Column(db.Numeric, nullable=False)
    panel_quantity = db.Column(db.Numeric, nullable=False)

    lead_id = db.Column(db.Integer, db.ForeignKey('lead.id'))
    panel_id = db.Column(db.Integer, db.ForeignKey('panel_price.id'))
    inversor_id = db.Column(
        db.Integer, db.ForeignKey('inverter_price.id'))


class SimulationSchema(ma.SQLAlchemySchema):

    class Meta:

        model = Simulation

    system_cost = fields.Float()
    energy_cost = fields.Float()
    worker_cost = fields.Float()
    project_cost = fields.Float()
    eletric_materials_cost = fields.Float()
    maintanance_cost = fields.Float()
    total_system_cost = fields.Float()
    roi_years = fields.Float()
    panel_quantity = fields.Float()

    lead_id = ma.auto_field()
    panel_id = ma.auto_field()
    inversor_id = ma.auto_field()


simulation_schema = SimulationSchema()
simulations_schema = SimulationSchema(many=True)
