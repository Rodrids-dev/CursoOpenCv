import cv2
import matplotlib.pyplot as plt

#Leemos la imagen
img = cv2.imread("LEC.png")

#Realizamos la correccion de colores
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Extraemos los canales
#R = img[:,:,0]
#G = img[:,:,1]
#B = img[:,:,2]

#Tambien existe otro metodo para extraer los canales con un metodo en una sola linea
R,G,B = cv2.split(img)

#PLOTEAMOS TODOS LOS CANALES POR SEPARADO
#CREAMOS UNA "FIGURA" PARA METER TODAS LAS SUBGRAFICAS EN UNA SOLA
figura = plt.figure()
#Canal Rojo
gfc1 = figura.add_subplot(2,2,1)
gfc1.imshow(R, cmap='gray')
gfc1.set_title("CANAL ROJO")
#Canal Verde
gfc2 = figura.add_subplot(2,2,2)
gfc2.imshow(G, cmap='gray')
gfc2.set_title("CANAL VERDE")
#Canal Azul
gfc3 = figura.add_subplot(2,2,3)
gfc3.imshow(B, cmap='gray')
gfc3.set_title("CANAL AZUL")

#RECONSTUCCIÓN
imgre = cv2.merge((R,G,B)) #Volvemos a agregar los canales porque los habiamos extraido antes

#Imagen Original
gfc4 = figura.add_subplot(2,2,4)
gfc4.imshow(imgre)
gfc4.set_title("IMAGEN ORIGINAL")

plt.show()
cv2.waitKey(0)
