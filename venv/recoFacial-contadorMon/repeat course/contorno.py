import cv2
imagen=cv2.imread("contorno.jpg")
#grises=cv2.cvtcolor(imagen, cv2.COLOR_BGR2GRAY)

cv2.imshow("imagen🤑🤑",imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()