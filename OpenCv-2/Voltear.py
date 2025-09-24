import cv2

img = cv2.imread("img.jpeg")

#Rotacion 1
rot1 = cv2.flip(img, 0)

#Rotacion 2
rot2 = cv2.flip(img, 1)

#Rotación 3
rot3 = cv2.flip(img, -1)

#Mostramos
cv2.imshow("original", img)
cv2.imshow("rotacion 1", rot1)
cv2.imshow("rotacion 2", rot2)
cv2.imshow("rotacion 3", rot3)

cv2.waitKey(0)