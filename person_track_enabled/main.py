import palmdetection as palm
import person_detection as person
import cv2

import threading 



cap = cv2.VideoCapture(0)
##thread this.. if movement detected track person

print("a")
lock = threading.Lock()
palm_thread = threading.Thread(target=palm.detect,args=(lock,cap))
person_thread = threading.Thread(target=person.detect_human,args=(lock,cap))
palm_thread.start()
person_thread.start()
while True:
    if ((cv2.waitKey(1) & 0xff )==27):
        break

