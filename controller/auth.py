from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from model.User import User, UserSchema
from config import db, hashing

""" Post method for sign up user """
def signup():
    
    if not request.is_json:
        return jsonify({"msg" : "Not a json output"}), 400
    username =  request.json.get("username", None)
    password =  request.json.get("password", None) 
    password_hash = hashing.hash_value(password, salt="boapp")
    user  = {
        "username" : username,
        "password" : password_hash
    }

    if not password:
        return jsonify({"msg" : "Password is empty"}), 400

    if not username:
        return jsonify({"msg" : "Username is empty"}), 400 

    #check whether there is user in db at same name
    existing_user = User.query.filter(User.username == username).first()
    # return jsonify({"username": username}), 200
    if existing_user is None:

        schema = UserSchema()
        new_user = schema.load(user, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return schema.dump(new_user), 200

    else :
        return jsonify({"msg" : "User has already exist !!!"}), 400
    
    

""" Post method login user """
def login():
    if not request.is_json:
        return jsonify({"msg" : "Not a json output !!!"}), 400
    username =  request.json.get("username", None)
    password =  request.json.get("password", None)
    password_hash = hashing.hash_value(password, salt="boapp")
    if not username:
        return jsonify({"msg" :  "Username is missing"}), 400

    if not password:
        return jsonify({"msg" : "Password is missing " }), 400 

    # Query in database whether user actually exists
    existing_user = User.query.filter_by( username = username, password = password_hash).first()
    
    if existing_user is None:
        return jsonify({"msg" : "Invalid username or user not exists!!!"})
    #create access token from username and id
    token_obj = {
        "username" : existing_user.username,
        "id" : existing_user.id
    } 
    access_token = create_access_token(token_obj)
    return jsonify(access_token = access_token)


""" Get current user from auth token """
@jwt_required
def get_user():
    if not request.is_json:
        return({"msg" : "This is not a valid json"})
    current_user = get_jwt_identity()
    return jsonify(current_user=current_user), 200