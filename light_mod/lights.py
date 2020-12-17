'''
Class sets up an invidual light on the board.
'''

import RPi.GPIO as GPIO
import time
import atexit

class Light:
    
    pin = 0
    
    def __init__(self,pin):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)

    def on(self):
       GPIO.output(self.pin, True) 
        
    def off(self):
        GPIO.output(self.pin, False)


