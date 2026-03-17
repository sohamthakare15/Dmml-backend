from flask import Blueprint
from controllers.directors_controller import get_all_directors, create_director, update_director, delete_director

directors_bp = Blueprint('directors', __name__)

directors_bp.route('', methods=['GET'])(get_all_directors)
directors_bp.route('', methods=['POST'])(create_director)
directors_bp.route('/<int:director_id>', methods=['PUT'])(update_director)
directors_bp.route('/<int:director_id>', methods=['DELETE'])(delete_director)
