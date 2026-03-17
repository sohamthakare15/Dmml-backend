import os
from flask import jsonify, request

def admin_login():
    data = request.get_json()
    secret = os.getenv("ADMIN_SECRET", "Soham@2005")
    
    if data and data.get("password") == secret:
        return jsonify({
            "success": True,
            "message": "Login successful"
        }), 200
    
    return jsonify({
        "success": False,
        "error": "Invalid credentials"
    }), 401
