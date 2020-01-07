
from os import listdir
from PyQt5 import QtCore
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject, QIODevice, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

from setup_product_ui import Ui_dlg_setup_product
from dialog_num_input import DialogNumInput

# from inputFile import extrac_data_file, read_words

"""
Setup product
"""


class DialogSetupProduct(QDialog, Ui_dlg_setup_product):
    #def __init__(self, *args, **kwds):
    def __init__(self, nest_id, parent=None):
        QWidget.__init__(self)
        self.ui = Ui_dlg_setup_product()
        self.ui.setupUi(self)
        self.setWindowTitle("MAIN APP")
        self.window_width = 1280
        self.window_height = 1024
        self.setFixedSize(self.window_width, self.window_height)
        self.move(0, 0)
        #self.setWindowFlags(Qt.FramelessWindowHint)
        #self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)

        # Application
        self.grn_no = "0"
        self.nest_id = nest_id
        self.fill_user_list()
        self.insert_list = []
        self.fill_product_list()
        self.fill_nest_list()
        self.fill_insert_list()
        self.user_name = ""
        self.product_name = ""
        self.insert_id = ""
        self.insert_number_duts = ""
        self.insert_template_name = ""
        self.action = 0
        self.ui.cb_user.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.enable_ok()

    def fill_user_list(self):
        self.ui.cb_user.addItem("")
        self.ui.cb_user.setModelColumn(0)
        file_name = "products/user_list.txt"
        file = open(file_name, "r")
        file_lines = [line.rstrip('\n') for line in file]
        file.close()
        for line in file_lines:
            if line[0] != "#" and line != "":
                self.ui.cb_user.addItem(line)

    def fill_product_list(self):
        self.ui.cb_product.clear()
        self.ui.cb_product.addItem("")
        self.ui.cb_product.setModelColumn(0)
        file_name = "products/product_list.txt"
        file = open(file_name, "r")
        file_lines = [line.rstrip('\n') for line in file]
        file.close()
        for line in file_lines:
            if line[0] != "#" and line != "":
                self.ui.cb_product.addItem(line)

    def fill_nest_list(self):
        self.ui.cb_nest.clear()
        self.ui.cb_nest.addItem("")
        self.ui.cb_nest.setModelColumn(0)
        file_name = "products/nest_list.txt"
        file = open(file_name, "r")
        file_lines = [line.rstrip('\n') for line in file]
        file.close()
        for line in file_lines:
            if line[0] != "#" and line != "":
                self.ui.cb_nest.addItem(line)

    def fill_insert_list(self):
        self.ui.cb_insert.clear()
        self.ui.cb_insert.addItem("")
        self.ui.cb_insert.setModelColumn(0)
        file_name = "products/insert_list.txt"
        file = open(file_name, "r")
        file_lines = [line.rstrip('\n') for line in file]
        file.close()
        for line in file_lines:
            if line[0] != "#" and line != "":
                self.insert_list.append(line)
                self.ui.cb_insert.addItem(line[:-2])

    def cb_user_index_change(self):
        if self.ui.cb_user.currentIndex():
            self.ui.cb_user.setStyleSheet("")
            self.user_name = self.ui.cb_user.currentText()
        else:
            self.ui.cb_user.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.enable_ok()

    def cb_product_index_change(self):
        if self.ui.cb_product.currentIndex():
            self.ui.cb_product.setStyleSheet("")
            self.product_name = self.ui.cb_product.currentText()
        else:
            self.ui.cb_product.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.enable_ok()

    def cb_nest_index_change(self):
        if self.ui.cb_nest.currentIndex():
            self.ui.cb_nest.setStyleSheet("")
            self.nest_id = self.ui.cb_nest.currentText()
        else:
            self.ui.cb_nest.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.enable_ok()

    def cb_insert_index_change(self):
        if self.ui.cb_insert.currentIndex():
            self.ui.cb_insert.setStyleSheet("")
            self.insert_number_duts = self.insert_list[self.ui.cb_insert.currentIndex()-1][-1:]
            self.insert_id = self.ui.cb_insert.currentText()
        else:
            self.ui.cb_insert.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.enable_ok()

    def btn_grn_click(self):
        dlg = DialogNumInput()
        dlg.move(500, 150)
        dlg.setWindowTitle(" INPUT GRN ")
        dlg.ui.pb_dot.setEnabled(False)
        dlg.exec_()
        self.grn_no = dlg.text
        dlg.close()
        self.ui.btn_grn.setText(self.grn_no)
        if self.grn_no == "":
            self.grn_no = "0"
            self.ui.btn_grn.setStyleSheet("background-color: rgb(85, 170, 255);")
        else:
            self.ui.btn_grn.setStyleSheet("")
        self.enable_ok()
            
    def enable_ok(self):
        enable = self.ui.cb_user.currentIndex() * \
                 self.ui.cb_product.currentIndex() * \
                 self.ui.cb_nest.currentIndex() * \
                 self.ui.cb_insert.currentIndex() * \
                 int(self.grn_no)
        self.ui.btnOK.setEnabled(enable)

    def btn_shut_down_click(self):
        dlg = DialogNumInput()
        dlg.move(600, 400)
        dlg.setWindowTitle("INPUT PASSWORD")
        dlg.ui.pb_dot.setEnabled(False)
        dlg.password_input = True
        dlg.exec_()
        if dlg.text == "1005":
            self.action = 2
            self.close()

    def btn_exit_os_click(self):
        dlg = DialogNumInput()
        dlg.move(600, 400)
        dlg.setWindowTitle("INPUT PASSWORD")
        dlg.ui.pb_dot.setEnabled(False)
        dlg.password_input = True
        dlg.exec_()
        if dlg.text == "8299":
            self.action = 3
            self.close()
        else:
            self.action = 3
            self.close()