from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtGui import QBrush, QColor, QPainter, QPainterPath
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QWidget, QPushButton, QSizePolicy

class AcknowledgeNotif(QWidget):
    def __init__(self, text: str, width: int, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout(self)

        self.text = text
        self.text_label = QLabel(self.text, self)
        self.ok_button = QPushButton("Okay", self)
        self.ok_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        self.ok_button.setStyleSheet("background-color: transparent;")
        self.ok_button.clicked.connect(self.ok)

        self.setFixedWidth(width)
        self.setFixedHeight(self.height() + 40)

        layout.addWidget(self.text_label)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)
    
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
    
    def ok(self):
        self.deleteLater()
