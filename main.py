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

        scrollarea_vbar = self.message_scrollarea.verticalScrollBar()

        # Maybe this will be changed later so that people can view older messages while other people're talking
        scrollarea_vbar.rangeChanged.connect(lambda: scrollarea_vbar.setValue(scrollarea_vbar.maximum()))

        self.username = "SSS_Says_Snek"

        haha_messages = [
            "Wowwwww \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nn\n\n\namogus Wowwwww amogus Wowwwww amogus Wowwwww amogus Wowwwww amogus Wowwwww amogus Wowwwww amogus Wowwwww amogus Wowwwww amogus Wowwwww amogus Wowwwww amogus Wowwwww amogus Wowwwww amogus !!",
            "cool",
            "cool",
            "cool"
        ]

        for message in haha_messages:
            self.messages.addWidget(Message(self.username, message))

    
    def send_message(self):
        text = self.messageToSend.text()
        self.messages.addWidget(
            Message(self.username, text)
        )
        
        # x = self.message_scrollarea.verticalScrollBar().maximum()
        # self.message_scrollarea.verticalScrollBar().setValue(
        #     x
        # )
        # scrollarea_vbar.setValue(scrollarea_vbar.maximum())

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
