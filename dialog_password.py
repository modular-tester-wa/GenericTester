
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from passw_input_ui import Ui_dlgPassword

"""
Numeric input Dialog
"""

class Password(QDialog, Ui_dlgPassword):
    #def __init__(self, *args, **kwds):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.ui = Ui_dlgPassword()
        self.ui.setupUi(self)
        self.setWindowTitle("MAIN APP")
        self.window_width = 540
        self.window_height = 230
        self.setFixedSize(self.window_width, self.window_height)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        self.text = ""

    def check(self):
        if len(self.text) == 4:
            self.close()

    def pb_1(self):
        self.text += "1"
        self.check()

    def pb_2(self):
        self.text += "2"
        self.check()

    def pb_3(self):
        self.text += "3"
        self.check()

    def pb_4(self):
        self.text += "4"
        self.check()

    def pb_5(self):
        self.text += "5"
        self.check()

    def pb_6(self):
        self.text += "A"
        self.check()

    def pb_7(self):
        self.text += "B"
        self.check()

    def pb_8(self):
        self.text += "C"
        self.check()

    def pb_9(self):
        self.text += "D"
        self.check()

    def pb_0(self):
        self.text += "E"
        self.check()