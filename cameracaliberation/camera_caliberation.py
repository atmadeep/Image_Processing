import numpy as np
import cv2
import glob

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TermCriteria_MAX_ITER,30,0.001)

objp=np.zeros((7*9, 3),np.float32)
objp[:,:2]= np.mgrid[0:9,0:7].T.reshape(-1,2)

objpoints = []
imgpoints = []

images = glob.glob('*.JPG')
fname = 'DSC00041.JPG'

img=cv2.imread(fname)
print(fname)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,corners = cv2.findChessboardCorners(gray,(9,7),None)
if ret==True:
    objpoints.append(objp)
    print('object points')
    print(objpoints)
    cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
    imgpoints.append(corners)
    print('image points')
    print(imgpoints)
    cv2.drawChessboardCorners(img,(9,7),corners,ret)
    cv2.imshow('img',img)
    cv2.waitKey()

print('\nobject and image points\n')

