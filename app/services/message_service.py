from app.models import Message, Lead


def get_lead_and_message(id):

    message = Message.get(id)
    lead = Lead.get(message.lead_id)
