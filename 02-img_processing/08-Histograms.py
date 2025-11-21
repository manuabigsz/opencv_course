import warnings
import cv2
import numpy as np
import matplotlib.pyplot as plt

dark_horse = cv2.imread("DATA/horse.jpg")
show_horse = cv2.cvtColor(dark_horse,cv2.COLOR_BGR2RGB)

rainbow = cv2.imread("DATA/rainbow.jpg")
show_rainbow = cv2.cvtColor(rainbow,cv2.COLOR_BGR2RGB)

blue_bricks = cv2.imread("DATA/bricks.jpg")
show_bricks= cv2.cvtColor(blue_bricks,cv2.COLOR_BGR2RGB)

# plt.imshow(blue_bricks)
# plt.show()

hist_values = cv2.calcHist([blue_bricks], channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.plot(hist_values)

hist_values = cv2.calcHist([dark_horse], channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.plot(hist_values)

img = blue_bricks
color = ('b','g','r')

plt.figure(figsize=(10,5))
plt.title('Histograma – Blue Bricks')
plt.xlabel('Intensidade')
plt.ylabel('Quantidade de Pixels')

for i, col in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col, label=f'Canal {col.upper()}')

plt.xlim([0,256])
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# histogram equalization

rainbow = cv2.imread("DATA/rainbow.jpg")
show_rainbow = cv2.cvtColor(rainbow,cv2.COLOR_BGR2RGB)

img = rainbow
print(img.shape)
mask = np.zeros(img.shape[:2], np.uint8)

mask[300:400,100:400] = 255
plt.imshow(mask,cmap='gray')

masked_img = cv2.bitwise_and(img,img,mask=mask)
show_masked = cv2.bitwise_and(show_rainbow,show_rainbow,mask=mask)

hint_mask_values_red=cv2.calcHist([rainbow], channels=[2], mask=mask, histSize=[256], ranges=[0,256])
hint_values_red=cv2.calcHist([rainbow], channels=[2], mask=None, histSize=[256], ranges=[0,256])


gorilla = cv2.imread("DATA/gorilla.jpg")
show_horse = cv2.cvtColor(gorilla,0)

def display_img(img, cmap=None):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap=cmap)

display_img(gorilla)

hint_values=cv2.calcHist([gorilla], channels=[0], mask=None, histSize=[256], ranges=[0,256])

eq_gorilla = cv2.equalizeHist(gorilla)
display_img(eq_gorilla, cmap='gray')

hint_values=cv2.calcHist([eq_gorilla], channels=[0], mask=None, histSize=[256], ranges=[0,256])

color_gorilla = cv2.imread("DATA/gorilla.jpg")
show_gorilla = cv2.cvtColor(color_gorilla,cv2.COLOR_BGR2RGB)

hsv=cv2.cvtColor(color_gorilla,cv2.COLOR_BGR2HSV)

hsv[:,:,2] = cv2.equalizeHist(hsv[:,:,2])

eq_color_gorilla = cv2.cvtColor(hsv,cv2.COLOR_HSV2RGB)
