from app import create_app
from config.db import db
from models.service import Service, Feature
from models.project import Project
from models.director import Director
from models.settings import Setting

def seed_data():
    app = create_app()
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Seed global settings
        initial_settings = [
            {"key": "showcase_video_url", "value": "https://drive.google.com/file/d/1dvwtPR5ji2mDFEarLUmQMZbdpfksTTKL/view?usp=sharing"}
        ]
        for s_set in initial_settings:
            new_setting = Setting(key=s_set['key'], value=s_set['value'])
            db.session.add(new_setting)

        # Seed Services
        services = [
            {
                "title": "Intelligent Traffic Management Systems (IITMS)",
                "description": "Advanced intelligent traffic systems with real-time monitoring, signal automation, and centralized control to optimize urban mobility.",
                "impact": "Reduced congestion, improved road safety, and data-driven traffic planning.",
                "features": ["Signal automation", "Centralized control systems", "Traffic analytics", "Real-time monitoring"]
            },
            {
                "title": "Smart City ICT Infrastructure",
                "description": "End-to-end ICT infrastructure solutions for smart city operations, enabling data-driven governance and efficient urban management.",
                "impact": "Better governance, improved urban efficiency, and scalable digital infrastructure.",
                "features": ["Integrated city systems", "Data-driven management", "Scalable infrastructure"]
            },
            {
                "title": "Safe City CCTV Surveillance",
                "description": "IP-based CCTV surveillance systems with centralized monitoring and high-resolution imaging for public safety and security.",
                "impact": "Increased public safety, faster incident response, and comprehensive monitoring.",
                "features": ["Real-time video monitoring", "Video management systems", "High-resolution cameras"]
            },
            {
                "title": "Metro Rail ICT & Telecom Solutions",
                "description": "Robust telecom and ICT infrastructure for reliable metro rail networks, ensuring seamless communication and operational safety.",
                "impact": "Reliable metro operations, improved passenger experience, and enhanced safety.",
                "features": ["Communication systems", "Network infrastructure", "System integration"]
            },
            {
                "title": "3D & 4D Urban Mapping",
                "description": "Advanced 3D and 4D mapping solutions for precise urban planning, development, and architectural visualization.",
                "impact": "Accurate city planning, efficient development, and better visualization of urban growth.",
                "features": ["3D visualization", "Temporal data mapping", "Planning tools"]
            },
            {
                "title": "Digital Building Assessment",
                "description": "Comprehensive digital assessment of building structures for safety, compliance, and structural integrity.",
                "impact": "Enhanced building safety, regulatory compliance, and structural health monitoring.",
                "features": ["Structural assessment", "Digital documentation", "Safety audits"]
            },
            {
                "title": "Traffic Towing Services",
                "description": "Efficient traffic towing and management services to ensure clear roads and disciplined traffic flow in urban areas.",
                "impact": "Reduced road obstructions, better traffic discipline, and improved emergency access.",
                "features": ["24/7 towing services", "Parking management", "Rapid response units"]
            }
        ]

        for s_data in services:
            new_service = Service(
                title=s_data['title'],
                description=s_data['description'],
                impact=s_data['impact']
            )
            db.session.add(new_service)
            db.session.flush()
            for f_text in s_data['features']:
                feature = Feature(service_id=new_service.id, feature_text=f_text)
                db.session.add(feature)

        # Seed Projects
        projects = [
            {
                "title": "Intelligent Traffic Signal System",
                "location": "Nagpur",
                "client": "Nagpur Municipal Corporation",
                "description": "Installation and maintenance of advanced intelligent traffic signal systems across Nagpur city.",
                "impact": "Optimized traffic flow, reduced wait times, and improved pedestrian safety at major intersections.",
                "image": "https://images.unsplash.com/photo-1473968512647-3e447244af8f?q=80&w=2070&auto=format&fit=crop"
            },
            {
                "title": "Smart City Operations & Maintenance",
                "location": "Nagpur",
                "client": "Nagpur Smart and Sustainable City Development Corporation Ltd",
                "description": "Long-term operations and maintenance of critical smart city infrastructure for a period of 5 years.",
                "impact": "Ensured 24/7 system reliability, proactive maintenance, and technical support for city-wide smart initiatives.",
                "image": "https://images.unsplash.com/photo-1519501025264-65ba15a82390?q=80&w=2064&auto=format&fit=crop"
            },
            {
                "title": "Metro ICT Infrastructure",
                "location": "Nagpur & Pune",
                "client": "Maha Metro Rail Corporation Limited",
                "description": "Deployment of comprehensive ICT and telecom infrastructure for the Nagpur and Pune metro rail networks.",
                "impact": "Seamless operational communication, integrated passenger information systems, and enhanced safety networks.",
                "image": "https://images.unsplash.com/photo-1449844908441-8829872d2607?q=80&w=2070&auto=format&fit=crop"
            },
            {
                "title": "Video Management System",
                "location": "Nagpur",
                "client": "Smart City Project",
                "description": "Implementation of an enterprise-grade Video Management System for centralized city surveillance and security monitoring.",
                "impact": "Centralized oversight, AI-driven incident detection, and improved coordination for public safety agencies.",
                "image": "https://images.unsplash.com/photo-1542382103328-98e87493a1cf?q=80&w=2069&auto=format&fit=crop"
            },
            {
                "title": "Traffic Towing Services",
                "location": "Nagpur",
                "client": "Nagpur Traffic Police",
                "description": "Providing end-to-end traffic towing and management services in collaboration with the Nagpur Traffic Police.",
                "impact": "Improved road congestion management, enforced parking discipline, and faster removal of disabled vehicles.",
                "image": "https://images.unsplash.com/photo-1514924013411-cbf25faa35bb?q=80&w=2064&auto=format&fit=crop"
            }
        ]

        for p_data in projects:
            new_project = Project(
                title=p_data['title'],
                location=p_data['location'],
                client=p_data['client'],
                description=p_data['description'],
                impact=p_data['impact'],
                image=p_data.get('image', '')
            )
            db.session.add(new_project)

        # Seed Directors
        directors = [
            {"name": "Rujuta Kayarkar", "role": "Director", "experience": "Strategic Leadership & Corporate Governance"},
            {"name": "Sameer Kayarkar", "role": "Director", "experience": "Operations & Project Management"},
            {"name": "Ajay Singh", "role": "Director", "experience": "Technical Strategy & Infrastructure Solutions"}
        ]

        for d_data in directors:
            new_director = Director(
                name=d_data['name'],
                role=d_data['role'],
                experience=d_data['experience']
            )
            db.session.add(new_director)

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()
