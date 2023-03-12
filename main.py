import sys

from pathlib import Path

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

from qt_material import apply_stylesheet

from src.ui.generated.main_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

app = QApplication(sys.argv)
window = MainWindow()

apply_stylesheet(app, theme='dark_cyan.xml')

with open(Path("src") / "style.qss") as f:
    style_src = f.read()
    app.setStyleSheet(app.styleSheet() + style_src)

window.show()
app.exec()