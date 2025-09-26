import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('DATA/00-puppy.jpg')

print(img)
print(img.shape)

# plt.imshow(img)
# plt.show()

# matplotlib --> expect rgb
# opencv -:> expect bgr
fix_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(fix_img)
# plt.show()

img_gray = cv2.imread('DATA/00-puppy.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(img_gray, cmap='gray')
# plt.show()

new_img = cv2.resize(fix_img, (1000,400))
plt.imshow(new_img)
# plt.show()

w_ratio = 0.8
h_ratio = 0.3

new_imag_ratio = cv2.resize(fix_img,(0,0), fix_img,w_ratio, h_ratio)
plt.imshow(new_imag_ratio)
# plt.show()


img_flip = cv2.flip(fix_img, 0)
plt.imshow(img_flip)
# plt.show()

print(type(fix_img))

cv2.imwrite('new.jpg', fix_img)

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
ax.imshow(fix_img)
plt.show()