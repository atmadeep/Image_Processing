import cv2
import numpy as np

cap = cv2.VideoCapture(0)
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
while(True):

	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, lower_blue, upper_blue)
 	resultant_frame = cv2.bitwise_and(frame, frame, mask= mask)
	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('resultant frame', resultant_frame)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
	if(k==32):
		cv2.imwrite('other_images/blue_original.jpeg',frame)
		cv2.imwrite('other_images/blue_mask.jpeg',mask)
		cv2.imwrite('other_images/blue_res.jpeg',resultant_frame)

cv2.destroyAllWindows()
cap.release()
