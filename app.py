from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Movie

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie'
}
initialize_db(app)


@app.route('/movies')
def get_movies():
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)


@app.route('/movies/<movie_id>')
def get_movie(movie_id):
    movie = Movie.objects().get(id=movie_id).to_json()
    return Response(movie, mimetype="application/json", status=200)


@app.route('/movies', methods=['POST'])
def add_movie():
    body = request.get_json()
    movie = Movie(**body).save()
    movie_id = movie.id
    return {'id': str(movie_id)}, 200


@app.route('/movies/<movie_id>', methods=['PUT'])
def update_movie(movie_id):
    body = request.get_json()
    Movie.objects.get(id=movie_id).update(**body)
    return '', 200


@app.route('/movies/<movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    Movie.objects.get(id=movie_id).delete()
    return '', 200


app.run()
