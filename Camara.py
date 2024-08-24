import cv2

#CREAMOS LA VIDEO CAPTURA
cap = cv2.VideoCapture(0)

#CREAMOS UN CICLO PARA EJECUTAR NUESTROS FRAMES
while True:
    # Leemos los fotogramas
    ret, frame = cap.read()

    print(ret)

    # Mostramos los frames
    cv2.imshow('VIDEO CAPTURA', frame)

    # Cerramos la lectura de teclado
    t = cv2.waitKey(1)
    if t == 32:
        break

#LIBERAMOS LA VIDEOCAPTURA
cap.release()
#CERRAMOS LA VENTANA
cv2.destroyAllWindows()