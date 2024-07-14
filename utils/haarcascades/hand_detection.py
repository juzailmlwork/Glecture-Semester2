import cv2
import numpy as numpy

left_cascade = cv2.CascadeClassifier("D:\\WorkSpace\\Testing\\Haarcascades\\Hand\\left.xml")  #PALM POINT LEFT
right_cascade = cv2.CascadeClassifier("D:\\WorkSpace\\Testing\\Haarcascades\\Hand\\right.xml") #RIGHT PALM POINT TOP cyan
left_palm = cv2.CascadeClassifier("D:\\WorkSpace\\Testing\\Haarcascades\\Hand\\lpalm.xml") 
right_palm = cv2.CascadeClassifier("D:\\WorkSpace\\Testing\\Haarcascades\\Hand\\rpalm.xml") #RIGHT PALM POINT TOP red IDK why
cap = cv2.VideoCapture(0)

ret , img = cap.read()

while(ret):
    ret , img = cap.read()
    if ret==False:
        break

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    lhands = left_cascade.detectMultiScale(gray,1.4,5)
    rhands = right_cascade.detectMultiScale(gray,1.3,5)
    lpalm = left_palm.detectMultiScale(gray,1.4,5)
    rpalm = right_palm.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in lhands:
        cv2.rectangle(img,(x-30,y-60),(x+w+30,y+h+40),(255,0,0),2)
    for (x,y,w,h) in rhands:
        cv2.rectangle(img,(x-30,y-60),(x+w+30,y+h+40),(255,255,0),2)
    for (x,y,w,h) in rpalm:
        cv2.rectangle(img,(x-30,y-60),(x+w+30,y+h+40),(0,0,255),2)
    for (x,y,w,h) in lpalm:
        cv2.rectangle(img,(x-30,y-60),(x+w+30,y+h+40),(0,255,0),2)


    cv2.imshow("img",img)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

