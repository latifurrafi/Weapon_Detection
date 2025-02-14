import sys
import cv2
import torch
from ultralytics import YOLO
from contextlib import redirect_stdout
import os

# Silence YOLO logs
with open(os.devnull, 'w') as f, redirect_stdout(f):
    model = YOLO("/home/rafi/VSCODE/Weapon_Detection/yolov8n.pt")

<<<<<<< HEAD
# For open webcam
=======
sound_file = "alert_sound.wav"

# Check if the file exists
if os.path.exists(sound_file):
    alert_sound = pygame.mixer.Sound(sound_file)
else:
    print("Error: Sound file not found!")

gun_cascade = cv2.CascadeClassifier('cascade.xml')

>>>>>>> d4c8a8d55aae31bca6c12de3b8716828dd96fa24
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        break

<<<<<<< HEAD
    # Run YOLO detection
    results = model(frame)

    gun_detected = False
    for result in results:
        for box in result.boxes:
            confidence = box.conf[0].item()
            class_id = int(box.cls[0].item())

            if class_id == 0 and confidence > 0.8:
                gun_detected = True

    if gun_detected:
        print("⚠️ Gun detected!")  # Only prints when a gun is detected

    cv2.imshow("Gun Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
=======
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gun_exist = False  

    guns = gun_cascade.detectMultiScale(gray, 1.3, 20, minSize=(100, 100))

    if len(guns) > 0:
        gun_exist = True

    for (x, y, w, h) in guns:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Red color for visibility

    # Add timestamp on display
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S %p"),
                (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.35, (0, 0, 255), 1)

    # Show detection status
    if gun_exist:
        print("Guns detected")
        alert_sound.play()
        cv2.imshow("Guns detected", frame)
    else:
        cv2.imshow("Security Feed", frame)


    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # Exit on 'q' press
>>>>>>> d4c8a8d55aae31bca6c12de3b8716828dd96fa24
        break

camera.release()
cv2.destroyAllWindows()
