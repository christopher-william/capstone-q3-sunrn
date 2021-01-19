from . import db, ma


class InverterPrice(db.Model):
    __tablename__ = "inverter_price"
    
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    power = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    
    simulation = db.relationship('Simulation')



class InverterPriceSchema(ma.SQLAlchemySchema):
    
    class Meta:
        model = InverterPrice

    id = ma.auto_field()
    model = ma.auto_field()
    brand = ma.auto_field()
    power = ma.auto_field()
    price = ma.auto_field()
    simulation = ma.auto_field()


inversor_price_schema = InverterPriceSchema()
inversors_prices_schema = InverterPriceSchema(many=True)