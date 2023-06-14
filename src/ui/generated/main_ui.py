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
        MainWindow.resize(801, 709)
        MainWindow.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabs = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabs.setObjectName("tabs")
        self.everyone_message = QtWidgets.QWidget()
        self.everyone_message.setObjectName("everyone_message")
        self.everyone_message_scrollarea = QtWidgets.QScrollArea(parent=self.everyone_message)
        self.everyone_message_scrollarea.setGeometry(QtCore.QRect(11, 11, 581, 561))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.everyone_message_scrollarea.sizePolicy().hasHeightForWidth())
        self.everyone_message_scrollarea.setSizePolicy(sizePolicy)
        self.everyone_message_scrollarea.setWidgetResizable(True)
        self.everyone_message_scrollarea.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.everyone_message_scrollarea.setObjectName("everyone_message_scrollarea")
        self.everyone_message_widget = QtWidgets.QWidget()
        self.everyone_message_widget.setGeometry(QtCore.QRect(0, 0, 579, 559))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.everyone_message_widget.sizePolicy().hasHeightForWidth())
        self.everyone_message_widget.setSizePolicy(sizePolicy)
        self.everyone_message_widget.setObjectName("everyone_message_widget")
        self.everyone_message_scrollarea.setWidget(self.everyone_message_widget)
        self.layoutWidget = QtWidgets.QWidget(parent=self.everyone_message)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 590, 731, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.everyone_send_box = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.everyone_send_box.setContentsMargins(0, 0, 0, 0)
        self.everyone_send_box.setObjectName("everyone_send_box")
        self.everyone_message_to_send = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.everyone_message_to_send.setObjectName("everyone_message_to_send")
        self.everyone_send_box.addWidget(self.everyone_message_to_send)
        self.everyone_send_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.everyone_send_button.setObjectName("everyone_send_button")
        self.everyone_send_box.addWidget(self.everyone_send_button)
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.everyone_message)
        self.layoutWidget1.setGeometry(QtCore.QRect(620, 10, 121, 561))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.everyone_online = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.everyone_online.setContentsMargins(0, 0, 0, 0)
        self.everyone_online.setObjectName("everyone_online")
        self.everyone_online_label = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.everyone_online_label.setFont(font)
        self.everyone_online_label.setObjectName("everyone_online_label")
        self.everyone_online.addWidget(self.everyone_online_label)
        self.everyone_online_users = QtWidgets.QListWidget(parent=self.layoutWidget1)
        self.everyone_online_users.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.everyone_online_users.setObjectName("everyone_online_users")
        self.everyone_online.addWidget(self.everyone_online_users)
        self.tabs.addTab(self.everyone_message, "")
        self.direct_message = QtWidgets.QWidget()
        self.direct_message.setObjectName("direct_message")
        self.dm_states = QtWidgets.QStackedWidget(parent=self.direct_message)
        self.dm_states.setGeometry(QtCore.QRect(0, 0, 781, 661))
        self.dm_states.setObjectName("dm_states")
        self.user_selection = QtWidgets.QWidget()
        self.user_selection.setObjectName("user_selection")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.user_selection)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(200, -1, 200, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.dm_selection_label = QtWidgets.QLabel(parent=self.user_selection)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.dm_selection_label.setFont(font)
        self.dm_selection_label.setObjectName("dm_selection_label")
        self.verticalLayout.addWidget(self.dm_selection_label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.dm_online_users = QtWidgets.QListWidget(parent=self.user_selection)
        self.dm_online_users.setObjectName("dm_online_users")
        self.verticalLayout.addWidget(self.dm_online_users)
        self.dm_states.addWidget(self.user_selection)
        self.dm = QtWidgets.QWidget()
        self.dm.setObjectName("dm")
        self.layoutWidget2 = QtWidgets.QWidget(parent=self.dm)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 10, 751, 641))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.dm_main_layout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.dm_main_layout.setContentsMargins(0, 10, 0, 0)
        self.dm_main_layout.setObjectName("dm_main_layout")
        self.dm_top = QtWidgets.QHBoxLayout()
        self.dm_top.setObjectName("dm_top")
        self.dm_back_button = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dm_back_button.sizePolicy().hasHeightForWidth())
        self.dm_back_button.setSizePolicy(sizePolicy)
        self.dm_back_button.setObjectName("dm_back_button")
        self.dm_top.addWidget(self.dm_back_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.dm_top.addItem(spacerItem2)
        self.dm_who_label = QtWidgets.QLabel(parent=self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.dm_who_label.setFont(font)
        self.dm_who_label.setObjectName("dm_who_label")
        self.dm_top.addWidget(self.dm_who_label)
        self.dm_main_layout.addLayout(self.dm_top)
        self.dm_message_scrollarea = QtWidgets.QScrollArea(parent=self.layoutWidget2)
        self.dm_message_scrollarea.setWidgetResizable(True)
        self.dm_message_scrollarea.setObjectName("dm_message_scrollarea")
        self.dm_message_widget = QtWidgets.QWidget()
        self.dm_message_widget.setGeometry(QtCore.QRect(0, 0, 747, 537))
        self.dm_message_widget.setObjectName("dm_message_widget")
        self.dm_message_scrollarea.setWidget(self.dm_message_widget)
        self.dm_main_layout.addWidget(self.dm_message_scrollarea)
        self.dm_send_box = QtWidgets.QHBoxLayout()
        self.dm_send_box.setObjectName("dm_send_box")
        self.dm_message_to_send = QtWidgets.QLineEdit(parent=self.layoutWidget2)
        self.dm_message_to_send.setObjectName("dm_message_to_send")
        self.dm_send_box.addWidget(self.dm_message_to_send)
        self.dm_send_button = QtWidgets.QPushButton(parent=self.layoutWidget2)
        self.dm_send_button.setObjectName("dm_send_button")
        self.dm_send_box.addWidget(self.dm_send_button)
        self.dm_main_layout.addLayout(self.dm_send_box)
        self.dm_states.addWidget(self.dm)
        self.tabs.addTab(self.direct_message, "")
        self.gridLayout.addWidget(self.tabs, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        self.dm_states.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.everyone_send_button.setText(_translate("MainWindow", "Send"))
        self.everyone_online_label.setText(_translate("MainWindow", "Online"))
        self.tabs.setTabText(self.tabs.indexOf(self.everyone_message), _translate("MainWindow", "Everyone Messages"))
        self.dm_selection_label.setText(_translate("MainWindow", "Select a user to Direct Message with"))
        self.dm_back_button.setText(_translate("MainWindow", "Back"))
        self.dm_who_label.setText(_translate("MainWindow", "Talking with: Chicken Sandwich#6969"))
        self.dm_send_button.setText(_translate("MainWindow", "Send"))
        self.tabs.setTabText(self.tabs.indexOf(self.direct_message), _translate("MainWindow", "Direct Messages"))
