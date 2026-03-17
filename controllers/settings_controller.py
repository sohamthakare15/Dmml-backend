from flask import jsonify, request
from models.settings import Setting
from config.db import db

def get_setting(key):
    setting = Setting.query.filter_by(key=key).first()
    if not setting:
        return jsonify({"success": False, "error": "Setting not found"}), 404
    return jsonify({"success": True, "data": setting.to_dict()}), 200

def update_setting(key):
    data = request.get_json()
    value = data.get('value')
    
    setting = Setting.query.filter_by(key=key).first()
    if not setting:
        # Create it if it doesn't exist
        setting = Setting(key=key, value=value)
        db.session.add(setting)
    else:
        setting.value = value
    
    try:
        db.session.commit()
        return jsonify({"success": True, "data": setting.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500

def get_all_settings():
    settings = Setting.query.all()
    return jsonify({"success": True, "data": {s.key: s.value for s in settings}}), 200
