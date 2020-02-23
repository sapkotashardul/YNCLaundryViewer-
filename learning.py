from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import models
import csv
import datetime
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import csv
print("hrm")
expiration_days = 550
if (datetime.datetime.now() < (datetime.datetime.now() - datetime.timedelta(days=expiration_days))):
    print("nah")
else :
    print("woots")
limit = datetime.datetime.now() - datetime.timedelta(days=expiration_days)
#print(limit)
#obj = models.Sensor.query.filter( models.Sensor.timestamp < limit).count()
#This this not work! objj = models.Sensor.query.column_descriptions
#print(obj)
#print(models.Sensor.machineLabel)
tada = db.session.query(models.Sensor).filter(models.Sensor.timestamp < limit).delete(synchronize_session=False)
print(tada)
#the code in # works.
#print(models.SensorStatus.query.all())
#print(models.Sensor.query.all())

#Filters out by their timestamp and then prints out all their values.
#obj = models.Sensor.query.filter(models.Sensor.machineLabel == "Washer_6" , models.Sensor.timestamp > limit).all()
#print(obj)

"""
outfile = open('humanreadable.csv', 'wb')
outcsv = csv.writer(outfile)
records = db.query(MyModel).all()
[outcsv.writerow([getattr(curr, column.name) for column in MyTable.__mapper__.columns]) for curr in records]
# or maybe use outcsv.writerows(records)
outfile.close()
"""

"""
with open('testdump.csv', 'wb') as csvfile:

    fieldnames = ['name', ]


    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)        
    writer.writeheader()


    rows = [{"name": "apples", "price": "$5"},
            {"name": "oranges", "price": "$4"}]

    for row in rows:
        writer.writerow(dict(
       (k, v.encode('utf-8') if type(v) is unicode else v) for k, v in row.iteritems()
    ))
"""