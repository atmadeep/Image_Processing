import cv2 as cv
cap_left=cv.VideoCapture(0)
cap_right=cv.VideoCapture(2)
fourcc = cv.VideoWriter_fourcc(*'MJPG') # Video codec to be used is XVID
video_right=cv.VideoWriter("video_right.avi",fourcc,60,(640,480)) # type : VideoWriter
video_left=cv.VideoWriter("video_left.avi",fourcc,60.0,(640,480)) # type : VideoWriter
counter=0  # type: int

while True:
    _,frame_left=cap_left.read()
    _,frame_right=cap_right.read()
    cv.imshow("Frame Left",frame_left)
    cv.imshow("Frame Right",frame_right)
    video_left.write(frame_left)
    video_right.write(frame_right)
    k=cv.waitKey(30) & 0xff
    if(k==27):
        break
    elif(k==32):
        cv.imwrite("imleft{}.jpg".format(counter),frame_left)
        cv.imwrite("imright{}.jpg".format(counter),frame_right)
        print("Wrote image pair",counter)
        counter+=1


video_left.release()
video_right.release()
cap_right.release()
cap_left.release()
cv.destroyAllWindows()