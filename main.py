from flask import Flask
# import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep
from flask import Flask, request, redirect, render_template, url_for
from jinja2 import Environment, FileSystemLoader


app = Flask(__name__)
# GPIO.setwarnings(False)    # Ignore warning for now
# GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
# GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/verify', methods=['POST'])
def verify_user():
    entered_pin = request.form['PIN']
    return f'Your PIN was {entered_pin}'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5555')