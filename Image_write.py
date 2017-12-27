import numpy as np
import cv2
img = cv2.imread('shapesPhoto.png', cv2.IMREAD_COLOR)

cv2.line(img,(0, 0), (150, 150), ([255,255,255]),1)
cv2.rectangle(img,(0,0) ,(200,200),(255,255,255),2)
cv2.circle(img , (100,50) ,(80) , (0,0,255),4)
pts = np.array([[13,56],[45,678],[456,100],[500,233]],np.int32)
pts=pts.reshape(-1,1,2)
cv2.polylines(img,[pts], True,(234,123,78),3)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Atmadeep Arya', (0,130),font,1,(200,244,244),2,cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
