from flask import Blueprint
from flask import abort
from flask import request
from flask import jsonify


from ..repository.user_repository import UserRepository
from .service.from_dict_to_user import FromDictToUser
from .service.user_validator import UserValidator

users = Blueprint("users", __name__, url_prefix="/users")


@users.route('', methods=["POST"])
def new_user():
    user_repository = UserRepository()

    if not UserValidator().validate_user(request.json):
        abort(400)

    email = request.json.get('email')
    if user_repository.getByEmail(email):
        abort(400)

    user = FromDictToUser.with_dict(request.json)
    user_repository.add(user)

    return '200'


@users.route('/', methods=["GET"])
def get_user():
    return jsonify({"Hola": "Hola"})
