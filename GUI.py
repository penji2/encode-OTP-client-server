#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PyQt5.QtGui import QIcon


class First(QWidget):
    def __init__(self):

        super().__init__()
        self.interface()

    def interface(self):
        # labels
        label = QLabel("Liczba1", self)

        layout = QGridLayout()
        layout.addWidget(label, 0, 0)

        self.setLayout(layout)

        self.setGeometry(20, 20, 300, 100)
        self.setWindowTitle("TITLE")
        self.resize(550, 300)

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = First()

    sys.exit(app.exec_())


