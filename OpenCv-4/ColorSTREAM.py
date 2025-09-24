import cv2
import numpy as np

#Capturamos video
cap = cv2.VideoCapture(0)

#CICLO PARA LA CAPTURA
while True:
    #Leer fotogramas
    ret, frame = cap.read()

    #CONVERSIONES
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    edg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #LE QUIERO BAJAR EL BRILLO A MI VIDEO ORIGINAL
    matriz = np.ones(frame.shape, dtype='uint8') * 40
    frame = cv2.subtract (frame, matriz)

    if ret == False:
        print('No se pudo realizar la videocaptura')
        break
    else:
        print(ret)

    #Mostramos los frames
    cv2.imshow('ORIGINAL',frame)
    cv2.imshow('HSV', hsv)
    cv2.imshow('ESCALA DE GRISES', edg)

    #CERRAMOS CON LECTURA DE TECLADO
    t = cv2.waitKey(1)
    if t == 27:
        break

#LIBERAMOS LA VIDEOCAPTURA
cap.release()
#CERRAMOS LA VENTANA
cv2.destroyAllWindows()