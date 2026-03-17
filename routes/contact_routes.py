from flask import Blueprint
from controllers.contact_controller import submit_contact, get_all_contacts, delete_contact

contact_bp = Blueprint('contact', __name__)

contact_bp.route('', methods=['POST'])(submit_contact)
contact_bp.route('', methods=['GET'])(get_all_contacts)
contact_bp.route('/<int:contact_id>', methods=['DELETE'])(delete_contact)
