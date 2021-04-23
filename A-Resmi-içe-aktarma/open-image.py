import cv2

# içe aktarma
img = cv2.imread("resim1.jpg", 0)

# görselleştir
cv2.imshow("ilk Resim", img)

# belirlenen tuş ile kapatma işlemi
k = cv2.waitKey(0) &0xFF

if k == 27: # esc
    cv2.destroyAllWindows()
elif k == ord('s'): # s tuşu ile var olan resmin siyah-beyaz formatta kaydediyoruz 
    cv2.imwrite("resim1_gray.png", img)
    cv2.destroyAllWindows()
    