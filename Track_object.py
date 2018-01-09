import cv2
import numpy as np
from collections import deque
import imutils

# laptop wecam
cap = cv2.VideoCapture(1)
pts = deque(maxlen=2)
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

# This drives the program into an infinite loop.
while (True):

    # Captures the live stream frame-by-frame
    _, frame = cap.read()
    frame = imutils.resize(frame,600)
    blur = cv2.GaussianBlur(frame,(11,11),0)
    # Converts images from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # This creates a mask of blue coloured
    # objects found in the frame.
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    #erodes small noises away
    mask=cv2.erode(mask,None,iterations=3)
    #accentuates the features of our blue object.
    mask = cv2.dilate(mask,None,iterations=2)
    contours = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    centre = None
    if(len(contours)) > 0:
        c=max(contours, key=cv2.contourArea)
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        M=cv2.moments(c)
        centre = (int(M['m10']/M['m00']), int(M['m01']/M['m00']))
        print(centre)

        if radius > 5:
            cv2.circle(frame,(int(x), int(y)),int(radius),(0,255,255),2)
            cv2.circle(frame,centre, 5 ,(0,0,255),-1)
        pts.append(centre)
        if(x  < 40):
            print("\ngo left\n")
        if(x > 540) :
            print("\ngo right\n")
        if(y < 20):
            print("\nmove back\n")
        if(y > 280):
            print("\nmove front\n")
        for i in xrange (1,len(pts)):
            if pts[i-1] is None or pts[i] is None :
                continue
            thickness = 2
            cv2.line(frame,pts[i-1],pts[i],(0,0,255),thickness)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

        # This displays the frame, mask
        # and res which we created in 3 separate windows.
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
         break

# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()

# release the captured frame
cap.release()