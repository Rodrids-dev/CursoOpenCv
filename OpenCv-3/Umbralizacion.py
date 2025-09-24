import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("alexa.jpeg")
#CONVERTIMOS A ESCALA DE GRISES
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#CREAMOS MATRIZ DEL TAMAÑO DE LA IMAGEN
matriz = np.ones(gray.shape, dtype='uint8') * 50
#PARA DISMINUIR EL BRILLO
matrizoscura = np.ones(gray.shape, dtype='uint8') * 50

#UMBRALIZAMOS IMAGEN BRILLANTE
#
#
#
#
#

#AUMENTAMOS EL BRILLO
brillantegray = cv2.add(gray, matriz)

# THRESHOLD
_, imgthresh1 = cv2.threshold(brillantegray, 210,255, cv2.THRESH_BINARY)

_, imgthresh2 = cv2.threshold(brillantegray, 210,255, cv2.THRESH_BINARY_INV)

# THRESHOLD ADAPTIVE
imgadaptive1 = cv2.adaptiveThreshold(brillantegray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 27, 2)

#DISMINUIMOS EL BRILLO EN GRAY
oscuragray = cv2.subtract(gray, matrizoscura)

#THRESHOLD
_, imgthresh3 = cv2.threshold(oscuragray, 50, 255, cv2.THRESH_BINARY)

_, imgthresh4 = cv2.threshold(oscuragray, 50, 255, cv2.THRESH_BINARY_INV)

#THRESHOLD ADAPTIVE
imgadaptive2 = cv2.adaptiveThreshold(oscuragray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 27, 2)

#MOSTRAMOS
fig = plt.figure()
#BRILLANTE
f1 = fig.add_subplot(2,4,1)
f1.imshow(brillantegray, cmap='gray')
f1.set_title("Brillante")
#BRILLANTE THRESH BINARY
f2 = fig.add_subplot(2,4,2)
f2.imshow(imgthresh1, cmap='gray')
f2.set_title("B-BINARY")
#BRILLANTE THRESH BINARY_INV
f3 = fig.add_subplot(2,4,3)
f3.imshow(imgthresh2, cmap='gray')
f3.set_title("B-BINARY_INV")
#BRILLANTE ADAPTATIVE
f4 = fig.add_subplot(2,4,4)
f4.imshow(imgadaptive1, cmap='gray')
f4.set_title("B-ADAPTATIVE")
#OSCURA
f5 = fig.add_subplot(2,4,5)
f5.imshow(oscuragray, cmap='gray')
f5.set_title("OSCURA")
#OSCURA THRESH BINARY
f6 = fig.add_subplot(2,4,6)
f6.imshow(imgthresh3, cmap='gray')
f6.set_title("O-BINARY")
#OSCURA BINARY_INV
f7 = fig.add_subplot(2,4,7)
f7.imshow(imgthresh4, cmap='gray')
f7.set_title("O-BINARY_INV")
#OSCURA ADAPTATIVE
f8 = fig.add_subplot(2,4,8)
f8.imshow(imgadaptive2, cmap='gray')
f8.set_title("O-ADAPTATIVE")


plt.show()
cv2.waitKey(0)