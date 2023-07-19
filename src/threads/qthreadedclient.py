from datetime import datetime

from hisock import HiSockClient
from PyQt6.QtCore import QThread, pyqtSignal


class QThreadedHiSockClient(QThread):
    everyone_message = pyqtSignal(str, datetime, str)
    client_join = pyqtSignal(str)
    client_leave = pyqtSignal(str)
    discriminator = pyqtSignal(int)
    online_users = pyqtSignal(list)
    dm_message = pyqtSignal(str, datetime, str)
    incoming_call = pyqtSignal(str)
    accepted_call = pyqtSignal(str)
    video_data = pyqtSignal(bytes)
    audio_data = pyqtSignal(bytes)
    end_call = pyqtSignal()

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

        @self.client.on("incoming_call")
        def on_incoming_call(sender: str):
            self.incoming_call.emit(sender)

        @self.client.on("accepted_call")
        def on_accepted_call(sender: str):
            self.accepted_call.emit(sender)

        @self.client.on("video_data")
        def on_video_data(video_data: bytes):
            self.video_data.emit(video_data)

        @self.client.on("audio_data")
        def on_audio_data(audio_data: bytes):
            self.audio_data.emit(audio_data)

        @self.client.on("end_call")
        def on_end_call():
            self.end_call.emit()

    def run(self):
        self.client.start()
