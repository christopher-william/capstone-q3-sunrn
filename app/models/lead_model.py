from marshmallow import fields

from . import db, ma


class Lead(db.Model):
    __tablename__ = "lead"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False, unique=True)

    energy_id = db.Column(db.Integer, db.ForeignKey('energy_data.id'))

    simulation = db.relationship('Simulation')
    hsp = db.relationship('Hsp', secondary='hsp_lead')
    seller = db.relationship('Seller', secondary='message')


class LeadSchema(ma.SQLAlchemySchema):

    class Meta:

        model = Lead

    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    phone = ma.auto_field()

    energy_id = ma.auto_field()


lead_schema = LeadSchema()
leads_schema = LeadSchema(many=True)
