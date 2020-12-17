'''
This script adds a user in to the data set of verified users.
'''

import numpy
import cv2
import os
faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640) #sets width
cap.set(4,480) #sets height

face_id = input('\n enter user id end press enter: ')
print("\n [info] Initializing face capture. look  at the camura and wait....")

count = 0
while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        count += 1
        
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        
        print("made pic " + str(count))
        cv2.imshow('image', img)
        
    k = cv2.waitKey(100) & 0xff #press 'esc' top stop
    if k == 27:
        break
    elif count >= 400:
        break
        
print("\n [info] exiting program and clean up stuff")
cap.release()
cv2.destroyAllWindows()