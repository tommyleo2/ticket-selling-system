from . import BaseModel, db

import datetime


class Order(BaseModel, db.Model):
    __tablename__ = "order"
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"),
                        nullable=False, index=True)
    order_at = db.Column(db.DateTime, default=datetime.datetime.now)
    user = db.relationship("User")
    tickets_in_order = db.relationship("TicketInOrder")
