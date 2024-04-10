import cv2 as cv

img = cv.imread('Cute-Cat-Images14.jpg', cv.IM_COLOR)

cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()


