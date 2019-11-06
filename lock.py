'''
Peter keres
oct 31 2019
v1.0

this simulates a lock that is being used in the 'facial scanning' app.

this version is currently set up to work with servo moters.
if the moter points to north/south it is locked
if the moter points to east/west it is unlocked
each lock starts out in 'locked' state

each lock object must run the 'destory()' method before termanting program.
'''

import RPi.GPIO as GPIO
import time
import atexit

class Lock:
    
    #variables 
    pin = 0
    locklink = None
    locked = False
    
    '''
    this sets up GPIO pins on the lock and starts in 'locked' state
    @param
        pin: the number of the pin the servo is hooked up too
    '''
    def __init__(self,pin):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin,GPIO.OUT)
        self.locklink = GPIO.PWM(pin,50)
        self.locklink.start(7.5)
        #self.locklink.ChangeDutyCycle(0)
        self.locked = True
        atexit.register(self.destroy)


    '''
    this locks the lock and sets the status to 'locked'
    '''
    def lock(self):
        self.locklink.ChangeDutyCycle(7.5)
        time.sleep(1)
        self.locklink.ChangeDutyCycle(0)
        self.locked = True
        
    '''
    this unlocks the lock and sets the status to 'unlocked'        
    '''
    def unlock(self):
        self.locklink.ChangeDutyCycle(12.5) #can also use 2.5 here
        time.sleep(1)
        self.locklink.ChangeDutyCycle(0)
        self.locked = False

    '''
    this will lock the lock and also free up the GPIO pin settings 
    '''
    def destroy(self):
        self.lock()
        time.sleep(1)
        self.locklink.stop()
        GPIO.cleanup()

    '''
    returns if the lock is currently in a locked state
    @return boolean
    '''
    def isLocked(self):
        return self.locked
    
    '''
    returns if the lock is curretnly in a unlocked state
    @return boolean
    '''
    def isUnLocked(self):
        return not self.locked
    
    '''
    this is just a set of debug statments for the class.
    do not call this class in production
    '''
    def debug(self):
        print('starting debug for lock')

        print('setting up lock at pin number: ' + str(self.pin))
        servoLock = self

        print('locking')
        servoLock.lock()
        print('is the servo locked? ' + str(servoLock.isLocked()))
        print('is the servo unlocked? ' + str(servoLock.isUnLocked()))

        time.sleep(5)

        print('unlocking')
        servoLock.unlock()
        print('is the servo locked? ' + str(servoLock.isLocked()))
        print('is the servo unlocked? ' + str(servoLock.isUnLocked()))

        time.sleep(5)

        print('destroying lock')
        print('end')




