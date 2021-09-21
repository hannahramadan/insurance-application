# Insurance Application
Webapp for submitting construction insurance requests and receiving a pdf of that request in return. 

# Features
- Two insurance form options are avaliable.
- Upon form submission, form is stored in postgres database. 
- Simultaneously, a PDF version of the submitted form is generated and shown to the user.
- Users must have a auth cookie with value "shepherd" to submit form. Adding document.cookie="auth=shepherd" to dev console allows form submission.

# Tech
- Backend: Python3, Flask, PostgreSQL, SQLAlchemy, Jinja2
- Frontend: HTML5, CSS, Bootstrap
- Libraries: pdfkit

# Future Updates
- Enhance styling with Bootstrap
- Mobile-friendly version
- Add additional insurance form field options
