import cv2

#Creamos la Captura
cap = cv2.VideoCapture('Video.avi')

#CREAMOS UN CICLO PARA EJECUTAR EL VIDEO
while True:
    #Leemos los fotogramas
    ret, frame = cap.read()
    #Exitoso
    if ret == False:
        print('No se pudo we')
        break
    else :
        print('Exitoso como tu futuro mamón')
    #Mostramos
    cv2.imshow('Video Captura',frame)
    #Cerramos con teclado (esc)
    t = cv2.waitKey(1)
    if t == 27:
        break

#Liberamos la captura
cap.release()
#Cerramos ventanas
cv2.destroyAllWindows()