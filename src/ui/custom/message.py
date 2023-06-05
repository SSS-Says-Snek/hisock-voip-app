from PyQt6.QtGui import QPainter, QBrush, QColor, QPainterPath, QPaintEvent, QFontMetrics
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QSizePolicy, QStyleOption, QStyle, QTextEdit


# HOW DO I MAKE QTEXTEDIT FIT TO CONTENT AAAAAAAAAAAAAAAAAAAAAAA
"""class IDontKnow(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)

        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)
        self.style().drawItemText(painter, self.rect(), Qt.AlignmentFlag.AlignLeft | Qt.TextFlag.TextWrapAnywhere, self.palette(), True, self.text())

class WTF(QTextEdit):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

    def sizeHint(self):
        return self.document().size().toSize()

    def resizeEvent(self, event):
        self.updateGeometry()
        super().resizeEvent(event)


class GrowingTextEdit(QTextEdit):

    def __init__(self, *args, **kwargs):
        super(GrowingTextEdit, self).__init__(*args, **kwargs)  
        self.document().contentsChanged.connect(self.sizeChange)

        self.heightMin = 0
        self.heightMax = 65000

    def sizeChange(self):
        docHeight = self.document().size().toSize().height()
        if self.heightMin <= docHeight <= self.heightMax:
            self.setMinimumHeight(docHeight)"""


class Message(QWidget):
    def __init__(self, username: str, message: str):
        super().__init__()

        self.username = username
        self.message = message

        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)


        self.username_label = QLabel(self.username)
        self.username_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.message_label = QLabel(self.message, self)
        self.message_label.setWordWrap(True)
        # self.message_label.setStyleSheet("border: none;")
        # self.message_label.setReadOnly(True)


        # print(self.message_label.document().size().toSize())
        # self.message_label.setFixedHeight(self.message_label.heightForWidth(self.message_label.width()))
        # self.message_label.setFixedHeight(self.message_label.document().size().toSize().height())
        self.message_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        # self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

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

