#IMPORTAMOS LIBRERIAS
import cv2
import numpy as np

#DEFINIMOS LOS PARAMETROS DE DETECCION DE ESQUINAS
esquinas_param = dict(maxCorners = 4,    # Maximo numero de esquinas a detectar
                      qualityLevel = 0.5,  # Umbral minimo para la deteccion de esquinas
                      minDistance = 100,    # Distacia entre pixeles
                      blockSize = 15)       # Area de pixeles

#CAPTURAMOS
cap = cv2.VideoCapture(0)

#CICLO PARA LA VIDEO CAPTURA
while True:
    #Lectura de la captura
    ret, frame = cap.read()

    #BAJAR BRILLO
    matriz = np.ones(frame.shape, dtype='uint8')*50
    frame = cv2.subtract(frame, matriz)

    #DETECCION DE ESQUINAS
    resultado = frame

    #Pasamos a edg
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Calculamos las caracteristicas de las esquinas
    esquinas = cv2.goodFeaturesToTrack(gray, **esquinas_param)

    #PREGUNTAMOS SI HAY ESQUINAS
    if esquinas is not None:
        #iteramos
        for x, y in np.float32(esquinas).reshape(-1,2):
            #Convertimos en enteros
            x, y = int(x), int(y)
            #Dibujamos la ubicación de las esquinas
            cv2.circle(resultado, (x,y), 5, (0,0,255), 1)

    #Mostramos el resultado
    cv2.imshow("Experimento", resultado)

    #Salimos si presionamos ESC
    t = cv2.waitKey(1)
    if t == 27:
        break

#Liberamos la camara
cap.release()
#CERRAMOS VENTANAS
cv2.destroyAllWindows()