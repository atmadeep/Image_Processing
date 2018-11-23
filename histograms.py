import cv2
from matplotlib import pyplot as plt
import glob

for image in  glob.glob('pot_holes/*.jpeg'):
    print(image)
    frame = cv2.imread(image)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow(image, gray)

    gaussianBlur = cv2.GaussianBlur(gray, (11, 11), 0)

    plt.hist(gray.ravel(),256,[0,256],color="green")
    plt.show()

    plt.hist(gaussianBlur.ravel(), 256, [0, 256],color="red")
    plt.show()

cv2.destroyAllWindows()

