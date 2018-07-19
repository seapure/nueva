import cv2
import os
os.chdir('C:/users/user/downloads')
image = cv2.imread("landscape.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Landscape", image)
cv2.imshow("landscape - gray", gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()