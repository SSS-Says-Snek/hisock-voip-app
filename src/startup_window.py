"""
This file is a part of the source code for hisock-voip-app
This project has been licensed under the MIT license.
Copyright (c) 2022-present SSS-Says-Snek
"""

from __future__ import annotations

from ipaddress import IPv4Address
from typing import Optional

from hisock import HiSockClient
from hisock.utils import ServerNotRunning
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QDialog, QLabel

from src.main_window import MainWindow
from src.ui.generated.startup_dialog import Ui_Dialog


class ConnectWorker(QThread):
    failed = pyqtSignal()
    succeeded = pyqtSignal(HiSockClient)

    def __init__(self, ip: str, port: str, username: str, parent=None):
        super().__init__(parent)

        self.ip = ip
        self.port = port
        self.username = username

    def run(self):
        try:
            client = HiSockClient((self.ip, int(self.port)), self.username)
        except (ServerNotRunning, TimeoutError):
            self.failed.emit()
        else:
            self.succeeded.emit(client)


class StartupWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.set_retain_size(self.ip_status)
        self.set_retain_size(self.port_status)
        self.set_retain_size(self.username_status)

        self.ip_status.hide()
        self.port_status.hide()
        self.username_status.hide()

        self.connect_button.clicked.connect(self.on_connect_attempt)

        self.connect_worker: Optional[ConnectWorker] = None
        self.main_window: Optional[MainWindow] = None

    def on_connect_attempt(self):
        ip = self.ip_input.text()
        port = self.port_input.text()
        username = self.username_input.text()

        self.ip_status.hide()
        self.port_status.hide()
        self.username_status.hide()

        try:
            IPv4Address(ip)
        except ValueError:
            self.status_message(self.ip_status, "red", "Please input a valid IPv4 address")

        if not port.isdigit() or not 0 < int(port) <= 65535:
            self.status_message(self.port_status, "red", "Please input a valid server port")

        if ip == "":
            self.status_message(self.ip_status, "red", "Please input an IPv4 address")
        if port == "":
            self.status_message(self.port_status, "red", "Please input a server port")
        if username == "":
            self.status_message(self.username_status, "red", "Please input a username")
        if len(username) > 16:
            self.status_message(self.username_status, "red", "Sorry, username cannot be above 16 characters long")

        if self.ip_status.isHidden() and self.port_status.isHidden() and self.username_status.isHidden():
            self.connect_worker = ConnectWorker(ip, port, username)
            self.connect_worker.succeeded.connect(self.on_connect_success)
            self.connect_worker.failed.connect(self.on_connect_fail)
            self.connect_worker.start()

    def on_connect_success(self, client):
        self.main_window = MainWindow(client, self.username_input.text())
        self.main_window.show()

        self.hide()

    def on_connect_fail(self):
        self.status_message(self.ip_status, "red", "The server either is not running or does not exist!")
        self.status_message(self.port_status, "red", "The server either is not running or does not exist!")

    @staticmethod
    def status_message(status: QLabel, color: str, text: str):
        status.setStyleSheet(f"QLabel {{color: {color}}}")
        status.setText(text)
        status.show()

    @staticmethod
    def set_retain_size(status: QLabel):
        status_sizepolicy = status.sizePolicy()
        status_sizepolicy.setRetainSizeWhenHidden(True)
        status.setSizePolicy(status_sizepolicy)
