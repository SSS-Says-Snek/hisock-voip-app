# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startup_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(470, 272)
        self.connect_button = QPushButton(Dialog)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setGeometry(QRect(250, 220, 181, 41))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 20, 391, 181))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.ip_label = QLabel(self.layoutWidget)
        self.ip_label.setObjectName(u"ip_label")

        self.gridLayout.addWidget(self.ip_label, 0, 0, 1, 1)

        self.ip_input = QLineEdit(self.layoutWidget)
        self.ip_input.setObjectName(u"ip_input")

        self.gridLayout.addWidget(self.ip_input, 0, 1, 1, 1)

        self.port_label = QLabel(self.layoutWidget)
        self.port_label.setObjectName(u"port_label")

        self.gridLayout.addWidget(self.port_label, 2, 0, 1, 1)

        self.port_input = QLineEdit(self.layoutWidget)
        self.port_input.setObjectName(u"port_input")

        self.gridLayout.addWidget(self.port_input, 2, 1, 1, 1)

        self.username_label = QLabel(self.layoutWidget)
        self.username_label.setObjectName(u"username_label")

        self.gridLayout.addWidget(self.username_label, 4, 0, 1, 1)

        self.username_input = QLineEdit(self.layoutWidget)
        self.username_input.setObjectName(u"username_input")

        self.gridLayout.addWidget(self.username_input, 4, 1, 1, 1)

        self.port_status = QLabel(self.layoutWidget)
        self.port_status.setObjectName(u"port_status")

        self.gridLayout.addWidget(self.port_status, 3, 0, 1, 2)

        self.ip_status = QLabel(self.layoutWidget)
        self.ip_status.setObjectName(u"ip_status")

        self.gridLayout.addWidget(self.ip_status, 1, 0, 1, 2)

        self.username_status = QLabel(self.layoutWidget)
        self.username_status.setObjectName(u"username_status")

        self.gridLayout.addWidget(self.username_status, 5, 0, 1, 2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.connect_button.setText(QCoreApplication.translate("Dialog", u"Connect to Server", None))
        self.ip_label.setText(QCoreApplication.translate("Dialog", u"Enter Server IP", None))
        self.port_label.setText(QCoreApplication.translate("Dialog", u"Enter Server Port", None))
        self.username_label.setText(QCoreApplication.translate("Dialog", u"Enter Username", None))
        self.port_status.setText(QCoreApplication.translate("Dialog", u"Temporary Status", None))
        self.ip_status.setText(QCoreApplication.translate("Dialog", u"Temporary Status", None))
        self.username_status.setText(QCoreApplication.translate("Dialog", u"Temporary Status", None))
    # retranslateUi

