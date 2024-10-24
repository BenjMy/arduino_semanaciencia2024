# # arduino_server.py
# import serial
# import time
# from flask import Flask, jsonify

# app = Flask(__name__)

# # Replace with your actual port and baud rate
# SERIAL_PORT = '/dev/ttyACM0'
# BAUD_RATE = 9600

# @app.route('/data')
# def get_data():
#     try:
#         ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
#         time.sleep(2)  # Wait for connection to be established
#         if ser.in_waiting > 0:
#             line = ser.readline().decode('utf-8').rstrip()
#             return jsonify(value=float(line))
#     except Exception as e:
#         return jsonify(error=str(e))

# if __name__ == "__main__":
#     app.run(port=5000)  # Run locally on port 5000
 
import tornado.ioloop
import tornado.web
import serial
import time
import json

# Replace with your actual port and baud rate
SERIAL_PORT = '/dev/ttyACM0'  # Change this as necessary for your Arduino
BAUD_RATE = 9600

class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)  # Wait for connection to be established

    def get(self):
        try:
            if self.ser.in_waiting > 0:
                line = self.ser.readline().decode('utf-8').rstrip()
                value = float(line)  # Convert to float
                self.write(json.dumps({'value': value}))
            else:
                self.write(json.dumps({'error': 'No data available'}))
        except Exception as e:
            self.write(json.dumps({'error': str(e)}))

def make_app():
    return tornado.web.Application([
        (r"/data", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(5000)  # Run on port 5000
    print("Server running on http://localhost:5000/data")
    tornado.ioloop.IOLoop.current().start()
