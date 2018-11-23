import cv2
import glob

def find_marker(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 35, 125)

    (frame,cnts,_) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    c = max(cnts, key=cv2.contourArea)
    return cv2.minAreaRect(c)

def distance_to_camera(knownWidth, focalLength, perWidth):
	# compute and return the distance from the maker to the camera
	return (knownWidth * focalLength) / perWidth

KNOWN_DISTANCE = 6
KNOWN_WIDTH = 1.5

IMAGE_PATHS=glob.glob('other_images/image_*.jpg')
print(IMAGE_PATHS)

image = cv2.imread(IMAGE_PATHS[0])
marker = find_marker(image)
focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH

for imagePath in IMAGE_PATHS:
    print(imagePath)
    image = cv2.imread(imagePath)
    marker = find_marker(image)
    distance = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])
    print(distance)
    cv2.imshow(str(imagePath), image)
    cv2.waitKey(0)