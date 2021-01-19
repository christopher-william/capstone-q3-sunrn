from . import db, ma
from .simulation_model import SimulationSchema


class PanelPrice(db.Model):
    __tablename__ = "panel_price"
    
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    power = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric, nullable=False)

    simulation = db.relationship('Simulation')

    def __repr__(self):
        return f"<Table name {self.Panel_price.__name__}>"


class PanelPriceSchema(ma.SQLAlchemySchema):
    
    class Meta:

        model = Panel_price

    id = ma.auto_field()
    model = ma.auto_field()
    brand = ma.auto_field()
    power = ma.auto_field()
    price = ma.auto_field()
    simulation = ma.auto_field()
        # simulation = fields.Nested(SimulationSchema, exclude=("panel_id",))
        


panel_price_schema = PanelPriceSchema()
panels_prices_schema = PanelPriceSchema(many=True)