import cv2
import matplotlib.pyplot as plt
import numpy as np

def display_img(img,cmap=None):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap)

##**TASK: Open and display the giaraffes.jpg image that is located in the DATA folder.**
giaraffes = cv2.imread("DATA/giaraffes.jpg")
show_giaraffes = cv2.cvtColor(giaraffes,cv2.COLOR_BGR2RGB)

##**TASK:Apply a binary threshold onto the image.**
giaraffes = cv2.imread("DATA/giaraffes.jpg",0)
ret,thresh1 = cv2.threshold(giaraffes,127,255,cv2.THRESH_BINARY)

##**TASK: Open the giaraffes.jpg file from the DATA folder and convert its colorspace to  HSV and display the image.**
giaraffes = cv2.imread("DATA/giaraffes.jpg")
show_giaraffes = cv2.cvtColor(giaraffes,cv2.COLOR_BGR2HSV)

##**TASK: Create a low pass filter with a 4 by 4 Kernel filled with values of 1/10 (0.01) and then use 2-D Convolution to blur the giraffer image (displayed in normal RGB)**
kernel = np.ones(shape=(4,4),dtype=np.float32)/10

giaraffes = cv2.imread("DATA/giaraffes.jpg")
giaraffes = cv2.cvtColor(giaraffes,cv2.COLOR_BGR2RGB)
dst = cv2.filter2D(giaraffes,-1,kernel)
display_img(dst)

##**TASK: Create a Horizontal Sobel Filter (sobelx from our lecture) with a kernel size of 5 to the grayscale version of the giaraffes image and then display the resulting gradient filtered version of the image.**
giaraffes = cv2.imread("DATA/giaraffes.jpg",0)
sobelx = cv2.Sobel(giaraffes,cv2.CV_64F,1,0,ksize=5)


##**TASK: Plot the color histograms for the RED, BLUE, and GREEN channel of the giaraffe image. Pay careful attention to the ordering of the channels.**
giaraffes = cv2.imread("DATA/giaraffes.jpg",0)
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([giaraffes],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.title('Giaraffes Histograms')
plt.show()
