'''
tests out the camura
'''

import numpy
import cv2
faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

from light_mod.lights import Light
import RPi.GPIO as GPIO

green = Light(33)
yellow = Light(31)
red = Light(29)

facefound = False

cap = cv2.VideoCapture(0)
cap.set(3,640) #sets width
cap.set(4,480) #sets height

green.on()

while (True):


    
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20,20)
    )
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        facefound = True
    
    if facefound == True:
        yellow.on()
    elif facefound == False:
        yellow.off()
    
    facefound = False
    
    cv2.imshow('video',img)
    
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:    #press 'esc' to quit
        cv2.imwrite('/home/pi/Desktop/project/hope.jpg', img)
        break

GPIO.cleanup()
cap.release()
cv2.destroyAllWindows()