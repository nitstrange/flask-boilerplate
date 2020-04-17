import os
from config import db, hashing
from model.User import User, Person 
from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

PEOPLE = [
    {
        "fname": "Doug",
        "lname": "Farrell",
        "user_id" : 1,
        "occupation": "Sanitari Worker",
        "location": "Yet to come from api",
        "cell": "013910239102",
        "email": "none@none.com",
        "timestamp": get_timestamp(),
    },
    {
        "fname": "Kent",
        "lname": "Brockman",
        "user_id" : 2,
        "occupation": "Electrician",
        "location": "Yet to come from api",
        "cell": "013910239102", 
        "email": "none@none.com",
        "timestamp": get_timestamp(),
    },
    {
        "fname": "Bunny",
        "lname": "Easter",
        "user_id" : 3,
        "occupation": "Gas worker",
        "location": "Yet to come from api",
        "cell": "013910239102", 
        "email": "none@none.com",
        "timestamp": get_timestamp(),
    }
]

USER = [
    {
        "username" : "user-a",
        "password" : "user-a-pass"
    }, 
    {
        "username" : "user-b",
        "password" : "user-b-pass"   
    },
    {
        "username" : "user-c",
        "password" : "user-c-pass "  
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

for user in USER:
    u = User(username = user['username'], password = hashing.hash_value(user['password'], salt="saltbhai"))
    db.session.add(u)
    u.id

db.session.commit()