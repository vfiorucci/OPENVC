import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# blank2 = np.zeros((500,500,3), dtype='uint8')
cv.imshow("Blank", blank)

# 1. Paint the image a cretain color
# blank[:] = 0,255,0
# cv.imshow("Green", blank)
# Red square
# blank[200:300, 300:400] = 0,0,255
# cv.imshow("Red Square", blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)
cv.imshow("Rectangle", blank)

# 3. Draw a circle
cv.circle(blank,(250,250), 40, (0,0,255), thickness=3)
cv.imshow("Circle", blank)

# 4. Draw a line
cv.line(blank, (225,225),(400,400),(255,255,255),thickness=3)
cv.imshow("Line", blank)

# 5. Write text on image
cv.putText(blank,'Hello', (40,40), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, (0,0,255), thickness=2)
cv.imshow("Text", blank)

cv.waitKey(0)