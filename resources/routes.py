from .movie import MovieApi, MoviesApi
from resources.auth import SignUpApi, LoginApi


def initialize_routes(api):
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(MovieApi, '/api/movies/<movie_id>')
    api.add_resource(SignUpApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
