import cv2
import numpy as np
from collections import deque


# laptop wecam
cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX
pts = deque(maxlen=2)
lower_green = np.array([33, 80, 40])
upper_green = np.array([102, 255, 255])
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])


# This drives the program into an infinite loop.
while (True):

    ret, image = cap.read()
    ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    y, cr, cb = cv2.split(ycrcb)
    y_eq = cv2.equalizeHist(y)
    # cr_eq = cv2.equalizeHist(cr)
    # cb_eq = cv2.equalizeHist(cb)

    ycrcb = cv2.merge((y_eq, cr, cb))
    new_image = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)
    cv2.imshow('original', image)
    cv2.imshow('equalized', new_image)
    blur = cv2.GaussianBlur(image, (5, 5), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    mask_green = cv2.inRange(hsv, lowerb=lower_green, upperb=upper_green)
    mask_blue = cv2.inRange(hsv, lowerb=lower_blue, upperb=upper_blue)
    mask = cv2.erode(cv2.bitwise_not(mask_blue - mask_green), None, iterations=15)
    imag, contours, heirarchy = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    algae = sorted(contours, key=cv2.contourArea)[:1]
    cv2.drawContours(image, algae, -1, (0, 255, 0), 4)
    #algae = np.array(algae)
    M = cv2.moments(algae)
    if int(M['m00']) != 0:
        cx = int(M['m10']) / int(M['m00'])
        cy = int(M['m01']) / int(M['m00'])
        rect = [[cx - 50, cy - 50], [cx + 50, cy - 50], [cx - 50, cy + 50], [cx + 50, cy + 50]]
        cv2.circle(image, (cx, cy), 1, (0, 0, 255), 3)
        cv2.rectangle(image, (cx - 50, cy - 50), (cx + 50, cy + 50), (0, 0, 255), 3)
    else:
        cx=0
        cy=0

    if (cx < 40):
            print("\ngo left\n")
            cv2.putText(image, 'left', (280, 200), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    elif (cx > 520):
            print("\ngo right\n")
            cv2.putText(image, 'right', (280, 200), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    elif (cy < 60):
            print("\nmove front\n")
            cv2.putText(image, 'front', (280, 200), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    elif (cy > 180):
            print("\nmove back\n")
            cv2.putText(image, 'back', (280, 200), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    else:
            print('\n clean \n')
    for i in range(1, len(pts)):
        if pts[i - 1] is None or pts[i] is None:
            continue
            thickness = 2
            cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
        res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', image)
    cv2.imshow('mask', mask_green)
    #   cv2.imshow('res', res)

    # This displays the frame, mask
    # and res which we created in 3 separate windows.
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()

# release the captured frame
cap.release()

