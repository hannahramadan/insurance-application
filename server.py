"""Server for insurance app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from dbmodel import connect_to_db
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
    """Builders Risk Application,"""

    return render_template('builders_risk.html')

@app.route('/commercial_general_liability')
def commercial_general_liability():
    """Commercial General Liability Application,"""

    return render_template('commercial_general_liability.html')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)