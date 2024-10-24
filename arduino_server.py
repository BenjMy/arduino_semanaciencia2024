# arduino_server.py
import serial
import time
from flask import Flask, jsonify

app = Flask(__name__)

# Replace with your actual port and baud rate
SERIAL_PORT = '/dev/ttyACM0'
BAUD_RATE = 9600

@app.route('/data')
def get_data():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)  # Wait for connection to be established
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            return jsonify(value=float(line))
    except Exception as e:
        return jsonify(error=str(e))

if __name__ == "__main__":
    app.run(port=5000)  # Run locally on port 5000
 
