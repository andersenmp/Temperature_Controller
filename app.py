import os
from API_hardware import tempSensor, relay
from flask import Flask, send_file, jsonify, request


#init Temp Sensor

tempSensor.init('/sys/bus/w1/devices/28-0115925d3eff/w1_slave')

# init list with pin numbers for relays
pinList = [16, 20, 21, 26]
relay.init(pinList)


app = Flask(__name__,static_url_path='/static')


@app.route("/")
def index():
    print os.name
    return send_file("index.html")


@app.route("/getTemp", methods=["GET"])
def getTemp():
    return jsonify(c=tempSensor.read_temp('C'))


@app.route("/relayOn", methods=["POST"])
def relayOn():
    item = pinList[int(request.form['relay'])]
    relay.relayOn(item)
    return jsonify(Relay_On=item)


@app.route("/relayOff", methods=["POST"])
def relayOff():
    item = pinList[int(request.form['relay'])]
    relay.relayOff(item)
    return jsonify(Relay_Off=item)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
