import os
import random
import time
import cv2
import numpy as np
from PIL import ImageGrab

base_path = os.path.dirname(os.path.abspath(__file__))
output_video_path = os.path.join(base_path, 'movie.mp4')

recording = False
frame_size = (1920, 1080)

def start_recording(duration=10, frame_rate=1.0):
    global recording
    recording = True
    total_frames = int(duration * frame_rate)
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_video_path, fourcc, frame_rate, frame_size)

    print(f"Recording started: {total_frames} frames will be captured.")
    
    for i in range(total_frames):
        if not recording:
            break
        screen = ImageGrab.grab(bbox=(0, 0, frame_size[0], frame_size[1]))
        frame = np.array(screen)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        video_writer.write(frame)
        print(f"Captured frame {i+1}")

        time.sleep(1 / frame_rate)

    video_writer.release()
    print("Recording stopped and video saved.")
    print(f"Video is saved at {output_video_path}")

def stop_recording():
    global recording
    recording = False


def take_screenshot():
    image_path = os.path.join(base_path, f"screenshot_{random.randint(1, 100000)}.jpg")
    screen = ImageGrab.grab()
    screen.save(image_path)
    print(f"Screenshot saved at {image_path}")