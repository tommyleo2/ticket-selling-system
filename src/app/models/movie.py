from . import BaseModel, db


class Movie(BaseModel, db.Model):
    __tablename__ = "movie"
    movie_id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(64), nullable=False, index=True)
    length = db.Column(db.Integer, nullable=False)
    info = db.Column(db.Text)
    show_in = db.relationship("ShowIn")
