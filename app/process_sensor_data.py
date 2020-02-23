from datetime import datetime, timedelta, timezone
import json

#constants
path = "./status_db.json"
ON = "AVAILABLE"
OFF = "UNAVAILABLE"
ERROR = "ERROR"
path = "./status_db.json"
with open(path) as db: 
    db = json.load(db)
#constants
t = datetime.strptime("Sunday, 11:56:57 PM, 23-Feb-2001", '%A, %I:%M:%S %p, %d-%b-%Y')
s = "yea"

def find_latest(db, college, washer):
    #state is "AVAILABLE OR UNAVAILABLE OR ERROR"
    global t, s
    for state in db[college][washer]:
        if datetime.strptime(db[college][washer][state], '%A, %I:%M:%S %p, %d-%b-%Y') >= t:
            #t = datetime.strptime(db[college][washer][state], '%I:%M:%S %p %d/%H/%Y')
            t = datetime.strptime(db[college][washer][state], '%A, %I:%M:%S %p, %d-%b-%Y')
            s = state
            time = datetime.strftime(t, '%A, %I:%M:%S %p, %d-%b-%Y')
    find_latest.status = s
    find_latest.time = time

#Method 1: fast method, just references what's on ram and paste
def update_status_hdd(filename=path):
    global db
    with open(filename,'w') as f: 
        json.dump(db, f, indent=4)


def update_status_ram(college, washer, status, time):
    global db
    db[college][washer][status] = time
    #json_data = json.dumps(tempjson)
    update_status_hdd()
    with open(path) as db: 
        db = json.load(db)

def determine_sensor_status(value):
    if value < 300:
        return ON
    # elif value > 800:
    elif value >= 300 or value <= 1100:
        return OFF
    else:
        return ERROR

#note, washer and machineLabel are the same things
def get_latest_sensor_value(college, machineLabel):
    global s
    with open(path) as db: 
        db = json.load(db)
    try:
        find_latest(db,college,machineLabel)
        s = find_latest.status + "\n" + find_latest.time
    except Exception as e:
        print(e)
        pass
    return s
#sanity check
update_status_ram("Saga", "Washer_6", "AVAILABLE", datetime.strftime(datetime.now(), "%A, %I:%M:%S %p, %d-%b-%Y"))
print(get_latest_sensor_value("Saga","Washer_6"))