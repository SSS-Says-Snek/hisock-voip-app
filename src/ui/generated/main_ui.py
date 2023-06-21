# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 750)
        MainWindow.setFocusPolicy(Qt.NoFocus)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setGeometry(QRect(10, 60, 781, 681))
        self.everyone_message = QWidget()
        self.everyone_message.setObjectName(u"everyone_message")
        self.everyone_message_scrollarea = QScrollArea(self.everyone_message)
        self.everyone_message_scrollarea.setObjectName(u"everyone_message_scrollarea")
        self.everyone_message_scrollarea.setGeometry(QRect(11, 11, 581, 561))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.everyone_message_scrollarea.sizePolicy().hasHeightForWidth())
        self.everyone_message_scrollarea.setSizePolicy(sizePolicy)
        self.everyone_message_scrollarea.setWidgetResizable(True)
        self.everyone_message_scrollarea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.everyone_message_widget = QWidget()
        self.everyone_message_widget.setObjectName(u"everyone_message_widget")
        self.everyone_message_widget.setGeometry(QRect(0, 0, 579, 559))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.everyone_message_widget.sizePolicy().hasHeightForWidth())
        self.everyone_message_widget.setSizePolicy(sizePolicy1)
        self.everyone_message_scrollarea.setWidget(self.everyone_message_widget)
        self.layoutWidget = QWidget(self.everyone_message)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 590, 731, 51))
        self.everyone_send_box = QHBoxLayout(self.layoutWidget)
        self.everyone_send_box.setObjectName(u"everyone_send_box")
        self.everyone_send_box.setContentsMargins(0, 0, 0, 0)
        self.everyone_message_to_send = QLineEdit(self.layoutWidget)
        self.everyone_message_to_send.setObjectName(u"everyone_message_to_send")

        self.everyone_send_box.addWidget(self.everyone_message_to_send)

        self.everyone_send_button = QPushButton(self.layoutWidget)
        self.everyone_send_button.setObjectName(u"everyone_send_button")

        self.everyone_send_box.addWidget(self.everyone_send_button)

        self.layoutWidget1 = QWidget(self.everyone_message)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(620, 10, 121, 561))
        self.everyone_online = QVBoxLayout(self.layoutWidget1)
        self.everyone_online.setObjectName(u"everyone_online")
        self.everyone_online.setContentsMargins(0, 0, 0, 0)
        self.everyone_online_label = QLabel(self.layoutWidget1)
        self.everyone_online_label.setObjectName(u"everyone_online_label")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        self.everyone_online_label.setFont(font)

        self.everyone_online.addWidget(self.everyone_online_label)

        self.everyone_online_users = QListWidget(self.layoutWidget1)
        self.everyone_online_users.setObjectName(u"everyone_online_users")
        self.everyone_online_users.setFocusPolicy(Qt.StrongFocus)

        self.everyone_online.addWidget(self.everyone_online_users)

        self.tabs.addTab(self.everyone_message, "")
        self.direct_message = QWidget()
        self.direct_message.setObjectName(u"direct_message")
        self.dm_states = QStackedWidget(self.direct_message)
        self.dm_states.setObjectName(u"dm_states")
        self.dm_states.setGeometry(QRect(0, 0, 781, 661))
        self.dm_user_selection = QWidget()
        self.dm_user_selection.setObjectName(u"dm_user_selection")
        self.verticalLayout = QVBoxLayout(self.dm_user_selection)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(200, -1, 200, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)

        self.dm_selection_label = QLabel(self.dm_user_selection)
        self.dm_selection_label.setObjectName(u"dm_selection_label")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.dm_selection_label.setFont(font1)

        self.verticalLayout.addWidget(self.dm_selection_label, 0, Qt.AlignHCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.dm_online_users = QListWidget(self.dm_user_selection)
        self.dm_online_users.setObjectName(u"dm_online_users")

        self.verticalLayout.addWidget(self.dm_online_users)

        self.dm_states.addWidget(self.dm_user_selection)
        self.dm = QWidget()
        self.dm.setObjectName(u"dm")
        self.layoutWidget2 = QWidget(self.dm)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 10, 751, 641))
        self.dm_main_layout = QVBoxLayout(self.layoutWidget2)
        self.dm_main_layout.setObjectName(u"dm_main_layout")
        self.dm_main_layout.setContentsMargins(0, 10, 0, 0)
        self.dm_top = QHBoxLayout()
        self.dm_top.setObjectName(u"dm_top")
        self.dm_back_button = QPushButton(self.layoutWidget2)
        self.dm_back_button.setObjectName(u"dm_back_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.dm_back_button.sizePolicy().hasHeightForWidth())
        self.dm_back_button.setSizePolicy(sizePolicy2)

        self.dm_top.addWidget(self.dm_back_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.dm_top.addItem(self.horizontalSpacer_3)

        self.dm_who_label = QLabel(self.layoutWidget2)
        self.dm_who_label.setObjectName(u"dm_who_label")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(16)
        self.dm_who_label.setFont(font2)

        self.dm_top.addWidget(self.dm_who_label)


        self.dm_main_layout.addLayout(self.dm_top)

        self.dm_message_scrollareas = QStackedWidget(self.layoutWidget2)
        self.dm_message_scrollareas.setObjectName(u"dm_message_scrollareas")

        self.dm_main_layout.addWidget(self.dm_message_scrollareas)

        self.dm_send_box = QHBoxLayout()
        self.dm_send_box.setObjectName(u"dm_send_box")
        self.dm_message_to_send = QLineEdit(self.layoutWidget2)
        self.dm_message_to_send.setObjectName(u"dm_message_to_send")

        self.dm_send_box.addWidget(self.dm_message_to_send)

        self.dm_send_button = QPushButton(self.layoutWidget2)
        self.dm_send_button.setObjectName(u"dm_send_button")

        self.dm_send_box.addWidget(self.dm_send_button)


        self.dm_main_layout.addLayout(self.dm_send_box)

        self.dm_states.addWidget(self.dm)
        self.tabs.addTab(self.direct_message, "")
        self.voip_tab = QWidget()
        self.voip_tab.setObjectName(u"voip_tab")
        self.voip_states = QStackedWidget(self.voip_tab)
        self.voip_states.setObjectName(u"voip_states")
        self.voip_states.setGeometry(QRect(0, 0, 771, 651))
        self.voip_user_selection = QWidget()
        self.voip_user_selection.setObjectName(u"voip_user_selection")
        self.layoutWidget3 = QWidget(self.voip_user_selection)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(0, 0, 781, 651))
        self.voip_user_selection_2 = QVBoxLayout(self.layoutWidget3)
        self.voip_user_selection_2.setObjectName(u"voip_user_selection_2")
        self.voip_user_selection_2.setContentsMargins(200, 11, 200, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.voip_user_selection_2.addItem(self.horizontalSpacer_4)

        self.voip_selection_label = QLabel(self.layoutWidget3)
        self.voip_selection_label.setObjectName(u"voip_selection_label")
        self.voip_selection_label.setFont(font1)
        self.voip_selection_label.setAlignment(Qt.AlignCenter)

        self.voip_user_selection_2.addWidget(self.voip_selection_label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.voip_user_selection_2.addItem(self.horizontalSpacer_5)

        self.voip_online_users = QListWidget(self.layoutWidget3)
        self.voip_online_users.setObjectName(u"voip_online_users")

        self.voip_user_selection_2.addWidget(self.voip_online_users)

        self.voip_states.addWidget(self.voip_user_selection)
        self.voip = QWidget()
        self.voip.setObjectName(u"voip")
        self.voip_states.addWidget(self.voip)
        self.tabs.addTab(self.voip_tab, "")
        self.frame_bar = QWidget(self.centralwidget)
        self.frame_bar.setObjectName(u"frame_bar")
        self.frame_bar.setGeometry(QRect(0, 0, 801, 31))
        self.logged_in_as = QLabel(self.frame_bar)
        self.logged_in_as.setObjectName(u"logged_in_as")
        self.logged_in_as.setGeometry(QRect(14, 5, 691, 21))
        self.minimize_button = QPushButton(self.frame_bar)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(710, 0, 31, 31))
        self.x_button = QPushButton(self.frame_bar)
        self.x_button.setObjectName(u"x_button")
        self.x_button.setGeometry(QRect(760, 0, 31, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(0)
        self.dm_states.setCurrentIndex(1)
        self.voip_states.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.everyone_send_button.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.everyone_online_label.setText(QCoreApplication.translate("MainWindow", u"Online", None))
        self.tabs.setTabText(self.tabs.indexOf(self.everyone_message), QCoreApplication.translate("MainWindow", u"Everyone Messages", None))
        self.dm_selection_label.setText(QCoreApplication.translate("MainWindow", u"Select a user to Direct Message with", None))
        self.dm_back_button.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.dm_who_label.setText(QCoreApplication.translate("MainWindow", u"Talking with: ", None))
        self.dm_send_button.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.tabs.setTabText(self.tabs.indexOf(self.direct_message), QCoreApplication.translate("MainWindow", u"Direct Messages", None))
        self.voip_selection_label.setText(QCoreApplication.translate("MainWindow", u"Select a user to Voice/Video Call with", None))
        self.tabs.setTabText(self.tabs.indexOf(self.voip_tab), QCoreApplication.translate("MainWindow", u"Voice/Video", None))
        self.logged_in_as.setText(QCoreApplication.translate("MainWindow", u"Logged in as: ", None))
        self.minimize_button.setText(QCoreApplication.translate("MainWindow", u"\u2014", None))
        self.x_button.setText(QCoreApplication.translate("MainWindow", u"X", None))
    # retranslateUi

