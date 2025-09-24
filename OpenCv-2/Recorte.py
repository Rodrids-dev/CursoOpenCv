import cv2
import numpy as np
import matplotlib.pyplot as plt

img =  100 * np.ones((10,10,3), np.uint8)
img2 = 100 * np.ones((10,10,3), np.uint8)

#Modificamos los pixeles que vamos a extraer
#Modificamos los pixeles de la matriz R
img[4,4,0] = 0
img[4,5,0] = 255
img[5,4,0] = 255
img[5,5,0] = 0
#Modificamos los pixeles de la matriz G
img[4,4,1] = 255
img[4,5,1] = 0
img[5,4,1] = 0
img[5,5,1] = 255
#Modificamos los pixeles de la matriz B
img[4,4,2] = 255
img[4,5,2] = 255
img[5,4,2] = 0
img[5,5,2] = 0

#Realizamos Recorte (Filas, Columnas)
recorte = img[3:7,3:7]

#Ploteamos para mostrar los dos al mismo tiempo
fig = plt.figure()
#imagen original
ImgO = fig.add_subplot(1,2,1)
ImgO.imshow(img)
ImgO.set_title("IMAGEN ORIGINAL")
#Imagen Recortada
ImgR = fig.add_subplot(1,2,2)
ImgR.imshow(recorte)
ImgR.set_title("RECORTE")

plt.show()

#Ahora con imagenes
imagen = cv2.imread("img.jpeg")

#Truco Paint
rct = imagen[35:135,75:172]

#Mostramos el recorte
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Recortada', rct)

cv2.waitKey(0)
