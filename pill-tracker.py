import RPi.GPIO as GPIO
import time
pin_list = (6, 13, 19, 26, 12, 16, 20)
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)

#initialise a previous input variable to 0 (Assume no pressure applied)
prev_input = 0
count = 0
try:
    while True:
        #take a reading
        input = GPIO.input(6)
        #if the last reading was low and this one high, alert us
        if ((not prev_input) and input):
            print("Under Pressure")
            count = count + 1
            print(count)
        #update previous input
        prev_input = input
        #slight pause
        time.sleep(0.10)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()