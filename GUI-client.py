#!/usr/bin/python3
# -*- coding: utf-8 -*-
import client
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, \
                            QHBoxLayout, QMainWindow, QPlainTextEdit
from PyQt5 import QtGui, QtCore


class Messenger(QWidget):
    def __init__(self):
        client.connect()
        super(Messenger, self).__init__()
        """Geometry and window positioning"""
        self.setGeometry(100, 200, 640, 480)
        self.setWindowIcon(QtGui.QIcon('messenger.png'))
        self.setWindowTitle("Mysterious messenger")

        """ """
        self.home()

    def home(self):

        """ labels """
        client_label = QLabel("Client", self)

        """edit fields"""
        self.information = QLineEdit("Enter your name")
        self.client_message = QPlainTextEdit("Your message")

        """Buttons"""
        name_btn = QPushButton("Give your name")
        name_btn.clicked.connect(client.user_name)
        name_btn.resize(name_btn.sizeHint())

        send_btn = QPushButton("SEND", self)
        send_btn.clicked.connect(client.send_message)
        send_btn.resize(send_btn.sizeHint())

        """ Grid layout """
        layout = QGridLayout()
        layout.addWidget(client_label, 0, 0)
        layout.addWidget(self.information, 1, 0)
        layout.addWidget(name_btn, 2, 0)
        layout.addWidget(self.client_message, 3, 0)
        layout.addWidget(send_btn)

        self.setLayout(layout)

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Messenger()

    sys.exit(app.exec_())


