
import numpy as np
import cv2
import sklearn
import pickle
from django.conf import settings
import os
from keras.models import model_from_json
import json


STATIC_DIR = settings.STATIC_DIR
print("----------------------------------" , STATIC_DIR)

face_detector_model = cv2.dnn.readNetFromCaffe(os.path.join(STATIC_DIR , 'models/deploy.prototxt.txt'),
                                               os.path.join(STATIC_DIR ,'models/res10_300x300_ssd_iter_140000.caffemodel'))
model_file = open(os.path.join(STATIC_DIR , 'models/better_model.json'), "r")
model_json = model_file.read()
model = model_from_json(model_json)
model.load_weights(os.path.join(STATIC_DIR , 'models/better_model_weights.h5'))

GENDER_PROTO = 'models/gender_deploy.prototxt'
GENDER_MODEL = 'models/gender_net.caffemodel'
MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
GENDER_LIST = ['Male', 'Female']

AGE_PROTO = 'models/age_deploy.prototxt'
AGE_MODEL = 'models/age_net.caffemodel'
AGE_INTERVALS = ['(0, 2)', '(4, 6)', '(8, 12)', '(15, 20)']
accepted_age = ['(0, 2)', '(4, 6)', '(8, 12)', '(15, 20)']

# Load age prediction model
age_net = cv2.dnn.readNetFromCaffe(os.path.join(STATIC_DIR , AGE_PROTO),
                                               os.path.join(STATIC_DIR ,AGE_MODEL))

# Load gender prediction model
gender_net = cv2.dnn.readNetFromCaffe(os.path.join(STATIC_DIR , GENDER_PROTO),
                                               os.path.join(STATIC_DIR ,GENDER_MODEL))

def predictor(image):
    IMAGE_SHAPE = (224, 224)
    IMAGE_SHAPE+(3,)
    img_resize = cv2.resize(image , IMAGE_SHAPE)
    predicted = model.predict(np.array([img_resize]))
    ind = np.argmax(predicted , axis = 1)
    index = ind[0]

    #print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++=========================",predicted[0][index])
    return index,predicted[0][index]

def get_gender_predictions(face_img):
    blob = cv2.dnn.blobFromImage(
        image=face_img, scalefactor=1.0, size=(227, 227),
        mean=MODEL_MEAN_VALUES, swapRB=False, crop=False
    )
    gender_net.setInput(blob)
    return gender_net.forward()


def get_age_predictions(face_img):
    blob = cv2.dnn.blobFromImage(
        image=face_img, scalefactor=1.0, size=(227, 227),
        mean=MODEL_MEAN_VALUES, swapRB=False
    )
    age_net.setInput(blob)
    return age_net.forward()



def pipeline_model(path):
    # pipeline model
    img = cv2.imread(path)
    image = img.copy()
    h,w = img.shape[:2]
    # face detection
    img_blob = cv2.dnn.blobFromImage(img,1,(300,300),(104,177,123),swapRB=False,crop=False)
    face_detector_model.setInput(img_blob)
    detections = face_detector_model.forward()
    
    # machcine results
    machinlearning_results = dict(face_detect_score = [], 
                                 face_name = [],
                                 face_name_score = [],
                                 emotion_name = [],
                                 emotion_name_score = [],
                                 count = [])
    count = 1
    if len(detections) > 0:
        for i , confidence in enumerate(detections[0,0,:,2]):
            if confidence > 0.5:
                box = detections[0,0,i,3:7]*np.array([w,h,w,h])
                startx,starty,endx,endy = box.astype(int)
                cropped = image[starty:endy , startx:endx]
                score = -1
                score = -1
                cnt = -1
                cnt1 = -1
                
                age_preds = get_age_predictions(image)
                gender_preds = get_gender_predictions(image)
                i = gender_preds[0].argmax()
                gender = GENDER_LIST[i]
                gender_confidence_score = gender_preds[0][i]
                i = age_preds[0].argmax()
                age = AGE_INTERVALS[i%4]
                age_confidence_score = age_preds[0][i]
                
                # label = "{}-{:.2f}%".format(gender, gender_confidence_score*100)
                # label = f"{gender}-{gender_confidence_score*100:.1f}%\n{age}-{age_confidence_score*100:.1f}%"
                # print(label)
                
                if age not in accepted_age:
                    print()
                    print("We Cannot Find This Person ...........................")
                    print()
                    break
                else:   
                    #Detected Face in Cropped Variable................................
                    try:
                        cnt,score = predicted(cropped)
                    except:
                        print()
                        print("Not Croppable .......... Moving Ahead with original image")
                    
                    cnt1,score1 = predictor(image)
                    
                    if score1 > score:
                        cnt=cnt1
                        score=score1
                    print()
                    print("Child Number               == " , cnt+1)
                    print("Face Verification Score    == " , score*100 , " %")
                    print()
                    print("Predicted Gender           == " , gender)
                    print("Predicted Gender Score     == " , gender_confidence_score*100 , " %")
                    print()
                    print("Predicted Age Interval     == " , age)
                    print("Predicted Age Score        == " , age_confidence_score*100 , " %")
                    print()  
                    break            
    return cropped , cnt, score





