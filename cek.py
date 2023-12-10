import os
import cv2
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QTextEdit, QWidget, QLabel, QFileDialog

class VideoFileChecker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video File Checker")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.info_label = QLabel("Pilih direktori untuk memeriksa file:")
        layout.addWidget(self.info_label)

        self.check_button = QPushButton("Pilih Direktori")
        self.check_button.clicked.connect(self.select_directory)
        layout.addWidget(self.check_button)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.central_widget.setLayout(layout)

    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Pilih Direktori")
        if directory:
            self.check_files(directory)

    def cek_sama(self, file1, file2):
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

    def cek_file_sama(self, direktori):
        daftar_file = os.listdir(direktori)
        file_sama = []
        file_tidak_sama = False

        for i in range(len(daftar_file)):
            for j in range(i + 1, len(daftar_file)):
                file1 = os.path.join(direktori, daftar_file[i])
                file2 = os.path.join(direktori, daftar_file[j])

                if self.cek_sama(file1, file2):
                    file_sama.append((daftar_file[i], daftar_file[j]))
                else:
                    file_tidak_sama = True
                    self.result_text.append(f"File [-] {daftar_file[i]} dan file {daftar_file[j]} tidak sama.")

        if file_sama:
            for file_pair in file_sama:
                self.result_text.append(f"File [+] {file_pair[0]} dan file {file_pair[1]} sama.")

        if file_tidak_sama == False and not file_sama:
            self.result_text.append("Semua file dalam direktori sama.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoFileChecker()
    window.show()
    sys.exit(app.exec_())
                        
