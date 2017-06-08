from . import db, BaseModel


class Cinema(BaseModel, db.Model):
    __tablename__ = "cinema"
    cinema_id = db.Column(db.Integer, primary_key=True)
    cinema_name = db.Column(db.String(64), nullable=False, unique=True)
    info = db.Column(db.Text)
