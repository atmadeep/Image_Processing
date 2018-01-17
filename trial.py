#!/usr/bin/env python
import cv2
img = cv2.imread('shapesPhoto.png')
yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
cv2.imshow('original',img)
cv2.imshow('yuv',yuv)
cv2.imshow('sub',cv2.bitwise_not(img,yuv,None))
cv2.waitKey()