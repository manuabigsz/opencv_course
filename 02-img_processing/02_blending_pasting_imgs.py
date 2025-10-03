import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('DATA/dog_backpack.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

img2 = cv2.imread('DATA/watermark_no_copy.png')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

img1 = cv2.resize(img1, (1200,1200))
img2 = cv2.resize(img2, (1200,1200))

blendeed = cv2.addWeighted(src1=img1, alpha=0.8 , src2=img2, beta=0.1, gamma=0)
# plt.imshow(blendeed)
# plt.show()

#overlay small image on top of a larger image (no blending)
#numpy reassigment
img1 = cv2.imread('DATA/dog_backpack.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

img2 = cv2.imread('DATA/watermark_no_copy.png')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

img2 = cv2.resize(img2, (600,600))

large_img = img1
small_img = img2

x_offset = 0
y_offset = 0

x_end = x_offset + small_img.shape[1]
y_end = y_offset + small_img.shape[0]

large_img[y_offset:y_end,x_offset:x_end] = small_img
plt.imshow(large_img)
plt.show()

#blend together images of different sizes


