from flask import Blueprint
from controllers.projects_controller import get_all_projects, create_project, update_project, delete_project

projects_bp = Blueprint('projects', __name__)

projects_bp.route('', methods=['GET'])(get_all_projects)
projects_bp.route('', methods=['POST'])(create_project)
projects_bp.route('/<int:project_id>', methods=['PUT'])(update_project)
projects_bp.route('/<int:project_id>', methods=['DELETE'])(delete_project)
