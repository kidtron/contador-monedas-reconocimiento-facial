import cv2
import numpy as np
def ordenarpuntos(puntos):
    n_puntos=np.concatenate([puntos[0],puntos[1],puntos[2],puntos[3]]).tolist()
    yOrder = sorted(n_puntos,key=lambda n_puntos:n_puntos[1])
    x1Order = yOrder[0:2]
    x1Order = sorted(x1Order,key=lambda x1Order:x1Order[0])
    x2Order = yOrder[2:4]
    x2Order = sorted(x2Order, key=lambda x2Order:x2Order[0])
    return [x1Order[0],x1Order[1],x2Order[0],x2Order[1]]
def alineamiento(imagen,ancho,alto):
    imagenAlineada = None
    grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    tipoUmbral,umbral = cv2.threshold(grises,150,255,cv2.THRESH_BINARY)
    cv2.imshow("Umbral",umbral)
    contorno = cv2.findContours(umbral,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
    contorno = sorted(contorno, key=cv2.contourArea,reverse=True)[:1]
    for c in contorno:
        epsilon = 0.01*cv2.arcLength(c,True)
        aproximacion = cv2.approxPolyDP(c,epsilon,True)
        if len(aproximacion)==4:
            puntos = ordenarpuntos(aproximacion)
            puntoS1 = np.float32(puntos)
            puntoS2 = np.float32([[0,0],[ancho,0],[0,alto],[ancho,alto]])
            m = cv2.getPerspectiveTransform(puntoS1,puntoS2)
            imagen_alineada = cv2.warpPerspective(imagen, m, (ancho,alto))
    return imagen_alineada
capturaVideo = cv2.VideoCapture(0)

while True:
    tipoCamara,Camara = capturaVideo.read()
    if tipoCamara == False:
        break
    imagen_A6=alineamiento(Camara,ancho=480,alto=640)
    if imagen_A6 is not None:
        puntos = []
        imagen_gris = cv2.cvtColor(imagen_A6,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(imagen_gris,(5,5),1)
        _,tumbral2 = cv2.threshold(blur,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)
        cv2.imshow("Umbral",tumbral2)
        contorno2 = cv2.findContours(tumbral2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(imagen_A6,contorno2,-1,(255,0,120),3)
        suma1= 0.0
        suma2= 0.0
        suma3= 0.0
        suma4= 0.0
        for c_2 in contorno2:
            area = cv2.contourArea(c_2)
            Momentos = cv2.moments(c_2)
            if(Momentos["m00"]==0):
                Momentos["m00"]=1.0
            x = int(Momentos["m10"])/Momentos["m00"]
            y = int(Momentos["m01"])/Momentos["m00"]

            if area < 12400 and area > 11000:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_A6,"1000$",(x,y),font,0.8,(0,255,122),3)
                suma1 = suma1 + 0.100
            if area < 9800 and area > 9000:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_A6,"500$",(x,y),font,0.8,(0,255,122),3)
                suma2 = suma2 + 0.50
            if area < 8800 and area > 7800:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_A6,"200$",(x,y),font,0.8,(0,255,122),3)
                suma3 = suma3 + 0.20
            if area < 7400 and area > 6900:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_A6,"100$",(x,y),font,0.8,(0,255,122),3)
                suma4 = suma4 + 0.10
        total = suma1+suma2+suma3+suma4
        print(f"sumatoria total en pesos colombianos es: {total}")
        cv2.imshow("contador",imagen_A6)
    if cv2.waitKey(1) == ord("x"):
        break
capturaVideo.release()
cv2.destroyAllWindows()