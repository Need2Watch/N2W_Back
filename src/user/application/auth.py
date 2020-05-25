from flask import Blueprint
from flask import abort
from flask import request
from flask import jsonify
from cerberus import Validator


from ..repository.user_repository import UserRepository
from .service.from_dict_to_user import FromDictToUser

users = Blueprint("users", __name__, url_prefix="/users")

user_schema = {
    'user_id': {'type': 'string', 'required': True},
    'username': {'type': 'string', 'required': True},
    'password': {'type': 'string', 'required': True},
    'first_name': {'type': 'string', 'required': True},
    'last_name': {'type': 'string', 'required': True},
    'email': {'type': 'string', 'required': True},
    'country': {'type': 'string', 'required': True},
    'city': {'type': 'string', 'required': True},
}


@users.route('/', methods=["POST"])
def new_user():
    user_repository = UserRepository()

    validator = Validator()
    if not validator.validate(request.json, user_schema):
        abort(400) # existing user

    email = request.json.get('email')
    if user_repository.getByEmail(email):
        abort(400) # existing user

    user = FromDictToUser.with_dict(request.json)
    user_repository.add(user)

    return 200


@users.route('/', methods=["GET"])
def get_user():
    return jsonify({"Hola": "Hola"})