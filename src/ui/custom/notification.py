"""
This file is a part of the source code for hisock-voip-app
This project has been licensed under the MIT license.
Copyright (c) 2022-present SSS-Says-Snek
"""

from __future__ import annotations

import time

from PyQt6.QtCore import QObject, QRectF, Qt, QThread, pyqtSignal
from PyQt6.QtGui import QBrush, QColor, QPainter, QPainterPath
from PyQt6.QtWidgets import (QGridLayout, QHBoxLayout, QLabel, QProgressBar,
                             QPushButton, QSizePolicy, QWidget)


class AutoProgressWorker(QObject):
    update = pyqtSignal(int)
    done = pyqtSignal()

    def __init__(self, duration: int):
        super().__init__()

        self.duration = duration

        self.running = True

    def run(self):
        start_time = time.time()

        while time.time() < start_time + self.duration and self.running:
            self.update.emit(int((time.time() - start_time) / self.duration * 100))
            time.sleep(1 / 120)
        self.done.emit()

    def stop(self):
        self.running = False


class Notif(QWidget):
    def __init__(self, text: str, width: int, parent=None):
        super().__init__(parent)

        self.text = text
        self.text_label = QLabel(self.text, self)

        self.setFixedWidth(width)
        self.setFixedHeight(self.height() + 40)

        self.closed = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.RenderHint.Antialiasing)
        path = QPainterPath()

        brush = QBrush()
        brush.setColor(QColor("#232629").darker(125))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        painter.setBrush(brush)

        rect = QRectF(0, 0, self.width(), self.height())
        path.addRect(rect)
        painter.setClipPath(path)

        painter.fillPath(path, painter.brush())

    def stop(self):
        pass


class AcknowledgeNotif(Notif):
    def __init__(self, text: str, width: int, duration: int, parent=None):
        super().__init__(text, width, parent)

        layout = QGridLayout(self)

        self.ok_button = QPushButton("Okay", self)
        self.ok_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        self.ok_button.setStyleSheet("background-color: transparent;")
        self.ok_button.clicked.connect(self.stop)

        self.auto_progressbar = QProgressBar(self)
        self.auto_progressbar.setFixedHeight(5)

        self.auto_progress_worker = AutoProgressWorker(duration)
        self.auto_progress_thread = QThread()
        self.auto_progress_worker.moveToThread(self.auto_progress_thread)
        self.auto_progress_thread.started.connect(self.auto_progress_worker.run)
        self.auto_progress_thread.finished.connect(self.thread_close)

        self.auto_progress_worker.update.connect(self.auto_progressbar.setValue)
        self.auto_progress_worker.done.connect(self.stop)
        self.auto_progress_thread.start()

        layout.addWidget(self.text_label, 0, 0)
        layout.addWidget(self.ok_button, 0, 1)
        layout.addWidget(self.auto_progressbar, 1, 0, 1, 2)
        self.setLayout(layout)

    def stop(self):
        self.auto_progress_thread.quit()
        self.auto_progress_worker.stop()
        self.hide()

    def thread_close(self):
        self.closed = True


class IncomingCallNotif(Notif):
    accepted = pyqtSignal()

    def __init__(self, text: str, width: int, parent=None):
        super().__init__(text, width, parent)

        layout = QHBoxLayout(self)

        self.ok_button = QPushButton("Accept", self)
        self.ok_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        self.ok_button.setStyleSheet("background-color: transparent;")
        self.ok_button.clicked.connect(self.accept)

        self.no_button = QPushButton("Decline", self)
        self.no_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        self.no_button.setStyleSheet("background-color: transparent;")
        self.no_button.clicked.connect(self.decline)

        layout.addWidget(self.text_label)
        layout.addWidget(self.no_button)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)

    def accept(self):
        self.accepted.emit()
        self.hide()
        self.closed = True

    def decline(self):
        self.hide()
        self.closed = True
