import cv2

img = cv2.imread('Cute-Cat-Images14.jpg', 2)
img = cv2.resize(img, (400,400))
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_image.jpg',img)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()