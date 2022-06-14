from flask import Response, request
from database.models import Movie
from flask_restful import Resource


class MoviesApi(Resource):
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        movie = Movie(**body).save()
        movie_id = movie.id
        return {'id': str(movie_id)}, 200


class MovieApi(Resource):
    def get(self, movie_id):
        movie = Movie.objects().get(id=movie_id).to_json()
        return Response(movie, mimetype="application/json", status=200)

    def put(self, movie_id):
        body = request.get_json()
        Movie.objects.get(id=movie_id).update(**body)
        return '', 200

    def delete(self, movie_id):
        Movie.objects.get(id=movie_id).delete()
        return '', 200
