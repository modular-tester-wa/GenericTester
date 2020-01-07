# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'num_keypad.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgNumInput(object):
    def setupUi(self, dlgNumInput):
        dlgNumInput.setObjectName("dlgNumInput")
        dlgNumInput.setWindowModality(QtCore.Qt.ApplicationModal)
        dlgNumInput.resize(535, 641)
        dlgNumInput.setSizeGripEnabled(True)
        dlgNumInput.setModal(False)
        self.pb_7 = QtWidgets.QPushButton(dlgNumInput)
        self.pb_7.setGeometry(QtCore.QRect(5, 65, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pb_7.setFont(font)
        self.pb_7.setStyleSheet(" QPushButton {\n"
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
" }")
        self.pb_7.setFlat(False)
        self.pb_7.setObjectName("pb_7")
        self.le_text = QtWidgets.QLineEdit(dlgNumInput)
        self.le_text.setGeometry(QtCore.QRect(5, 5, 246, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.le_text.setFont(font)
        self.le_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.le_text.setStyleSheet(" QPushButton {\n"
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
" }")
        self.le_text.setMaxLength(10)
        self.le_text.setFrame(True)
        self.le_text.setAlignment(QtCore.Qt.AlignCenter)
        self.le_text.setReadOnly(True)
        self.le_text.setObjectName("le_text")
        self.pb_8 = QtWidgets.QPushButton(dlgNumInput)
        self.pb_8.setGeometry(QtCore.QRect(65, 65, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pb_8.setFont(font)
        self.pb_8.setStyleSheet(" QPushButton {\n"
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
" }")
        self.pb_8.setFlat(False)
        self.pb_8.setObjectName("pb_8")
        self.pb_9 = QtWidgets.QPushButton(dlgNumInput)
        self.pb_9.setGeometry(QtCore.QRect(125, 65, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pb_9.setFont(font)
        self.pb_9.setStyleSheet(" QPushButton {\n"
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
" }")
        self.pb_9.setFlat(False)
        self.pb_9.setObjectName("pb_9")
        self.pb_6 = QtWidgets.QPushButton(dlgNumInput)
        self.pb_6.setGeometry(QtCore.QRect(125, 125, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pb_6.setFont(font)
        self.pb_6.setStyleSheet(" QPushButton {\n"
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
" }")
        self.pb_6.setFlat(False)
        self.pb_6.setObjectName("pb_6")
        self.pb_5 = QtWidgets.QPushButton(dlgNumInput)
        self.pb_5.setGeometry(QtCore.QRect(65, 125, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pb_5.setFont(font)
        self.pb_5.setStyleSheet(" QPushButton {\n"
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
" }")
        self.pb_5.setFlat(False)
        self.pb_5.setObjectName("pb_5")
        self.pb_4 = QtWidgets.QPushButton(dlgNumInput)
        self.pb_4.setGeometry(QtCore.QRect(5, 125, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pb_4.setFont(font)
        self.pb_4.setStyleSheet(" QPushButton {\n"
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
" }")
        self.pb_4.setFlat(False)
        self.pb_4.setObjectName("pb_4")
        self.pb_1 = QtWidgets.QPushButton(dlgNumInput)
        self.pb_1.setGeometry(QtCore.QRect(5, 185, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pb_1.setFont(font)
        self.pb_1.setStyleSheet(" QPushButton {\n"
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
" }")
        self.pb_1.setFlat(False)
        self.pb_1.setObjectName("pb_1")
        self.pb_2 = QtWidgets.QPushButton(dlgNumInput)
        self.pb_2.setGeometry(QtCore.QRect(65, 185, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pb_2.setFont(font)
        self.pb_2.setStyleSheet(" QPushButton {\n"
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
" }")
        self.pb_2.setFlat(False)
        self.pb_2.setObjectName("pb_2")
        self.pb_3 = QtWidgets.QPushButton(dlgNumInput)
        self.pb_3.setGeometry(QtCore.QRect(125, 185, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pb_3.setFont(font)
        self.pb_3.setStyleSheet(" QPushButton {\n"
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
" }")
        self.pb_3.setFlat(False)
        self.pb_3.setObjectName("pb_3")
        self.pb_dot = QtWidgets.QPushButton(dlgNumInput)
        self.pb_dot.setGeometry(QtCore.QRect(125, 245, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pb_dot.setFont(font)
        self.pb_dot.setStyleSheet(" QPushButton {\n"
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
" }")
        self.pb_dot.setFlat(False)
        self.pb_dot.setObjectName("pb_dot")
        self.pb_enter = QtWidgets.QPushButton(dlgNumInput)
        self.pb_enter.setGeometry(QtCore.QRect(185, 185, 66, 121))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pb_enter.setFont(font)
        self.pb_enter.setStyleSheet(" QPushButton {\n"
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
" }")
        self.pb_enter.setFlat(False)
        self.pb_enter.setObjectName("pb_enter")
        self.pb_0 = QtWidgets.QPushButton(dlgNumInput)
        self.pb_0.setGeometry(QtCore.QRect(5, 245, 120, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pb_0.setFont(font)
        self.pb_0.setStyleSheet(" QPushButton {\n"
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
" }")
        self.pb_0.setFlat(False)
        self.pb_0.setObjectName("pb_0")
        self.pb_bkspc = QtWidgets.QPushButton(dlgNumInput)
        self.pb_bkspc.setGeometry(QtCore.QRect(185, 65, 66, 121))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pb_bkspc.setFont(font)
        self.pb_bkspc.setStyleSheet(" QPushButton {\n"
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
" }")
        self.pb_bkspc.setFlat(False)
        self.pb_bkspc.setObjectName("pb_bkspc")

        self.retranslateUi(dlgNumInput)
        self.pb_1.clicked.connect(dlgNumInput.pb_1_click)
        self.pb_2.clicked.connect(dlgNumInput.pb_2_click)
        self.pb_3.clicked.connect(dlgNumInput.pb_3_click)
        self.pb_4.clicked.connect(dlgNumInput.pb_4_click)
        self.pb_5.clicked.connect(dlgNumInput.pb_5_click)
        self.pb_6.clicked.connect(dlgNumInput.pb_6_click)
        self.pb_7.clicked.connect(dlgNumInput.pb_7_click)
        self.pb_8.clicked.connect(dlgNumInput.pb_8_click)
        self.pb_9.clicked.connect(dlgNumInput.pb_9_click)
        self.pb_0.clicked.connect(dlgNumInput.pb_0_click)
        self.pb_dot.clicked.connect(dlgNumInput.pb_dot_click)
        self.pb_enter.clicked.connect(dlgNumInput.accept)
        self.pb_bkspc.clicked.connect(dlgNumInput.pb_bkspc_click)
        QtCore.QMetaObject.connectSlotsByName(dlgNumInput)
        dlgNumInput.setTabOrder(self.pb_1, self.pb_2)
        dlgNumInput.setTabOrder(self.pb_2, self.pb_3)
        dlgNumInput.setTabOrder(self.pb_3, self.pb_4)
        dlgNumInput.setTabOrder(self.pb_4, self.pb_5)
        dlgNumInput.setTabOrder(self.pb_5, self.pb_6)
        dlgNumInput.setTabOrder(self.pb_6, self.pb_7)
        dlgNumInput.setTabOrder(self.pb_7, self.pb_8)
        dlgNumInput.setTabOrder(self.pb_8, self.pb_9)
        dlgNumInput.setTabOrder(self.pb_9, self.pb_0)
        dlgNumInput.setTabOrder(self.pb_0, self.pb_dot)
        dlgNumInput.setTabOrder(self.pb_dot, self.pb_enter)
        dlgNumInput.setTabOrder(self.pb_enter, self.le_text)

    def retranslateUi(self, dlgNumInput):
        _translate = QtCore.QCoreApplication.translate
        dlgNumInput.setWindowTitle(_translate("dlgNumInput", "Dialog"))
        self.pb_7.setText(_translate("dlgNumInput", "7"))
        self.le_text.setText(_translate("dlgNumInput", "0"))
        self.pb_8.setText(_translate("dlgNumInput", "8"))
        self.pb_9.setText(_translate("dlgNumInput", "9"))
        self.pb_6.setText(_translate("dlgNumInput", "6"))
        self.pb_5.setText(_translate("dlgNumInput", "5"))
        self.pb_4.setText(_translate("dlgNumInput", "4"))
        self.pb_1.setText(_translate("dlgNumInput", "1"))
        self.pb_2.setText(_translate("dlgNumInput", "2"))
        self.pb_3.setText(_translate("dlgNumInput", "3"))
        self.pb_dot.setText(_translate("dlgNumInput", "."))
        self.pb_enter.setText(_translate("dlgNumInput", "OK"))
        self.pb_0.setText(_translate("dlgNumInput", "0"))
        self.pb_bkspc.setText(_translate("dlgNumInput", "<"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgNumInput = QtWidgets.QDialog()
    ui = Ui_dlgNumInput()
    ui.setupUi(dlgNumInput)
    dlgNumInput.show()
    sys.exit(app.exec_())
