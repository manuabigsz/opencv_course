import cv2
import matplotlib.pyplot as plt
import numpy as np

def display_img(img,cmap=None):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')
    plt.show()



sep_coins = cv2.imread('DATA/pennies.jpg', 0)

# median blur
# grayscale
# binary treshold and find countours


sep_blur = cv2.medianBlur(sep_coins, 25)

gray_sep_coins = sep_blur

ret, sep_tresh = cv2.threshold(gray_sep_coins, 160, 255, cv2.THRESH_BINARY_INV)
display_img(sep_tresh)


image,contours, hierarchy = cv2.findContours(sep_tresh.copy(),cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(sep_coins, contours, i, (255,0,0))

img = cv2.imread('DATA/pennies.jpg')
img = cv2.medianBlur(img,35)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, tresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# noise removal

kernel = np.ones((3,3), np.uint8)

opening = cv2.morphologyEx(tresh, cv2.MORPH_OPEN, kernel, iterations=2)

dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2,5)

sure_bg = cv2.dilate(opening,kernel,iterations=3)

ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(),255,0)

sure_fg = np.uint8(sure_fg)
unknow = cv2.subtract(sure_bg, sure_fg)

ret, markers = cv2.connectedComponents(sure_fg)
markers = markers +1
markers[unknow==255] = 0

markers = cv2.watershed(img, markers)

display_img(markers)

image,contours, hierarchy = cv2.findContours(sep_tresh.copy(),cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(sep_coins, contours, i, (255,0,0))

display_img(sep_coins)