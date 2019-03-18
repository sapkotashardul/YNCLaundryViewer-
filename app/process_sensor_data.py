import app.constants as CONSTANTS
from app import app, db
from app.models import Sensor, SensorStatus

ON = CONSTANTS.ON
OFF = CONSTANTS.OFF
READ_LIMIT = CONSTANTS.NUMBER_OF_READINGS_BEFORE_DEEPSLEEP


SENSORVALS = []


def determine_sensor_status(value):
    if value < 300:
        return ON
    # elif value > 800:
    else:
        return OFF


def get_latest_sensor_value(college, machineLabel):
    global SENSORVALS
    latest_result = Sensor.query.order_by(Sensor.timestamp.desc()).filter_by(machineLabel=machineLabel, college=college).first()
    print ("latest sensor result: ", latest_result)
    # logger.debug("latest sensor result: {0}".format(latest_result))

    if len(SENSORVALS) < READ_LIMIT:
        print ("SENSORVALS Count: ", len(SENSORVALS))
        # logger.debug("SENSORVALS Count: {0}".format(SENSORVALS))
        SENSORVALS.append(latest_result.sensorValue)
        result = SensorStatus.query.order_by(SensorStatus.timestamp.desc()).filter_by(machineLabel=machineLabel,
                                                                                            college=college).first_or_404().status
        return result, True
        # return 'Sorry! No information available yet', True
    if len(SENSORVALS) == READ_LIMIT:
        print ("SENSORVALS ready to be processed")
        # logger.debug("SENSORVALS ready to be processed")
        result = verify_sensor_status(SENSORVALS)
        print ("result of processing sensor stats: ", result)
        # logger.debug("result of processing sensor stats: {0}".format(result))
        try:
            sensorStatus = SensorStatus.query.order_by(SensorStatus.timestamp.desc()).filter_by(machineLabel=machineLabel, college=college).first_or_404().status
            print ("current sensor status: ", sensorStatus)
            # logger.debug("current sensor status: {0}".format(sensorStatus))
        except:
            sensorStatus = None

        if result != sensorStatus:
            college = latest_result.college
            machineLabel = latest_result.machineLabel
            timestamp = latest_result.timestamp
            status = result

            sensorData = SensorStatus(college=college, machineLabel=machineLabel, timestamp=timestamp, status=status)
            db.session.add(sensorData)
            db.session.commit()

        SENSORVALS = []

        return result, sensorStatus


# datetime.timedelta.total_seconds(datetime.datetime.utcnow() - Sensor.query.order_by(Sensor.timestamp.desc()).filter_by(machineLabel='Washer_1', college='Elm').first().timestamp)


def verify_sensor_status(latestFiveVals):
    result = process_sensor_values(latestFiveVals)
    if result == ON:
        return ON
    if result == OFF:
        return OFF

    # for i in range(10):
    #     result = process_sensor_values(latestFifteenVals[i:(i+5)])
    #     if result == ON:
    #         return ON
    #         break
    #     if result == OFF:
    #         return OFF
    #         break



def process_sensor_values(firstFiveVals):
    totalOn = 0
    totalOff = 0
    for value in firstFiveVals:
        if determine_sensor_status(value) == ON:
            totalOn += 1
        else:
            totalOff += 1

    if totalOn == 5:
        return ON

    if totalOff == 5:
        return OFF
