'''
Main script of the program
'''

import cv2
import numpy
import os
import time

#gets what triner to use
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "Cascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX

#sets up lights
from light_mod.lights import Light
import RPi.GPIO as GPIO

green = Light(33)
yellow = Light(31)
red = Light(29)

#set up values for tests
facefound = False
test = False
attemp = 0
pas = 0

#sets up lock
from lock_mod.lock import Lock

lock = Lock(18)

#sets up an email connection
from email_mod.Emailer import gmailMailer
gmail = gmailMailer()

#names for people
id = 0

names = ['Maidel', 'Peter' , 'phill']

#sets up camura
cam = cv2.VideoCapture(0)
cam.set(3,640)#640
cam.set(4,480)#480

minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

#system start
green.on()

while True:
    #takes a frame
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #trys to find face and to match to our dataset
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH))
    )
    
    #puts box around face 
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,225,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        
        if (confidence < 75):
            id = names[id]
            confidence = " {0}%".format(round(100- confidence))
            if test == True:
                pas = pas + 1
        else:
            id = "unknown"
            confidence = " {0}%".format(round(100 - confidence))
        
        
        cv2.putText(img, str(id), (x+5, y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
        
        facefound = True
        
        
    if test == True:
        attemp = attemp + 1

    #light up for if face is found
    if facefound == True:
        yellow.on()
    elif facefound == False:
        yellow.off()
    
    #sets up button
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    button = not GPIO.input(10)
    
    #checks if button is hit
    if facefound == True and button == True:
        test = True
    
    #stuff for result of test, allows to enter or not
    if test == True:
        if attemp >= 10 and pas >= 8:
            print("let them in")
            lock.unlock()
            time.sleep(3)
            pas = 0
            attemp = 0
            test = False
            lock.lock()         
        elif attemp >= 10:
            print("dont let them in")
            red.on()
            cv2.imwrite('project/hope.jpg', img)
            time.sleep(2)
            gmail.sendAlert("project/hope.jpg")
            time.sleep(2)
            os.remove("project/hope.jpg")
            time.sleep(3)
            pas = 0
            attemp = 0
            test = False
            red.off()
            gmail = gmailMailer()
            
    
    
    facefound = False

    #display image of frame and waits for sec to be hit to quit
    cv2.imshow('camera', img)
    
    k = cv2.waitKey(10) & 0xff
    if k ==27:
        break
    

#clean up 
red.off()
yellow.off()
green.off()
print("\n [info] exiting program and clean up")
cam.release()
cv2.destroyAllWindows()