from flask import Flask
# import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep
from flask import Flask, request, redirect, render_template, url_for
from jinja2 import Environment, FileSystemLoader
import random
import time

app = Flask(__name__)
# GPIO.setwarnings(False)    # Ignore warning for now
# GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
# GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

@app.route('/')
def index():
    door_status = random.randint(0,1)
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
    time.sleep(3)
    return redirect(url_for("index"))




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5555')