import json

from app import app
from ..models import ShowIn, Movie


@app.route("/movie", methods=["GET"])
def get_movie_list():
    movies = Movie.query.all()
    result = []
    for movie in movies:
        result.append({
            "id": movie.movie_id,
            "name": movie.movie_name,
            "length": movie.length
        })
    return json.dumps(result), 200


@app.route("/movie/<int:movie_id>/info", methods=["GET"])
def get_movie_info(movie_id):
    movie = Movie.query.filter_by(movie_id=movie_id).first()
    if movie is None:
        return json.dumps({
            "message": "unknown movie"
        }), 404

    return json.dumps({
        "info": movie.info
    }), 200


@app.route("/movie/<int:movie_id>/cinemas", methods=["GET"])
def get_movie_cinemas(movie_id):
    movie = Movie.query.filter_by(movie_id=movie_id).first()
    if movie is None:
        return json.dumps({
            "message": "unknown movie"
        }), 404

    show_in = ShowIn.query.filter_by(movie_id=movie_id).all()
    result = []
    for each in show_in:
        cinema = each.cinema
        result.append({
            "id": cinema.cinema_id,
            "name": cinema.cinema_name
        })
    return json.dumps(result), 200
