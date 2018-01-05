import cv2
import numpy as np
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
while(True) :
    ret,image=cap.read()
    output=image.copy()
    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)  # cv2.cv.CV_HOUGH_GRADIENT is not used anymore.
    if circles is not None:
        circles = np.round(circles[0, :]).astype('int')
        for (x, y) in circles:
            cv2.circle(output, (x, y), r, (255, 0, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    cv2.imshow('gray',image)
    cv2.imshow('circles',output)
    k=cv2.waitKey(30) & 0xFF
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()