import cv2
import numpy as np
image = cv2.imread('shapesPhoto.png')
blurred=cv2.pyrMeanShiftFiltering(image,31,41)
gray=cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
th,contours,hierarchy=cv2.findContours(threshold,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
print('no. of contours detected ', len(contours))
cv2.drawContours(blurred,contours,-1,(0,255,255),4)
cv2.namedWindow('display',cv2.WINDOW_NORMAL)
cv2.imshow('Display',image)
cv2.waitKey()