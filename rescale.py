"""Facial Recognition Software."""
import cv2 as cv

"""Reading in an Image."""
img = cv.imread('Photo\Cat.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# img = cv.imread('Photo\Cat_large.jpg')
# cv.imshow("Cat", gray)
cv.imshow("Cat", img)

# Rescale of the image or video
def rescale_frame(frame, scale = .75):
    """Images, Video and Live Video."""
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    """Live Video."""
    capture.set(3, width)
    capture.set(4, height)



resized_image = rescale_frame(img)
cv.imshow("Image Resized", resized_image)


"""Reading in a Video."""
capture = cv.VideoCapture(r'Videos\dog.mp4')
# While loop for video
while True:
    isTrue, frame = capture.read()
    frame_resized = rescale_frame(frame)

    cv.imshow('Video', frame)
    cv.imshow("Video Resized", frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
# cv.waitKey(0)