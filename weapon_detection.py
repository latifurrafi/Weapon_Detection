import sys
import cv2
import torch
from ultralytics import YOLO
from contextlib import redirect_stdout
import os

# Silence YOLO logs
with open(os.devnull, 'w') as f, redirect_stdout(f):
    model = YOLO("/home/rafi/VSCODE/Weapon_Detection/yolov8n.pt")

# For open webcam
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        break

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
        break

camera.release()
cv2.destroyAllWindows()
