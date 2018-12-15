import cv2 as cv
cap_left = cv.VideoCapture(0)
#cap_right = cv.VideoCapture(2)
i=0
while True:
    _, frame_left = cap_left.read()
 #   _, frame_right = cap_right.read()
    frame_left=cv.cvtColor(frame_left, cv.COLOR_BGR2GRAY)
   # frame_right=cv.cvtColor(frame_right, cv.COLOR_BGR2GRAY)
    cv.imshow("image_left", frame_left)
  #  cv.imshow("image_right", frame_right)
    k = (cv.waitKey(25) & 0xFF)
    if(k==27):
        break
    if(k==32):
     #   name_right = 'image_right{}.jpg'.format(i)
        name_left = 'image_left{}.jpg'.format(i)
    #    cv.imwrite(name_right, frame_right)
        cv.imwrite(name_left,frame_left)
        print("\nwrote iamge pair ",i)
        i+=1;



#cap_right.release()
cap_left.release()
cv.destroyAllWindows()