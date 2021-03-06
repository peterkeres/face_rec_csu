'''
This script will look at all the 'users' in the system and 'trains' the openCV libary to
recognize there faces.
'''

import cv2
import numpy
from PIL import Image
import os

path = 'dataset'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

def getImagesAndLables(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faceSamples = []
    ids = []
    
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') #convert to grayscale
        img_numpy = numpy.array(PIL_img, 'uint8')
        id = int(os.path.split(imagePath)[-1].split('.')[1])
        faces = detector.detectMultiScale(img_numpy)
        
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    
    return faceSamples,ids


print("\n [info] training faces. it will take a few seconds. wait....")
faces,ids = getImagesAndLables(path)
recognizer.train(faces, numpy.array(ids))

recognizer.write('trainer/trainer.yml') #recognizer.save() wors on mac, but no on pi

print("\n [info] {0} faces trained. exiting program".format(len(numpy.unique(ids))))