import cv2 as cv
capturaCamara = cv.VideoCapture(0)
if not capturaCamara.isOpened:
    print("no se ha encontrado una camara")
    exit()
while True:
    tipoCamara,camara = capturaCamara.read()
    grises=cv.cvtColor(camara, cv.COLOR_BGR2GRAY)

    cv.imshow("camara",camara)
    if cv.waitKey(1)== ord("x"):
        break
capturaCamara.release()
cv.destroyAllWindows()