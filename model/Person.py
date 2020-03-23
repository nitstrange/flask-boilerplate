from datetime import datetime
from config import db, ma

class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), index=True)
    fname = db.Column(db.String(32))
    cell = db.Column(db.String(13))
    occupation = db.Column(db.String(32))
    location = db.Column(db.String(32))
    email = db.Column(db.String(32),nullable=True) 
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person
        sqla_session = db.session