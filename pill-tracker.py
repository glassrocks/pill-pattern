#import RPi.GPIO as GPIO
import time
import threading
from flask import Flask, render_template

"""
def start_reading():

    PINS = (6, 13, 19, 26, 12, 16, 20)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.IN)

    # initialise a previous input variable to 0 (Assume no pressure applied)
    prev_input = 0
    count = 0

    try:
        while True:

            # take a reading
            input = GPIO.input(6)
            # if the last reading was low and this one high, alert us
            if ((not prev_input) and input):
                print("Under Pressure")
                count = count + 1
                print(count)
            # update previous input
            prev_input = input
            # slight pause
            time.sleep(0.10)

    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
"""


def start_website():
    app = Flask(__name__)

    @app.route('/<string:page_name>/')
    def render_static(page_name):
        if ".jpeg" in page_name:
            return render_template('./%s.jpeg' % page_name)
        elif page_name != "favicon.ico":
            return render_template('./%s.html' % page_name)
        else:
            return ""

    return threading.Thread(app.run(use_reloader=False))


if __name__ == "__main__":
    #reader = threading.Thread(start_reading())
    website = start_website()
