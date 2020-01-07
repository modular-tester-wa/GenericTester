# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup_product.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlg_setup_product(object):
    def setupUi(self, dlg_setup_product):
        dlg_setup_product.setObjectName("dlg_setup_product")
        dlg_setup_product.resize(1280, 1024)
        self.btnOK = QtWidgets.QDialogButtonBox(dlg_setup_product)
        self.btnOK.setGeometry(QtCore.QRect(260, 672, 143, 65))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnOK.setFont(font)
        self.btnOK.setAutoFillBackground(True)
        self.btnOK.setStyleSheet(" QPushButton {\n"
"    border-style: ridge;\n"
"     border: 2px solid DarkSlateGray;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     width: 140px;\n"
"     height:  65px;\n"
"    font: 24px;\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QPushButton:!enabled {\n"
"     background-color:DarkGray;\n"
" }\n"
"\n"
"\n"
" QPushButton:default {\n"
"     border-color: navy; /* make the default button prominent */\n"
" }")
        self.btnOK.setOrientation(QtCore.Qt.Horizontal)
        self.btnOK.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.btnOK.setObjectName("btnOK")
        self.lbl_gnr = QtWidgets.QLabel(dlg_setup_product)
        self.lbl_gnr.setEnabled(True)
        self.lbl_gnr.setGeometry(QtCore.QRect(82, 536, 96, 36))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_gnr.setFont(font)
        self.lbl_gnr.setObjectName("lbl_gnr")
        self.lbl_product_id = QtWidgets.QLabel(dlg_setup_product)
        self.lbl_product_id.setGeometry(QtCore.QRect(76, 240, 106, 36))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_product_id.setFont(font)
        self.lbl_product_id.setObjectName("lbl_product_id")
        self.cb_product = QtWidgets.QComboBox(dlg_setup_product)
        self.cb_product.setGeometry(QtCore.QRect(202, 240, 211, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.cb_product.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cb_product.setFont(font)
        self.cb_product.setStyleSheet("")
        self.cb_product.setObjectName("cb_product")
        self.lbl_user_id = QtWidgets.QLabel(dlg_setup_product)
        self.lbl_user_id.setGeometry(QtCore.QRect(80, 154, 106, 36))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_user_id.setFont(font)
        self.lbl_user_id.setObjectName("lbl_user_id")
        self.cb_user = QtWidgets.QComboBox(dlg_setup_product)
        self.cb_user.setGeometry(QtCore.QRect(200, 150, 211, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.cb_user.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cb_user.setFont(font)
        self.cb_user.setStyleSheet("")
        self.cb_user.setObjectName("cb_user")
        self.btn_exit_os = QtWidgets.QPushButton(dlg_setup_product)
        self.btn_exit_os.setEnabled(True)
        self.btn_exit_os.setGeometry(QtCore.QRect(1082, 926, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_exit_os.setFont(font)
        self.btn_exit_os.setStyleSheet(" QPushButton {\n"
"    border-style: ridge;\n"
"     border: 2px solid DarkSlateGray;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QPushButton:!enabled {\n"
"     background-color:DarkGray;\n"
" }\n"
"")
        self.btn_exit_os.setObjectName("btn_exit_os")
        self.btn_shut_down = QtWidgets.QPushButton(dlg_setup_product)
        self.btn_shut_down.setEnabled(True)
        self.btn_shut_down.setGeometry(QtCore.QRect(1080, 30, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_shut_down.setFont(font)
        self.btn_shut_down.setStyleSheet(" QPushButton {\n"
"    border-style: ridge;\n"
"     border: 2px solid DarkSlateGray;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QPushButton:!enabled {\n"
"     background-color:DarkGray;\n"
" }\n"
"")
        self.btn_shut_down.setObjectName("btn_shut_down")
        self.btn_grn = QtWidgets.QPushButton(dlg_setup_product)
        self.btn_grn.setEnabled(True)
        self.btn_grn.setGeometry(QtCore.QRect(204, 534, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_grn.setFont(font)
        self.btn_grn.setStyleSheet(" QPushButton {\n"
"    border-style: ridge;\n"
"     border: 2px solid DarkSlateGray;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QPushButton:!enabled {\n"
"     background-color:DarkGray;\n"
" }\n"
"")
        self.btn_grn.setObjectName("btn_grn")
        self.lbl_nest_id = QtWidgets.QLabel(dlg_setup_product)
        self.lbl_nest_id.setGeometry(QtCore.QRect(102, 330, 79, 36))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_nest_id.setFont(font)
        self.lbl_nest_id.setObjectName("lbl_nest_id")
        self.cb_nest = QtWidgets.QComboBox(dlg_setup_product)
        self.cb_nest.setGeometry(QtCore.QRect(200, 330, 211, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.cb_nest.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cb_nest.setFont(font)
        self.cb_nest.setStyleSheet("")
        self.cb_nest.setObjectName("cb_nest")
        self.cb_insert = QtWidgets.QComboBox(dlg_setup_product)
        self.cb_insert.setGeometry(QtCore.QRect(200, 416, 211, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.cb_insert.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cb_insert.setFont(font)
        self.cb_insert.setStyleSheet("")
        self.cb_insert.setObjectName("cb_insert")
        self.lbl_insert_id = QtWidgets.QLabel(dlg_setup_product)
        self.lbl_insert_id.setGeometry(QtCore.QRect(72, 416, 103, 36))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_insert_id.setFont(font)
        self.lbl_insert_id.setObjectName("lbl_insert_id")

        self.retranslateUi(dlg_setup_product)
        self.btnOK.accepted.connect(dlg_setup_product.accept)
        self.cb_product.currentIndexChanged['int'].connect(dlg_setup_product.cb_product_index_change)
        self.cb_user.currentIndexChanged['int'].connect(dlg_setup_product.cb_user_index_change)
        self.btn_shut_down.clicked.connect(dlg_setup_product.btn_shut_down_click)
        self.btn_exit_os.clicked.connect(dlg_setup_product.btn_exit_os_click)
        self.btn_grn.clicked.connect(dlg_setup_product.btn_grn_click)
        self.cb_nest.currentIndexChanged['int'].connect(dlg_setup_product.cb_nest_index_change)
        self.cb_insert.currentIndexChanged['int'].connect(dlg_setup_product.cb_insert_index_change)
        QtCore.QMetaObject.connectSlotsByName(dlg_setup_product)

    def retranslateUi(self, dlg_setup_product):
        _translate = QtCore.QCoreApplication.translate
        dlg_setup_product.setWindowTitle(_translate("dlg_setup_product", "Setup product"))
        self.lbl_gnr.setText(_translate("dlg_setup_product", "GRN #:"))
        self.lbl_product_id.setText(_translate("dlg_setup_product", "Product:"))
        self.lbl_user_id.setText(_translate("dlg_setup_product", "User ID:"))
        self.btn_exit_os.setText(_translate("dlg_setup_product", "EXIT TO OS"))
        self.btn_shut_down.setText(_translate("dlg_setup_product", "SHUT DOWN"))
        self.btn_grn.setText(_translate("dlg_setup_product", "0"))
        self.lbl_nest_id.setText(_translate("dlg_setup_product", "NEST:"))
        self.lbl_insert_id.setText(_translate("dlg_setup_product", "INSERT:"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlg_setup_product = QtWidgets.QDialog()
    ui = Ui_dlg_setup_product()
    ui.setupUi(dlg_setup_product)
    dlg_setup_product.show()
    sys.exit(app.exec_())
