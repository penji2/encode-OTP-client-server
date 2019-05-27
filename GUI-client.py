#!/usr/bin/python3
# -*- coding: utf-8 -*-
import client
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, \
                            QHBoxLayout, QMainWindow, QPlainTextEdit
from PyQt5 import QtGui, QtCore


class Messenger(QWidget):
    def __init__(self, client_obj, parent=None):
        super(Messenger, self).__init__(parent)

        """Object that allows us to attempt connection"""
        client_obj.connect()

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
        self.client_name = QLineEdit("Enter your name")
        self.client_message = QLineEdit("Your message")

        """Buttons"""
        name_btn = QPushButton("Give your name")
        name_btn.clicked.connect(self.get_client_name)
        name_btn.resize(name_btn.sizeHint())

        send_btn = QPushButton("SEND", self)
        send_btn.clicked.connect(client.Client.send_message)    #  HERE WILL BE SEND FUNCTION
        print(client_info.my_username)
        send_btn.resize(send_btn.sizeHint())

        """ Grid layout """
        layout = QGridLayout()
        layout.addWidget(client_label, 0, 0)
        layout.addWidget(self.client_name, 1, 0)
        layout.addWidget(name_btn, 2, 0)
        layout.addWidget(self.client_message, 3, 0)
        layout.addWidget(send_btn)

        self.setLayout(layout)

        self.show()

    def get_client_name(self):
        client.Client.my_username = self.client_name.text()
        print(client.Client.my_username)

    def get_client_message(self):
        pass

if __name__ == '__main__':
    """Initialize our GUI"""
    app = QApplication(sys.argv)

    """Initialize a Client.py object"""
    client_info = client.Client()

    """Initialize a main window"""
    window = Messenger(client_info)

    """Loop that shows our application"""
    sys.exit(app.exec_())


