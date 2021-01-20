from . import db, ma


class PanelPrice(db.Model):
    __tablename__ = "panel_price"

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    power = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric, nullable=False)


class PanelPriceSchema(ma.SQLAlchemySchema):

    class Meta:

        model = PanelPrice
       
    id = ma.auto_field()
    model = ma.auto_field()
    brand = ma.auto_field()
    power = ma.auto_field()
    price = ma.auto_field()


panel_price_schema = PanelPriceSchema()
panels_prices_schema = PanelPriceSchema(many=True)
