#LECTURA DE IMAGENES
import cv2
import numpy as np
import matplotlib.pyplot as plt

#LECTURA DE IMAGEN EN ESACALA DE GRISES
imggray = cv2.imread("LEC.png", 0)
#LECTURA DE IMAGEN A COLOR
imgcolor = cv2.imread("LEC.png", 1)
#LECTURA
img = cv2.imread("LEC.png")

#EXTRAER ATRIBUTOS PRINCIPALES
tamano = imggray.shape
tipo = imggray.dtype
print("tamaño gray | tipo de dato", tamano,tipo)

#EXTRAER ATRIBUTOS PRINCIPALES
tamanoRGB = imgcolor.shape
tipoRGB = imgcolor.dtype
print("Tamaño RGB | Tipo RGB", tamanoRGB, tipoRGB)

#MOSTRAR IMAGENES
cv2.imshow("GRAY", imggray)
cv2.imshow("RGB", imgcolor)
cv2.imshow("IMG", img)

#CORREGIR LOS COLORES PARA QUE EL PLOT ESTE BIEN
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#PLOTEAR LA IMAGEN
plt.imshow(img)
plt.show()

#PARA QUE SE QUEDEN ABIERTAS
cv2.waitKey(0)