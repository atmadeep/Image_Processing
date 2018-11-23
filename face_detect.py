import cv2

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
while(True) :
    ret,image=cap.read()
    image = cv2.resize(image,(640,480))
    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image , (x,y),(x+w,y+h),(0,0,255),2)
        cx = (2*x+w)/2
        cy = (2*y+h)/2
        cv2.circle(image,(cx,cy),2,(255,255,0),-1)
        if (cx < 200):
            cv2.putText(image, 'left', (280, 200), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
        elif (cx > 440):
            cv2.putText(image, 'right', (280, 200), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
        elif (cy < 180):
            cv2.putText(image, 'front', (280, 200), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
        elif (cy > 300):
            cv2.putText(image, 'back', (280, 200), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
        else:
            cv2.putText(image, 'in frame', (280, 200), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=image[y:y+h,x:x+w]
        eyes=eye.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes :
            cv2.rectangle(roi_color,(ex,ey), (ex+ew,ey+eh), (0,255,0),2)
        

    cv2.imshow('primary',image)
    k=cv2.waitKey(30) & 0xFF
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()