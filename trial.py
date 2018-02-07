import cv2
import numpy as np
from collections import deque

pts = deque(maxlen=2)
lower_green = np.array([33, 80, 40])
upper_green = np.array([102, 255, 255])
lower_blue= np.array([160,50,50])
upper_blue= np.array([220,255,255])
font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(1)
left_limit = 40
right_limit = 300
upper_limit = 60
lower_limit = 180
while True:
    ret,image = cap.read()
    image = cv2.resize(image, (340, 220))
    ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    y, cr, cb = cv2.split(ycrcb)
    y_eq = cv2.equalizeHist(y)

    kernel = np.ones((2,2),np.uint8)
    ycrcb = cv2.merge((y_eq, cr, cb))
    new_image = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)
    cv2.imshow('original', image)
    cv2.imshow('equalized', new_image)
    blur = cv2.GaussianBlur(new_image,(5,5),0)
    hsv= cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    mask_green = cv2.inRange(hsv,lowerb=lower_green,upperb=upper_green)
    mask_blue = cv2.inRange(hsv,lowerb=lower_blue,upperb=upper_blue)
    #mask_blue = cv2.dilate(mask_blue,kernel=kernel,iterations=4)
    #cv2.imshow('MASK_BLUE',mask_blue)
    mask = cv2.erode(mask_green,kernel=kernel,iterations=2)
    imag,contours,heirarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[:5]
    if(contours != None):
        algae = max(contours,key=cv2.contourArea)

    cv2.drawContours(image,algae,-1,(0,255,0),4)
    M = cv2.moments(algae)
    if int(M['m00']) != 0:
        cx = int(M['m10'])/int(M['m00'])
        cy = int(M['m01'])/int (M['m00'])
        rect  = [[cx-50,cy-50],[cx+50,cy-50],[cx-50,cy+50],[cx+50,cy+50]]
        cv2.circle(image,(cx,cy),1,(0,0,255),3)
        cv2.rectangle(image,(cx-50,cy-50),(cx+50,cy+50),(0,0,255),3)
    if (cx < left_limit):
            print("\ngo left\n")
            cv2.putText(image, 'left', (170, 110), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    if (cx > right_limit):
            print("\ngo right\n")
            cv2.putText(image, 'right', (170, 110), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    if (cy < upper_limit):
            print("\nswim up\n")
            cv2.putText(image, 'swim up', (170, 110), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    if (cy > lower_limit):
            print("\nswim down\n")
            cv2.putText(image, 'swim down', (170, 110), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    if((cx > left_limit and cx < right_limit) and (cy > upper_limit and cy < lower_limit)):
            print('\n clean \n')
            cv2.putText(image, 'CLEAN', (170, 110), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('image',image)
    cv2.imshow('mask green',mask_green)

    k=cv2.waitKey(30) & 0xFF
    if k==27:
        break
print("\ngood run\n")
cap.release()
cv2.destroyAllWindows()



