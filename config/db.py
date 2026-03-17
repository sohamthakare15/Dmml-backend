import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

db = SQLAlchemy()

def init_db(app):
    host = os.getenv("DB_HOST", "localhost")
    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "")
    db_name = os.getenv("DB_NAME", "dmml_db")
    
    # Percent-encode password for URI (handles special characters like @)
    encoded_password = quote_plus(password)
    
    # Use pymysql as the driver
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{user}:{encoded_password}@{host}/{db_name}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)
