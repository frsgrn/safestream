#!/usr/bin/python -u

import cv2
import os
import datetime
import time
import _thread

face_cascade = cv2.CascadeClassifier('./src/cascades/data/haarcascade_frontalface_alt2.xml')

def addTimestamp(img):
    cv2.putText(img, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), (10,20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255))

def saveImage(img):
    if not os.path.exists("images"):
        os.makedirs("images")
    cv2.imwrite("images/latest.jpg",img) #save image

def removeFaces(img):
    gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=5)
    for (x, y, w, h) in faces:
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,0), -1)

def record():
    cam = cv2.VideoCapture(0)
    try:
        while True:
            s, img = cam.read()
            if s:
                removeFaces(img)
                addTimestamp(img)
                saveImage(img)
                print("image captured")
                time.sleep(5)
            else:
                print("image capture failed")
                time.sleep(10)
                cam = cv2.VideoCapture(0)
    except KeyboardInterrupt:
        print('interrupted!')

def main():
    record()

if __name__ == '__main__':
    main()