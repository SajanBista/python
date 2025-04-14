import cv2
import dlib

# Load pre-trained face detector and landmark predictor from dlib
face_detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Start the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_detector(gray)

    for face in faces:
        # Predict landmarks on the detected face
        landmarks = landmark_predictor(gray, face)
        
        # Loop through each of the 68 landmarks
        for n in range(0, 68):  # 68 landmarks in total
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            
            # Draw a small circle (dot) on each landmark
            cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)

    # Show the frame with landmarks
    cv2.imshow("Face Landmark Detection", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()