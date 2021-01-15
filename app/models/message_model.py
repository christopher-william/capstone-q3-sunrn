from . import db, ma


class Message(db.Model):
    __tablename__ = "message"

    id = db.Column(db.Integer, primary_key=True)
    classification = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String, nullable=False)
    lead_id = db.Column(db.Integer, db.ForeignKey('lead.id'))


class MessageSchema(ma.SQLAlchemySchema):
    class Meta:

        fields = ('id', 'classification', 'message', 'lead_id')

        id = ma.auto_field()
        classification = ma.auto_field()
        message = ma.auto_field()
        lead_id = ma.auto_field()


message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)
