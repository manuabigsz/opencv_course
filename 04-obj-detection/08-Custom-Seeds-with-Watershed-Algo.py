import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

def display_img(img, cmap=None):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')
    plt.show()

# Load image in COLOR, watershed requires 3 channels
road = cv2.imread('DATA/road_image.jpg')
road_copy = road.copy()

# Marker and segment images
marker_image = np.zeros(road.shape[:2], dtype=np.int32)
segments = np.zeros(road.shape, dtype=np.uint8)

# Function to create RGB colors using tab10 colormap
def create_rgb(i):
    rgb = np.array(cm.tab10(i % 10)[:3]) * 255
    return (int(rgb[2]), int(rgb[1]), int(rgb[0])) 


# Generate random colors
colors = [create_rgb(i) for i in range(10)]

# Global variables
current_marker = 1
marks_updated = False
n_markers = 10

# Mouse callback
def mouse_callback(event, x, y, flags, param):
    global marks_updated

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(marker_image, (x, y), 10, current_marker, -1)
        cv2.circle(road_copy, (x, y), 10, colors[current_marker], -1)
        marks_updated = True

cv2.namedWindow('road image')
cv2.setMouseCallback('road image', mouse_callback)

while True:
    cv2.imshow('watershed segments', segments)
    cv2.imshow('road image', road_copy)

    k = cv2.waitKey(1)

    if k == 27:
        break
    
    elif k == ord('c'):
        road_copy = road.copy()
        marker_image = np.zeros(road.shape[:2], dtype=np.int32)
        segments = np.zeros(road.shape, dtype=np.uint8)

    elif k > 0 and chr(k).isdigit():
        current_marker = int(chr(k))

    if marks_updated:
        marker_image_copy = marker_image.copy()
        cv2.watershed(road, marker_image_copy)

        segments = np.zeros(road.shape, dtype=np.uint8)
        for color_ind in range(n_markers):
            segments[marker_image_copy == color_ind] = colors[color_ind]

        marks_updated = False

cv2.destroyAllWindows()
