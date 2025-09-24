import cv2

img = cv2.imread("novena.jpg")

#PARA DIBUJAR UNA LINEA SE USA EL COMANDO:
#linea = cv2.line(imagen, P1(x,y), P2(x2,y2), color, grosor(thikness), tipoLinea)
linea = cv2.line(img, (11,706), (466,706), (220,0,0), thickness=3, lineType=cv2.LINE_AA)

#CIRCULO:
#circulo = cv2.circle(imagen, centro, radio, color, grosor, tipo)
circulo = cv2.circle(img, (252,72), 60, (255,0,0), thickness=2, lineType=cv2.LINE_AA)

#RECTANGULO
rectangulo = cv2.rectangle(img, (200,472), (297,658), (0,0,255), thickness=2, lineType=cv2.LINE_AA)

#TEXTO
#texto = cv2.putText(img, texto, P(x,y), tipoLetra, tamLetra, color, grosor, tipoLinea)
txt = "La Novena"
tipoL = cv2.FONT_ITALIC
tamL = 0.8
color = (220,0,0)
grosor = 2
pt = (180,683)
texto = cv2.putText(img, txt, pt, tipoL, tamL, color, grosor, lineType=cv2.LINE_AA)

cv2.imshow("LA NOVENA", img)
cv2.waitKey(0)