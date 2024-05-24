from cvzone.ClassificationModule import Classifier
import cv2

cap = cv2.VideoCapture(0)
myClassifier = Classifier("Model-1/keras_model.h5", "Model-1/labels.txt")

while True:
    success, img = cap.read()
    predection = myClassifier.getPrediction(img)

    cv2.imshow("Image", img)
    cv2.waitKey(1)