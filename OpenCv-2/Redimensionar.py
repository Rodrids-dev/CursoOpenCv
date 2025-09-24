import cv2

img = cv2.imread("img.jpeg")

#PARA REDIMENSIONAR SE OCUPA:
#red = cv2.resize(imagen, (si queremos un tamaño especifico de salida), fx, fy, interpolation)

#Redimensionamiento 1
red1 = cv2.resize(img, None, fx=2.5, fy=2.5)

#Redimensionamiento 2 (Por Área)
red2 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

#Redimencionamiento 3 (Cubico)
red3 = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

#Redimensionamiento 4 (Especificando el tamaño)
ancho = 700
alto = 350
med = (ancho, alto)

red4 = cv2.resize(img, med, interpolation=cv2.INTER_CUBIC)

#GUARDAMOS LAS IMAGENES
cv2.imshow("original", img)
cv2.imshow("Primera", red1)
cv2.imshow("Segunda_con_0.5_de_Area", red2)
cv2.imshow("tercera_con_1.5_cubica", red3)
cv2.imshow("cuarta_con_ancho_y_alto_cubica", red4)

cv2.waitKey(0)