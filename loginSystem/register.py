# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(660, 409)
        font = QtGui.QFont()
        font.setFamily("黑体")
        Form.setFont(font)
        Form.setStyleSheet("QWidget#Form{border-image:url(:/register/wallpaper/weather.jpg)}\n"
"\n"
"")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 190, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 240, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 301, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 350, 171, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(180, 179, 191, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(" background-color: transparent;\n"
"        border: none;\n"
"        border-bottom: 2px solid #000;\n"
"        outline: none;\n"
"        padding-bottom: 10px;\n"
"        text-align: center;\n"
"        width: 400px;\n"
"        font-size: 300%;\n"
"        color: #000000;\n"
"        font-weight: 100;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 229, 191, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(" background-color: transparent;\n"
"        border: none;\n"
"        border-bottom: 2px solid #000;\n"
"        outline: none;\n"
"        padding-bottom: 10px;\n"
"        text-align: center;\n"
"        width: 400px;\n"
"        font-size: 300%;\n"
"        color: #000;\n"
"        font-weight: 100;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 289, 191, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet(" background-color: transparent;\n"
"        border: none;\n"
"        border-bottom: 2px solid #000;\n"
"        outline: none;\n"
"        padding-bottom: 10px;\n"
"        text-align: center;\n"
"        width: 400px;\n"
"        font-size: 300%;\n"
"        color: #000;\n"
"        font-weight: 100;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "账       号："))
        self.label_2.setText(_translate("Form", "密       码："))
        self.label_3.setText(_translate("Form", "确认密码："))
        self.pushButton.setText(_translate("Form", "注册"))
import resource.source_rc
