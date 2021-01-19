from . import db, ma


class Message(db.Model):
    __tablename__ = "message"

    id = db.Column(db.Integer, primary_key=True)
    classification = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String, nullable=False)
    lead_id = db.Column(db.Integer, db.ForeignKey('lead.id', onupdate='CASCADE',
     ondelete='CASCADE'))
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.id', onupdate='CASCADE',
     ondelete='CASCADE') )


class MessageSchema(ma.SQLAlchemySchema):
    class Meta:

        model = Message
            
    id = ma.auto_field()
    classification = ma.auto_field()
    message = ma.auto_field()
    lead_id = ma.auto_field()
    seller_id = ma.auto_field()


message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)
