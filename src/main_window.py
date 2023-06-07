from datetime import datetime
from PyQt6 import QtGui

from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget
from PyQt6.QtCore import Qt, QThread, pyqtSignal

from hisock import HiSockClient

from src.ui.generated.main_ui import Ui_MainWindow
from src.ui.custom.message import Message


class QThreadedHiSockClient(QThread):
    new_message = pyqtSignal(str, datetime, str)
    client_connect = pyqtSignal(str)
    client_disconnect = pyqtSignal(str)

    def __init__(self, client: HiSockClient, username: str):
        super().__init__()

        self.client = client
        self.username = username

        @self.client.on("recv_everyone_message")
        def on_recv_everyone_message(data: dict):
            if data["username"] != self.username:
                time_sent = datetime.fromtimestamp(data["time_sent"])
                self.new_message.emit(data["username"], time_sent, data["message"])
        
        @self.client.on("client_connect")
        def on_client_connect(client_data):
            if client_data.name == self.username:
                return

            self.client_connect.emit(client_data.name)
        
        @self.client.on("client_disconnect")
        def on_client_disconnect(client_data):
            if client_data.name == self.username:
                return

            self.client_disconnect.emit(client_data.name)

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

        self.message_to_send.returnPressed.connect(self.send_message)
        self.send_button.clicked.connect(self.send_message)

        self.scrollarea_vbar = self.message_scrollarea.verticalScrollBar()
        self.scrollarea_vbar.rangeChanged.connect(self.on_scroll_change)
        
        # Client thread setup
        self.client_thread = QThreadedHiSockClient(client, username)
        self.client_thread.new_message.connect(self.on_new_message)
        self.client_thread.client_connect.connect(self.on_client_connect)
        self.client_thread.client_disconnect.connect(self.on_client_disconnect)
        self.client_thread.start()

        self.messages.addWidget(
            Message(
                "[Welcome Bot]",
                datetime.now().strftime(self.TIME_FMT),
                f"Welcome to the hisock VoIP and messaging app, \"{self.username}\"! yay"
            )
        )

        self.online_users.addItem("WOWWWWW")
    
    # def mousePressEvent(self, event):
    #     print("G")
    #     focused_widget = QApplication.focusWidget()
    #     print(focused_widget, type(focused_widget))
    #     if isinstance(focused_widget, QListWidget):
    #         print("W")
    #         self.online_users.clearFocus()
        
    #     super().mousePressEvent(event)

    def on_scroll_change(self):
        self.scrollarea_vbar.setValue(self.scrollarea_vbar.maximum())
    
    def send_message(self):
        text = self.message_to_send.text()
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

        self.message_to_send.clear()
    
    def on_new_message(self, username: str, time_sent: datetime, message: str):
        time_sent_str = time_sent.strftime(self.TIME_FMT)
        self.messages.addWidget(
            Message(username, time_sent_str, message)
        )
    
    def on_client_connect(self, username: str):
        # TEMP
        time_connected = datetime.now().strftime(self.TIME_FMT)

        self.messages.addWidget(
            Message("[Server]", time_connected, f"New user \"{username}\" just joined! Say hi!")
        )

    def on_client_disconnect(self, username: str):
        # TEMP
        time_disconnected = datetime.now().strftime(self.TIME_FMT)

        self.messages.addWidget(
            Message("[Server]", time_disconnected, f"User \"{username}\" just left! Seeya!")
        )