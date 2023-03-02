"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, People, Planets, Favorites, Vehicles
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

api = Blueprint('api', __name__)


@api.route("/login", methods=["POST"])
def login():
    req_email = request.json.get("email", None)
    get_user:User = User.query.filter_by(email=req_email).first()
    password = request.json.get("password", None)
    if get_user.password != password:
        return jsonify({"msg": "Bad email or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)


@api.route("/people", methods=["Get"])
def people_data():
    get_people_list = [person.serialize() for person in People.query.all()]
    return jsonify(get_people_list)

@api.route("/planets", methods=["Get"])
def planets_data():
    get_planets_list = [planet.serialize() for planet in Planets.query.all()]
    return jsonify(get_planets_list) 

@api.route("/favorites", methods=["Get"])
def favorites_data():
    get_favorites_list = [favorite.serialize() for favorite in Favorites.query.all()]
    return jsonify(get_favorites_list)

@api.route("/vehicles", methods=["Get"])
def vehicles_data():
    get_vehicles_list = [vehicle.serialize() for vehicle in Vehicles.query.all()]
    return jsonify(get_vehicles_list)



    



