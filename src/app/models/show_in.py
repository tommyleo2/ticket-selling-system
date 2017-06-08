from . import BaseModel, db


class ShowIn(BaseModel, db.Model):
    __tablename__ = "show_in"
    showin_id = db.Column(db.Integer, primary_key=True)
    cinema_id = db.Column(db.Integer, db.ForeignKey("cinema.cinema_id"),
                          nullable=False, index=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.movie_id"),
                         nullable=False, index=True)
    cinema = db.relationship("Cinema")
    movie = db.relationship("Movie")
    timetable = db.relationship("TimeTable")
