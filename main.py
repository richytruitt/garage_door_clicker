from flask import Flask
# import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep
from flask import Flask, request, redirect, render_template, url_for
from jinja2 import Environment, FileSystemLoader
import random
import time

app = Flask(__name__)
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

RELAIS_1_GPIO = 17
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)

@app.route('/')
def index():
    door_status = 1
    print(f'door status is {door_status}')
    if door_status == 0:
        return render_template('door_closed.html')
    else:
        return render_template('door_open.html')


@app.route('/verify_and_open', methods=['POST'])
def verify_and_open():
    entered_pin = request.form['PIN']
    if entered_pin == '12345':
        print('DOOR OPENING')
        time.sleep(3)
    return redirect(url_for("index"))
    

@app.route('/close_door')
def close_door():
    print('Door has been triggered to close')
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)

    return redirect(url_for("index"))




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5555')