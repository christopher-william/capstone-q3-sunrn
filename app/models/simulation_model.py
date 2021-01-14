from . import db


class Simulation(db.Model):
    __tablename__ = "simulation"
    
    id = db.Column(db.Integer, primary_key=True)
    lead_id = db.Column(db.Integer, db.ForeignKey('lead.id'))