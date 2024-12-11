"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, favPeople, favPlanets
#from models import Person
app = Flask(__name__)
app.url_map.strict_slashes = False
db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)
# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code
# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)
@app.route('/user', methods=['GET'])
def get_users():
    usuarios = User.query.all()
    usuarios_serializados = [usuario.serialize() for usuario in usuarios]
    return jsonify(usuarios_serializados), 200
@app.route('/people', methods=['GET'])
def get_people():
    personas = People.query.all()
    personas_serializadas = [persona.serialize() for persona in personas]
    return jsonify(personas_serializadas), 200
@app.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    personas = People.query.filter_by(id = people_id)
    personas_serializadas = [persona.serialize() for persona in personas]
    if(personas_serializadas == []):
        return jsonify('No hay ninguna persona con este ID'), 400
    return jsonify(personas_serializadas), 200
@app.route('/planets', methods=['GET'])
def get_planets():
    planetas = Planets.query.all()
    planetas_serializados = [planeta.serialize() for planeta in planetas]
    return jsonify(planetas_serializados), 200
@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planetas = Planets.query.filter_by(id = planet_id)
    planetas_serializados = [planeta.serialize() for planeta in planetas]
    if(planetas_serializados == []):
        return jsonify('No hay ninguna persona con este ID'), 400
    return jsonify(planetas_serializados), 200
@app.route('/user/favorites', methods=['GET'])
def get_favs():
    favoritos = favPlanets.query.all(), favPeople.query.all()
    favoritos_serializados = [favorito.serialize() for favorito in favoritos]
    return jsonify(favoritos_serializados), 200
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
