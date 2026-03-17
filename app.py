import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from config.db import init_db, db
from routes.services_routes import services_bp
from routes.projects_routes import projects_bp
from routes.directors_routes import directors_bp
from routes.contact_routes import contact_bp
from routes.admin_routes import admin_bp
from models.settings import Setting

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Enable CORS
    CORS(app, resources={r"/api/*": {"origins": os.getenv("CORS_ORIGIN", "http://localhost:3000")}})
    
    # Initialize Database
    init_db(app)
    
    # Create tables if they don't exist
    with app.app_context():
        db.create_all()
    
    # Register Blueprints
    app.register_blueprint(services_bp, url_prefix='/api/services')
    app.register_blueprint(projects_bp, url_prefix='/api/projects')
    app.register_blueprint(directors_bp, url_prefix='/api/directors')
    app.register_blueprint(contact_bp, url_prefix='/api/contact')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    
    @app.route('/')
    def index():
        return {"message": "DMML API is running"}, 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
