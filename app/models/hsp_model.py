from . import db, ma


class Hsp(db.Model):
    __tablename__ = "hsp"

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80), nullable=False)
    uf = db.Column(db.String(120), nullable=False)
    md_anual = db.Column(db.Integer, nullable=False)
    lon = db.Column(db.Numeric, nullable=False)
    lat = db.Column(db.Numeric, nullable=False)


class HspSchema(ma.SQLAlchemySchema):
    class Meta:

        model = Hsp

    id = ma.auto_field()
    city = ma.auto_field()
    uf = ma.auto_field()


hsp_schema = HspSchema()
hsps_schema = HspSchema(many=True)
