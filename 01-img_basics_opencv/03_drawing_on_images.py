import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('DATA/00-puppy.jpg')

blank_img = np.zeros(shape=(512,512,3), dtype=np.int16)

blank_img.shape
# plt.imshow(blank_img)

cv2.rectangle(blank_img, pt1=(340,0),pt2=(410,140),color=(0,255,0), thickness=10)
plt.imshow(blank_img)
# plt.show()

cv2.rectangle(blank_img, pt1=(200,200),pt2=(300,300),color=(0,255,0), thickness=10)
plt.imshow(blank_img)
# plt.show()

cv2.circle(blank_img, center=(100,100), radius=50,color=(255,0,0), thickness=8)
plt.imshow(blank_img)
# plt.show()

cv2.circle(blank_img, center=(400,400), radius=50,color=(0,255,0), thickness=-1)
plt.imshow(blank_img)
# plt.show()

cv2.line(blank_img,pt1=(0,0),pt2=(512,512),color=(102,255,255),thickness=5)
plt.imshow(blank_img)
# plt.show()

font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(blank_img, text='hi', org=(10,500),fontFace=font,fontScale=4,color=(255,255,255), thickness=3, lineType=cv2.LINE_AA)
plt.imshow(blank_img)
# plt.show()

new_blank_img = np.zeros(shape=(512,512,3), dtype=np.int32)
vertices = np.array([[100,300],[200,200],[400,300],[200,400]],dtype=np.int32)
pts = vertices.reshape((-1,1,2))

cv2.polylines(new_blank_img,[pts], isClosed=True,color=(255,0,0), thickness=4)
plt.imshow(new_blank_img)
plt.show()

