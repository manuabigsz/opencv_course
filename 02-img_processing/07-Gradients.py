import warnings
import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image():
    blank_img = np.zeros((600,600))
    font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv2.putText(blank_img, text='ABCDE', org=(50,300), fontFace=font, fontScale=5, color=(255,255,255))
    return blank_img

img = cv2.imread('DATA\sudoku.jpg',0)
# plt.imshow(img)
# plt.show()

sobelx = cv2.Sobel(img, cv2.CV_64F, 1,0,ksize=5)
# plt.imshow(sobelx)
# plt.show()

sobelx = cv2.Sobel(img, cv2.CV_64F, 0,1,ksize=5)
# plt.imshow(sobelx)
# plt.show()

laplacian = cv2.Laplacian(img, cv2.CV_64F)
# plt.imshow(laplacian)
# plt.show()

blended = cv2.addWeighted(src1=sobelx, alpha=0.5, src2=sobelx, beta=0.5, gamma=0)
# plt.imshow(laplacian)
# plt.show()

ret,th1=cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
# plt.imshow(th1)
# plt.show()

kernel = np.ones((4,4), np.uint8)
gradient = cv2.morphologyEx(blended, cv2.MORPH_GRADIENT, kernel)