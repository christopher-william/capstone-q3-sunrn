from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
mg = Migrate()
ma = Marshmallow()


def configure(app: Flask):
    db.init_app(app)
    mg.init_app(app, db)
    ma.init_app(app)
    app.db = db


from .hsp_model import Hsp, hsp_schema, hsps_schema

from .inverter_price_model import (
    Inverter_price, inversor_price_schema, inversors_prices_schema)

from .panel_price_model import (
    Panel_price, panel_price_schema, panels_prices_schema)

from .energy_data_model import Energy_data

from .lead_model import Lead, lead_schema, leads_schema

from .simulation_model import (
    Simulation, simulation_schema, simulations_schema)

from .seller_model import Seller, seller_schema, sellers_schema

from .message_model import Message, message_schema, messages_schema

