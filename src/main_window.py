"""
This file is a part of the source code for hisock-voip-app
This project has been licensed under the MIT license.
Copyright (c) 2022-present SSS-Says-Snek
"""

from __future__ import annotations

from datetime import datetime

from hisock import HiSockClient
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QListWidget, QListWidgetItem, QLabel

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
        self.username = ""

        @self.client.on("recv_everyone_message")
        def on_recv_everyone_message(data: dict):
            if data["username"] != self.username:
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
            self.username = f"{self.name}#{self.discriminator_num:04}"

            self.discriminator.emit(discriminator)

            self.client.change_name(self.username)
        
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
        self.username = ""

        # UI setup and widget overrides
        self.setupUi(self)
        self.messages = QVBoxLayout()
        self.everyone_message_widget.setLayout(self.messages)
        self.messages.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.set_title_font(self.dm_selection_label, 12)
        self.set_title_font(self.dm_who_label, 20, True)

        # Signals
        self.everyone_message_to_send.returnPressed.connect(self.send_everyone_message)
        self.everyone_send_button.clicked.connect(self.send_everyone_message)

        self.dm_online_users.itemDoubleClicked.connect(self.dm_selection)
        self.dm_back_button.clicked.connect(self.dm_go_back)

        self.dm_message_to_send.returnPressed.connect(self.send_dm_message)
        self.dm_send_button.clicked.connect(self.send_dm_message)

        self.scrollarea_vbar = self.everyone_message_scrollarea.verticalScrollBar()
        self.scrollarea_vbar.rangeChanged.connect(self.scroll_change)

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

    @staticmethod
    def remove_username_from_list(online_users: QListWidget, username: str):
        online_users.takeItem(
            online_users.row(
                online_users.findItems(username, Qt.MatchFlag.MatchExactly)[0]
            )
        )
    
    @staticmethod
    def set_title_font(label: QLabel, size: int, bold: bool = False):
        font = QFont("Segoe UI", size)
        if bold:
            font.setBold(True)
        
        label.setFont(font)

    def scroll_change(self):
        self.scrollarea_vbar.setValue(self.scrollarea_vbar.maximum())

    def send_everyone_message(self):
        text = self.everyone_message_to_send.text()
        if text == "" or text.isspace():
            return

        self.messages.addWidget(Message("You", datetime.now().strftime(self.TIME_FMT), text))
        self.client.send("send_everyone_message", text)

        self.everyone_message_to_send.clear()
    
    def dm_selection(self, item: QListWidgetItem):
        self.dm_states.setCurrentIndex(1)

        self.dm_who_label.setText(f"Talking with: {item.text()}")
        self.set_title_font(self.dm_who_label, 20, True)
    
    def dm_go_back(self):
        self.dm_states.setCurrentIndex(0)
    
    def send_dm_message(self):
        pass
    
    # CLIENT CALLBACKS

    def on_new_message(self, username: str, time_sent: datetime, message: str):
        time_sent_str = time_sent.strftime(self.TIME_FMT)
        self.messages.addWidget(Message(username, time_sent_str, message))

    def on_client_join(self, username: str):
        # TEMP
        time_connected = datetime.now().strftime(self.TIME_FMT)

        self.messages.addWidget(Message("[Server]", time_connected, f'New user "{username}" just joined! Say hi!'))
    
        self.everyone_online_users.addItem(username)

        item = QListWidgetItem(username)
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dm_online_users.addItem(item)

    def on_client_leave(self, username: str):
        # TEMP
        time_disconnected = datetime.now().strftime(self.TIME_FMT)

        self.messages.addWidget(Message("[Server]", time_disconnected, f'User "{username}" just left! Seeya!'))

        self.remove_username_from_list(self.everyone_online_users, username)
        self.remove_username_from_list(self.dm_online_users, username)

    def on_discriminator(self, discriminator: int):
        self.discriminator = discriminator
        self.username = f"{self.name}#{self.discriminator:04}"

        self.messages.addWidget(
            Message(
                "[Welcome Bot]",
                datetime.now().strftime(self.TIME_FMT),
                f'Welcome to the hisock VoIP and messaging app, "{self.username}"! yay',
            )
        )

    def on_online_users(self, online_users: list[str]):
        self.everyone_online_users.addItems(online_users)

        for online_user in online_users:
            item = QListWidgetItem(online_user)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.dm_online_users.addItem(item)