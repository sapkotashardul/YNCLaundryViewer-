from flask import request, render_template, jsonify
from app import app, db
from app.models import Sensor
from app.process_sensor_data import get_latest_sensor_value
import app.constants as CONSTANTS

ON = CONSTANTS.ON
OFF = CONSTANTS.OFF


# @app.route('/index/<uuid>', methods=['GET','POST'])
# def index(uuid):
#     content = 0
#     if request.method == 'POST':
#         app.logger.info('successfully posted')
#         content = request.get_json()
#         # data_str = content.decode('utf-8')
#         # json_data = simplejson.loads(data_str, strict=False)
#         #sensorValue = content.get("sensorValue")
#         print "CONTENT ", content
#         #print "SENSORVAL ", sensorValue
#         return "STATUS: SUCCESS "
#     posted_data = content
#     if request.method == 'GET':
#         print "POSTED CONTENT ", posted_data
#         return render_template('index.html', content=posted_data)

# @app.route('/index', methods=['GET'])
# def view_index():
#     print "Get Content:", contents

## Need to update and migrate the database.... because of the changes

sensorStatus = (1,"college","machine")

@app.route('/index', methods=['GET','POST'])
def index():
    app.logger.info('successfully posted')
    print("making a post request....")
    # logger.debug("making a post request....")
    content = request.get_json()
    if content:
        print(content)
        # logger.debug(content)
        global sensorStatus
        value = int(content.get("sensorValue"))
        college = str(content.get("college"))
        machineLabel = str(content.get("machineLabel"))
        sensorStatus = Sensor(sensorValue=value, college=college, machineLabel=machineLabel)
        db.session.add(sensorStatus)
        db.session.commit()
        #print(get_latest_sensor_value(college=college, machineLabel=machineLabel))
        return "STORE SUCCESS "
    return render_template('index.html', content=content)



@app.route('/test')
def view_index_test():
    queried_value = Sensor.query.order_by(Sensor.timestamp.desc()).first()
    value = queried_value.sensorValue
    print("DB VAL ", value)
    elm_washer1 = get_latest_sensor_value(college='Elm', machineLabel='Washer_1')
    elm_washer2 = get_latest_sensor_value(college='Elm', machineLabel='Washer_2')
    elm_washer3 = get_latest_sensor_value(college='Elm', machineLabel='Washer_3')
    elm_washer4 = get_latest_sensor_value(college='Elm', machineLabel='Washer_4')
    elm_washer5 = get_latest_sensor_value(college='Elm', machineLabel='Washer_5')
    elm_washer6 = get_latest_sensor_value(college='Elm', machineLabel='Washer_6')
    cendana_washer1 = get_latest_sensor_value(college='Cendana', machineLabel='Washer_1')
    cendana_washer2 = get_latest_sensor_value(college='Cendana', machineLabel='Washer_2')
    cendana_washer3 = get_latest_sensor_value(college='Cendana', machineLabel='Washer_3')
    cendana_washer4 = get_latest_sensor_value(college='Cendana', machineLabel='Washer_4')
    cendana_washer5 = get_latest_sensor_value(college='Cendana', machineLabel='Washer_5')
    cendana_washer6 = get_latest_sensor_value(college='Cendana', machineLabel='Washer_6')

    return render_template('index.html', elm_washer1=elm_washer1, elm_washer2=elm_washer2, elm_washer3=elm_washer3, elm_washer4=elm_washer4, elm_washer5=elm_washer5, elm_washer6=elm_washer6, cendana_washer1=cendana_washer1, cendana_washer2=cendana_washer2, cendana_washer3=cendana_washer3, cendana_washer4=cendana_washer4, cendana_washer5=cendana_washer5, cendana_washer6=cendana_washer6)

@app.route('/')
def view_index():
    # queried_value = Sensor.query.order_by(Sensor.timestamp.desc()).first()
    # value = queried_value.sensorValue
    # print("DB VAL ", value)
    # elm_washer1, _ = get_latest_sensor_value(college='Elm', machineLabel='Washer_1')
    # elm_washer2, _ = get_latest_sensor_value(college='Elm', machineLabel='Washer_2')
    # elm_washer3, _ = get_latest_sensor_value(college='Elm', machineLabel='Washer_3')
    # elm_washer4, _ = get_latest_sensor_value(college='Elm', machineLabel='Washer_4')
    # elm_washer5, _ = get_latest_sensor_value(college='Elm', machineLabel='Washer_5')
    # elm_washer6, _ = get_latest_sensor_value(college='Elm', machineLabel='Washer_6')

    return render_template('coming_soon.html')


@app.route('/elm_washer1_status')
def elm_washer1_status():
    elm_washer1 = None
    elm_washer1 = get_latest_sensor_value(college='Elm', machineLabel='Washer_1')
    print("elm_washer1_status: ", elm_washer1)
    return elm_washer1
try:
    elm_washer1_status()
except:
    pass

@app.route('/elm_washer2_status')
def elm_washer2_status():
    elm_washer2 = None
    elm_washer2 = get_latest_sensor_value(college='Elm', machineLabel='Washer_2')
    print("elm_washer2_status: ", elm_washer2)
    return elm_washer2
try:
    elm_washer2_status()
except:
    pass

@app.route('/elm_washer3_status')
def elm_washer3_status():
    elm_washer3 = None
    elm_washer3 = get_latest_sensor_value(college='Elm', machineLabel='Washer_3')
    print("elm_washer3_status: ", elm_washer3)
    return elm_washer3
try:
    elm_washer3_status()
except:
    pass
@app.route('/elm_washer4_status')
def elm_washer4_status():
    elm_washer4 = None
    elm_washer4 = get_latest_sensor_value(college='Elm', machineLabel='Washer_4')
    print("elm_washer4_status: ", elm_washer4)
    return elm_washer4
try:
    elm_washer4_status()
except:
    pass

@app.route('/elm_washer5_status')
def elm_washer5_status():
    elm_washer5 = get_latest_sensor_value(college='Elm', machineLabel='Washer_5')
    print("elm_washer5_status: ", elm_washer5)
    return elm_washer5
try:
    elm_washer5_status()
except:
    pass

@app.route('/elm_washer6_status')
def elm_washer6_status():
    elm_washer6 = get_latest_sensor_value(college='Elm', machineLabel='Washer_6')
    print("elm_washer6_status: ", elm_washer6)
    return elm_washer6
try:
    elm_washer6_status()
except:
    pass

@app.route('/cendana_washer1_status')
def cendana_washer1_status():
    cendana_washer1 = get_latest_sensor_value(college='Cendana', machineLabel='Washer_1')
    print("Cednana_washer1_status: ", cendana_washer1)
    return cendana_washer1
try:
    cendana_washer1_status()
except:
    pass

@app.route('/cendana_washer2_status')
def cendana_washer2_status():
    cendana_washer2 = None
    cendana_washer2 = get_latest_sensor_value(college='Cendana', machineLabel='Washer_2')
    print("cendana_washer2_status: ", cendana_washer2)
    return cendana_washer2
try:
    cendana_washer2_status()
except:
    pass

@app.route('/cendana_washer3_status')
def cendana_washer3_status():
    cendana_washer3 = None
    cendana_washer3 = get_latest_sensor_value(college='Cendana', machineLabel='Washer_3')
    print("cendana_washer3_status: ", cendana_washer3)
    return cendana_washer3
try:
    cendana_washer3_status()
except:
    pass

@app.route('/cendana_washer4_status')
def cendana_washer4_status():
    cendana_washer4 = None
    cendana_washer4 = get_latest_sensor_value(college='Cendana', machineLabel='Washer_4')
    print("cendana_washer4_status: ", cendana_washer4)
    return cendana_washer4
try:
    cendana_washer4_status()
except:
    pass

@app.route('/cendana_washer5_status')
def cendana_washer5_status():
    cendana_washer5 = None
    cendana_washer5 = get_latest_sensor_value(college='Cendana', machineLabel='Washer_5')
    print("cendana_washer5_status: ", cendana_washer5)
    return cendana_washer5

@app.route('/cendana_washer6_status')
def cendana_washer6_status():
    cendana_washer6 = None
    cendana_washer6 = get_latest_sensor_value(college='Cendana', machineLabel='Washer_6')
    print("cendana_washer6_status: ", cendana_washer6)
    return cendana_washer6
try:
    cendana_washer6_status()
except:
    pass

#@app.route('/why')
#def cendana

    # elm_washer2, _ = get_latest_sensor_value(college='Elm', machineLabel='Washer_2')
    # elm_washer3, _ = get_latest_sensor_value(college='Elm', machineLabel='Washer_3')
    # elm_washer4, _ = get_latest_sensor_value(college='Elm', machineLabel='Washer_4')
    # elm_washer5, _ = get_latest_sensor_value(college='Elm', machineLabel='Washer_5')
    # elm_washer6, _ = get_latest_sensor_value(college='Elm', machineLabel='Washer_6')

    # return render_template('index.html', elm_washer1=elm_washer1)

    # return render_template('index.html', elm_washer1=elm_washer1, elm_washer2=elm_washer2, elm_washer3=elm_washer3,
    #                        elm_washer4=elm_washer4, elm_washer5=elm_washer5, elm_washer6=elm_washer6)



