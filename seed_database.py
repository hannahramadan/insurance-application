"""Script to seed database."""

import os
import crud
import model
import server
from model import db, Broker, BuildersRisk, GeneralLiability

os.system('dropdb insuranceapp')
os.system('createdb insuranceapp')

model.connect_to_db(server.app) 
model.db.create_all() 

for n in range(2): 
    """Create fake brokers"""
    email = f'user{n}@test.com' 
    password = 'test'

    broker = crud.create_broker(email, password)

for n in range(2): 
    """Create fake builders risk"""
    email = f'user{n}@test.com' 
    company_name = f'company{n}' 
    zip_code = f'1111{n}'
    project_description = "some project description" 
    building_type = "Hotel/Motel"

    broker = crud.create_builders_risk(email, company_name, zip_code, 
                        project_description, building_type)

for n in range(2): 
    """Create fake general liability"""
    email = f'user{n}@test.com' 
    company_name = f'company{n}' 
    zip_code = f'1111{n}'
    project_description = "some project description" 
    business_type = "developer"

    broker = crud.create_general_liability(email, company_name, zip_code, 
                        project_description, business_type)