from datetime import datetime

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt, QThread, pyqtSignal

from hisock import HiSockClient

from src.ui.generated.main_ui import Ui_MainWindow
from src.ui.custom.message import Message


class QThreadedHiSockClient(QThread):
    new_message = pyqtSignal(str, datetime, str)

    def __init__(self, client: HiSockClient, username: str):
        super().__init__()

        self.client = client
        self.username = username

        @self.client.on("recv_everyone_message")
        def on_recv_everyone_message(data: dict):
            if data["username"] != self.username:
                time_sent = datetime.fromtimestamp(data["time_sent"])
                self.new_message.emit(data["username"], time_sent, data["message"])

    def run(self):
        self.client.start()


class MainWindow(QMainWindow, Ui_MainWindow):
    TIME_FMT = "%I:%M %p, %m/%d/%Y"

    def __init__(self, client: HiSockClient, username: str):
        super().__init__()

        self.client = client
        self.username = username

        self.setupUi(self)
        self.messages.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.messageToSend.returnPressed.connect(self.send_message)
        self.sendButton.clicked.connect(self.send_message)

        self.scrollarea_vbar = self.message_scrollarea.verticalScrollBar()
        self.scrollarea_vbar.rangeChanged.connect(self.on_scroll_change)
        
        # Client thread setup
        self.client_thread = QThreadedHiSockClient(client, username)
        self.client_thread.new_message.connect(self.on_new_message)
        self.client_thread.start()

        self.messages.addWidget(
            Message(
                "[Welcome Bot]",
                datetime.now().strftime(self.TIME_FMT),
                "Welcome to the hisock VoIP and messaging app! yay"
            )
        )

    def on_scroll_change(self):
        self.scrollarea_vbar.setValue(self.scrollarea_vbar.maximum())
    
    def send_message(self):
        text = self.messageToSend.text()
        if text == "" or text.isspace():
            return

        self.messages.addWidget(
            Message("You", datetime.now().strftime(self.TIME_FMT), text)
        )
        self.client.send("send_everyone_message", text)
        
        # x = self.message_scrollarea.verticalScrollBar().maximum()
        # self.message_scrollarea.verticalScrollBar().setValue(
        #     x
        # )
        # scrollarea_vbar.setValue(scrollarea_vbar.maximum())

        self.messageToSend.clear()
    
    def on_new_message(self, username: str, time_sent: datetime, message: str):
        time_sent_str = time_sent.strftime(self.TIME_FMT)
        self.messages.addWidget(
            Message(username, time_sent_str, message)
        )