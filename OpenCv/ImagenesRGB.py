#CREAR IMAGENES CON RGB
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = 255 * np.ones((10,10,3), np.uint8)

R = img[:,:,0] #Decimos que R(RED), SON ODOS LOS PIXELES DE ANCHOxALTO DE LA MATRIZ CERO
G = img[:,:,1] #Todos los pixeles anchoXalto de la matriz 1 es Green
B = img[:,:,2] #Todos los pixeles de anchoXalto de la matriz dos son Blue

#Entonces hasta aquí ya tenemos nuestras tres matrices de 10x10

#MODIFICAMOS LA MATRIZ
B[:,:] = 100
R[:,:] = 255
G[:,:] = 100

#MODIFICAMOS LA IMAGEN
img[:,:,0] = R
img[:,:,1] = G
img[:,:,2] = B

plt.imshow(img)
plt.show()
