from datetime import datetime
from model.Location import db, ma 

class Location(db.Model):
    __tablename__ = "Location"
    person_id = db.Column(db.Interger, primary_key = True)
    local = db.Column(db.String(32))
    zipcode =  db.Column(db.String(32))
    city = db.Column(db.String(32))
    state = db.Column(db.String(32))


class LocationSchema(ma.ModelSchema):

    class Meta : 
        model = Location
        sqla_session = db.session