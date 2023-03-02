from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    __tablename__ = "user"

    

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    height = db.Column(db.String(25), unique=False, nullable=False)
    weight = db.Column(db.String(20), unique=False, nullable=False)
    gender = db.Column(db.String(20), unique=False, nullable=False)
    planets_id = db.Column(db.Integer, db.ForeignKey("planets.id"), nullable=False)
    __tablename__ = "people"
    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "gender": self.gender,
            # do not serialize the password, its a security breach
        }


class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    terrain = db.Column(db.String(150), unique=False, nullable=False)
    gravity = db.Column(db.String(150),unique=False, nullable=False)
    name = db.Column(db.String(150), unique=False, nullable=False)
    population = db.Column(db.Integer, unique=False, nullable=False)
    people = db.relationship("People", backref="Planets", lazy=True)
    __tablename__ = "planets"
    

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain,
            "population": self.population,
            "gravity": self.gravity,
            # do not serialize the password, its a security breach
        }


class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planets = db.relationship("Planets", backref="favorites")
    people = db.relationship("People", backref="favorites")
    user = db.relationship("User", backref="favorites", uselist=True)
    planet_id = db.Column(db.Integer, db.ForeignKey("planets.id") )
    people_id = db.Column(db.Integer, db.ForeignKey("people.id") )
    user_id = db.Column(db.Integer, db.ForeignKey("user.id") )
    __tablename__ = "favorites"


    def __repr__(self):
        return '<Favorites %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain,
            "population": self.population,
            "gravity": self.gravity,
            # do not serialize the password, its a security breach
        } 

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=False, nullable=False)
    model = db.Column(db.String(150),unique=False, nullable=False)
    length = db.Column(db.String(150), unique=False, nullable=False)
    crew = db.Column(db.String(150), unique=False, nullable=False)
    people = db.relationship("People", backref="Vehicless", lazy=True)
    planet_id = db.Column(db.Integer, db.ForeignKey("planets.id") )
    people_id = db.Column(db.Integer, db.ForeignKey("people.id") )
    user_id = db.Column(db.Integer, db.ForeignKey("user.id") )


    __tablename__ = "vehicles"
    

    def __repr__(self):
        return '<Vehicles %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "length": self.length,
            "crew": self.crew,
            # do not serialize the password, its a security breach
        }
