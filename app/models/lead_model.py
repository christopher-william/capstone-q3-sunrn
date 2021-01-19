from . import db, ma
from .simulation_model import SimulationSchema

class Lead(db.Model):
    __tablename__ = "lead"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False, unique=True)
    hsp_id = db.Column(db.Integer, db.ForeignKey('hsp.id'))
    energy_id = db.Column(db.Integer, db.ForeignKey('energy_data.id'))
    simulations = db.relationship('Simulation')
    seller_id = db.relationship('Seller', secondary='message')



class LeadSchema(ma.SQLAlchemySchema):
    
    class Meta:

        model = Lead

    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    phone = ma.auto_field()
    hsp_id = ma.auto_field()
    energy_id = ma.auto_field()
    messages = ma.auto_field()
    simulation = ma.auto_field()
        # simulation = fields.Nested(SimulationSchema, exclude=("lead_id",))


lead_schema = LeadSchema()
leads_schema = LeadSchema(many=True)
