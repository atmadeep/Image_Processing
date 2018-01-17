import cv2

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
while(True) :
    ret,image=cap.read()
    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image , (x,y),(x+w,y+h),(0,0,255),2)
        #
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