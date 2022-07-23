from flask import Flask
# import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep
from flask import Flask, request, redirect, render_template, url_for
from jinja2 import Environment, FileSystemLoader
import random
import time

from helpers.db import DbAccess

app = Flask(__name__)
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

RELAY_1_GPIO = 17
GPIO.setup(RELAY_1_GPIO, GPIO.OUT)
GPIO.setwarnings(False)

@app.route('/')
def index():
    door_status = 0
    print(f'door status is {door_status}')
    
    db = DbAccess('localhost','pi','raspberry','garage_door')

    db_connection = db.connect()

    users = db.get_users(db_connection)

    return render_template('door_closed.html', users=users)


@app.route('/verify_and_open', methods=['POST'])
def verify_and_open():
    selected_user = request.form.get('USER')
    entered_pin = request.form['PIN']
    print(f'Selected user was {selected_user}')
    if entered_pin == '12345':
        # GPIO.output(RELAY_1_GPIO, GPIO.HIGH)
        # time.sleep(1)
        # GPIO.output(RELAY_1_GPIO, GPIO.LOW)
        print('Hello World')
    return redirect(url_for("index"))
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5555')