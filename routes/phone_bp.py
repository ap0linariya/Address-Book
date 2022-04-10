from flask import Blueprint

from controllers.PhoneController import read, create, show, update, delete

phone_bp = Blueprint('phone_bp', __name__)

phone_bp.route('', methods=['GET'])(read)
phone_bp.route('', methods=['POST'])(create)
phone_bp.route('/', methods=['GET'])(show)
phone_bp.route('', methods=['PUT'])(update)
phone_bp.route('', methods=['DELETE'])(delete)