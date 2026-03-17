from flask import jsonify, request
from models.contact import Contact
from config.db import db

def submit_contact():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data or 'message' not in data:
        return jsonify({"success": False, "error": "Name, email, and message are required"}), 400
    
    try:
        new_contact = Contact(
            name=data['name'],
            email=data['email'],
            message=data['message']
        )
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({
            "success": True,
            "data": new_contact.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500

def get_all_contacts():
    try:
        contacts = Contact.query.order_by(Contact.created_at.desc()).all()
        return jsonify({
            "success": True,
            "data": [c.to_dict() for c in contacts]
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def delete_contact(contact_id):
    try:
        contact = Contact.query.get(contact_id)
        if not contact:
            return jsonify({"success": False, "error": "Contact not found"}), 404
        
        db.session.delete(contact)
        db.session.commit()
        return jsonify({"success": True, "message": "Contact deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500
