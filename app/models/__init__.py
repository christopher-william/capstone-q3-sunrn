from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_marshmallow import Marshmallow
# from marshmallow import fields

db = SQLAlchemy()
mg = Migrate()
# ma = Marshmallow()


class Hsp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80), nullable=False)
    uf = db.Column(db.String(120), nullable=False)
    md_anual = db.Column(db.Integer, nullable=False)
    lon = db.Column(db.Numeric, nullable=False)
    lat = db.Column(db.Numeric, nullable=False)
    leads = db.relationship('Lead', backref='hsp', lazy=True)

    def __repr__(self):
        return f'<User {self.city}>'


class Inverter_price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    power = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric, nullable=False)

    def __repr__(self):
        return f'<User {self.model}>'


class Panel_price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    power = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric, nullable=False)

    def __repr__(self):
        return f"<Table name {self.Panel_price.__name__}>"


class Energy_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    leads = db.relationship('Lead', backref='energy_data', lazy=True)


class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False, unique=True)
    hsp_id = db.Column(db.Integer, db.ForeignKey('hsp.id'))
    energy_id = db.Column(db.Integer, db.ForeignKey('energy_data.id'))
    simulations = db.relationship('Simulation', backref='lead', lazy=True)


class Simulation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lead_id = db.Column(db.Integer, db.ForeignKey('lead.id'))
