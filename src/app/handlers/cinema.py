import json

from app import app
from ..models import Cinema, ShowIn, Movie


@app.route("/cinema", methods=["GET"])
def get_cinema_list():
    cinemas = Cinema.query.all()
    result = []
    for cinema in cinemas:
        result.append({
            "id": cinema.cinema_id,
            "name": cinema.cinema_name
        })
    return json.dumps(result), 200


@app.route("/cinema/<int:cinema_id>/info", methods=["GET"])
def get_cinema_info(cinema_id):
    cinema = Cinema.query.filter_by(cinema_id=cinema_id).first()
    if cinema is None:
        return json.dumps({
            "message": "unknown cinema name"
        }), 404

    return json.dumps({
        "info": cinema.info
    }), 200


@app.route("/cinema/<int:cinema_id>/movies", methods=["GET"])
def get_cinema_movies(cinema_id):
    cinema = Cinema.query.filter_by(cinema_id=cinema_id).first()
    if cinema is None:
        return json.dumps({
            "message": "unknown cinema"
        }), 404

    show_in = ShowIn.query.filter_by(cinema_id=cinema_id).all()
    result = []
    for each in show_in:
        movie = each.movie
        result.append({
            "id": movie.movie_id,
            "name": movie.movie_name,
            "length": movie.length
        })
    return json.dumps(result), 200


@app.route("/cinema/<int:cinema_id>/movie/<int:movie_id>", methods=["GET"])
def get_cinema_movie_show_itme(cinema_id, movie_id):
    cinema = Cinema.query.filter_by(cinema_id=cinema_id).first()
    if cinema is None:
        return json.dumps({
            "message": "unknown cinema"
        }), 404

    movie = Movie.query.filter_by(movie_id=movie_id).first()
    if movie is None:
        return json.dumps({
            "message": "unknown movie"
        }), 404

    show_in = ShowIn.query.filter_by(cinema_id=cinema_id,
                                     movie_id=movie_id).all()
    result = []
    for each in show_in:
        timetables = each.timetables
        for timetable in timetables:
            result.append(timetable.start_at.strftime("%Y-%m-%d %H:%M"))
    return json.dumps(result), 200
