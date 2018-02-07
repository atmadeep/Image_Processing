import cv2
import numpy as np
import imutils

def shape_detect(c):
    shape="unidentified"
    perimeter = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.04*perimeter,True,approxCurve=None)

    if len(approx)==3:
        shape="triangle"

    elif len(approx)==4:
        (x,y,w,h) = cv2.boundingRect(approx)
        ar = w/float(h)
        shape = "square" if ar > .95 and ar < 1.05 else "rectangle"

    elif len(approx)==5:
        shape="pentagon"

    elif len(approx) == 6:
        shape="hexagon"

    else:
        shape = "circle"

    return shape,approx

cap = cv2.VideoCapture(0)
min_area = 0
max_area = 100000
while True:
    ret,image  = cap.read()
    #image = cv2.imread('left_instruction.jpg')
    ratio = image.shape[0]/300.0
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray,(3,3),0)
    thresh = cv2.threshold(blur,100,255,cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]
    canny  = cv2.Canny(thresh,100,255,)
    rectangles = []
    frame,cnts,hierarchy = cv2.findContours(canny.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts,key=cv2.contourArea,reverse=True)
    cv2.drawContours(image,cnts,0,(0,255,200),2)

    for c in cnts:
        shape,rectangle = shape_detect(c)
        area = cv2.contourArea(rectangle)
        if(shape=='rectangle' ):
            sign = rectangle






    pts = sign.reshape(4,2)
    rect = np.zeros((4,2),dtype="float32")
    s= pts.sum(axis=1)
    rect[0]=pts[np.argmin(s)]
    rect[2]=pts[np.argmax(s)]
    diff = np.diff(pts,axis=1)
    rect[1]=pts[np.argmin(diff)]
    rect[3]=pts[np.argmax(diff)]

    rect*=ratio

    (tl, tr, br, bl) = rect
    widthA = np.sqrt(((br[0]-bl[0])**2)+((br[1]-bl[1])**2))
    widthB = np.sqrt(((tr[0]-tl[0])**2)+((tr[1]-tl[1])**2))

    heightA = np.sqrt(((tr[0]-br[0])**2)+((tr[1]-br[1])**2))
    heightB = np.sqrt(((tl[0]-bl[0])**2)+((tl[1]-bl[1])**2))

    maxwidth = max(int(widthA),int(widthB))
    maxheight = max(int(heightA),int(heightB))

    dst = np.array([
            [0,0],
                [maxwidth-1, 0],
                [maxwidth-1,maxheight-1],
                [0,maxheight-1]],dtype="float32")
    Perspective=cv2.getPerspectiveTransform(rect,dst)
    warp = cv2.warpPerspective(image.copy(),Perspective,(maxwidth,maxheight))
    warp = cv2.cvtColor(warp,cv2.COLOR_BGR2GRAY)
    cv2.imshow('warp',warp)
    cv2.imshow('image',image)
    cv2.imshow('canny',canny)
    k=cv2.waitKey(30) & 0xFF
    if k == 27:
        break

print("good run.")
cap.release()
cv2.destroyAllWindows()