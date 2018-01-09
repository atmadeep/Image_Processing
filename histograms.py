import cv2
import numpy as np
from matplotlib import pyplot as py
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required = True,help = 'path to image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('image',image)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


