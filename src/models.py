from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.email
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email
            # do not serialize the password, its a security breach
        }
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    height = db.Column(db.String(80), unique=False, nullable=False)
    mass = db.Column(db.Integer, unique=False, nullable=False)
    hair_color = db.Column(db.String(120), unique=False, nullable=False)
    def __repr__(self):
        return '<People %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color
            # do not serialize the password, its a security breach
        }
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    climate = db.Column(db.String(80), unique=False, nullable=False)
    terrain = db.Column(db.String(80), unique=False, nullable=False)
    population = db.Column(db.Integer, unique=False, nullable=False)
    def __repr__(self):
        return '<Planets %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.population
            # do not serialize the password, its a security breach
        }
class favPeople(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), unique=False, nullable=True)
    person_id = db.Column(db.Integer, db.ForeignKey(People.id), unique=False, nullable=False)
    usuario = db.relationship('User')
    people = db.relationship('People')
    def __repr__(self):
        return '<favPeople %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "person_id": self.person_id
            # do not serialize the password, its a security breach
        }
class favPlanets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), unique=False, nullable=True)
    planet_id = db.Column(db.Integer, db.ForeignKey(Planets.id), unique=False, nullable=False)
    usuario = db.relationship('User')
    planet = db.relationship('Planets')
    def __repr__(self):
        return '<favPlanets %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "planet_id": self.planet_id
            # do not serialize the password, its a security breach
        }