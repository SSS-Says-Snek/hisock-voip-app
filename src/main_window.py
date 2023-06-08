"""
This file is a part of the source code for hisock-voip-app
This project has been licensed under the MIT license.
Copyright (c) 2022-present SSS-Says-Snek
"""

from __future__ import annotations

from datetime import datetime

from hisock import HiSockClient
from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout

from src.ui.custom.message import Message
from src.ui.generated.main_ui import Ui_MainWindow


class QThreadedHiSockClient(QThread):
    new_message = pyqtSignal(str, datetime, str)
    client_join = pyqtSignal(str)
    client_leave = pyqtSignal(str)
    discriminator = pyqtSignal(int)
    online_users = pyqtSignal(list)

    def __init__(self, client: HiSockClient, name: str):
        super().__init__()

        self.client = client
        self.name = name
        self.discriminator_num = 0  # Server will send

        @self.client.on("recv_everyone_message")
        def on_recv_everyone_message(data: dict):
            if data["username"] != f"{self.name}#{self.discriminator_num}":
                time_sent = datetime.fromtimestamp(data["time_sent"])
                self.new_message.emit(data["username"], time_sent, data["message"])

        @self.client.on("client_join")
        def on_client_join(username: str):
            self.client_join.emit(username)

        @self.client.on("client_leave")
        def on_client_leave(username: str):
            self.client_leave.emit(username)

        @self.client.on("discriminator")
        def on_discriminator(discriminator: int):
            self.discriminator_num = discriminator
            self.discriminator.emit(discriminator)
        
        @self.client.on("online_users")
        def on_online_users(online_users: list):
            self.online_users.emit(online_users)

    def run(self):
        self.client.start()


class MainWindow(QMainWindow, Ui_MainWindow):
    TIME_FMT = "%I:%M %p, %m/%d/%Y"

    def __init__(self, client: HiSockClient, name: str):
        super().__init__()

        self.client = client
        self.name = name
        self.discriminator = 0  # Server will send

        # UI setup and widget overrides
        self.setupUi(self)
        self.messages = QVBoxLayout()
        self.widget.setLayout(self.messages)
        self.messages.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Signals
        self.message_to_send.returnPressed.connect(self.send_message)
        self.send_button.clicked.connect(self.send_message)

        self.scrollarea_vbar = self.message_scrollarea.verticalScrollBar()
        self.scrollarea_vbar.rangeChanged.connect(self.on_scroll_change)

        # Client thread setup
        self.client_thread = QThreadedHiSockClient(client, name)
        self.client_thread.new_message.connect(self.on_new_message)
        self.client_thread.client_join.connect(self.on_client_join)
        self.client_thread.client_leave.connect(self.on_client_leave)
        self.client_thread.discriminator.connect(self.on_discriminator)
        self.client_thread.online_users.connect(self.on_online_users)
        self.client_thread.start()

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

        self.messages.addWidget(Message("You", datetime.now().strftime(self.TIME_FMT), text))
        self.client.send("send_everyone_message", text)

        # x = self.message_scrollarea.verticalScrollBar().maximum()
        # self.message_scrollarea.verticalScrollBar().setValue(
        #     x
        # )
        # scrollarea_vbar.setValue(scrollarea_vbar.maximum())

        self.message_to_send.clear()

    def on_new_message(self, username: str, time_sent: datetime, message: str):
        time_sent_str = time_sent.strftime(self.TIME_FMT)
        self.messages.addWidget(Message(username, time_sent_str, message))

    def on_client_join(self, username: str):
        # TEMP
        time_connected = datetime.now().strftime(self.TIME_FMT)

        self.messages.addWidget(Message("[Server]", time_connected, f'New user "{username}" just joined! Say hi!'))
        self.online_users.addItem(username)

    def on_client_leave(self, username: str):
        # TEMP
        time_disconnected = datetime.now().strftime(self.TIME_FMT)

        self.messages.addWidget(Message("[Server]", time_disconnected, f'User "{username}" just left! Seeya!'))
        self.online_users.takeItem(
            self.online_users.row(self.online_users.findItems(username, Qt.MatchFlag.MatchExactly)[0])
        )

    def on_discriminator(self, discriminator: int):
        self.discriminator = discriminator

        self.messages.addWidget(
            Message(
                "[Welcome Bot]",
                datetime.now().strftime(self.TIME_FMT),
                f'Welcome to the hisock VoIP and messaging app, "{self.name}#{self.discriminator}"! yay',
            )
        )

        self.online_users.addItem(f"{self.name}#{discriminator}")

    def on_online_users(self, online_users: list[str]):
        self.online_users.addItems(online_users)