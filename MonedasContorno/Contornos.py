from cv2 import cv2
#leer la imagen, tiene que estar en la misma carpeta
imagen=cv2.imread('contorno.jpg')
#Imagen a escala de grises
grises=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

#esto devuelve 2 valores y se recogen asi (el primero no lo queremos)
#nos saca el umbral sino no se pueden reconocer las imagenes
_,umbral=cv2.threshold(grises,100,255,cv2.THRESH_BINARY)
#detecta los puntos de los contornos y los dibuja
contorno,jerarquía = cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen,contorno,-1,(251, 63, 52),3)

#Mostrar
cv2.imshow('Imagen original',imagen)
#cv2.imshow('Imagen en grises',grises)
#cv2.imshow('Imagen Umbral',umbral)

#para que no cierre la ventana emergente (0 foto 1 videos)
cv2.waitKey(0)
cv2.destroyAllWindows()