import cv2 as cv
import numpy as np

img = cv.imread(r'Photo\boston.jpg')
cv.imshow('Boston', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur =  cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)  # ksize determins the blurryness, must be odd
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

canny_blur = cv.Canny(blur, 125, 175)
cv.imshow('Canny-Blur', canny_blur)

# Dilating the Image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_LINEAR)
# INTER_CUBIC - most detail
# INTER_AREA - default
# INTER_LINEAR - Increase image size
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey()