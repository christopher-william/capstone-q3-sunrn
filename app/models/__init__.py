from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_marshmallow import Marshmallow
# from marshmallow import fields

db = SQLAlchemy()
mg = Migrate()
# ma = Marshmallow()


def configure(app: Flask):
    db.init_app(app)
    mg.init_app(app, db)
    app.db = db


from .hsp_model import Hsp
from .inverter_price_model import Inverter_price
from .panel_price_model import Panel_price
from .energy_data_model import Energy_data
from .lead_model import Lead
from .simulation_model import Simulation