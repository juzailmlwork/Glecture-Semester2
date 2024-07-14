import utils
import cv2
import numpy as numpy
import gesturedetection as gd
import time
import os


cap = cv2.VideoCapture(0)

ret , img = cap.read()
height, width, channels = img.shape
xmin_offset=70
ymin_offset=60
ymax_offset=70
xmax_offset=60

while ret:
    ret , img = cap.read()
    	if ret==False:
    	    break
    flag = False
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    coords = utils.palm_detect(gray)
    if coords:
	flag = True
	time.sleep(1)
	ret , refreshed = cap.read()
	refreshed = refreshed[coords[1]:coords[3],coords[0]:coords[2]]
	guess,scores = utils.detect_gesture(refreshed)
	if guess!="Unknown":
	    utils.press_key(guess)





