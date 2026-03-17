from config.db import db

class Director(db.Model):
    __tablename__ = 'directors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255), nullable=False)
    experience = db.Column(db.String(255), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "experience": self.experience,
            "bio": self.bio,
            "image": self.image
        }
