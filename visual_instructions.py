import cv2
import numpy as np
from matplotlib import pyplot as py
frame = cv2.imread('right.png')

blur = cv2.GaussianBlur(frame,(15,15),0)
blur = cv2.pyrMeanShiftFiltering(frame,51,91)
blur = cv2.erode(blur,(5,5),iterations=2)
gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY,cv2.THRESH_OTSU)
th, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
print(len(contours))
cv2.drawContours(frame,contours,3,(0,0,255),4 )
cv2.imshow('frame',frame)
cv2.waitKey()

