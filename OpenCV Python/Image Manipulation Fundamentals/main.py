import cv2
import random

img = cv2.imread('Cute-Cat-Images14.jpg')
img = cv2.resize(img, (400,400))

# accessing pixel values --- random
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

# copy and pasting  part of an image
tag = img[200:350, 300:400]
img[100:250,100:200 ] = tag

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
