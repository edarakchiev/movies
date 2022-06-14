from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restful import Api
from database.db import initialize_db
from resources.routes import initialize_routes
from flask_jwt_extended import JWTManager

app = Flask(__name__)
# app.config.from_envvar('ENV')
app.config['JWT_SECRET_KEY'] = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie'
}
initialize_db(app)
initialize_routes(api)

app.run()
