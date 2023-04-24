from PyQt6.QtGui import QPainter, QBrush, QColor, QPainterPath, QPaintEvent
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QSizePolicy, QLayout


class Message(QWidget):
    def __init__(self, username: str, message: str):
        super().__init__()

        self.username = username
        self.message = message


        self.username_label = QLabel(self.username)

        self.message_label = QLabel(self.message)
        # self.message_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        self.message_label.setWordWrap(True)

        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

        layout = QGridLayout(self)
        # layout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.setLayout(layout)

        layout.addWidget(self.username_label, 0, 0)
        layout.setColumnStretch(0, 1)

        time = QLabel("11:03 AM, 3/30/2023")
        time.setObjectName("time")
        layout.addWidget(time, 0, 1)

        layout.addWidget(self.message_label, 1, 0, 1, 2)


    
    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.RenderHint.Antialiasing)
        path = QPainterPath()

        brush = QBrush()
        brush.setColor(QColor("#232629"))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        painter.setBrush(brush)

        rect = QRectF(0, 0, self.width(), self.height())
        path.addRoundedRect(rect, 10, 10)
        painter.setClipPath(path)

        painter.fillPath(path, painter.brush())

