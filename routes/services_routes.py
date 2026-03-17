from flask import Blueprint
from controllers.services_controller import get_all_services, create_service, update_service, delete_service

services_bp = Blueprint('services', __name__)

services_bp.route('', methods=['GET'])(get_all_services)
services_bp.route('', methods=['POST'])(create_service)
services_bp.route('/<int:service_id>', methods=['PUT'])(update_service)
services_bp.route('/<int:service_id>', methods=['DELETE'])(delete_service)
