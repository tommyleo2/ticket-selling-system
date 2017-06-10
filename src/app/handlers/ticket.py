from flask import session, request
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


@app.route("/ticket", methods=["GET"])
def get_movie_cinema_ticket():
    cinema = request.args.get("cinema")
    movie = request.args.get("movie")
    if cinema is None or movie is None:
        return json.dumps({
            "message": "invalid query parameters"
        }), 400

    tickets = Ticket.query.filter_by(cinema_id=cinema, movie_id=movie)
    result = []
    for ticket in tickets:
        result.append({
            "id": ticket.ticket_id,
            "room": ticket.room,
            "seat": ticket.seat,
            "is_booked": ticket.user_id is not None,
            "start_at": format_datetime(ticket.timetable.start_at)
        })
    return json.dumps(result), 200
