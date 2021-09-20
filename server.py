"""Server for insurance app."""

from flask import (Flask, render_template, request, flash, session, redirect)
import requests
from model import connect_to_db
import crud

# Asks Jinja2 to throw errors for undefined variables, else fails silently
from jinja2 import StrictUndefined

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View insurance app homepage."""

    return render_template('homepage.html')

@app.route('/builders_risk')
def builders_risk():
    """Builders Risk Application."""

    return render_template('builders_risk.html')

@app.route('/commercial_general_liability')
def commercial_general_liability():
    """Commercial General Liability Application."""

    return render_template('commercial_general_liability.html')

@app.route('/builders_risk_form', methods=['POST'])
def builders_risk_form():
    email = request.form.get('email')
    company_name = request.form.get('company_name')
    zip_code = request.form.get('zip_code')
    project_description = request.form.get('project_description')
    building_type = request.form.get('building_type')

    form = crud.create_builders_risk(email, company_name, zip_code, 
                        project_description, building_type)

    return render_template('success.html')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)