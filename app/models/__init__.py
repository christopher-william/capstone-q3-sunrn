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
