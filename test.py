import json
#This comes from the python status_db

from datetime import datetime

path = "./status_db.json"
"""
def find_status(db, college, washer):
    t=0
    #state is "AVAILABLE OR UNAVAILABLE OR ERROR"
    for state in db[college][washer]:
        if int(db[college][washer][state]) > t:
            t = int(db[college][washer][state])
            s = state
    print(str(t)+s)
    
"""
datetime_str = '09/19/18 13:55:26'
t = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
s = "yea"
#t=datetime.strptime("01/01/2020 00:00:00", '%d/%m/%y %H:%M:%S')
#Loads from Json file then checks
with open(path) as db: 
    db = json.load(db)

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
colleges =["Cendana","Elm","Saga"]
sixes = ["1","2","3","4","5","6"]
statuses=["AVAILABLE","UNAVAILABLE","ERROR"]
tt = "09/19/18 13:55:26"
for x in colleges:
    for y in sixes:
        for z in statuses:
            update_status_ram(db, x , "Washer_{}".format(y), z, tt)
            update_status_hdd()
find_latest(db,"Cendana",'Washer_1')
print(find_latest.status, find_latest.time)

#slow method command:
#update_status_hdd("Cendana", "Washer 1", "AVAILABLE", "100")
