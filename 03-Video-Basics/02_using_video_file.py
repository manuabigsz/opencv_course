import cv2
import time
cap = cv2.VideoCapture('DATA/video_capture.mp4')

# FRAMES PER SECOND FOR VIDEO
fps = 25

if cap.isOpened()== False: 
    print("Error opening the video file. Please double check your file path for typos. Or move the movie file to the same location as this script/notebook")
    

while cap.isOpened():

    # Read the video file.
    ret, frame = cap.read()
    
    # If we got frames, show them.
    if ret == True:
        # Display the frame at same frame rate of recording
        # Watch lecture video for full explanation
        time.sleep(1/fps)
        cv2.imshow('frame',frame)
 
        # Press q to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            
            break
 
    else:
        break
        
cap.release()
# Closes all the frames
cv2.destroyAllWindows()