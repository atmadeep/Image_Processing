import numpy as np
import cv2
from matplotlib import pyplot as plt
cap1 = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(2)
while True:
    ret1,imgL = cap1.read()
    ret2,imgR = cap1.read()
    grayL = cv2.cvtColor(imgL,cv2.COLOR_BGR2GRAY)
    grayR = cv2.cvtColor(imgR,cv2.COLOR_BGR2GRAY)
    blurL = cv2.GaussianBlur(grayL,(5,5),0)
    blurR = cv2.GaussianBlur(grayR,(5,5),0)

    stereo = cv2.StereoBM_create(numDisparities=96, blockSize=15)
    disparity=stereo.compute(blurL,blurR)
    cv2.imshow('disparity',disparity)
    #plt.show()
    k= cv2.waitKey() & 0xFF
    if(k==27):
        break
cap1.release()
cap2.release()
cv2.destroyAllWindows()