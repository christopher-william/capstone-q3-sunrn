from . import db


class Energy_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    leads = db.relationship('Lead', backref='energy_data', lazy=True)
