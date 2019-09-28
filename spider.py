# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/jormungandr/Desktop/Spider/spider.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(544, 496)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 501, 33))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(430, 50, 94, 66))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 190, 101, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(430, 120, 91, 54))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(20, 50, 401, 411))
        self.tableView.setObjectName("tableView")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(30, 470, 87, 20))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Form)
        self.pushButton_3.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "龙族5爬虫v1.1"))
        self.label.setText(_translate("Form", "网址"))
        self.lineEdit.setText(_translate("Form", "http://longzu5.yunzhonggexiaoshuo.com/"))
        self.pushButton.setText(_translate("Form", "获取更新"))
        self.pushButton_3.setText(_translate("Form", "退出程序"))
        self.pushButton_4.setText(_translate("Form", "查看内容"))
        self.pushButton_2.setText(_translate("Form", "更新数据"))
        self.label_2.setText(_translate("Form", "未更新"))
        self.label_3.setText(_translate("Form", "总章节"))
        self.checkBox.setText(_translate("Form", "全选"))

