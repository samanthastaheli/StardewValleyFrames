"""
Get frames from a video at set intervals and save them as images.
"""

import cv2
import os

VIDEOS_FOLDER = "videos"
OUTPUT_DIR = "frames"

def get_label(video_name):
    label = video_name.split("_")[0]
    label = label.replace(".mp4", "")
    return label

def get_frames(video, label):
    count = 0
    vidcap = cv2.VideoCapture(f"{VIDEOS_FOLDER}/{video}")
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    interval = 0.5  # in seconds
    frame_interval = int(fps * interval)

    os.makedirs(f"{OUTPUT_DIR}/{label}", exist_ok=True)

    success, image = vidcap.read()
    while success:
        if count % frame_interval == 0:
            cv2.imwrite(os.path.join(f"{OUTPUT_DIR}/{label}", f"{label}_{count}.jpg"), image)
        success, image = vidcap.read()
        count += 1

    vidcap.release()
    cv2.destroyAllWindows()

def main():
    videos = os.listdir(VIDEOS_FOLDER)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for video in videos:
        label = get_label(video)
        get_frames(video, label)

if __name__ == "__main__":
    main()