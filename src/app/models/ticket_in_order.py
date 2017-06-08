from . import BaseModel, db


class TicketInOrder(BaseModel, db.Model):
    __tablename__ = "ticket_in_order"
    order_id = db.Column(db.Integer, db.ForeignKey("order.order_id"),
                         primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey("ticket.ticket_id"),
                          nullable=False)
    order = db.relationship("Order")
    ticket = db.relationship("Ticket")
