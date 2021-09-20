"""CRUD operations."""
import json
from model import db, Broker, BuildersRisk, GeneralLiability, connect_to_db

def create_broker(email, password):
    """Create and return a new broker."""
    broker = Broker(email= email, 
                password= password)

    db.session.add(broker)
    db.session.commit()
    return broker

def create_builders_risk(email, company_name, zip_code, 
                        project_description, building_type):
    """Create and return a new builders risk form."""
    builders_risk = BuildersRisk(email = email, 
                company_name = company_name, 
                zip_code = zip_code,
                project_description = project_description, 
                building_type = building_type)

    db.session.add(builders_risk)
    db.session.commit()
    return builders_risk

def create_general_liability(email, company_name, zip_code, 
                        project_description, business_type):
    """Create and return a new builders risk form."""
    general_liability = GeneralLiability(email = email, 
                company_name = company_name, 
                zip_code = zip_code,
                project_description = project_description, 
                business_type = business_type)

    db.session.add(general_liability)
    db.session.commit()
    return general_liability