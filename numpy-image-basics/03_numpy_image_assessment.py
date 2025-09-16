import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

## **TASK: Create a 5 by 5 array where every number is a 10**
arr = np.full((5,5),10)
print(arr)

## **TASK: Run the cell below to create an array of random numbers and see if you can figure out how it works.**

# This line sets a "seed" so you get the same random numbers we do
np.random.seed(101)
# This line creates an array of random numbers
arr = np.random.randint(low=0,high=100,size=(5,5))

print("arr", arr)

print(arr.max())
print(arr.min())

## **TASK: Use PIL and matplotlib to read and display the ../DATA/00-puppy.jpg image.**

pic = Image.open('DATA/00-puppy.jpg')
#plt.imshow(pic)
#plt.show()

## **TASK: Convert the image to a NumPy Array**
pic_arr = np.asarray(pic)
print(pic_arr.shape)

## **FINAL TASK: Use slicing to set the RED and GREEN channels of the picture to 0, then use imshow() to show the isolated blue channel**
pic_blue = pic_arr.copy()
pic_blue[:,:,0] = 0
pic_blue[:,:,1] = 0
plt.imshow(pic_blue, cmap='gray')
plt.show()