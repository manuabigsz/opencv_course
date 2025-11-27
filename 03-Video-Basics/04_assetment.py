# **Guide**

# * Create a draw_circle function for the callback function
# * Use two events cv2.EVENT_LBUTTONDOWN and cv2.EVENT_LBUTTONUP
# * Use a boolean variable to keep track if the mouse has been clicked up and down based on the events above
# * Use a tuple to keep track of the x and y where the mouse was clicked.
# * You should be able to then draw a circle on the frame based on the x,y coordinates from the Event 

# Check out the skeleton guide below:

import cv2
import numpy as np


# Create a function based on a CV2 Event (Left button click)
def draw_circle(event,x,y,flags,param):

    global center,clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        center = (x, y)
        clicked = False
    
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

        
center = (0,0)
clicked = False

cap = cv2.VideoCapture(0) 

cv2.namedWindow('Test')

cv2.setMouseCallback('Test', draw_circle) 


while True:
    ret, frame = cap.read()

    if clicked==True:
        # Draw circle on frame
        cv2.circle(frame, center=center, radius=50, color=(255,0,0), thickness=5)
        
    # Display the resulting frame
    cv2.imshow('Test', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()