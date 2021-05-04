"""Facial Recognition Software."""
import cv2 as cv

"""Reading in an Image"""
# img = cv.imread('Photo\Cat.jpg')
# img = cv.imread('Photo\Cat_large.jpg')
# cv.imshow("Cat", img)
# cv.waitKey(0)

"""Reading in a Video"""
capture = cv.VideoCapture(r'Videos\dog.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
