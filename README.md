Notes:

- Database (Postgres):
    - 3 tables: 2 forms + users

- UI (Bootstrap, CSS, HTML). source: https://constructioncoverage.com/construction-insurance 
    - Forms:
        - Builders Risk
            - Company Name (input)
            - Email Address (email)
            - Company Website (url)
            - Zip Code (5-digits)
            - Project address (input)
            - Project description (textarea w/charmax)
            - Builing type: Apartment, Warehouse, single family home, hotel/motel,other:specify (radio button)
            - Coverage needed: Building materials, foundation, temporary structures, weather damage,other:specify (checkbox)
        - Commercial General Liability
            - Company Name (input)
            - Email Address (email)
            - Company Website (url)
            - Zip Code (5-digits)
            - Project address (input)
            - Project description (textarea w/charmax)
            - Type of business: Residential general contractor, developer, remodeler, speciality contractor, other:specify (radio button)
            - Coverage needed: faulty workmanship, job-related injury, other:specify (checkbox)

- PDF Generator (Library: PyFPDF?)

- Web framework (Flask):
    - Landing page: 2 application options
    - Forms, required: "shepherd" auth cookie
        - Builders Risk
        - General Liability
