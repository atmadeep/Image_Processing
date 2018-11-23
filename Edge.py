import cv2

frame = cv2.imread('other_images/shapesPhoto.png')

sobelx=cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
sobely=cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
canny = cv2.Canny(frame, 80, 80)
laplacian = cv2.Laplacian(frame, cv2.CV_64F)
cv2.imshow('orginal',frame)
cv2.imshow('laplacian_grdient',laplacian)
cv2.imwrite('other_images/Laplacain_edge.jpeg',laplacian)
cv2.imshow('x_grdient',sobelx)
cv2.imwrite('other_images/Sobel_x.jpeg',sobelx)
cv2.imshow('y_grdient',sobely)
cv2.imwrite('other_images/Sobel_y.jpeg',sobely)
cv2.imshow('edges', canny)
cv2.imwrite('other_images/canny_edge.jpeg', canny)

k=cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
