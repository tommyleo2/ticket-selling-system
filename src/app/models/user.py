from . import BaseModel, db


class User(BaseModel, db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, index=True)
    email = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(20))
    password = db.Column(db.CHAR(128), nullable=False)
