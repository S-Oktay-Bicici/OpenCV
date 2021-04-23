import cv2
import matplotlib.pyplot as plt
import numpy as np

# 5 morfolojik operasyon
#   Erozyon - Genişleme - Açma - Kapatma 


# resmi içe aktar
img = cv2.imread("datai_team.jpg",0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("Orijinal Img")

# erozyon
# nesnenin sınırlanı aşındırır
kernel = np.ones((5,5), dtype = np.uint8)
result = cv2.erode(img, kernel, iterations = 1)
plt.figure(), plt.imshow(result, cmap = "gray"), plt.axis("off"), plt.title("Erozyon")

# genişleme dilation 
# erozyonun tam tersi 
result2 = cv2.dilate(img, kernel, iterations = 1)
plt.figure(), plt.imshow(result2, cmap = "gray"), plt.axis("off"), plt.title("Genisleme")

#----------------------------------------------------------------------------------------

# white noise
# açılma işlmei için resme beyaz gürültü ekliyoruz 
whiteNoise = np.random.randint(0,2, size = img.shape[:2])
whiteNoise = whiteNoise*255
plt.figure(), plt.imshow(whiteNoise, cmap = "gray"), plt.axis("off"), plt.title("White Noise")

# gürültü ile resmi birleştiriyoruz 
noise_img = whiteNoise + img
plt.figure(), plt.imshow(noise_img, cmap = "gray"), plt.axis("off"), plt.title("Img w White Noise")

# açılma 
# erozyon + genişleme (gürültünün giderilmesinde faydalıdır)
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure(), plt.imshow(opening, cmap = "gray"), plt.axis("off"), plt.title("Acilma")

#----------------------------------------------------------------------------------------

# black noise
# kapatma işlemi için resme siyah gürültü ekliyoruz 
blackNoise = np.random.randint(0,2, size = img.shape[:2])
blackNoise = blackNoise*-255
plt.figure(), plt.imshow(blackNoise, cmap = "gray"), plt.axis("off"), plt.title("Black Noise")

# gürültü ile resmi birleştiriyoruz 
black_noise_img = blackNoise + img 
black_noise_img[black_noise_img <= -245] = 0
plt.figure(), plt.imshow(black_noise_img, cmap = "gray"), plt.axis("off"), plt.title("Black Noise Img")

# kapatma
# genişleme + erozyon (açmann tam tersi)
closing = cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure(), plt.imshow(opening, cmap = "gray"), plt.axis("off"), plt.title("Kapama")

#----------------------------------------------------------------------------------------

# gradient (kenar tespiti)
# bir görüntünün genişleme ve erozyon arasındaki fark 
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient, cmap = "gray"), plt.axis("off"), plt.title("Gradyan")
























