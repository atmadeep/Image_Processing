import numpy as np
import cv2
cap = cv2.VideoCapture(0)
ret,frame = cap.read()
#hardcoded values for initial location of window
r,h,c,w = 250,90,400,125
track_win = (c,r,w,h)
#setting up region of interest.
roi= frame[r:r+h, c:c+w]
hsv_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
low = np.array([0,60,32])
high=np.array([180,255,255])
mask=cv2.inRange(hsv_roi,low,high)
#calculating histogram of region of interest
roi_hist = cv2.calcHist([hsv_roi], [0],mask, [180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
#this is the termination criteria.
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,1)

while(True):
    ret,frame=cap.read()
    if(ret == True):
        hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #generating a backproject image from the given frame
        dst=cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        #using meanshit to get new centroid
        ret, track_win=cv2.meanShift(dst,track_win,term_crit)
        #putting it back on image.
        x,y,w,h=track_win
        img2=cv2.rectangle(frame,(x,y),(x+w,y+h),255,2)
        cv2.imshow('Tracked',img2)
        k=cv2.waitKey(60) & 0xff
        if k==27:
            break
        else:
            cv2.imwrite(chr(k) + '.jpg',img2)
    else:
        break
cv2.destroyAllWindows()
cap.release()