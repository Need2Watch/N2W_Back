from flask import Blueprint
from flask import request
from flask import jsonify
from flask import abort

from ..repository.user_repository import UserRepository
from .service.from_user_to_dict import FromUserToDict
from .service.login_validator import LoginValidator

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/login", methods=["POST"])
def login():
    user_repository = UserRepository()

    if not LoginValidator().validate_login(request.json):
        abort(400)

    email = request.json.get('email')
    password = request.json.get('password')

    user = user_repository.getByEmail(email)
    if not user:
        abort(404)

    if not user.verifyPassword(password):
        abort(403)

    return jsonify(FromUserToDict.with_user(user))
