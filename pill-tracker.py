import RPi.GPIO as GPIO
from time import sleep
import threading
from flask import Flask, render_template


def start_reading():

    PINLIST= (6, 13, 19, 26, 12, 16, 20)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PINLIST[0], GPIO.IN)
    GPIO.setup(PINLIST[1], GPIO.IN)

    # initialise a previous input variable to 0 (Assume no pressure applied)
    prev_input = 0
    count = 0
    global pinput
    pinput = 0

    try:
        
        while True:
            # take a reading
            pin_outputlist = list()
            day_sun = GPIO.input(PINLIST[0])
            day_mon = GPIO.input(PINLIST[1])
            print("pin 1: {0}".format(day_sun))
            print("pin 2: {0}".format(day_mon))
            pin_outputlist.append(GPIO.input(PINLIST[0]))
            pin_outputlist.append(GPIO.input(PINLIST[1]))
            print("loop:")
            for pin_output in range(len(pin_outputlist)):
                #pinput = pinput + pin_outputlist[pin_output]
                print(pin_output)
            print("Pinput is: {0}".format(pinput))
            # if the last reading was low and this one high, alert us
            if (prev_input is not pinput):
                print("Change detected!")
                count = count + 1
                print("Num of changes: {0}".format(count))

            input()
            # update previous input
            prev_input = pinput
            del pin_outputlist
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
            return render_template('./%s.jpeg' % page_name, )
        elif page_name != "favicon.ico":
            if page_name == "calendar":
                threading.Thread(start_reading())
            return render_template('./%s.html' % page_name)
        else:
            return ""

    return (threading.Thread(app.run(use_reloader=False)))


if __name__ == "__main__":
    #website, pins = start_website()
    start_reading()
