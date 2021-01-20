from . import db, ma


class EnergyData(db.Model):
    __tablename__ = "energy_data"

    id = db.Column(db.Integer, primary_key=True)
    month_energy = db.Column(db.Numeric, nullable=False)
    month_value = db.Column(db.Numeric, nullable=False)
    leads = db.relationship('Lead', uselist=False)


class EnergyDataSchema(ma.SQLAlchemySchema):
    class Meta:

        model = EnergyData

    id = ma.auto_field()
    month_energy = ma.auto_field()
    month_value = ma.auto_field()
    leads = ma.auto_field()


energy_data_schema = EnergyDataSchema()