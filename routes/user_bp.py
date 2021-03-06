from flask import Blueprint

from controllers.UserController import read, create, show, update, delete

#разделение кода
user_bp = Blueprint('user_bp', __name__)

#определение маршрутов и запросов
user_bp.route('', methods=['GET'])(read)
user_bp.route('', methods=['POST'])(create)
user_bp.route('/', methods=['GET'])(show)
user_bp.route('', methods=['PUT'])(update)
user_bp.route('', methods=['DELETE'])(delete)