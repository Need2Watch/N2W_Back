from flask import Blueprint, abort, jsonify, request

from ..application.create_user import CreateUser
from ..application.update_user import UpdateUser
from ..domain.already_existing_user_error import AlreadyExistingUserError
from ..domain.no_existing_user_with_id_error import NoExistingUserWithIdError
from ..domain.user_id import UserId
from .from_dict_to_user import FromDictToUser
from .from_user_to_dict import FromUserToDict
from .login_validator import LoginValidator
from .user_mysql_repository import UserMysqlRepository
from .user_validator import UserValidator

users = Blueprint("users", __name__, url_prefix="/users")


@users.route('', methods=["POST"])
def new_user():
    user_repository = UserMysqlRepository()

    if not UserValidator().validate_user(request.json):
        abort(400)

    try:
        CreateUser(user_repository).run(request.json)
    except Exception as error:
        if isinstance(error, AlreadyExistingUserError):
            abort(409)
        else:
            abort(500)

    return '200'


@users.route('/<string:user_id>', methods=["PUT"])
def user_update(user_id: str):
    user_repository = UserMysqlRepository()

    try:
        UpdateUser(user_repository).run(user_id, request.json)
    except Exception as error:
        if isinstance(error, NoExistingUserWithIdError):
            abort(404)
        else:
            abort(500)

    return '200'


@users.route("/login", methods=["POST"])
def login():
    user_repository = UserMysqlRepository()

    if not LoginValidator().validate_login(request.json):
        abort(400)

    email = request.json.get('email')
    password = request.json.get('password')

    user = user_repository.find_by_email(email)
    if not user:
        abort(404)

    if not user.verifyPassword(password):
        abort(403)

    return jsonify(FromUserToDict.with_user(user))
