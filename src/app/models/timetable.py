from . import BaseModel, db


class TimeTable(BaseModel, db.Model):
    __tablename__ = "timetable"
    timetable_id = db.Column(db.Integer, primary_key=True)
    showin_id = db.Column(db.Integer, db.ForeignKey("show_in.showin_id"),
                          index=True)
    start_at = db.Column(db.DateTime, nullable=False)
    show_in = db.relationship("ShowIn")
