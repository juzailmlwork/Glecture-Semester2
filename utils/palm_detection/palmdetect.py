import cv2
import numpy as numpy
import gesturedetection as gd
import time
import os

def detect(Lock,cap):
    while True:
        
        print("GesturePredRunning")
        
        ret,img = cap.read()
        if(not ret):
            print("error")
            continue
        height, width, channels = img.shape
        flag = False
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        lhands = left_cascade.detectMultiScale(gray,1.4,4)
        rhands = right_cascade.detectMultiScale(gray,1.3,4)
        lpalm = left_palm.detectMultiScale(gray,1.2,3)
        rpalm = right_palm.detectMultiScale(gray,1.3,4)
        for (x,y,w,h) in lhands:
            #cv2.rectangle(img,(x-30,y-60),(x+w+30,y+h+40),(255,0,0),2)
            flag = True
            coords = max(x-xmin_offset,0),max(y-ymin_offset,0),min(x+w+xmax_offset,width),min(y+h+ymax_offset,height)
        for (x,y,w,h) in rhands:
            #cv2.rectangle(img,(x-30,y-60),(x+w+30,y+h+40),(255,255,0),2)
            flag = True
            coords = max(x-xmin_offset,0),max(y-ymin_offset,0),min(x+w+xmax_offset,width),min(y+h+ymax_offset,height)
        for (x,y,w,h) in rpalm:
            #cv2.rectangle(img,(x-30,y-60),(x+w+30,y+h+40),(0,0,255),2)
            flag = True 
            coords = max(x-xmin_offset,0),max(y-ymin_offset,0),min(x+w+xmax_offset,width),min(y+h+ymax_offset,height)
        for (x,y,w,h) in lpalm:
            #cv2.rectangle(img,(x-30,y-60),(x+w+30,y+h+40),(0,255,0),2)
            flag = True
            coords = max(x-xmin_offset,0),max(y-ymin_offset,0),min(x+w+xmax_offset,width),min(y+h+ymax_offset,height)
        cv2.imshow("img",img)
        Lock.acquire()
        if flag:
            print("TAKING IMAGE IN 1s")
            time.sleep(1)
            boo,refreshed=cap.read()
            img = refreshed[coords[1]:coords[3],coords[0]:coords[2]]
            cv2.imwrite("F:\\WorkSpace\\Projects\\GrayClassifier\\with_haar_test\\working_folder\\test.jpg",img)
            guess,scores = gd.detectgesture(img)
            print(guess)
        Lock.release() 

        k=cv2.waitKey(1) & 0xff
        if(k==27):
            break       
#os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
#os.chdir("F:\\WorkSpace\\Projects\\GrayClassifier\\with_haar_test")
left_cascade = cv2.CascadeClassifier("D:\\WorkSpace\\Testing\\Haarcascades\\Hand\\left.xml")  #PALM POINT LEFT
right_cascade = cv2.CascadeClassifier("D:\\WorkSpace\\Testing\\Haarcascades\\Hand\\right.xml") #RIGHT PALM POINT TOP cyan
left_palm = cv2.CascadeClassifier("D:\\WorkSpace\\Testing\\Haarcascades\\Hand\\lpalm.xml") 
right_palm = cv2.CascadeClassifier("D:\\WorkSpace\\Testing\\Haarcascades\\Hand\\rpalm.xml") #RIGHT PALM POINT TOP 

xmin_offset=70
ymin_offset=60
ymax_offset=70
xmax_offset=60
coords = ()
