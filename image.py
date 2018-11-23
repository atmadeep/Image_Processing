import cv2
image = cv2.imread('other_images/shapesPhoto.png')
cv2.imshow('frame',image)
cv2.waitKey(0)
cv2.imwrite('new_image.jpg',image)
cv2.destroyAllWindows()