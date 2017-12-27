import numpy as np
import cv2
cap=cv2.VideoCapture(0)
feature_parameter = dict(maxCorners = 100, qualityLevel = 0.5, minDistance = 7,
                         blockSize =7)
#lucas_kanade optical flow parametres
lk_parametres = dict(winSize = (20,20), maxLevel = 2,
                     criteria =((cv2.TermCriteria_EPS | cv2.TermCriteria_COUNT),10, 0.03 ))
color = np.random.randint(0,255,(100,3))
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame,cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray,mask=None, **feature_parameter)
mask = np.zeros_like(old_frame)

while(True):
    ret,frame = cap.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    p1,st,err = cv2.calcOpticalFlowPyrLK(old_gray,frame_gray,p0,None,**lk_parametres)

    #selecting good points
    good_new = p1[st==1]
    good_old = p0[st==1]

    #drawing the tracks
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv2.line(mask,(a,b),(c,d),color[i].tolist(),2)
        frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
        img = cv2.add(frame,mask)
        cv2.imshow('Image',img)
        k=cv2.waitKey(30) & 0xff
        if k==27:
            break
        old_gray=frame_gray.copy()
        p0=good_new.reshape(-1,1,2)

cv2.destroyAllWindows()
cap.release()