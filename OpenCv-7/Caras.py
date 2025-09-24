import cv2

# Cargar el clasificador preentrenado para la detección de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Capturar video desde la cámara
cap = cv2.VideoCapture(0)

while True:
    # Leer cada fotograma
    ret, frame = cap.read()

    # Convertir el fotograma a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostros en el fotograma
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Dibujar un cuadro alrededor de cada rostro detectado
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Mostrar el fotograma con los cuadros dibujados
    cv2.imshow('Rostro Detectado', frame)

    # Salir del bucle si se presiona la tecla 'Esc'
    t = cv2.waitKey(1)
    if t == 27:
        break

# Liberar la captura y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
