import cv2
import matplotlib.pyplot as plt

#Leemos y convertimos la imagen a rgb para despues pasarla a hsv
img = cv2.imread("LEC.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imghsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

#Extraer los canales
H,S,V = cv2.split(imghsv)

#Plotear los canales
fig = plt.figure()
#Canal H
fig1 = fig.add_subplot(2,2,1)
fig1.imshow(H, cmap='gray')
fig1.set_title("CANAL H")
#Canal H
fig2 = fig.add_subplot(2,2,2)
fig2.imshow(S, cmap='gray')
fig2.set_title("CANAL S")
#Canal H
fig3 = fig.add_subplot(2,2,3)
fig3.imshow(V, cmap='gray')
fig3.set_title("CANAL V")

#Reconstruccion
imgre = cv2.merge((H,S,V))

#Para la original
fig4 = fig.add_subplot(2,2,4)
fig4.imshow(img)
fig4.set_title("IMAGEN ORIGINAL")

#######################
plt.show()
cv2.waitKey(0)