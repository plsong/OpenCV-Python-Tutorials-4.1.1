import cv2 as cv

img = cv.imread('messi.jpg',0)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
