import cv2 as cv
import numpy as np
import glob
image=cv.imread('image0.jpg')
criteria = (cv.TermCriteria_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
CHECKERBOARDROW = 6
CHECKERBOARDCOLUMN=9
meanError = 0
objp=np.zeros((CHECKERBOARDROW * CHECKERBOARDCOLUMN, 3), np.float32)
objp[:,:2] = np.mgrid[0:CHECKERBOARDCOLUMN, 0:CHECKERBOARDROW].T.reshape(-1, 2)

objpoints =[]
imgpoints = []

images = glob.glob('image_right*.jpg')
for fname in images:
    img=cv.imread(fname)
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    image=gray;
    ret,corners=cv.findChessboardCorners(gray, (CHECKERBOARDCOLUMN, CHECKERBOARDROW), None)
    if(ret==True):
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria=criteria)
        imgpoints.append(corners)
        cv.drawChessboardCorners(img,(9,6),corners2,ret)
        cv.imshow(fname,img)
        cv.waitKey()
        cv.destroyWindow(fname)
print('All images have been read, going for calibration')
#Calibrate the camera
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, image.shape[::-1], None, None)
img = cv.imread('Face0.jpg')
h,w=img.shape[:2]
camera_mtx,roi=cv.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
dst=cv.undistort(img,mtx,dist,None,newCameraMatrix=camera_mtx)
x,y,w,h=roi
dst=dst[y:y+h,x:x+w]
cv.imshow("calibrated image 0",dst)
cv.imshow("un calibrated image",img)
for i in range(len(objpoints)):
    imgpoints2, _ = cv.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2)/len(imgpoints2)
meanError += error

print( "total error: {}".format(meanError/len(objpoints)) )
cv.waitKey()
cv.destroyAllWindows()