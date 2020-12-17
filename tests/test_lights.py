'''
Tests that the lights are working
'''

from light_mod.lights import Light
import RPi.GPIO as GPIO
import time



green = Light(33)
yellow = Light(31)
red = Light(29)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)

'''
while True:
    button = GPIO.input(10)
    if button == False:
        print("this worked")
        green.on()
        time.sleep(2)
        green.off()
        time.sleep(.5)
        

green.on()
time.sleep(2)
green.off()

yellow.on()
time.sleep(2)
yellow.off()
'''


GPIO.cleanup()