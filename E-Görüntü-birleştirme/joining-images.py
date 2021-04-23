import cv2
import numpy as np 

# resmi içe aktar 
img = cv2.imread("lenna.png")
cv2.imshow("Orijinal", img)

# yatay birleştirme
hor = np.hstack((img,img))
cv2.imshow("Yatay",hor)

# dikey birleştirme
ver = np.vstack((img,img))
cv2.imshow("Dikey",ver)