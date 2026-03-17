from flask import jsonify, request
from models.service import Service, Feature
from config.db import db

def get_all_services():
    try:
        services = Service.query.all()
        return jsonify({
            "success": True,
            "data": [s.to_dict() for s in services]
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def create_service():
    data = request.get_json()
    if not data or 'title' not in data or 'description' not in data:
        return jsonify({"success": False, "error": "Title and description are required"}), 400
    
    try:
        new_service = Service(
            title=data['title'],
            description=data['description'],
            impact=data.get('impact', '')
        )
        db.session.add(new_service)
        db.session.flush() # Get the internal ID
        
        if 'features' in data and isinstance(data['features'], list):
            for f_text in data['features']:
                feature = Feature(service_id=new_service.id, feature_text=f_text)
                db.session.add(feature)
        
        db.session.commit()
        return jsonify({
            "success": True,
            "data": new_service.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500

def update_service(service_id):
    data = request.get_json()
    try:
        service = Service.query.get(service_id)
        if not service:
            return jsonify({"success": False, "error": "Service not found"}), 404
        
        service.title = data.get('title', service.title)
        service.description = data.get('description', service.description)
        service.impact = data.get('impact', service.impact)

        # Update features if provided
        if 'features' in data and isinstance(data['features'], list):
            # Clear old features
            Feature.query.filter_by(service_id=service_id).delete()
            # Add new features
            for f_text in data['features']:
                feature = Feature(service_id=service_id, feature_text=f_text)
                db.session.add(feature)

        db.session.commit()
        return jsonify({"success": True, "data": service.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500

def delete_service(service_id):
    try:
        service = Service.query.get(service_id)
        if not service:
            return jsonify({"success": False, "error": "Service not found"}), 404
        
        # Cascade delete is handled by model but we can be explicit
        Feature.query.filter_by(service_id=service_id).delete()
        db.session.delete(service)
        db.session.commit()
        return jsonify({"success": True, "message": "Service deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500
