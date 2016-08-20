import os
import platform
import datetime
from API_hardware import tempSensor, relay, jsonLog
from flask import Flask, send_file, jsonify, request


#init Temp Sensor

tempSensor.init('/sys/bus/w1/devices/28-0115925d3eff/w1_slave')

# init list with pin numbers for relays
pinList = [16, 20, 21, 26]
relay.init(pinList)


app = Flask(__name__, static_url_path='/static')


@app.route("/")
def index():
    data = {'timestap':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'function':'index'}
    jsonLog.log(data)
    return send_file("index.html")


@app.route("/getTemp", methods=["GET"])
def getTemp():
    temp = tempSensor.read_temp('C')
    data = {'timestap':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'function':"getTemp", 'temp':temp}
    jsonLog.log(data)
    return jsonify(c=temp)


@app.route("/relayOn", methods=["POST"])
def relayOn():
    item = pinList[int(request.form['relay'])]
    relay.relayOn(item)
    data = {'timestap': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'function': "relayOn", 'relay': int(request.form['relay'])}
    jsonLog.log(data)
    return jsonify(Relay_On=item)


@app.route("/relayOff", methods=["POST"])
def relayOff():
    item = pinList[int(request.form['relay'])]
    relay.relayOff(item)
    data = {'timestap': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'function': "relayOff", 'relay': int(request.form['relay'])}
    jsonLog.log(data)
    return jsonify(Relay_Off=item)

@app.route("/shutdown")
def shutdown():
    data = {'timestap': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'function': "shutdown"}
    jsonLog.log(data)
    os.system("sudo shutdown -h now")
    return 0

@app.route("/reboot")
def reboot():
    data = {'timestap': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'function': "reboot"}
    jsonLog.log(data)
    os.system("sudo reboot")
    return 0

if __name__ == "__main__":
    if platform.system() == 'Darwin':
        app.run(host='127.0.0.1', port=5000, debug=True)
    else:
        app.run(host='0.0.0.0', port=80, debug=False)
