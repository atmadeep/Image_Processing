import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(True):
    ret,frame = cap.read()
    #converting to HSV values
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_range = np.array([110,50,50])
    upper_range = np.array([130,255,255])
    #binary image of pixels falling under the color range
    mask=cv2.inRange(hsv,lower_range,upper_range)
    result = cv2.bitwise_or(frame,frame,mask=mask)
    cv2.imshow('blue_mask',result)
    cv2.imshow('HSV', hsv)
    cv2.imshow('original', frame)
    if(cv2.waitKey(1)==27):
        break
cap.release()
cv2.destroyAllWindows()