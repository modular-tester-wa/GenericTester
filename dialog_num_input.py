
import PyQt5
from PyQt5.QtWidgets import *
from num_keypad_ui import Ui_dlgNumInput

"""
Numeric input Dialog
"""


class DialogNumInput(QDialog, Ui_dlgNumInput):
    def __init__(self, *args, **kwds):
        QWidget.__init__(self)
        self.ui = Ui_dlgNumInput()
        self.ui.setupUi(self)
        self.window_width = 260
        self.window_height = 320
        self.setFixedSize(self.window_width, self.window_height)
        self.text = ""
        self.ui.le_text.setText(self.text)
        self.dot_enabled = False
        self.password_input = False

    def update_input_text(self):
        if self.password_input:
            pass_text = "*" * len(self.text)
            self.ui.le_text.setText(pass_text)
        else:
            self.ui.le_text.setText(self.text)

    def pb_1_click(self):
        self.text += "1"
        self.update_input_text()

    def pb_2_click(self):
        self.text += "2"
        self.update_input_text()

    def pb_3_click(self):
        self.text += "3"
        self.update_input_text()

    def pb_4_click(self):
        self.text += "4"
        self.update_input_text()

    def pb_5_click(self):
        self.text += "5"
        self.update_input_text()

    def pb_6_click(self):
        self.text += "6"
        self.ui.le_text.setText(self.text)

    def pb_7_click(self):
        self.text += "7"
        self.update_input_text()

    def pb_8_click(self):
        self.text += "8"
        self.update_input_text()

    def pb_9_click(self):
        self.text += "9"
        self.update_input_text()

    def pb_0_click(self):
        self.text += "0"
        self.update_input_text()

    def pb_dot_click(self):
        if self.dot_enabled:
            self.text += "."
            self.update_input_text()
            self.ui.pb_dot.setEnabled(False)

    def pb_bkspc_click(self):
        if self.text != "":
            self.text = self.text[:len(self.text)-1]
            self.update_input_text()
            if self.dot_enabled:
                self.ui.pb_dot.setDisabled("." in self.text)