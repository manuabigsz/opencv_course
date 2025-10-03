import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('DATA/rainbow.jpg')

img = cv2.imread('/DATA/rainbow.jpg',0)


## Different Threshold Types

#binary
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
plt.imshow(thresh1,cmap='gray')
plt.show()


#inverse
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
plt.imshow(thresh2,cmap='gray')

#truncation
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
plt.imshow(thresh3,cmap='gray')

#threshold to zero
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
plt.imshow(thresh4,cmap='gray')

#treshold to zero invert
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
plt.imshow(thresh5,cmap='gray')

# Real World Applications
## Adaptive Thresholding
### Sudoku Image

img = cv2.imread("/DATA/crossword.jpg",0)
def show_pic(img):
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')

show_pic(img)

## Simple Binary
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
show_pic(th1)


### Adaptive Threshold

# https://stackoverflow.com/questions/28763419/adaptive-threshold-parameters-confusion

#     @param src Source 8-bit single-channel image.
#     .   @param dst Destination image of the same size and the same type as src.
#     .   @param maxValue Non-zero value assigned to the pixels for which the condition is satisfied
#     .   @param adaptiveMethod Adaptive thresholding algorithm to use, see #AdaptiveThresholdTypes.
#     .   The #BORDER_REPLICATE | #BORDER_ISOLATED is used to process boundaries.
#     .   @param thresholdType Thresholding type that must be either #THRESH_BINARY or #THRESH_BINARY_INV,
#     .   see #ThresholdTypes.
#     .   @param blockSize Size of a pixel neighborhood that is used to calculate a threshold value for the
#     .   pixel: 3, 5, 7, and so on.
#     .   @param C Constant subtracted from the mean or weighted mean (see the details below). Normally, it
#     .   is positive but may be zero or negative as well.

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8) # Play around with these last 2 numbers
show_pic(th2)

th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,15,8)
show_pic(th3)

blended = cv2.addWeighted(src1=th1,alpha=0.7,src2=th2,beta=0.3,gamma=0)
show_pic(blended)