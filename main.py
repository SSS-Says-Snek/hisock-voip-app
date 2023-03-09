import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HiVoIP")
        self.resize(800, 800)

        button = QPushButton("Jarquavious will be summoned")
        button.clicked.connect(lambda: print("Hi"))
        self.setCentralWidget(button)

app = QApplication(sys.argv)
window = MainWindow()

window.show()
app.exec()