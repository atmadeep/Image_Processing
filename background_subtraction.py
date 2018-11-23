import cv2 as cv

cap=cv.VideoCapture(0)
backgroundMOG2 = cv.createBackgroundSubtractorMOG2()
backgroundKNN = cv.createBackgroundSubtractorKNN()
while True:
    ret, frame = cap.read()
    background_mask_MOG = backgroundMOG2.apply(frame)
    background_mask_KNN = backgroundKNN.apply(frame)
    cv.imshow('Original',frame)
    cv.imshow('background removed using MOG', background_mask_MOG)
    cv.imshow('background removed using KNN', background_mask_KNN)

    k=cv.waitKey(30) & 0xFF
    if(k==27):
        break
    if(k==32):
        cv.imwrite('other_images/original.jpeg',frame)
        cv.imwrite('other_images/MOG.jpeg',background_mask_MOG)
        cv.imwrite('other_images/KNN.jpeg',background_mask_KNN)

cap.release()
cv.destroyAllWindows()