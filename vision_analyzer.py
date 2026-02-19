import cv2
import time
import os

# ---------------------------------------------------------
# Function: analyze_interview_presence
# Uses a stable path for face detection and adds a warm-up delay
# ---------------------------------------------------------
def analyze_interview_presence():
    """
    Opens the webcam, waits for focus, and detects a face.
    This version fixes the 'Assertion failed' error.
    """
    print("[Vision] Initializing camera...")
    
    # 1. Load the detection data using the built-in OpenCV path
    # This ensures the file is found regardless of your computer's setup
    xml_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(xml_path)

    if face_cascade.empty():
        return 0.0, "Internal Error: Could not load detection data."

    # 2. Open the camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return 0.0, "Webcam not found."

    # --- CRITICAL: Wait 2 seconds for camera light/focus adjustment ---
    time.sleep(2) 
    
    ret, frame = cap.read()
    if not ret:
        cap.release()
        return 0.0, "Capture failed."

    print("[Vision] Scanning for face...")
    
    # 3. Process the image in Grayscale (Black & White)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 4. Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        score = 9.5
        message = "Professional presence detected."
    else:
        score = 2.0
        message = "Face not clearly visible. Ensure you are in a well-lit room."

    cap.release()
    return score, message