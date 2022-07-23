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

DB = DbAccess('localhost','pi','raspberry','garage_door')
DB.set_connection()
DB.set_cur()

@app.route('/')
def index():
    door_status = 0
    print(f'door status is {door_status}')
    
    users = DB.get_users()

    return render_template('door_controller.html', users=users)


@app.route('/verify_and_open', methods=['POST'])
def verify_and_open():
    selected_user = request.form.get('USER')
    entered_pin = request.form['PIN']

    validated = DB.validate_user(selected_user, entered_pin)

    if validated:
        GPIO.output(RELAY_1_GPIO, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(RELAY_1_GPIO, GPIO.LOW)
    return redirect(url_for("index"))



@app.route('/new_user')
def add_user():

    return render_template('add_user.html')


@app.route('/new_user_attempt', methods=['POST'])
def new_user_attempt():
    form_new_user = request.form['USER']
    form_new_user_pass = request.form['PASS']
    form_admin_passwd = request.form['ADMIN_PASS']

    validated = DB.validate_user('admin', form_admin_passwd)

    if validated:
        DB.add_user(form_new_user, form_new_user_pass)
        return redirect(url_for("add_user"))
    else:
        return "User not created, check admin credentials"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5555')