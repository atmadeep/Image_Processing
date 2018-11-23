import cv2
cap=cv2.VideoCapture(0)
FPS = float(cap.get(cv2.CAP_PROP_FPS))
SIZE = (int(cv2.CAP_PROP_FRAME_WIDTH),int(cv2.CAP_PROP_FRAME_HEIGHT))
FOUR_CC = cv2.VideoWriter_fourcc(*'MJPG')
output = cv2.VideoWriter('output.avi',FOUR_CC,10,SIZE)
#output = cv2.VideoWriter('output.avi',FOUR_CC,FPS,(640,480))
while(cap.isOpened()):
	ret,frame = cap.read()
	if(ret):
		cv2.imshow('Frame',frame)
		output.write(frame)
		if(cv2.waitKey(1) & 0xFF == ord('q')):
			break

	else:
		break

cap.release()
output.release()
cv2.destroyAllWindows()
