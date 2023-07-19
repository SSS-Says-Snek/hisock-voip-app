# Form implementation generated from reading ui file 'src/ui/main.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 750)
        MainWindow.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(10, 60, 781, 680))
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
        self.dm_states.setGeometry(QtCore.QRect(0, 0, 780, 660))
        self.dm_states.setObjectName("dm_states")
        self.dm_user_selection = QtWidgets.QWidget()
        self.dm_user_selection.setObjectName("dm_user_selection")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dm_user_selection)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(200, -1, 200, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.dm_selection_label = QtWidgets.QLabel(parent=self.dm_user_selection)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.dm_selection_label.setFont(font)
        self.dm_selection_label.setObjectName("dm_selection_label")
        self.verticalLayout.addWidget(self.dm_selection_label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.dm_online_users = QtWidgets.QListWidget(parent=self.dm_user_selection)
        self.dm_online_users.setObjectName("dm_online_users")
        self.verticalLayout.addWidget(self.dm_online_users)
        self.dm_states.addWidget(self.dm_user_selection)
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
        font.setPointSize(16)
        self.dm_who_label.setFont(font)
        self.dm_who_label.setObjectName("dm_who_label")
        self.dm_top.addWidget(self.dm_who_label)
        self.dm_main_layout.addLayout(self.dm_top)
        self.dm_message_scrollareas = QtWidgets.QStackedWidget(parent=self.layoutWidget2)
        self.dm_message_scrollareas.setObjectName("dm_message_scrollareas")
        self.dm_main_layout.addWidget(self.dm_message_scrollareas)
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
        self.voip_tab = QtWidgets.QWidget()
        self.voip_tab.setObjectName("voip_tab")
        self.voip_states = QtWidgets.QStackedWidget(parent=self.voip_tab)
        self.voip_states.setGeometry(QtCore.QRect(0, 0, 771, 651))
        self.voip_states.setObjectName("voip_states")
        self.voip_user_selection = QtWidgets.QWidget()
        self.voip_user_selection.setObjectName("voip_user_selection")
        self.layoutWidget3 = QtWidgets.QWidget(parent=self.voip_user_selection)
        self.layoutWidget3.setGeometry(QtCore.QRect(1, -4, 771, 651))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.preview_video_label = QtWidgets.QLabel(parent=self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview_video_label.sizePolicy().hasHeightForWidth())
        self.preview_video_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.preview_video_label.setFont(font)
        self.preview_video_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.preview_video_label.setObjectName("preview_video_label")
        self.gridLayout.addWidget(self.preview_video_label, 0, 0, 1, 3)
        self.start_call_button = QtWidgets.QPushButton(parent=self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start_call_button.setFont(font)
        self.start_call_button.setObjectName("start_call_button")
        self.gridLayout.addWidget(self.start_call_button, 2, 1, 1, 1)
        self.voip_selection_label = QtWidgets.QLabel(parent=self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.voip_selection_label.sizePolicy().hasHeightForWidth())
        self.voip_selection_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.voip_selection_label.setFont(font)
        self.voip_selection_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.voip_selection_label.setObjectName("voip_selection_label")
        self.gridLayout.addWidget(self.voip_selection_label, 4, 0, 1, 3)
        self.preview_frame = QtWidgets.QLabel(parent=self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview_frame.sizePolicy().hasHeightForWidth())
        self.preview_frame.setSizePolicy(sizePolicy)
        self.preview_frame.setMinimumSize(QtCore.QSize(720, 0))
        self.preview_frame.setMaximumSize(QtCore.QSize(16777215, 405))
        self.preview_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.preview_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.preview_frame.setLineWidth(2)
        self.preview_frame.setText("")
        self.preview_frame.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.preview_frame.setObjectName("preview_frame")
        self.gridLayout.addWidget(self.preview_frame, 1, 0, 1, 3, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.video_button = QtWidgets.QPushButton(parent=self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video_button.sizePolicy().hasHeightForWidth())
        self.video_button.setSizePolicy(sizePolicy)
        self.video_button.setObjectName("video_button")
        self.gridLayout.addWidget(self.video_button, 2, 2, 1, 1)
        self.mute_button = QtWidgets.QPushButton(parent=self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mute_button.sizePolicy().hasHeightForWidth())
        self.mute_button.setSizePolicy(sizePolicy)
        self.mute_button.setObjectName("mute_button")
        self.gridLayout.addWidget(self.mute_button, 2, 0, 1, 1)
        self.voip_online_users = QtWidgets.QComboBox(parent=self.layoutWidget3)
        self.voip_online_users.setObjectName("voip_online_users")
        self.gridLayout.addWidget(self.voip_online_users, 3, 0, 1, 3)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 4)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setRowStretch(1, 1)
        self.voip_states.addWidget(self.voip_user_selection)
        self.voip = QtWidgets.QWidget()
        self.voip.setObjectName("voip")
        self.layoutWidget4 = QtWidgets.QWidget(parent=self.voip)
        self.layoutWidget4.setGeometry(QtCore.QRect(0, 0, 771, 651))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.own_video_label = QtWidgets.QLabel(parent=self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.own_video_label.sizePolicy().hasHeightForWidth())
        self.own_video_label.setSizePolicy(sizePolicy)
        self.own_video_label.setMinimumSize(QtCore.QSize(480, 270))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.own_video_label.setFont(font)
        self.own_video_label.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.own_video_label.setLineWidth(2)
        self.own_video_label.setText("")
        self.own_video_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.own_video_label.setObjectName("own_video_label")
        self.gridLayout_2.addWidget(self.own_video_label, 1, 0, 2, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.pushButton = QtWidgets.QPushButton(parent=self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.opp_video_label = QtWidgets.QLabel(parent=self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opp_video_label.sizePolicy().hasHeightForWidth())
        self.opp_video_label.setSizePolicy(sizePolicy)
        self.opp_video_label.setMinimumSize(QtCore.QSize(480, 270))
        self.opp_video_label.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.opp_video_label.setLineWidth(2)
        self.opp_video_label.setText("")
        self.opp_video_label.setObjectName("opp_video_label")
        self.gridLayout_2.addWidget(self.opp_video_label, 3, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.call_who_label = QtWidgets.QLabel(parent=self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.call_who_label.sizePolicy().hasHeightForWidth())
        self.call_who_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        self.call_who_label.setFont(font)
        self.call_who_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.call_who_label.setObjectName("call_who_label")
        self.gridLayout_2.addWidget(self.call_who_label, 0, 0, 1, 2)
        self.voip_states.addWidget(self.voip)
        self.tabs.addTab(self.voip_tab, "")
        self.frame_bar = QtWidgets.QWidget(parent=self.centralwidget)
        self.frame_bar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.frame_bar.setObjectName("frame_bar")
        self.logged_in_as = QtWidgets.QLabel(parent=self.frame_bar)
        self.logged_in_as.setGeometry(QtCore.QRect(14, 5, 690, 20))
        self.logged_in_as.setObjectName("logged_in_as")
        self.minimize_button = QtWidgets.QPushButton(parent=self.frame_bar)
        self.minimize_button.setGeometry(QtCore.QRect(710, 0, 30, 30))
        self.minimize_button.setObjectName("minimize_button")
        self.x_button = QtWidgets.QPushButton(parent=self.frame_bar)
        self.x_button.setGeometry(QtCore.QRect(760, 0, 30, 30))
        self.x_button.setObjectName("x_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(2)
        self.dm_states.setCurrentIndex(0)
        self.voip_states.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.everyone_send_button.setText(_translate("MainWindow", "Send"))
        self.everyone_online_label.setText(_translate("MainWindow", "Online"))
        self.tabs.setTabText(self.tabs.indexOf(self.everyone_message), _translate("MainWindow", "Everyone Messages"))
        self.dm_selection_label.setText(_translate("MainWindow", "Select a user to Direct Message with"))
        self.dm_back_button.setText(_translate("MainWindow", "Back"))
        self.dm_who_label.setText(_translate("MainWindow", "Talking with: "))
        self.dm_send_button.setText(_translate("MainWindow", "Send"))
        self.tabs.setTabText(self.tabs.indexOf(self.direct_message), _translate("MainWindow", "Direct Messages"))
        self.preview_video_label.setText(_translate("MainWindow", "Preview Video"))
        self.start_call_button.setText(_translate("MainWindow", "Start Call"))
        self.voip_selection_label.setText(_translate("MainWindow", "User to voice/video with"))
        self.video_button.setText(_translate("MainWindow", "Turn off Video"))
        self.mute_button.setText(_translate("MainWindow", "Mute"))
        self.pushButton.setText(_translate("MainWindow", "Mute"))
        self.pushButton_2.setText(_translate("MainWindow", "Turn Off Video"))
        self.call_who_label.setText(_translate("MainWindow", "Calling: "))
        self.tabs.setTabText(self.tabs.indexOf(self.voip_tab), _translate("MainWindow", "Voice/Video"))
        self.logged_in_as.setText(_translate("MainWindow", "Logged in as: "))
        self.minimize_button.setText(_translate("MainWindow", "—"))
        self.x_button.setText(_translate("MainWindow", "X"))
