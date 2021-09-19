"""Models for insurance application."""

from flask_sqlalchemy import SQLAlchemy

#create new SQLAlchemy instance variable. 
db = SQLAlchemy()

# Config the object
def connect_to_db(flask_app, db_uri="postgresql:///insuranceapp", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

class Broker(db.Model):
    """A Shepherd broker."""

    __tablename__ = "brokers"

    broker_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique = True)
    password = db.Column(db.String(50), nullable=False)

class Forms(db.Model):
    """A brokers form(s)."""

    __tablename__ = "forms"

    form_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    #making nullable for now since might not add brokers/users
    broker_id = db.Column(db.Integer, db.ForeignKey('brokers.broker_id'),nullable=True)
    builders_risk_id = db.Column(db.Integer, db.ForeignKey('builders_risk.builders_risk_id'), nullable=True)
    general_liability_id = db.Column(db.Integer, db.ForeignKey('general_liability.general_liability_id'), nullable=True)

    broker = db.relationship('Broker', backref = "forms") 
    builders_risk = db.relationship('BuildersRisk', backref = "forms")
    general_liability = db.relationship('GeneralLiability', backref = "forms")

class BuildersRisk(db.Model):
    """A builders risk form."""

    __tablename__ = "builders_risk"

    builders_risk_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    company_name = db.Column(db.String(100))
    email = db.Column(db.String(50))
    company_url = db.Column(db.String(50))
    zip_code = db.Column(db.Integer)
    project_address = db.Column(db.String(200))
    building_type = db.Column(db.String(50))
    coverage_needed = db.relationship('BuildersRiskCoverage', backref = "builders_risk_coverage")

class BuildersRiskCoverage(db.Model):
    """A builders risk coverage."""

    __tablename__ = "builders_risk_coverage"

    coverage_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    builders_risk_id = db.Column(db.Integer, db.ForeignKey('builders_risk.builders_risk_id'))
    materials = db.Column(db.Boolean, unique=False)
    foundation = db.Column(db.Boolean, unique=False)
    temp_strucutres = db.Column(db.Boolean, unique=False)
    weather = db.Column(db.Boolean, unique=False)

class GeneralLiability(db.Model):
    """A general liability form."""

    __tablename__ = "general_liability"

    general_liability_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    company_name = db.Column(db.String(100))
    email = db.Column(db.String(50))
    company_url = db.Column(db.String(50))
    zip_code = db.Column(db.Integer)
    project_address = db.Column(db.String(200))
    business_type = db.Column(db.String(50))
    coverage_needed = db.relationship('GeneralLiabilityCoverage', backref = "general_liability_coverage")

class GeneralLiabilityCoverage(db.Model):
    """A general liability coverage."""

    __tablename__ = "general_liability_coverage"

    coverage_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    general_liability_id = db.Column(db.Integer, db.ForeignKey('general_liability.general_liability_id'))
    general_contractor = db.Column(db.Boolean, unique=False)
    developer = db.Column(db.Boolean, unique=False)
    remodeler = db.Column(db.Boolean, unique=False)
    speciality_contractor = db.Column(db.Boolean, unique=False)

if __name__ == "__main__":
    from server import app
    connect_to_db(app)