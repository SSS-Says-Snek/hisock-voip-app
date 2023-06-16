"""
This file is a part of the source code for hisock-voip-app
This project has been licensed under the MIT license.
Copyright (c) 2022-present SSS-Says-Snek
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from hisock import HiSockClient
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QLabel, QListWidget, QListWidgetItem, QMainWindow,
                             QScrollArea, QVBoxLayout, QWidget)

from src.ui.custom.message import Message
from src.ui.generated.main_ui import Ui_MainWindow


class QThreadedHiSockClient(QThread):
    everyone_message = pyqtSignal(str, datetime, str)
    client_join = pyqtSignal(str)
    client_leave = pyqtSignal(str)
    discriminator = pyqtSignal(int)
    online_users = pyqtSignal(list)
    dm_message = pyqtSignal(str, datetime, str)

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
                self.everyone_message.emit(data["username"], time_sent, data["message"])

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

        @self.client.on("recv_dm_message")
        def on_recv_dm_message(data: dict):
            time_sent = datetime.fromtimestamp(data["time_sent"])
            self.dm_message.emit(data["username"], time_sent, data["message"])

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
        self.everyone_messages = QVBoxLayout()
        self.everyone_message_widget.setLayout(self.everyone_messages)
        self.everyone_messages.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.dm_messageboxes = {}
        self.dm_message_scrollareas_idx = {}

        self.set_title_font(self.dm_selection_label, 12)
        self.set_title_font(self.dm_who_label, 16, True)

        # Signals
        self.everyone_message_to_send.returnPressed.connect(self.send_everyone_message)
        self.everyone_send_button.clicked.connect(self.send_everyone_message)

        self.dm_online_users.itemDoubleClicked.connect(self.dm_selection)
        self.dm_back_button.clicked.connect(self.dm_go_back)

        self.dm_message_to_send.returnPressed.connect(self.send_dm_message)
        self.dm_send_button.clicked.connect(self.send_dm_message)

        self.scrollarea_vbar = self.everyone_message_scrollarea.verticalScrollBar()
        self.scrollarea_vbar.rangeChanged.connect(self.scroll_change)

        # soon
        # self.users_not_read = []

        # Client thread setup
        self.client_thread = QThreadedHiSockClient(client, name)
        self.client_thread.everyone_message.connect(self.on_everyone_message)
        self.client_thread.client_join.connect(self.on_client_join)
        self.client_thread.client_leave.connect(self.on_client_leave)
        self.client_thread.discriminator.connect(self.on_discriminator)
        self.client_thread.online_users.connect(self.on_online_users)
        self.client_thread.dm_message.connect(self.on_dm_message)
        self.client_thread.start()
    
    @staticmethod
    def find_username_from_list(online_users: QListWidget, username: str):
        return online_users.row(online_users.findItems(username, Qt.MatchFlag.MatchExactly)[0])

    def remove_username_from_list(self, online_users: QListWidget, username: str):
        online_users.takeItem(self.find_username_from_list(online_users, username))

    @staticmethod
    def set_title_font(label: QLabel, size: int, bold: bool = False):
        font = QFont("Segoe UI", size)
        if bold:
            font.setBold(True)

        label.setFont(font)
    
    def send_server_message(self, messages: QVBoxLayout, message: str, time: Optional[datetime] = None):
        messages.addWidget(
            Message("[Server]", (datetime.now() if time is None else time).strftime(self.TIME_FMT), message)
        )


    def add_messagebox(self, username: str):
        dm_scrollarea_widget = QScrollArea()
        dm_messages_widget = QWidget()
        dm_messages = QVBoxLayout()
        dm_messages.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.dm_message_scrollareas.addWidget(dm_scrollarea_widget)
        dm_scrollarea_widget.setWidget(dm_messages_widget)
        dm_scrollarea_widget.setLayout(dm_messages)

        self.dm_messageboxes[username] = dm_messages
        self.dm_message_scrollareas_idx[username] = len(self.dm_message_scrollareas) - 1

        self.send_server_message(dm_messages, "Looks like there's no messages between you two yet!")

    def scroll_change(self):
        self.scrollarea_vbar.setValue(self.scrollarea_vbar.maximum())

    def send_everyone_message(self):
        text = self.everyone_message_to_send.text()
        if text == "" or text.isspace():
            return

        self.everyone_messages.addWidget(Message("You", datetime.now().strftime(self.TIME_FMT), text))
        self.client.send("send_everyone_message", text)

        self.everyone_message_to_send.clear()

    def dm_selection(self, item: QListWidgetItem):
        username = item.text()

        self.dm_states.setCurrentIndex(1)
        self.dm_message_scrollareas.setCurrentIndex(self.dm_message_scrollareas_idx[username])

        self.dm_who_label.setText(f"Talking with: {username}")
        self.set_title_font(self.dm_who_label, 16, True)

    def dm_go_back(self):
        self.dm_states.setCurrentIndex(0)

    def send_dm_message(self):
        text = self.dm_message_to_send.text()
        if text == "" or text.isspace():
            return

        recipient = self.dm_who_label.text().removeprefix("Talking with: ")
        dm_messages = self.dm_messageboxes[recipient]

        dm_messages.addWidget(Message("You", datetime.now().strftime(self.TIME_FMT), text))
        self.client.send("send_dm_message", [recipient, text])

        self.dm_message_to_send.clear()

    # CLIENT CALLBACKS

    def on_everyone_message(self, username: str, time_sent: datetime, message: str):
        time_sent_str = time_sent.strftime(self.TIME_FMT)
        self.everyone_messages.addWidget(Message(username, time_sent_str, message))

    def on_client_join(self, username: str):
        self.send_server_message(self.everyone_messages, f'New user "{username}" just joined! Say hi!')
        self.everyone_online_users.addItem(username)

        item = QListWidgetItem(username)
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dm_online_users.addItem(item)

        self.add_messagebox(username)

    def on_client_leave(self, username: str):
        self.send_server_message(self.everyone_messages, f'User "{username}" just left! Seeya!')
        self.remove_username_from_list(self.everyone_online_users, username)

        if username in self.dm_who_label.text():
            self.dm_states.setCurrentIndex(0)

        # if username not in self.users_not_read:
        if True:
            self.remove_username_from_list(self.dm_online_users, username)

            self.dm_message_scrollareas.removeWidget(
                self.dm_message_scrollareas.widget(self.dm_message_scrollareas_idx[username])
            )

            del self.dm_messageboxes[username]
            del self.dm_message_scrollareas_idx[username]
        else:
            dm_user = self.dm_online_users.findItems(username, Qt.MatchFlag.MatchExactly)[0]
            dm_user.setText(dm_user.text() + " (left)")

    def on_discriminator(self, discriminator: int):
        self.discriminator = discriminator
        self.username = f"{self.name}#{self.discriminator:04}"

        self.setWindowTitle(f"{self.windowTitle()} (Logged in as {self.username})")

        self.everyone_messages.addWidget(
            Message(
                "[Welcome Bot]",
                datetime.now().strftime(self.TIME_FMT),
                f'Welcome to the hisock VoIP and messaging app, "{self.username}"! yay',
            )
        )

    def on_dm_message(self, username: str, time_sent: datetime, message: str):
        dm_messages = self.dm_messageboxes[username]

        time_sent_str = time_sent.strftime(self.TIME_FMT)
        dm_messages.addWidget(Message(username, time_sent_str, message))

    def on_online_users(self, online_users: list[str]):
        for online_user in online_users:
            # No self for DMs (I mean, yeah)
            if online_user == self.username:
                self.everyone_online_users.addItem(f"{online_user} (YOU)")
                continue
            else:
                self.everyone_online_users.addItem(online_user)

            item = QListWidgetItem(online_user)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.dm_online_users.addItem(item)

            self.add_messagebox(online_user)
