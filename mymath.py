import cv2
import numpy as np
import math


class Shapes:
    def __init__(self, img):
        self.img = img

    def preprocessing(self):
        lower=np.array([0, 0, 0],)
        upper=np.array([15, 15, 15],)
        mask = cv2.inRange(self.img, lower, upper)
        cv2.imshow('IMAGE_MASK',mask)
        (flags, contours, h) = cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        print contours
        return contours
img = cv2.imread('contour1.png')
shape = Shapes(img)
contours = shape.preprocessing()
cv2.imshow('Display', img)
cv2.waitKey(0)
cv2.destroyAllWindows()