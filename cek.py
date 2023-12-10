import cv2
import numpy as np

def cek_sama(file1, file2):
    cap1 = cv2.VideoCapture(file1)
    cap2 = cv2.VideoCapture(file2)

    if not cap1.isOpened() or not cap2.isOpened():
        return False

    try:
        while True:
            ret1, frame1 = cap1.read()
            ret2, frame2 = cap2.read()

            if not ret1 or not ret2:
                break

            if frame1.shape != frame2.shape or not np.array_equal(frame1, frame2):
                return False

        return True

    finally:
        cap1.release()
        cap2.release()

if __name__ == "__main__":
    file1 = "video1.mp4"
    file2 = "video2.mp4"

    sama = cek_sama(file1, file2)

    if sama:
        print("Dua buah file video sama.")
    else:
        print("Dua buah file video tidak sama.")
