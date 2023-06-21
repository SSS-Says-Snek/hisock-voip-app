"""
This file is a part of the source code for hisock-voip-app
This project has been licensed under the MIT license.
Copyright (c) 2022-present SSS-Says-Snek
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QPainter, QPaintEvent
from PySide6.QtWidgets import QHBoxLayout, QLabel, QWidget


class UnreadNotif(QLabel):
    def __init__(self, radius: int, parent=None, *args, **kwargs):
        super().__init__(parent=parent, *args, **kwargs)
        self.radius = radius

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFixedSize(self.radius * 2, self.radius * 2)
        self.setStyleSheet(f"border-radius: {self.radius}px; background-color: red;")


class DMListItem(QWidget):
    def __init__(self, username: str, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout(self)

        self.username = username
        self.unread_notif = UnreadNotif(15, self, "0")

        unread_sizepolicy = self.unread_notif.sizePolicy()
        unread_sizepolicy.setRetainSizeWhenHidden(True)
        self.unread_notif.setSizePolicy(unread_sizepolicy)
        self.unread_notif.hide()

        layout.addWidget(QLabel(self.username, self))
        layout.addWidget(self.unread_notif)

        layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.setLayout(layout)

    def new_unread(self):
        num_unreads = int(self.unread_notif.text()) + 1
        self.unread_notif.setText(str(num_unreads))
        self.unread_notif.show()

    def read_messages(self):
        self.unread_notif.setText("0")
        self.unread_notif.hide()
