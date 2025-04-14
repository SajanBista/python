import cv2

# Test OpenCV installation
print("OpenCV version:", cv2.__version__)

# Access webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot access the camera")
else:
    print("Camera is working!")

# Release the camera
cap.release()
