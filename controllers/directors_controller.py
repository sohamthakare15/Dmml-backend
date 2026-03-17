from flask import jsonify, request
from models.director import Director
from config.db import db

def get_all_directors():
    try:
        directors = Director.query.all()
        return jsonify({
            "success": True,
            "data": [d.to_dict() for d in directors]
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def create_director():
    data = request.get_json()
    if not data or 'name' not in data or 'role' not in data:
        return jsonify({"success": False, "error": "Name and role are required"}), 400
    
    try:
        new_director = Director(
            name=data['name'],
            role=data['role'],
            experience=data.get('experience', ''),
            bio=data.get('bio', ''),
            image=data.get('image', '')
        )
        db.session.add(new_director)
        db.session.commit()
        return jsonify({"success": True, "data": new_director.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500

def update_director(director_id):
    data = request.get_json()
    try:
        director = Director.query.get(director_id)
        if not director:
            return jsonify({"success": False, "error": "Director not found"}), 404
        
        director.name = data.get('name', director.name)
        director.role = data.get('role', director.role)
        director.experience = data.get('experience', director.experience)
        director.bio = data.get('bio', director.bio)
        director.image = data.get('image', director.image)

        db.session.commit()
        return jsonify({"success": True, "data": director.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500

def delete_director(director_id):
    try:
        director = Director.query.get(director_id)
        if not director:
            return jsonify({"success": False, "error": "Director not found"}), 404
        
        db.session.delete(director)
        db.session.commit()
        return jsonify({"success": True, "message": "Director deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500
