from . import db, ma


class Seller(db.Model):
    __tablename__ = "seller"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    lead_id = db.relationship('Lead', secondary='message')
<<<<<<< HEAD

    def __repr__(self):
        return f'<Seller {self.name}>'
=======
>>>>>>> 6ba8dcbc7f49e7b66de3f17f40c905748338a38a


class SellerSchema(ma.SQLAlchemySchema):
    class Meta:

<<<<<<< HEAD
        fields = ('id', 'name', 'email', 'password', 'lead_id')

        id = ma.auto_field()
        name = ma.auto_field()
        email = ma.auto_field()
        password = ma.auto_field()
        lead_id = ma.auto_field()
=======
        model = Seller
        
    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    password = ma.auto_field()
>>>>>>> 6ba8dcbc7f49e7b66de3f17f40c905748338a38a


seller_schema = SellerSchema()
sellers_schema = SellerSchema(many=True)
