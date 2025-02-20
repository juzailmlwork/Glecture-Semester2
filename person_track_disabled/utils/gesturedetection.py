import keras
import cv2
import tensorflow as tf
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

def getgesture(scores):
    legend = {
        0:"Fist",
        1:"PointLeft",
        2:"PointRight",
        3:"Unknown"
    }
    gesture = max(scores)
    if gesture>=0.5:
        i=scores.index(gesture)
        return legend[i]
    else:
        return "Unknown"
        
def detectgesture(image):
    img = cv2.cvtColor(cv2.resize(image,(240,240)),cv2.COLOR_BGR2GRAY)
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array/=255.
    img_array = tf.expand_dims(img_array, 0)
    predictions = model_loaded.predict(img_array)
    scores = predictions[0][0],predictions[0][1],predictions[0][2]
    return getgesture(scores) , scores
'''
def detectgesture(coord):
    capture = cv2.VideoCapture(0)
    ret, img = capture.read()
    
    img = img[coord[1]:coord[3],coord[0]:coord[2]]
    cv2.imwrite("F:\\WorkSpace\\Projects\\GrayClassifier\\with_haar_test\\working_folder\\test.jpg",img)
    img = cv2.cvtColor(cv2.resize(img,(240,240)),cv2.COLOR_BGR2GRAY)
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array/=255.
    img_array = tf.expand_dims(img_array, 0)
    
    predictions = model_loaded.predict(img_array)
    capture.release()
    scores = predictions[0][0],predictions[0][1],predictions[0][2],predictions[0][3]
    return getgesture(scores) , scores
'''
model_loaded = keras.models.load_model('F:\\WorkSpace\\Projects\\GrayClassifier\\classification_model\\date_09_25.h5')



