from datetime import datetime
from config import db, ma
from model.Person import Person

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(256))
    person = db.relationship( 'Person', backref='user', lazy=True)
    timestamp = db.Column(db.DateTime, default = datetime.utcnow, onupdate=datetime.utcnow)

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        sqla_session = db.session
