import json
from datetime import datetime, timedelta, timezone

path = "./status_db.json"

colleges =["Cendana","Elm","Saga"]
sixes = ["1","2","3","4","5","6"]
statuses=["AVAILABLE","UNAVAILABLE","ERROR"]
tt = "01/01/20 00:00:00"
db = {}
for x in colleges:
    total = {}
    last = {}
    for y in sixes:
        stotal = {}
        for z in statuses:
            stotal.update({z:tt})
        total.update({"Washer_{}".format(y):stotal})
    db.update({x:total})

def update_status_hdd(filename=path):
    with open(filename,'w') as f: 
        json.dump(db, f, indent=4) 
        
update_status_hdd()