from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
from operator import itemgetter
import threading
def detect_human(Lock,cap):
    while True:
        print("humanTrackrunning")
        ret,img = cap.read()
        image = cv2.cvtColor(cv2.resize(img,(300,300)),cv2.COLOR_BGR2GRAY)
    
        rects,weights = hog.detectMultiScale(image, winStride=(4, 4),
            padding=(8, 8), scale=1.07)
        try:
            ind = np.argmax(weights)
            rect_max = rects[ind]

    
            x,y,w,h=list(rect_max)
            Lock.acquire()
            if (x<50):
                print("moveleft")
            if(x+w>250):
                print("moveright")
            if(y<50):
                print("movetop")
            if(y+h>250):
                print("movebottom")
            Lock.release()
            #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            #cv2.putText(image,"noink",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
            
        except:
            pass
        k=cv2.waitKey(1) & 0xff
        if(k==27):
            break


hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
