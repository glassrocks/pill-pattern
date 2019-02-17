import RPi.GPIO as GPIO
from time import sleep
import threading
from flask import Flask, render_template


def start_reading():

    PINS = (6, 13, 19, 26, 12, 16, 20)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.IN)

    # initialise a previous input variable to 0 (Assume no pressure applied)
    prev_input = 0
    count = 0

    try:
        while True:

            global pinput
            # take a reading
            pinput = GPIO.input(6)
            # if the last reading was low and this one high, alert us
            if ((not prev_input) and pinput):
                print("Under Pressure")
                count = count + 1
                print(count)
            # update previous input
            prev_input = pinput
            # slight pause
            sleep(0.10)

    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    finally:
        GPIO.cleanup()


def start_website():
    app = Flask(__name__)

    @app.route('/<string:page_name>/')
    def render_static(page_name):
        if ".jpeg" in page_name:
            return render_template('./%s.jpeg' % page_name)
        elif page_name != "favicon.ico":
            if page_name == "calendar":
                threading.Thread(start_reading())
            return render_template('./%s.html' % page_name)
        else:
            return ""

    return (threading.Thread(app.run(use_reloader=False)))


if __name__ == "__main__":
    website, pins = start_website()
