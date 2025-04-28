import cv2 as cv
import numpy as np  # Faltaba importar numpy

# Asegurar que la ruta sea válida
img = cv.imread(r'F:\9-Semestre\Inteligencia Artificial\Unidad 1\manzana.jpg')  

if img is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

# Convertir imagen a HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Definir rangos de color
ub = np.array([0, 40, 40])
ua = np.array([10, 255, 255])
ub1 = np.array([170, 40, 40])
ua1 = np.array([180, 255, 255])

# Crear máscaras para cada rango de color
mascara1 = cv.inRange(hsv, ub, ua)
mascara2 = cv.inRange(hsv, ub1, ua1)

# Unir ambas máscaras
mascara = cv.add(mascara1, mascara2)

# Aplicar la máscara a la imagen original
resultado = cv.bitwise_and(img, img, mask=mascara)

# Mostrar resultados
cv.imshow('Resultado', resultado)
cv.imshow('Imagen Original', img)
cv.imshow('Mascara', mascara)
cv.imshow('Imagen HSV', hsv)

cv.waitKey(0)  # Corrección de "waytKey"
cv.destroyAllWindows()
