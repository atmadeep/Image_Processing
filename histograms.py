import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse
images = ['pot_1.jpeg','pot_2.jpeg','pot_3.jpeg','pot_4.jpeg','pot_5.jpeg','pot_6.jpeg',]
for name in images :
    image = cv2.imread(name)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    plt.hist(gray.ravel(),256,[0,256])
    plt.hist(blur.ravel(),256,[0,256])
    plt.show()

cv2.waitKey()



