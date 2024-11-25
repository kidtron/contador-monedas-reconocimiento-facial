import cv2
path = r'C:\Users\kidtr\Downloads\2OpenCV\venv\recoFacial-contadorMon\monedascontorno\contorno.jpg'
imagen = cv2.imread(path)
grises = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
_,umbral = cv2.threshold(grises,100,255,cv2.THRESH_BINARY)
contorno,jerarquia = cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imagen,contorno,-1,(76, 22, 108),4)
#mostrar
cv2.imshow('imagen original',grises)
cv2.waitKey(0)
cv2.destroyAllWindows()