"""
This file is a part of the source code for hisock-voip-app
This project has been licensed under the MIT license.
Copyright (c) 2022-present SSS-Says-Snek
"""

from __future__ import annotations

from PyQt6 import QtCore, QtGui, QtWidgets

# Form implementation generated from reading ui file 'src\ui\startup_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(470, 272)
        self.connect_button = QtWidgets.QPushButton(parent=Dialog)
        self.connect_button.setGeometry(QtCore.QRect(250, 220, 181, 41))
        self.connect_button.setObjectName("connect_button")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 20, 391, 181))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ip_label = QtWidgets.QLabel(parent=self.widget)
        self.ip_label.setObjectName("ip_label")
        self.gridLayout.addWidget(self.ip_label, 0, 0, 1, 1)
        self.ip_input = QtWidgets.QLineEdit(parent=self.widget)
        self.ip_input.setObjectName("ip_input")
        self.gridLayout.addWidget(self.ip_input, 0, 1, 1, 1)
        self.port_label = QtWidgets.QLabel(parent=self.widget)
        self.port_label.setObjectName("port_label")
        self.gridLayout.addWidget(self.port_label, 2, 0, 1, 1)
        self.port_input = QtWidgets.QLineEdit(parent=self.widget)
        self.port_input.setObjectName("port_input")
        self.gridLayout.addWidget(self.port_input, 2, 1, 1, 1)
        self.username_label = QtWidgets.QLabel(parent=self.widget)
        self.username_label.setObjectName("username_label")
        self.gridLayout.addWidget(self.username_label, 4, 0, 1, 1)
        self.username_input = QtWidgets.QLineEdit(parent=self.widget)
        self.username_input.setObjectName("username_input")
        self.gridLayout.addWidget(self.username_input, 4, 1, 1, 1)
        self.port_status = QtWidgets.QLabel(parent=self.widget)
        self.port_status.setObjectName("port_status")
        self.gridLayout.addWidget(self.port_status, 3, 0, 1, 2)
        self.ip_status = QtWidgets.QLabel(parent=self.widget)
        self.ip_status.setObjectName("ip_status")
        self.gridLayout.addWidget(self.ip_status, 1, 0, 1, 2)
        self.username_status = QtWidgets.QLabel(parent=self.widget)
        self.username_status.setObjectName("username_status")
        self.gridLayout.addWidget(self.username_status, 5, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.connect_button.setText(_translate("Dialog", "Connect to Server"))
        self.ip_label.setText(_translate("Dialog", "Enter Server IP"))
        self.port_label.setText(_translate("Dialog", "Enter Server Port"))
        self.username_label.setText(_translate("Dialog", "Enter Username"))
        self.port_status.setText(_translate("Dialog", "Temporary Status"))
        self.ip_status.setText(_translate("Dialog", "Temporary Status"))
        self.username_status.setText(_translate("Dialog", "Temporary Status"))
