import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("monedas.jpg")
imgmat = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#CONVERTIMOS A ESCALA DE GRISES
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#CREAMOS UNA MATRIZ DEL TAMAÑO DE LA IMAGEN
matriz = np.ones(gray.shape, dtype='uint8') * 50
matrizrgb = np.ones(img.shape, dtype='uint8') * 50

#AUMENTAMOS EL BRILLO DE LA IMAGEN EN RGB
brillantergb = cv2.add(imgmat, matrizrgb)
brillantergba = cv2.cvtColor(brillantergb, cv2.COLOR_RGB2RGBA)

#DISMINUIMOS EL BRILLO EN LA IMAGEN EN RGB
oscurargb = cv2.subtract(imgmat, matrizrgb)
oscurargba = cv2.cvtColor(oscurargb, cv2.COLOR_RGB2RGBA)

#AUMENTAMOS BRILLO EN IMAGEN GRAY
brillantegray = cv2.add(gray, matriz)

#DISMINUIMOS BRILLO EN IMAGEN EDG
oscuragray = cv2.subtract(gray, matriz)

#MOSTRAMOS IMAGENES
fig = plt.figure()
#IMAGEN ORIGINAL
f1 = fig.add_subplot(4,3,1)
f1.imshow(img)
f1.set_title("IMAGEN ORIGINAL")
#EN ESCALA DE GRISES
f2 = fig.add_subplot(4,3,2)
f2.imshow(gray, cmap='gray')
f2.set_title("IMAGEN EN EDG")
#EN RGB
f3 = fig.add_subplot(4,3,3)
f3.imshow(imgmat)
f3.set_title("IMAGEN EN RGB")
#BRILLANTE EN RGB
f4 = fig.add_subplot(4,3,4)
f4.imshow(brillantergb)
f4.set_title("BRILLANTE RGB")
#OSCURA RGB
f5 = fig.add_subplot(4,3,6)
f5.imshow(oscurargb)
f5.set_title("OSCURA RGB")
#BRILLANTE EN RGBA
f6 = fig.add_subplot(4,3,7)
f6.imshow(brillantergba)
f6.set_title("BRILLANTE RGBA")
#OSCURA RGBA
f7 = fig.add_subplot(4,3,9)
f7.imshow(oscurargba)
f7.set_title("OSCURA RGBA")
#BRILLANTE GRIS
f8 = fig.add_subplot(4,3,10)
f8.imshow(brillantegray, cmap='gray')
f8.set_title("BRILLANTE GRAY")
#OSCURA GRAY
f9 = fig.add_subplot(4,3,12)
f9.imshow(oscuragray, cmap='gray')
f9.set_title("OSCURA GRAY")

plt.show()

cv2.waitKey(0)