import os
import cv2
import numpy as np
import sys

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

def cek_file_sama(direktori):
    daftar_file = os.listdir(direktori)
    file_sama = []
    file_tidak_sama = False

    for i in range(len(daftar_file)):
        for j in range(i + 1, len(daftar_file)):
            file1 = os.path.join(direktori, daftar_file[i])
            file2 = os.path.join(direktori, daftar_file[j])

            if cek_sama(file1, file2):
                file_sama.append((daftar_file[i], daftar_file[j]))
            else:
                file_tidak_sama = True
                print(f"[-] File {daftar_file[i]} dan file {daftar_file[j]} tidak sama.")

    if file_sama:
        for file_pair in file_sama:
            print(f"[+] File {file_pair[0]} dan file {file_pair[1]} sama.")

    if file_tidak_sama == False and not file_sama:
        print("Semua file dalam direktori sama.")

if __name__ == "__main__":
    direktori = "nama_direktori"  # Ganti dengan nama direktori yang ingin dicek

    # Redirect output to os.devnull
    with open(os.devnull, 'w') as f:
        # Redirect stdout and stderr to os.devnull
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = f
        sys.stderr = f

        cek_file_sama(direktori)

        # Restore stdout and stderr
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        
