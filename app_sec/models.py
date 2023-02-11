from flask_login import UserMixin
from app_sec import db, ma

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    morada = db.Column(db.String(200))
    contact = db.Column(db.String(13))
    SSN = db.Column(db.String(12))
    isAdmin = db.Column(db.Boolean, default=False)
    image = db.Column(db.String(20), nullable=False, default='default.png')

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patientId = db.Column(db.Integer, db.ForeignKey('user.id'))
    subject = db.Column(db.String(100))
    date = db.Column(db.String(10))
    time = db.Column(db.String(10))
    description = db.Column(db.String(1000))

class AppointmentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'patientId', 'subject', 'date', 'time', 'description')

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.String(1000))

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patientId = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.String(10))
    description = db.Column(db.String(1000))
    code = db.Column(db.String(100))