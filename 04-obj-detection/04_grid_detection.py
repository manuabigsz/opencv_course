import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('DATA/flat_chessboard.png')
plt.imshow(img)
plt.show()

found, corners = cv2.findChessboardCorners(img, (7,7))

cv2.drawChessboardCorners(img,(7,7),corners,found)
dots = cv2.imread('DATA/dot_grid.png')

found, corners = cv2.findCirclesGrid(dots, (10,10), cv2.CALIB_CB_SYMMETRIC_GRID)

cv2.drawChessboardCorners(dots, (10,10), corners,found)
