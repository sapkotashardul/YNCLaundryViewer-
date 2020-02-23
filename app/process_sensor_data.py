from datetime import datetime, timedelta, timezone
import json

#constants
path = "./status_db.json"
ON = "AVAILABLE"
OFF = "UNAVAILABLE"
ERROR = "ERROR"

#constants
t = datetime.strptime("Sunday, 11:56:57 PM, 23-Feb-2001", '%A, %I:%M:%S %p, %d-%b-%Y')
s = "yea"

path = "./status_db.json"
with open(path) as db: 
    db = json.load(db)

def find_latest(db, college, washer):
    #state is "AVAILABLE OR UNAVAILABLE OR ERROR"
    global t, s
    for state in db[college][washer]:
        if datetime.strptime(db[college][washer][state], '%A, %I:%M:%S %p, %d-%b-%Y') >= t:
            #t = datetime.strptime(db[college][washer][state], '%I:%M:%S %p %d/%H/%Y')
            time = db[college][washer][state]
            s = state
        else:
            pass
    find_latest.status = s
    find_latest.time = time

def update_status_ram(db, college, washer, status, time):
    db[college][washer][status] = time
    json_data = json.dumps(db)

#Method 1: fast method, just references what's on ram and paste
def update_status_hdd(filename=path):
    with open(filename,'w') as f: 
        json.dump(db, f, indent=4) 

#examples of the above commands
#update_status_ram(db,"Cendana", "Washer 1", "AVAILABLE", "8800")
#find_status(db,'Cendana','Washer 1')
#update_status_hdd()


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
    try:
        find_latest(db,college,machineLabel)
        status = find_latest.status + "\n" + find_latest.time
    except Exception as e:
        print(e)
        pass
    return status

update_status_ram(db,"Saga", "Washer_6", "AVAILABLE", datetime.strftime(datetime.now(), "%A, %I:%M:%S %p, %d-%b-%Y"))
update_status_hdd()
print(get_latest_sensor_value("Saga","Washer_6"))