import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

pic = Image.open('4ded5fe5b3438f20121a6e9102b82f4e.jpg')

print(type(pic))

pic_arr = np.asarray(pic)

print(pic_arr.shape)

plt.imshow(pic_arr)

pic_red = pic_arr.copy()

# r g b
# 0 = no color value
# 255 = full color 
# each of the 3 channels has a range of these values

# 0 no red, pure black -255 full pure red
plt.imshow(pic_red[:,:,0], cmap='gray')
#plt.show()

plt.imshow(pic_red[:,:,1], cmap='gray')
#plt.show()

plt.imshow(pic_red[:,:,2], cmap='gray')
#plt.show()

#green channel 
pic_red[:,:,2] = 0

#green channel 
pic_red[:,:,2] = 0
