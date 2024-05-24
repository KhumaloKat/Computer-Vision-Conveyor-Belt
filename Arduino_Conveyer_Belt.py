import cvzone
from cvzone.ClassificationModule import Classifier
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
myClassifier = Classifier("Model-1/keras_model.h5", "Model-1/labels.txt")
imgHeader = cv2.imread("HeaderCustomClassification.png", cv2.IMREAD_UNCHANGED)

cars, airplanes = 0, 0
counter, countDelay = 0, 0
while True:
    success, img = cap.read()
    predection = myClassifier.getPrediction(img,draw= False)
    classDetected = predection[1]

    if classDetected != 0:
        counter += 1
        if counter > 3 and countDelay == 0:
            if classDetected == 1:
                airplanes += 1
            else:
                cars += 1
            countDelay = 1
            counter = 0

        else:
            countDelay += 1
            if countDelay > 15:
                countDelay = 0
    print(airplanes, cars)

    img = cvzone.overlayPNG(img, imgHeader, [0, 50])
    img, _ = cvzone.putTextRect(img,str(cars),[450,135],scale=5)
    img, _ = cvzone.putTextRect(img,str(airplanes),[1050,135],scale=5)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
