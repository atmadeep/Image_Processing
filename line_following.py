import cv2


cap = cv2.VideoCapture(0)
cap.set(3,640.0)
cap.set(4,480.0)
cap.set(5,15)
fourcc = cv2.VideoWriter_fourcc(*'XVID') #for recording videos. Currently it does not work on Raspberry pi 2B+. so we are using a scree recording utility.
video = cv2.VideoWriter('video.avi',fourcc, 7.5 ,(640,480))
font = cv2.FONT_HERSHEY_SIMPLEX
while cv2.waitKey(1)!= 27:
    flag,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret,threshold = cv2.threshold(blur,35,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ret2,threshold2=cv2.threshold(threshold,127,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('temp',threshold2)

    _,contours,hierarchy = cv2.findContours(threshold2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    max_cnt = max(contours, key=cv2.contourArea)
    cv2.drawContours(frame,max_cnt,-1,(0,255,0),2)

    for cnt in contours:

        area = cv2.contourArea(max_cnt)
        if(area>=500):
            M=cv2.moments(max_cnt)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            if(cx <= 280):
                l = (cx*100/160)
                print("\nturn left\n")
                cv2.putText(frame,'LEFT',(300,220),font,1,(0,0,255),2,cv2.LINE_AA)

            elif(cx >= 360):
                r = ((320-cx)*100/160)
                print("\nTurn right\n")
                cv2.putText(frame, 'RIGHT', (300, 220), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
            else:
                print("\ngo straight\n")
                cv2.putText(frame,'STRAIGHT',(300,220),font,1,(0,0,255),2,cv2.LINE_AA)

            cv2.imshow('frame', frame)
            video.write(frame)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
         break
cap.release()
video.release()
cv2.destroyAllWindows()
