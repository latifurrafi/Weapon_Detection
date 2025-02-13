import numpy as np
import cv2
import imutils
import datetime
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Path to your alert sound file
sound_file = "alert_sound.wav"  # Replace with your actual file path

# Check if the file exists
if os.path.exists(sound_file):
    alert_sound = pygame.mixer.Sound(sound_file)
else:
    print("Error: Sound file not found!")

# Load gun cascade
gun_cascade = cv2.CascadeClassifier('cascade.xml')

# Open camera
camera = cv2.VideoCapture(0)
firstFrame = None

while True:
    ret, frame = camera.read()
    if frame is None:
        break

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Reset gun detection flag
    gun_exist = False  

    # Detect guns
    guns = gun_cascade.detectMultiScale(gray, 1.3, 20, minSize=(100, 100))

    if len(guns) > 0:
        gun_exist = True  # Set to True only if gun is detected

    # Draw rectangles if guns are found
    for (x, y, w, h) in guns:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Red color for visibility

    # Add timestamp
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S %p"),
                (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.35, (0, 0, 255), 1)

    # Show detection status
    if gun_exist:
        print("Guns detected")
        alert_sound.play()  # Play the alert sound
        cv2.imshow("Guns detected", frame)
    else:
        cv2.imshow("Security Feed", frame)


    # Exit on 'q' press
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# Release resources
camera.release()
cv2.destroyAllWindows()
