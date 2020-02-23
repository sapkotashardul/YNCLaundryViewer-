from datetime import datetime, timedelta, timezone
import json

#constants
path = "./status_db.json"
ON = "AVAILABLE"
OFF = "UNAVAILABLE"
ERROR = "ERROR"
with open(path) as db: 
    db = json.load(db)

#Searches for the laundry state from the json file
def find_latest(db, college, washer):
    #state is "AVAILABLE OR UNAVAILABLE OR ERROR"
    s = "yea"
    t = datetime.strptime('09/19/18 13:55:26', '%m/%d/%y %H:%M:%S')
    for state in db[college][washer]:
        if datetime.strptime(db[college][washer][state], "%m/%d/%y %H:%M:%S") >= t:
            t = datetime.strptime(db[college][washer][state], "%m/%d/%y %H:%M:%S")
            s = state
    find_latest.time = t
    find_latest.status = s

def update_status_ram(db, college, washer, status, time):
    db[college][washer][status] = time
    print(db)
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
result = 0

#note, washer and machineLabel are the same things
def get_latest_sensor_value(college, machineLabel):
    global result
    try:
        time_sg_complex = find_latest.time + timedelta(hours=8)
        time_sg = time_sg_complex.strftime("%I:%M %p, %d %b %Y ")
        status = str(find_latest.status) + " since: "+ str(time_sg)
    except Exception as e:
        print(e)
        pass
    return status
