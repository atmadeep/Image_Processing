import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0)

while(True):
    _, frame=cap.read()
    sobelx=cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely=cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    edges = cv2.Canny(frame,80,80)
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    cv2.imshow('orginal',frame)
   # cv2.imshow('laplacian_grdient',laplacian)
    #cv2.imshow('x_grdient',sobelx)
    #cv2.imshow('y_grdient',sobely)
    cv2.imshow('edges',edges)

    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()