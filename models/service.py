from config.db import db

class Service(db.Model):
    __tablename__ = 'services'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    impact = db.Column(db.Text, nullable=True)
    
    # Relationship: One Service -> Many Features
    features = db.relationship('Feature', backref='service', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "impact": self.impact,
            "features": [f.feature_text for f in self.features]
        }

class Feature(db.Model):
    __tablename__ = 'features'
    
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)
    feature_text = db.Column(db.String(255), nullable=False)
