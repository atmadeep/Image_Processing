import cv2 as cv
image = cv.imread('deep.jpg')
cv.imshow('Frame',image)
cv.imwrite('opencv_sample.jpg',image)
cv.waitKey(10000)



