"""
Get frames from a video at set intervals and save them as images.
"""

import cv2
import os

videos_folder = "videos"
videos = os.listdir(videos_folder)
output_dir = "src/frames"
os.makedirs(output_dir, exist_ok=True)

count = 0
for video in videos:
    vidcap = cv2.VideoCapture(f"{videos_folder}/{video}")
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    interval = 0.5  # in seconds
    frame_interval = int(fps * interval)

    success, image = vidcap.read()
    while success:
        if count % frame_interval == 0:
            cv2.imwrite(os.path.join(output_dir, f"frame_{count}.jpg"), image)
        success, image = vidcap.read()
        count += 1

    vidcap.release()
    cv2.destroyAllWindows()
