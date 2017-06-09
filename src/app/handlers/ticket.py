from flask import session
import json

from app import app
from ..models import Ticket
from ..utility import format_datetime


@app.route("/myticket", methods=["GET"])
def get_myticket():
    if 'id' not in session:
        return json.dumps({
            "message": "not logged in"
        }), 401

    tickets = Ticket.query.filter_by(user_id=session["id"])
    result = []
    for ticket in tickets:
        movie = ticket.movie
        cinema = ticket.cinema
        result.append({
            "id": ticket.ticket_id,
            "movie_id": movie.movie_id,
            "cinema_id": cinema.cinema_id,
            "movie_name": movie.movie_name,
            "cinema_name": cinema.cinema_name,
            "start_at": format_datetime(ticket.timetable.start_at)
        })
    return json.dumps(result), 200
