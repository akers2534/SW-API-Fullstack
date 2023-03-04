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

@api.route("/people/<int:person_id>", methods=["Get"])
def person_data(person_id):
    person = People.query.get(person_id)
    if person is None:
        raise APIException("Person not found!",status_code=404)
    one_person = person.serialize()
    db.session.commit()
    return (jsonify(one_person)),200

@api.route("/people", methods=["Post"])
def post_data():
    request_body_user = request.get_json()
    new_person = People(name=request_body_user["name"],height=request_body_user["height"],weight=request_body_user["weight"],gender=request_body_user["gender"])
    db.session.add(new_person)
    db.session.commit()
    return jsonify(request_body_user),200

@api.route("/planets", methods=["Get"])
def planets_data():
    get_planets_list = [planet.serialize() for planet in Planets.query.all()]
    return jsonify(get_planets_list) 

@api.route("/planets", methods=["Post"])
def post_planets():
    request_body_user =requ.get_json()
    new_planet = Planets(user=request_body_user["user"],people=request_body_user["people"],planets=request_body_user["planets"],vehicles=request_body_user["vehicles"])
    db.session.add(new_planet)
    db.session.commit()
    return jsonify(request_body_user),200

@api.route("/favorites", methods=["Get"])
def favorites_data():
    get_favorites_list = [favorite.serialize() for favorite in Favorites.query.all()]
    return jsonify(get_favorites_list)

@api.route("/favorites", methods=["Delete"])
def delete_data():
    request_body_user =requ.get_json()
    new_favorite = Favorites(name=request_body_user["name"],terrain=request_body_user["terrain"],population=request_body_user["population"],gravity=request_body_user["gravity"])
    db.session.add(new_planet)
    db.session.commit()
    return jsonify(request_body_user),200

@api.route("/vehicles", methods=["Get"])
def vehicles_data():
    get_vehicles_list = [vehicle.serialize() for vehicle in Vehicles.query.all()]
    return jsonify(get_vehicles_list)

@api.route("/vehicles", methods=["Get"])
def vehicle_data():
    vehicle = Vehicle.query.get(vehicle_data)
    if vehicle is None:
        raise APIException("Vehicle not found!",status_code=404)
    one_vehicle = vehicle.serialize()
    db.session.commit()
    return (jsonify(one_vehicle)),200

@api.route("/vehicles", methods=["Post"])
def post_vehicles():
    request_body_user =requ.get_json()
    new_vehicle = Vehicles(name=request_body_user["name"],model=request_body_user["model"],length=request_body_user["length"],crew=request_body_user["crew"])
    db.session.add(new_vehicle)
    db.session.commit()
    return jsonify(request_body_user),200




    



