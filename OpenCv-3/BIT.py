import cv2
import matplotlib.pyplot as plt

#TENEMOS 4 TIPOS (OPERACIONES LOGICAS)
#cv2.bitwise_and(img1, img2, mask) cv2.bitwise_.../ or / xor / not

#IMAGENES
img1 = cv2.imread('img1.jpg', 0)
#RECORTO LA IMG 1 PARA QUE QUEDE DEL MISMO TAMAÑO QUE LA 2
img1 = cv2.resize(img1, (640,640), interpolation=cv2.INTER_CUBIC)
img2 = cv2.imread('img2.jpg', 0)

#OPERACION AND
imgand = cv2.bitwise_and(img1,img2, mask = None)

#OPERACION OR
imgor = cv2.bitwise_or(img1,img2, mask = None)

#OPERACION XOR
imgxor = cv2.bitwise_xor(img1,img2, mask = None)

#PLOTEAMOS
fig = plt.figure()
#IMAGEN 1
f1 = fig.add_subplot(2,3,1)
f1.imshow(img1, cmap='gray')
f1.set_title('IMAGEN 1')
#IMAGEN 2
f2 = fig.add_subplot(2,3,3)
f2.imshow(img2, cmap='gray')
f2.set_title('IMAGEN 2')
#OPERACION AND
f3 = fig.add_subplot(2,3,4)
f3.imshow(imgand, cmap='gray')
f3.set_title('OP. AND')
#OPERACION OR
f4 = fig.add_subplot(2,3,5)
f4.imshow(imgor, cmap='gray')
f4.set_title('OP. OR')
#OPERACION XOR
f5 = fig.add_subplot(2,3,6)
f5.imshow(imgxor, cmap='gray')
f5.set_title('OP. XOR')

plt.show()

cv2.waitKey(0)