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
        # Fungsi cek_sama sama seperti sebelumnya

    def cek_file_sama(self, direktori):
        # Fungsi cek_file_sama sama seperti sebelumnya

    def check_files(self, directory):
        self.result_text.clear()
        self.result_text.append(f"Memeriksa file di: {directory}\n\n")
        self.cek_file_sama(directory)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoFileChecker()
    window.show()
    sys.exit(app.exec_())
