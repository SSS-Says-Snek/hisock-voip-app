import threading
import time

import cv2 as cv
import numpy as np
from hisock import HiSockClient
from PyQt6.QtCore import QObject, pyqtSignal


class VideoCapWorker(QObject):
    frame = pyqtSignal(np.ndarray)
    video_data = pyqtSignal(list)
    done = pyqtSignal()

    def __init__(self, client: HiSockClient):
        super().__init__()

        self.client = client

        self.cap = cv.VideoCapture(0)
        self.invalid_camera = False
        if self.cap is None or not self.cap.isOpened():
            self.invalid_camera = True

        self.running = False
        self.recipient = ""

        self.recipient_lock = threading.Lock()

    def run(self):
        self.running = True

        while self.running:
            time.sleep(1 / 60)
            if self.invalid_camera:
                continue

            ret, frame = self.cap.read()
            if not ret:  # idk what to do
                break
            self.frame.emit(frame)

            with self.recipient_lock:
                if self.recipient == "":
                    continue

            height, width = frame.shape[:2]
            ratio = height / width

            reduced_width = 480
            reduced_height = int(reduced_width * ratio)

            frame_bytes = cv.imencode(".jpg", cv.resize(frame, (reduced_width, reduced_height)))[1].tobytes()

            self.video_data.emit([self.recipient, frame_bytes])
            print(f"\033[32m{time.time()}: sent video data to {self.recipient} of length {len(frame_bytes)}\033[0m")

        print("Exiting from videocap thread")
        self.done.emit()

    def stop(self):
        self.running = False

    def cleanup(self):
        self.cap.release()