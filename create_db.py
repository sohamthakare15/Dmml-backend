import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def create_database():
    host = os.getenv("DB_HOST", "127.0.0.1")
    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "")
    db_name = os.getenv("DB_NAME", "dmml_db")

    try:
        # Connect without specifying a database
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password
        )
        
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            print(f"Database '{db_name}' created or already exists.")
            
        connection.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_database()
