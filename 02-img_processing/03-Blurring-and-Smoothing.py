import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = cv2.imread('DATA/dog_backpack.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

img2 = cv2.imread('DATA/watermark_no_copy.png')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

#blend together images of different sizes

img2 = cv2.resize(img2, (600,600))

x_offset = 934 - 600
y_offset = 1401 - 600

rows,cols,channels = img2.shape

rol = img1[y_offset:1401, x_offset:934]
# plt.imshow(rol)
# plt.show()

img2gray = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

#invert
mask_inv = cv2.bitwise_not(img2gray)

white_background = np.full(img2.shape,255,dtype=np.uint8)
bk = cv2.bitwise_or(white_background,white_background,mask=mask_inv)
# plt.imshow(bk)
# plt.show()

fg = cv2.bitwise_or(img2,img2,mask=mask_inv)
# plt.imshow(fg)

final_rol = cv2.bitwise_or(rol,fg)

large_img = img1
small_img = final_rol

large_img[y_offset:y_offset+small_img.shape[0],x_offset:x_offset+small_img.shape[1]] = small_img
plt.imshow(large_img)
plt.show()





