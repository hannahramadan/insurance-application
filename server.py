"""Server for insurance app."""

from flask import (Flask, render_template, request, flash, session, redirect, make_response)
import requests
import pdfkit
from model import connect_to_db
import crud
# Asks Jinja2 to throw errors for undefined variables, else fails silently
from jinja2 import StrictUndefined
from pyvirtualdisplay import Display

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

    crud.create_builders_risk(email, company_name, zip_code, 
                        project_description, building_type)

    rendered = render_template('builders_risk_pdf.html',email=email, company_name=company_name, zip_code=zip_code, 
                        project_description=project_description, building_type=building_type)

    display = Display(visible=0, size=(1024, 768))

    try:
        display.start()
        pdf = pdfkit.from_string(rendered, False)
    finally:
        display.stop()

    response = make_response(pdf)

    # tells brower its about to get a pdf file
    response.headers['Content-Type'] = 'application/pdf'
    # loads pdf in browers vs download
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'

    return response

@app.route('/general_liability_form', methods=['POST'])
def general_liability_form():
    email = request.form.get('email')
    company_name = request.form.get('company_name')
    zip_code = request.form.get('zip_code')
    project_description = request.form.get('project_description')
    business_type = request.form.get('business_type')

    crud.create_general_liability(email, company_name, zip_code, 
                        project_description, business_type)

    rendered = render_template('general_liability_pdf.html',email=email, company_name=company_name, zip_code=zip_code, 
                        project_description=project_description, business_type=business_type)

    display = Display(visible=0, size=(1024, 768))

    try:
        display.start()
        pdf = pdfkit.from_string(rendered, False)
    finally:
        display.stop()

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'

    return response


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)