import numpy as np
import matplotlib.pyplot as plt
import cv2

#### TASK: Open the *dog_backpack.jpg* image from the DATA folder and display it in the notebook. Make sure to correct for the RGB order.
img = cv2.imread('DATA/dog_backpack.jpg')
plt.imshow(img)
# plt.show()

fix_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(fix_img)
# plt.show()

#### TASK: Flip the image upside down and display it in the notebook.
img_flip = cv2.flip(fix_img, 0)
plt.imshow(img_flip)
# plt.show()

#### TASK: Draw an empty RED rectangle around the dogs face and display the image in the notebook.
# cv2.rectangle(fix_img, pt1=(600,370),pt2=(200,720),color=(255,0,0), thickness=10)
plt.imshow(fix_img)
# plt.show()

#### TASK: Draw a BLUE TRIANGLE in the middle of the image. The size and angle is up to you, but it should be a triangle (three sides) in any orientation.
vertices = np.array([[400,400],[200,700],[600,700]],dtype=np.int32)
pts = vertices.reshape((-1,1,2))
# cv2.polylines(fix_img,[pts], isClosed=True,color=(0,0,255), thickness=8)
# plt.imshow(fix_img)
# plt.show()

### BONUS TASK. Can you figure our how to fill in this triangle? It requires a different function that we didn't show in the lecture! See if you can use google search to find it.
## [CLICK ME FOR A DIRECT LINK TO THE HINT](https://docs.opencv.org/3.0-beta/modules/imgproc/doc/drawing_functions.html#fillpoly)
vertices = np.array([[400,400],[200,700],[600,700]],dtype=np.int32)
pts = vertices.reshape((-1,1,2))
cv2.fillPoly(fix_img, [pts], color=(0,0,255))

plt.imshow(fix_img)
plt.axis("off")
plt.show()


#### TASK: (NOTE: YOU WILL NEED TO RUN THIS AS A SCRIPT). Create a script that opens the picture and allows you to draw empty red circles whever you click the RIGHT MOUSE BUTTON DOWN.