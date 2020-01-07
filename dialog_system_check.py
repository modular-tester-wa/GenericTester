
from os import listdir
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from system_check_ui import Ui_dlg_system_check
"""
System check dialog
"""


class DialogSystemCheck(QDialog, Ui_dlg_system_check):
    #def __init__(self, *args, **kwds):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.ui = Ui_dlg_system_check()
        self.ui.setupUi(self)
        self.setWindowTitle("MAIN APP")
        # self.window_width = 800
        # self.window_height = 500
        # self.setFixedSize(self.window_width, self.window_height)
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        # self.setModal(False)

        # Application