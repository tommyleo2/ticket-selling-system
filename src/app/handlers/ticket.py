from flask import session, request
import json

from app import app, db
from ..models import Ticket, TicketInOrder, Order
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

@app.route("/ticket/buy", methods=["POST"])
def buy_ticket():
    print("Fuck")
    if 'id' not in session:
        return json.dumps({
                "message": "not logged in",
            }), 401

    req = request.get_json()
    if not req or isinstance(req, list):
        return json.dumps({
                "message": "you are a sb!"
            }), 404

    non_existed_or_sold_tickets = []
    tickets = []
    for id in req:
        ticket = Ticket.query.filter_by(ticket_id=id, user_id=None).first()
        if ticket is None:
            non_existed_or_sold_tickets.append(id)
        else:
            tickets.append(ticket)

    if len(non_existed_or_sold_tickets) == 0:
        user_id = session["id"]
        order = Order(user_id = user_id)
        db.session.add(Order)
        for ticket in tickets:
            tIo = TicketInOrder(order_id = order.order_id, ticket_id = ticket.ticket_id)
            db.session.add(tIo)
            ticket.user_id = user_id

        try:
            db.session.commit()
            return json.dumps({
                    "message":"success"
                }), 200
        except:
            return json.dumps({
                    "message":"Unknown error"
                }), 403

    else:
        return json.dumps({
                "message":"tickets not exist or already been sold",
                "tickets": non_existed_or_sold_tickets
            }), 404

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
