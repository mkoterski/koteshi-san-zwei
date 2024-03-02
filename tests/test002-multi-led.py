import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

print("T E S T   0 0 2   -   M U L T I   L E D")

GPIO.output(17, True)

print("R E D")

time.sleep(5)
GPIO.output(17, False)
time.sleep(1)
GPIO.output(18, True)

print("Y E L L O W")

time.sleep(5)
GPIO.output(18, False)
time.sleep(1)
GPIO.output(22, True)

print("G R E E N")

time.sleep(5)
GPIO.output(22, False)
time.sleep(1)
GPIO.output(23, True)

print("W H I T E")

time.sleep(5)
GPIO.output(23, False)
time.sleep(1)
GPIO.cleanup()