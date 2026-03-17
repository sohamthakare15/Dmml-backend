from flask import Blueprint
from controllers.admin_controller import admin_login
from controllers.upload_controller import upload_image
from controllers.settings_controller import get_all_settings, update_setting

admin_bp = Blueprint('admin', __name__)

admin_bp.route('/login', methods=['POST'])(admin_login)
admin_bp.route('/upload', methods=['POST'])(upload_image)
admin_bp.route('/settings', methods=['GET'])(get_all_settings)
admin_bp.route('/settings/<key>', methods=['POST'])(update_setting)
