""" Sensor reader and web server for Pill Pattern"""

import RPi.GPIO as GPIO
from time import sleep
from threading import Thread
from flask import Flask, render_template

global pinput
pinput = {"Sun": 0,
          "Mon": 0,
        # "Tue": 0,
        # "Wed": 0,
        # "Thu": 0,
        # "Fri": 0,
        # "Sat": 0,
}

def start_reading():
    """ Starts a while loop to get data from sensors"""

    global stop_reading
    stop_reading = True
    # Setup pin readings
    PINLIST = (6, 13, 19, 26, 12, 16, 20)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PINLIST[0], GPIO.IN)
    GPIO.setup(PINLIST[1], GPIO.IN)

    # initialise a previous input variable to 0 (Assume no pressure applied)
    prev_input = {}
    count = 0

    # Create dictionary to share information with the server
   

    try:

        while stop_reading:
            # take a reading
            pin_outputdict = {}

            pinput = {"Sun": GPIO.input(PINLIST[0]),
                      "Mon": GPIO.input(PINLIST[1]),
                    # "Tue": GPIO.input(PINLIST[2]),
                    # "Wed": GPIO.input(PINLIST[3]),
                    # "Thu": GPIO.input(PINLIST[4]),
                    # "Fri": GPIO.input(PINLIST[5]),
                    # "Sat": GPIO.input(PINLIST[6]),
                      }

            print("pin 1: {0}".format(pinput["Sun"]))
            print("pin 2: {0}".format(pinput["Mon"]))
            pin_outputdict = pinput
            print("loop:")
            for pin_output in range(len(pin_outputdict)):
                # pinput = pinput + pin_outputdict[pin_output]
                print(pin_output)
            # if the last reading was low and this one high, alert us
            for key, value in pinput.items():
                try:
                    if prev_input[key] is not value:
                        print("Change detected on the %s sensor!" % (key))
                        count += 1
                        print("Num of changes: {0}".format(count))
                except KeyError:
                    print("No previous input!")
            # update previous input
            prev_input = pinput
            del pin_outputdict
            # slight pause
            sleep(5)

    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    finally:
        GPIO.cleanup()


def start_website():
    """ Starts a Flask webserver to access UI"""

    app = Flask(__name__, static_url_path='/static')

    @app.route('/')
    def homepage():
        return render_template("index.html", pinput=pinput)

    @app.route('/<string:page_name>/')
    def render_static(page_name):
        if page_name != "favicon.ico":
            if page_name == "calendar":
                Thread(start_reading())
            return render_template('./%s.html' % page_name, pinput=pinput)
        else:
            return ""

    @app.route('/stop_reader/', methods=['GET', 'POST'])
    def stop_reader():
        global stop_reading
        stop_reading = False

    return (Thread(app.run(use_reloader=False)))


if __name__ == "__main__":
    website = start_website()
    reader = Thread(start_reading())
