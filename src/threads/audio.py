from queue import Empty, Queue

import time

from hisock import HiSockClient
import sounddevice as sd
from PyQt6.QtCore import QObject, pyqtSignal


class AudioReadWorker(QObject):
    audio_data = pyqtSignal(list)
    done = pyqtSignal()

    def __init__(self, client: HiSockClient):
        super().__init__()

        self.client = client
        self.recipient = ""

        self.running = False

    def run(self):
        self.running = True

        with sd.RawInputStream(samplerate=44100, blocksize=2048) as stream:
            while self.running:
                buffer, overflowed = stream.read(2048)
                data = bytes(buffer)  # type: ignore

                if not overflowed:
                    print(f"\033[33m{time.time()}: send audio data of length {len(data)}\033[0m")
                    self.audio_data.emit([self.recipient, data])
                else:
                    print("YOOOO")
                # FORGOT TO CHANGE TYPE HINTS

            self.done.emit()

    def stop(self):
        if not self.running:
            self.done.emit()

        self.running = False


class AudioWriteWorker(QObject):
    done = pyqtSignal()

    def __init__(self, client: HiSockClient):
        super().__init__()

        self.client = client
        self.recipient = ""
        self.queue = Queue()

        self.running = False

    def run(self):
        self.running = True

        with sd.RawOutputStream(samplerate=44100, blocksize=2048) as stream:
            while self.running:
                try:
                    data = self.queue.get_nowait()
                except Empty:
                    pass
                else:
                    print(f"\033[93m{time.time()}: recv audio data of length {len(data)}\033[0m")
                    stream.write(data)

            self.done.emit()

    def stop(self):
        if not self.running:
            self.done.emit()

        self.running = False