from . import db


class Energy_data(db.Model):
    __tablename__ = "energydata"
    
    id = db.Column(db.Integer, primary_key=True)
    month_energy = db.Column(db.Numeric, nullable=False)
    leads = db.relationship('Lead')
