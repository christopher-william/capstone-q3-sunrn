from . import db


class Energy_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month_energy = db.Column(db.Integer, nullable=False)
    leads = db.relationship('Lead', backref='energy_data', lazy=True)
