from config.db import db

class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    client = db.Column(db.String(255), nullable=True)
    location = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    impact = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(500), nullable=True)
    video_url = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "client": self.client,
            "location": self.location,
            "description": self.description,
            "impact": self.impact.split('\n') if self.impact else [],
            "image": self.image,
            "video_url": self.video_url
        }
