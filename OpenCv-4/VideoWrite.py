import cv2

cap = cv2.VideoCapture(0)
ancho = int(cap.get(3))
alto = int(cap.get(4))

print(ancho, alto)

#cv2.VideoWriter(Nombre, Codificacion, FPS, Tamaño)
out = cv2.VideoWriter('Video.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 30, (ancho, alto))
outhsv = cv2.VideoWriter('VideoHSV.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 30, (ancho, alto))

#CREAMOS EL BUCLE PARA EL FRAME
while True:
    #Leemos los videos
    ret, frame = cap.read()

    #LO CONVIERTO A HSV PARA GUARDARLO APARTE DEL OTRO
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Guardamos los videos
    out.write(frame)
    outhsv.write(hsv)
    #Mostramos los frames
    cv2.imshow('Videocaptura', frame)
    #Cerramos con la tecla space
    t = cv2.waitKey(1)
    if t == 32:
        break

#Liberamos
cap.release()
#Cerramos ventanas
cv2.destroyAllWindows()