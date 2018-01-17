# import the necessary packages
import numpy as np
import cv2


def find_marker(image):
    # convert the image to grayscale, blur it, and detect edges
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 35, 125)

    # find the contours in the edged image and keep the largest one;
    # we'll assume that this is our piece of paper in the image
    (frame,cnts,_) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    c = max(cnts, key=cv2.contourArea)

    # compute the bounding box of the of the paper region and return it
    return cv2.minAreaRect(c)


def distance_to_camera(knownWidth, focalLength, perWidth):
	# compute and return the distance from the maker to the camera
	return (knownWidth * focalLength) / perWidth


KNOWN_DISTANCE = 6

# initialize the known object width, which in this case, the piece of
# paper is 11 inches wide
KNOWN_WIDTH = 1.5

# initialize the list of images that we'll be using
IMAGE_PATHS = ["image_1.jpg", "image_2.jpg", "image_3.jpg","image_4.jpg","image_5.jpg"]

# load the furst image that contains an object that is KNOWN TO BE 2 feet
# from our camera, then find the paper marker in the image, and initialize
# the focal length
image = cv2.imread(IMAGE_PATHS[0])
marker = find_marker(image)
focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH
#print(focalLength)
# loop over the images
for imagePath in IMAGE_PATHS:
    # load the image, find the marker in the image, then compute the
    # distance to the marker from the camera
    image = cv2.imread(imagePath)
    marker = find_marker(image)
    inches = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])
    print(inches)
    # draw a bounding box around the image and display it

    cv2.imshow("image", image)
    cv2.waitKey(0)