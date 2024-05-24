import cvzone
import cv2
import time
from cvzone.ColorModule import ColorFinder

debug = False

interval = 0.15
detectionLine = 200
myColorFinder = ColorFinder(debug)
delayTimer = 0
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

colors = [['Green', {'hmin': 40, 'smin': 95, 'vmin': 0, 'hmax': 70, 'smax': 206, 'vmax': 255}],
          ['Yellow', {'hmin': 19, 'smin': 138, 'vmin': 0, 'hmax': 36, 'smax': 255, 'vmax': 255}],
          ['Orange', {'hmin': 5, 'smin': 131, 'vmin': 0, 'hmax': 13, 'smax': 255, 'vmax': 255}]]

counterList = [0] * len(colors)

imgHeader = cv2.imread("header.png", cv2.IMREAD_UNCHANGED)


def objectCounter(img, hsvVals):
    imgColor, mask = myColorFinder.update(img, hsvVals)
    img, contours = cvzone.findContours(img, mask, drawCon=True, minArea=5000)

    if contours:
        if detectionLine - 20 < contours[0]["center"][0] < detectionLine + 20:
            return True
    return False

while True:
    success, img = cap.read()

    if debug:
        imgColor, mask = myColorFinder.update(img)
        imgColor, contours = cvzone.findContours(img, mask, drawCon=True, minArea=1000)
        cv2.imshow("Image", imgColor)

    else:
        colorList = []
        if delayTimer ==0:
            colorDetectionLine = (0, 0, 255)
            for x, (color, colorHSV) in enumerate(colors):
                detected = objectCounter(img, colorHSV)
                if detected:
                    counterList[x] += 1
                colorList.append(detected)

        # print(colorList,any(colorList))
        if any(colorList):
            delayTimer = time.time()

        if delayTimer > 0:
            colorDetectionLine = (0, 255, 0)
            totalTime = time.time() - delayTimer
            print(totalTime)
            if totalTime > interval:
                delayTimer = 0

        print(counterList)

        cv2.line(img,(detectionLine, 0), (detectionLine,img.shape[0]), colorDetectionLine, 15)

        img = cvzone.overlayPNG(img, imgHeader, [0, 50])
        for x,counter in enumerate(counterList):
            cv2.putText(img, str(counter), (330+(x*360), 150), cv2.FONT_HERSHEY_PLAIN,5, (25, 25, 25), 5)

        cv2.imshow("Image", img)
    cv2.waitKey(1)
