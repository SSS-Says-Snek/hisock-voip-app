import sys

from pathlib import Path

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

from qt_material import apply_stylesheet

from src.ui.generated.main_ui import Ui_MainWindow
from src.ui.custom.message import Message


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.messageToSend.returnPressed.connect(self.send_message)
        self.sendButton.clicked.connect(self.send_message)

        haha_messages = [
            Message("SSS_Says_Snek", "Wowwwww \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nn\n\n\namogus Wowwwww amogus Wowwwww amogus Wowwwww amogus Wowwwww amogus Wowwwww amogus Wowwwww amogus Wowwwww amogus Wowwwww amogus Wowwwww amogus Wowwwww amogus Wowwwww amogus Wowwwww amogus !!"),
            Message("SSS_Says_Snek", "cool"),
            Message("SSS_Says_Snek", "cool"),
            Message("SSS_Says_Snek", "cool"),
            Message("SSS_Says_Snek", "cool")
        ]

        for message in haha_messages:
            self.messages.addWidget(message)

    
    def send_message(self):
        self.messageToSend.clear()


def load_stylesheet(name: str):
    with open(Path("src") / "styles" / name) as f:
        style_src = f.read()
        app.setStyleSheet(app.styleSheet() + style_src)


app = QApplication(sys.argv)
window = MainWindow()

apply_stylesheet(app, theme='dark_cyan.xml')

load_stylesheet("override.qss")
load_stylesheet("main.qss")

window.show()
app.exec()
