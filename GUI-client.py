#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, \
                            QHBoxLayout, QMainWindow, QPlainTextEdit
from PyQt5 import QtGui, QtCore


class Messenger(QWidget):
    def __init__(self):

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

        """ONE line edit fields"""
        self.client_edt = QPlainTextEdit("Your message")

        """Buttons"""
        send_btn = QPushButton("SEND", self)

        # send_btn.clicked.connect(SEND FUNCTION HERE)

        send_btn.resize(send_btn.sizeHint())

        """ Grid layout """
        layout = QGridLayout()
        layout.addWidget(client_label, 0, 1)
        layout.addWidget(self.client_edt, 1, 0, 50, 50)
        layout.addWidget(send_btn)

        self.setLayout(layout)

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Messenger()

    sys.exit(app.exec_())


