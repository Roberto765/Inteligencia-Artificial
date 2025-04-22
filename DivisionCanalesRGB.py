import cv2 as cv
import numpy as np

img = cv.imread("F:/9-Semestre/Inteligencia Artificial/Unidad 1/canalRGB.jpg")

# Crear una imagen en negro (cero) para los canales que no vamos a usar
imgn = np.zeros(img.shape[:2], np.uint8)

# Dividir la imagen en sus canales BGR
b, g, r = cv.split(img)

# Convertir la imagen a otros modelos de color
img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # Cambio a RGB
img3 = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # Cambio a HSV

# Crear imágenes solo con un canal
imgb = cv.merge([b, imgn, imgn])  # Solo canal azul
imgg = cv.merge([imgn, g, imgn])  # Solo canal verde
imgr = cv.merge([imgn, imgn, r])  # Solo canal rojo

# Cambiar el orden de los canales RGB a BRG
gbr = cv.merge([g, b, r])

# Guardar una imagen de prueba
cv.imwrite('imagen_resultado.jpg', img)

# Mostrar las imágenes resultantes
cv.imshow('Canal Azul', b)
cv.imshow('Canal Verde', g)
cv.imshow('Canal Rojo', r)
cv.imshow('Imagen Original', img)
cv.imshow('Imagen RGB', img2)
cv.imshow('Imagen HSV', img3)
cv.imshow('Imagen en Negativo', imgn)
cv.imshow('Imagen Azul', imgb)
cv.imshow('Imagen Verde', imgg)
cv.imshow('Imagen Roja', imgr)
cv.imshow('Imagen BRG', gbr)

cv.waitKey(0)  # Esperar hasta que se presione una tecla
cv.destroyAllWindows()  # Cerrar todas las ventanas de OpenCV
