"""Facial Recognition Software."""
import cv2 as cv

"""Reading in an Image"""
img = cv.imread('Photo\Cat.jpg')
# img = cv.imread('Photo\Cat_large.jpg')
cv.imshow("Cat", img)

def rescale_frame(frame, scale = .75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resized_image = rescale_frame(img)
cv.imshow("Image Resized", resized_image)


"""Reading in a Video"""
capture = cv.VideoCapture(r'Videos\dog.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescale_frame(frame)

    cv.imshow('Video', frame)
    cv.imshow("Video Resized", frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
# cv.waitKey(0)