"""
This file is a part of the source code for hisock-voip-app
This project has been licensed under the MIT license.
Copyright (c) 2022-present SSS-Says-Snek
"""

from __future__ import annotations

import os
import time

from datetime import datetime
from functools import partial
from typing import Optional

import cv2 as cv
import numpy as np
from hisock import HiSockClient
from PyQt6.QtCore import QPoint, Qt, QThread
from PyQt6.QtGui import QFont, QImage, QMouseEvent, QPixmap
from PyQt6.QtWidgets import (QLabel, QListWidget, QListWidgetItem,
                             QMainWindow, QScrollArea, QScrollBar, QVBoxLayout,
                             QWidget)

from src.threads.qthreadedclient import QThreadedHiSockClient
from src.threads.videocap import VideoCapWorker
from src.threads.audio import AudioReadWorker, AudioWriteWorker

from src.ui.custom.dm_list_item import DMListItem
from src.ui.custom.message import Message
from src.ui.custom.notification import (AcknowledgeNotif, IncomingCallNotif,
                                        Notif)
from src.ui.generated.main_ui import Ui_MainWindow


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
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.everyone_messages = QVBoxLayout(self.everyone_message_widget)
        self.everyone_message_widget.setLayout(self.everyone_messages)
        self.everyone_messages.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.everyone_messages.setSizeConstraint(QVBoxLayout.SizeConstraint.SetMinAndMaxSize)

        # Notifications
        self.notif: Optional[Notif] = None
        self.calling = False
        self.close_mode = "normal"
        self.threads_stopped = 0  # Video cap, Audio read, Audio write

        # Client thread setup
        self.client_thread = QThreadedHiSockClient(client, name)
        self.client_thread_dict = {
            self.client_thread.everyone_message: self.on_everyone_message,
            self.client_thread.client_join: self.on_client_join,
            self.client_thread.client_leave: self.on_client_leave,
            self.client_thread.discriminator: self.on_discriminator,
            self.client_thread.online_users: self.on_online_users,
            self.client_thread.dm_message: self.on_dm_message,
            self.client_thread.incoming_call: self.on_incoming_call,
            self.client_thread.accepted_call: self.on_accepted_call,
            self.client_thread.video_data: self.on_video_data,
            self.client_thread.audio_data: self.on_audio_data,
            self.client_thread.end_call: self.on_end_call
        }
        for signal, callback in self.client_thread_dict.keys():
            signal.connect(callback)
        self.client_thread.start()

        # Video Cap thread setup
        self.videocap_worker = VideoCapWorker(self.client)
        if self.videocap_worker.invalid_camera:
            self.add_notif(AcknowledgeNotif("No camera available!", self.width(), 5, self))

        self.videocap_thread = QThread()
        self.videocap_worker.moveToThread(self.videocap_thread)
        self.videocap_thread.started.connect(self.videocap_worker.run)
        self.videocap_worker.frame.connect(self.on_video_frame)
        self.videocap_worker.video_data.connect(partial(self.send_voip_data, command="video_data"))
        self.videocap_worker.done.connect(self.thread_stopped)
        self.videocap_thread.start()

        # Audio(s) thread setup
        self.audio_read_worker = AudioReadWorker(self.client)
        self.audio_read_thread = QThread()
        self.audio_read_worker.audio_data.connect(partial(self.send_voip_data, command="audio_data"))
        self.audio_read_worker.moveToThread(self.audio_read_thread)
        self.audio_read_thread.started.connect(self.audio_read_worker.run)
        self.audio_read_worker.done.connect(self.thread_stopped)

        self.audio_write_worker = AudioWriteWorker(self.client)
        self.audio_write_thread = QThread()
        self.audio_write_worker.moveToThread(self.audio_write_thread)
        self.audio_write_thread.started.connect(self.audio_write_worker.run)
        self.audio_write_worker.done.connect(self.thread_stopped)

        # Frame bar styles
        self.window_drag_pos = QPoint()
        self.mouse_original_pos = QPoint()

        self.frame_bar.setStyleSheet(f"background-color: {os.environ['QTMATERIAL_SECONDARYCOLOR']};")
        self.minimize_button.setStyleSheet("color: white; border-color: transparent;")
        self.x_button.setStyleSheet("color: white; border-color: transparent;")

        # DM selections
        self.dm_messageboxes = {}
        self.dm_message_scrollareas_idx = {}

        self.set_title_font(self.dm_selection_label, 12)
        self.set_title_font(self.dm_who_label, 16, bold=True)
        self.set_title_font(self.preview_video_label, 20)
        self.set_title_font(self.voip_selection_label, 12)
        self.set_title_font(self.call_who_label, 16, bold=True)

        # Signals
        self.frame_bar.mousePressEvent = self.framebar_mousepress
        self.frame_bar.mouseMoveEvent = self.move_window

        self.minimize_button.clicked.connect(self.showMinimized)
        self.x_button.clicked.connect(self.request_close)

        self.everyone_message_to_send.returnPressed.connect(self.send_everyone_message)
        self.everyone_send_button.clicked.connect(self.send_everyone_message)

        self.dm_online_users.itemDoubleClicked.connect(self.dm_selection)
        self.dm_back_button.clicked.connect(self.dm_go_back)

        self.dm_message_to_send.returnPressed.connect(self.send_dm_message)
        self.dm_send_button.clicked.connect(self.send_dm_message)

        self.start_call_button.clicked.connect(self.start_call)

        self.register_scrollbar(self.everyone_message_scrollarea)

    # HELPERS

    @staticmethod
    def set_title_font(label: QLabel, size: int, bold: bool = False):
        font = QFont("Segoe UI", size)
        if bold:
            font.setBold(True)

        label.setFont(font)

    @staticmethod
    def scroll_change(vbar: QScrollBar):
        vbar.setValue(vbar.maximum())

    def register_scrollbar(self, scrollarea: QScrollArea):
        scrollarea_vbar = scrollarea.verticalScrollBar()
        scrollarea_vbar.rangeChanged.connect(lambda: self.scroll_change(scrollarea_vbar))

    def add_dm_selection(self, username: str):
        item = QListWidgetItem()
        thing = DMListItem(username)
        item.setSizeHint(thing.sizeHint())

        self.dm_online_users.addItem(item)
        self.dm_online_users.setItemWidget(item, thing)

    def add_messagebox(self, username: str):
        dm_scrollarea = QScrollArea()
        dm_messages_widget = QWidget()
        dm_messages = QVBoxLayout()
        dm_messages.setAlignment(Qt.AlignmentFlag.AlignTop)

        dm_scrollarea.setWidgetResizable(True)
        self.register_scrollbar(dm_scrollarea)

        dm_messages_widget.setLayout(dm_messages)
        dm_scrollarea.setWidget(dm_messages_widget)
        self.dm_message_scrollareas.addWidget(dm_scrollarea)

        self.dm_messageboxes[username] = dm_messages
        self.dm_message_scrollareas_idx[username] = len(self.dm_message_scrollareas) - 1

        self.send_server_message(dm_messages, "Looks like there's no messages between you two yet!")

    def add_notif(self, notif):
        if self.active_notif():
            return

        self.notif = notif
        self.notif.move(0, 35)
        self.notif.show()

    def active_notif(self):
        return self.notif is not None and not self.notif.closed

    def remove_username_from_list(self, online_users: QListWidget, username: str):
        online_users.takeItem(online_users.row(online_users.findItems(username, Qt.MatchFlag.MatchExactly)[0]))

    def find_dm_selection(self, username: str) -> Optional[tuple[int, DMListItem]]:
        for i in range(self.dm_online_users.count()):
            item = self.dm_online_users.item(i)

            # AAAAAAAAAAAA
            dm_item: DMListItem = self.dm_online_users.itemWidget(item)  # type: ignore
            if dm_item.username == username:
                return i, dm_item

    def remove_dm_selection(self, username: str):
        dm_item = self.find_dm_selection(username)
        if dm_item is None:
            return

        i, dm_item = dm_item
        if dm_item.username == username:
            self.dm_online_users.takeItem(i)

    def current_dm_username(self):
        return self.dm_who_label.text().removeprefix("Talking with: ")

    def current_call_username(self):
        return self.call_who_label.text().removeprefix("Calling: ")

    def send_server_message(self, messages: QVBoxLayout, message: str, time: Optional[datetime] = None):
        messages.addWidget(
            Message("[Server]", (datetime.now() if time is None else time).strftime(self.TIME_FMT), message)
        )
    
    def send_voip_data(self, data: list, command: str):
        self.client.send(command, data)

    # Threads cleanup/close

    def stop_threads(self):
        self.videocap_worker.stop()
        self.audio_read_worker.stop()
        self.audio_write_worker.stop()

    def thread_stopped(self):
        self.threads_stopped += 1
        if self.threads_stopped == 3:
            self.on_threads_close()

    def request_close(self):
        if self.notif is not None:
            self.notif.stop()

        self.stop_threads()
        if self.calling:
            self.close_mode = "actively_ending_call"
        else:
            self.close_mode = "normal"

    def on_threads_close(self):
        self.videocap_worker.cleanup()
        self.videocap_thread.quit()

        if self.close_mode == "actively_ending_call":
            self.client.send("end_call", self.current_call_username())
            self.client.recv("ended_call")

            self.client.close()
            self.close()
        elif self.close_mode == "normal":
            self.client.close()
            self.close()

    # ACTIONS

    def framebar_mousepress(self, a0: QMouseEvent):
        self.window_drag_pos = self.pos()
        self.mouse_original_pos = self.mapToGlobal(a0.pos())

    def move_window(self, a0: QMouseEvent):
        if self.isMaximized():
            self.showNormal()
        else:
            if a0.buttons() == Qt.MouseButton.LeftButton:
                # y
                last_pos = self.window_drag_pos + self.mapToGlobal(a0.pos()) - self.mouse_original_pos  # type: ignore
                self.move(last_pos)
                a0.accept()

    def send_everyone_message(self):
        text = self.everyone_message_to_send.text()
        if text == "" or text.isspace():
            return

        self.everyone_messages.addWidget(Message("You", datetime.now().strftime(self.TIME_FMT), text))
        self.client.send("send_everyone_message", text)

        self.everyone_message_to_send.clear()

    def dm_selection(self, item: QListWidgetItem):
        dm_item: DMListItem = self.dm_online_users.itemWidget(item)  # type: ignore
        if dm_item is None:
            return
        username = dm_item.username

        self.dm_states.setCurrentIndex(1)
        self.dm_message_scrollareas.setCurrentIndex(self.dm_message_scrollareas_idx[username])

        self.dm_who_label.setText(f"Talking with: {username}")
        self.set_title_font(self.dm_who_label, 16, True)

        dm_item.read_messages()

    def dm_go_back(self):
        self.dm_who_label.setText(f"Talking with: ")
        self.dm_states.setCurrentIndex(0)

    def send_dm_message(self):
        text = self.dm_message_to_send.text()
        if text == "" or text.isspace():
            return

        recipient = self.current_dm_username()
        dm_messages = self.dm_messageboxes[recipient]

        dm_messages.addWidget(Message("You", datetime.now().strftime(self.TIME_FMT), text))
        self.client.send("send_dm_message", [recipient, text])

        self.dm_message_to_send.clear()

    def start_call(self):
        if self.active_notif():
            return

        recipient = self.voip_online_users.currentText()

        self.add_notif(AcknowledgeNotif(f"Calling {recipient}...", self.width(), 3, self))
        self.client.send("request_call", self.voip_online_users.currentText())

    # CLIENT CALLBACKS

    def on_everyone_message(self, username: str, time_sent: datetime, message: str):
        time_sent_str = time_sent.strftime(self.TIME_FMT)
        self.everyone_messages.addWidget(Message(username, time_sent_str, message))

    def on_client_join(self, username: str):
        self.send_server_message(self.everyone_messages, f'New user "{username}" just joined! Say hi!')
        self.everyone_online_users.addItem(username)

        self.add_dm_selection(username)
        self.add_messagebox(username)
        self.voip_online_users.addItem(username)

    def on_client_leave(self, username: str):
        self.send_server_message(self.everyone_messages, f'User "{username}" just left! Seeya!')
        self.remove_username_from_list(self.everyone_online_users, username)

        if username in self.dm_who_label.text():
            self.dm_states.setCurrentIndex(0)

        # if username not in self.users_not_read:
        if True:
            self.remove_dm_selection(username)

            self.dm_message_scrollareas.removeWidget(
                self.dm_message_scrollareas.widget(self.dm_message_scrollareas_idx[username])
            )

            del self.dm_messageboxes[username]
            del self.dm_message_scrollareas_idx[username]

            self.voip_online_users.removeItem(self.voip_online_users.findText(username))
        else:
            dm_user = self.dm_online_users.findItems(username, Qt.MatchFlag.MatchExactly)[0]
            dm_user.setText(dm_user.text() + " (left)")

    def on_discriminator(self, discriminator: int):
        self.discriminator = discriminator
        self.username = f"{self.name}#{self.discriminator:04}"

        # self.logged_in_as.setStyleSheet("font-weight: bold;")
        self.logged_in_as.setText(f"Logged in as: {self.username}")

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

        dm_item = self.find_dm_selection(username)
        if dm_item is not None and self.current_dm_username() != username:
            _, dm_item = dm_item
            dm_item.new_unread()

    def on_online_users(self, online_users: list[str]):
        for online_user in online_users:
            # No self for DMs (I mean, yeah)
            if online_user == self.username:
                self.everyone_online_users.addItem(f"{online_user} (YOU)")
                continue
            else:
                self.everyone_online_users.addItem(online_user)

            self.add_dm_selection(online_user)
            self.add_messagebox(online_user)
            self.voip_online_users.addItem(online_user)

    def on_incoming_call(self, sender: str):
        if self.active_notif():
            return

        call_notif = IncomingCallNotif(f"Incoming call from {sender}...", self.width(), self)
        call_notif.accepted.connect(lambda: self.on_accepted_call(sender))
        self.add_notif(call_notif)

    def on_video_data(self, video_data: bytes):
        print(f"\033[92m{time.time()}: recv video data of length {len(video_data)}\033[0m")
        frame_np = np.frombuffer(video_data, np.uint8)
        frame = cv.imdecode(frame_np, cv.IMREAD_COLOR)
        height, width = frame.shape[:2]
        image = QImage(frame.data, width, height, QImage.Format.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(image)

        label_width, label_height = self.opp_video_label.width(), self.opp_video_label.height()
        self.opp_video_label.setPixmap(pixmap.scaled(label_width, label_height, Qt.AspectRatioMode.KeepAspectRatio))

    def on_audio_data(self, audio_data: bytes):
        self.audio_write_worker.queue.put(audio_data)

    # Thing idk

    def on_video_frame(self, frame: np.ndarray):
        height, width = frame.shape[:2]
        image = QImage(frame.data, width, height, QImage.Format.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(image)

        if not self.calling:
            label_width, label_height = self.preview_frame.width(), self.preview_frame.height()
            self.preview_frame.setPixmap(pixmap.scaled(label_width, label_height, Qt.AspectRatioMode.KeepAspectRatio))
        else:
            label_width, label_height = self.own_video_label.width(), self.own_video_label.height()
            self.own_video_label.setPixmap(
                pixmap.scaled(label_width, label_height, Qt.AspectRatioMode.KeepAspectRatio)
            )

    def on_accepted_call(self, original_sender: str):
        self.voip_states.setCurrentIndex(1)

        if self.call_who_label.text() == "Calling: ":
            self.client.send("accepted_call", original_sender)
        self.call_who_label.setText(f"Calling: {original_sender}")

        self.calling = True

        self.videocap_worker.recipient = original_sender
        self.audio_read_worker.recipient = original_sender
        self.audio_write_worker.recipient = original_sender
        self.audio_read_thread.start()
        self.audio_write_thread.start()

    def on_end_call(self):
        # Don't stop vid (yet)
        self.audio_read_worker.stop()
        self.audio_write_worker.stop()
        self.add_notif(AcknowledgeNotif("Call ended!", self.width(), 5, self))

        self.voip_states.setCurrentIndex(0)  # Reset to call screen
        self.call_who_label.setText("Calling: ")

        self.own_video_label.clear()
        self.opp_video_label.clear()

        with self.videocap_worker.recipient_lock:
            self.recipient = ""

        self.client.send("ended_call", self.current_call_username())
        self.calling = False
        self.close_mode = "normal"
