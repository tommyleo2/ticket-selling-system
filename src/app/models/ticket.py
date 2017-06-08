from . import BaseModel, db


class Ticket(BaseModel, db.Model):
    __tablename__ = "ticket"
    ticket_id = db.Column(db.Integer, primary_key=True)
    cinema_id = db.Column(db.Integer, db.ForeignKey("cinema.cinema_id"),
                          nullable=False, index=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.movie_id"),
                         nullable=False, index=True)
    timetable_id = db.Column(db.Integer, db.ForeignKey("timetable.timetable_id"))
    room = db.Column(db.String(10), nullable=False)
    seat = db.Column(db.String(10), nullable=False)
    cinema = db.relationship("Cinema")
    movie = db.relationship("Movie")
    ticket_in_order = db.relationship("TicketInOrder")
    timetable = db.relationship("TimeTable")
