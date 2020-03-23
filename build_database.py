import os
from config import db
from model.Person import Person
from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to initialize database with
# PEOPLE = [
#     {'fname': 'Doug', 'lname': 'Farrell'},
#     {'fname': 'Kent', 'lname': 'Brockman'},
#     {'fname': 'Bunny','lname': 'Easter'}
# ]

PEOPLE = [
    {
        "fname": "Doug",
        "lname": "Farrell",
        "occupation": "Sanitari Worker",
        "location": "Yet to come from api",
        "cell": "013910239102",
        "email": "none@none.com",
        "timestamp": get_timestamp(),
    },
    {
        "fname": "Kent",
        "lname": "Brockman",
        "occupation": "Electrician",
        "location": "Yet to come from api",
        "cell": "013910239102", 
        "email": "none@none.com",
        "timestamp": get_timestamp(),
    },
    {
        "fname": "Bunny",
        "lname": "Easter",
        "occupation": "Gas worker",
        "location": "Yet to come from api",
        "cell": "013910239102", 
        "email": "none@none.com",
        "timestamp": get_timestamp(),
    }
]

# Delete database file if it exists currently
if os.path.exists('people.db'):
    os.remove('people.db')

# Create the database
db.create_all()

# Iterate over the PEOPLE structure and populate the database
for person in PEOPLE:
    p = Person(lname=person['lname'], fname=person['fname'],cell=person['cell'],location=person['location'],occupation=person['occupation'],email=person['email'])
    db.session.add(p)

db.session.commit()