# Form implementation generated from reading ui file 'src\ui\main.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 664)
        MainWindow.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(630, 30, 121, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.online = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.online.setContentsMargins(0, 0, 0, 0)
        self.online.setObjectName("online")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.online.addWidget(self.label)
        self.online_users = QtWidgets.QListWidget(parent=self.layoutWidget)
        self.online_users.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.online_users.setObjectName("online_users")
        self.online.addWidget(self.online_users)
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 580, 741, 61))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.send_box = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.send_box.setContentsMargins(0, 0, 0, 0)
        self.send_box.setObjectName("send_box")
        self.message_to_send = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.message_to_send.setObjectName("message_to_send")
        self.send_box.addWidget(self.message_to_send)
        self.send_button = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.send_button.setObjectName("send_button")
        self.send_box.addWidget(self.send_button)
        self.message_scrollarea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.message_scrollarea.setGeometry(QtCore.QRect(20, 30, 591, 541))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message_scrollarea.sizePolicy().hasHeightForWidth())
        self.message_scrollarea.setSizePolicy(sizePolicy)
        self.message_scrollarea.setWidgetResizable(True)
        self.message_scrollarea.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.message_scrollarea.setObjectName("message_scrollarea")
        self.widget = QtWidgets.QWidget()
        self.widget.setGeometry(QtCore.QRect(0, 0, 589, 539))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.messages = QtWidgets.QVBoxLayout(self.widget)
        self.messages.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.messages.setObjectName("messages")
        self.message_scrollarea.setWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Online"))
        self.send_button.setText(_translate("MainWindow", "Send"))
