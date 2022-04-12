from flask import Blueprint

from controllers.EmailController import read, create, show, update, delete

#разделение кода
email_bp = Blueprint('email_bp', __name__)

#определение маршрутов и запросов
email_bp.route('', methods=['GET'])(read)
email_bp.route('', methods=['POST'])(create)
email_bp.route('/', methods=['GET'])(show)
email_bp.route('', methods=['PUT'])(update)
email_bp.route('', methods=['DELETE'])(delete)