#REPRESENTACION DE IMAGEN POR DATOS, EN ESCALA DE GRISES.
import cv2
import numpy as np
import matplotlib.pyplot as plt

#CREAR UNA IMAGEN NEGRA
img = np.zeros((10,10,1), np.uint8) #CREA UNA MATRIZ DE CEROS DE 10X10 (EL 0 ES NEGRO)

#Cambiamos algunos pixeles
img[0,0]=30
img[1,1]=50
img[2,2]=70
img[3,3]=90
img[4,4]=110
img[5,5]=130
img[6,6]=150
img[7,7]=170
img[8,8]=190
img[9,9]=210

print(img)

#PARA MOSTRAR LA IMAGEN
plt.imshow(img, cmap='gray')
plt.show()