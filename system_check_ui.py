# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'system_check.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlg_system_check(object):
    def setupUi(self, dlg_system_check):
        dlg_system_check.setObjectName("dlg_system_check")
        dlg_system_check.resize(443, 188)
        self.lbl_lbl_mm_port = QtWidgets.QLabel(dlg_system_check)
        self.lbl_lbl_mm_port.setGeometry(QtCore.QRect(15, 96, 180, 36))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_lbl_mm_port.setFont(font)
        self.lbl_lbl_mm_port.setObjectName("lbl_lbl_mm_port")
        self.lbl_mm_port = QtWidgets.QLabel(dlg_system_check)
        self.lbl_mm_port.setGeometry(QtCore.QRect(198, 98, 106, 36))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_mm_port.setFont(font)
        self.lbl_mm_port.setObjectName("lbl_mm_port")
        self.lbl_lbl_sg_port = QtWidgets.QLabel(dlg_system_check)
        self.lbl_lbl_sg_port.setGeometry(QtCore.QRect(15, 134, 180, 36))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_lbl_sg_port.setFont(font)
        self.lbl_lbl_sg_port.setObjectName("lbl_lbl_sg_port")
        self.lbl_sg_port = QtWidgets.QLabel(dlg_system_check)
        self.lbl_sg_port.setGeometry(QtCore.QRect(198, 134, 106, 36))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_sg_port.setFont(font)
        self.lbl_sg_port.setObjectName("lbl_sg_port")
        self.pbProgress = QtWidgets.QProgressBar(dlg_system_check)
        self.pbProgress.setGeometry(QtCore.QRect(106, 18, 118, 25))
        self.pbProgress.setMaximum(8)
        self.pbProgress.setProperty("value", 0)
        self.pbProgress.setObjectName("pbProgress")
        self.lbl_lbl_progress = QtWidgets.QLabel(dlg_system_check)
        self.lbl_lbl_progress.setGeometry(QtCore.QRect(15, 10, 95, 36))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_lbl_progress.setFont(font)
        self.lbl_lbl_progress.setObjectName("lbl_lbl_progress")
        self.lbl_check_info = QtWidgets.QLabel(dlg_system_check)
        self.lbl_check_info.setGeometry(QtCore.QRect(15, 46, 180, 36))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_check_info.setFont(font)
        self.lbl_check_info.setObjectName("lbl_check_info")

        self.retranslateUi(dlg_system_check)
        QtCore.QMetaObject.connectSlotsByName(dlg_system_check)

    def retranslateUi(self, dlg_system_check):
        _translate = QtCore.QCoreApplication.translate
        dlg_system_check.setWindowTitle(_translate("dlg_system_check", "System check"))
        self.lbl_lbl_mm_port.setText(_translate("dlg_system_check", "MM  on  port:"))
        self.lbl_mm_port.setText(_translate("dlg_system_check", "?"))
        self.lbl_lbl_sg_port.setText(_translate("dlg_system_check", "SG  on  port:"))
        self.lbl_sg_port.setText(_translate("dlg_system_check", "?"))
        self.lbl_lbl_progress.setText(_translate("dlg_system_check", "Check:"))
        self.lbl_check_info.setText(_translate("dlg_system_check", "...."))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlg_system_check = QtWidgets.QDialog()
    ui = Ui_dlg_system_check()
    ui.setupUi(dlg_system_check)
    dlg_system_check.show()
    sys.exit(app.exec_())
