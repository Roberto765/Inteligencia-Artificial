import numpy as np
import cv2 as cv
import os

base_path = r'F:\9-Semestre\Inteligencia Artificial\Caras\persona1'
person_name = 'Jeta'  # Cambia esto para cada persona que quieras capturar
save_path = os.path.join(base_path, 'persona1')

# Verificar si la carpeta existe, si no, crearla
if not os.path.exists(save_path):
    os.makedirs(save_path)

# Cargar el clasificador de rostros
rostro = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_alt.xml')
cap = cv.VideoCapture(0)
i = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    rostros = rostro.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in rostros:
        frame2 = frame[y:y+h, x:x+w]
        frame2 = cv.resize(frame2, (100, 100), interpolation=cv.INTER_AREA)
        
        # Mostrar el rostro detectado
        cv.imshow('Rostro Detectado', frame2)
        
        # Guardar cada 5 frames (para evitar duplicados muy similares)
        if i % 5 == 0:
            filename = os.path.join(save_path, f'{person_name}_{i}.jpg')
            cv.imwrite(filename, frame2)
            print(f'Imagen guardada: {filename}')
    
    # Mostrar el video completo
    cv.imshow('Capturando Rostros', frame)
    
    i += 1
    k = cv.waitKey(1)
    if k == 27:  # ESC para salir
        break

cap.release()
cv.destroyAllWindows()