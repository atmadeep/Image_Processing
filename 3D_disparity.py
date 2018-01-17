import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL= cv2.imread('DSC00033.JPG',0)
imgR= cv2.imread('DSC00036.JPG',0)
blurL = cv2.GaussianBlur(imgL,(3,3),0)
blurR = cv2.GaussianBlur(imgR,(3,3),0)

stereo = cv2.StereoBM_create(numDisparities=96, blockSize=15)
disparity=stereo.compute(blurL,blurR)
plt.imshow(disparity,'gray')
plt.show()