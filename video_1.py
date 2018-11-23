import numpy as np
import cv2
cap1=cv2.VideoCapture(1)
cap2=cv2.VideoCapture(2)
while(True):
	ret,frame1=cap1.read()
	ret,frame2=cap2.read()
	gray1=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
	gray2=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
	cv2.imshow('left' ,gray1)
	cv2.imshow('right',gray2)

	if(cv2.waitKey(25) & 0xFF==ord('q')):
		break
cap.release()
cv2.destroyAllWindows()
