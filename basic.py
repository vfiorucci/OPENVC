import cv2 as cv
import numpy as np

img = cv.imread('Photo\Cat.jpg')
cv.imshow('Cat', img)
# 1. Converting to grayscale



cv.waitKey()