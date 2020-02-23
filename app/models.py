from app import db
from datetime import datetime

class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensorValue = db.Column(db.Integer, index=True)
    college = db.Column(db.String, index=True)
    machineLabel = db.Column(db.String, index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # username = db.Column(db.String(64), index=True, unique=True)
    # email = db.Column(db.String(120), index=True, unique=True)
    # password_hash = db.Column(db.String(128))

    def __repr__(self):
        template = '{0.sensorValue} {0.college} {0.machineLabel} {0.timestamp}'
        return template.format(self)
#https://stackoverflow.com/questions/39883950/str-returned-non-string-type-tuple
#'<Value {}>'.format(self.sensorValue)
class SensorStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    college = db.Column(db.String, index=True)
    machineLabel = db.Column(db.String, index=True)
    status = db.Column(db.String, index=True)
    timestamp = db.Column(db.DateTime, index=True)

    def __repr__(self):
        return '<Status {}>'.format(self.status)