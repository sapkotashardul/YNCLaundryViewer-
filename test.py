import json
#This comes from the python status_db
from datetime import datetime

#constants
datetime_str = '09/19/18 13:55:26'
t = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
s = "yea"

path = "./status_db.json"
with open(path) as db: 
    db = json.load(db)

def find_status(db, college, washer):
    t=0
    #state is "AVAILABLE OR UNAVAILABLE OR ERROR"
    for state in db[college][washer]:
        if int(db[college][washer][state]) > t:
            t = int(db[college][washer][state])
            s = state
    print(str(t)+s)

#t=datetime.strptime("01/01/2020 00:00:00", '%d/%m/%y %H:%M:%S')
#Loads from Json file then checks


def find_latest(db, college, washer):
    #state is "AVAILABLE OR UNAVAILABLE OR ERROR"
    global t, s
    for state in db[college][washer]:
        if datetime.strptime(db[college][washer][state], "%m/%d/%y %H:%M:%S") >= t:
            t = datetime.strptime(db[college][washer][state], "%m/%d/%y %H:%M:%S")
            s = state
    find_latest.time = t
    find_latest.status = s

def update_status_ram(db, college, washer, status, time):
    db[college][washer][status] = time
    json_data = json.dumps(db)
    print(db)

#Method 1: fast method, just references what's on ram and paste
def update_status_hdd(filename=path):
    with open(filename,'w') as f: 
        json.dump(db, f, indent=4) 

#Method 2: slow method, extract out and edit and paste back.
"""
def update_status_hdd(college,washer,status,time, filename=path):
    with open(path) as json_file: 
        json_full = json.load(json_file) 
        temp = json_full[college][washer]
             #python object to be appended 
        y = {status:time}
            # appending data  
        temp.update(y)
    with open(filename,'w') as f: 
        json.dump(db, f, indent=4) 
"""
print(db)
colleges =["Cendana","Elm","Saga"]
sixes = ["1","2","3","4","5","6"]
statuses=["AVAILABLE","UNAVAILABLE","ERROR"]
tt = "01/01/20 00:00:00"
#Script to generate database in case of corruption
db = {"Cendana":"_"}
for x in colleges:
    db.update({x:"_"})
for x in colleges:
    total = {}
    for y in sixes:
        total.update({"Washer_{}".format(y):"_"})
    db.update({x:total})

for x in colleges:
    total = {}
    last = {}
    for y in sixes:
        stotal = {}
        for z in statuses:
            stotal.update({z:tt})
        total.update({"Washer_{}".format(y):stotal})
    db.update({x:total})
print(db)

"""
for z in statuses:
    for y in sixes:
        db[college][washer] = x
        for x in colleges:
            db[college] = x
#update_status_ram(db, x , "Washer_{}".format(y), z, tt)
"""

update_status_hdd()


#update_status_ram(db,"Cendana", "Washer 1", "AVAILABLE", "8800")
#update_status_hdd()
#find_latest(db,"Cendana",'Washer_1')
#print(find_latest.status, find_latest.time)

#slow method command:
#update_status_hdd("Cendana", "Washer 1", "AVAILABLE", "100")
