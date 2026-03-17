from flask import jsonify, request
from models.project import Project
from config.db import db

def get_all_projects():
    try:
        projects = Project.query.all()
        return jsonify({
            "success": True,
            "data": [p.to_dict() for p in projects]
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def create_project():
    data = request.get_json()
    if not data or 'title' not in data or 'location' not in data or 'description' not in data:
        return jsonify({"success": False, "error": "Title, location, and description are required"}), 400
    
    try:
        new_project = Project(
            title=data['title'],
            client=data.get('client', ''),
            location=data['location'],
            description=data['description'],
            impact=data.get('impact', ''),
            image=data.get('image', ''),
            video_url=data.get('video_url', '')
        )
        db.session.add(new_project)
        db.session.commit()
        return jsonify({
            "success": True,
            "data": new_project.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500

def update_project(project_id):
    data = request.get_json()
    try:
        project = Project.query.get(project_id)
        if not project:
            return jsonify({"success": False, "error": "Project not found"}), 404
        
        project.title = data.get('title', project.title)
        project.client = data.get('client', project.client)
        project.location = data.get('location', project.location)
        project.description = data.get('description', project.description)
        project.impact = data.get('impact', project.impact)
        project.image = data.get('image', project.image)
        project.video_url = data.get('video_url', project.video_url)

        db.session.commit()
        return jsonify({"success": True, "data": project.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500

def delete_project(project_id):
    try:
        project = Project.query.get(project_id)
        if not project:
            return jsonify({"success": False, "error": "Project not found"}), 404
        
        db.session.delete(project)
        db.session.commit()
        return jsonify({"success": True, "message": "Project deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500
