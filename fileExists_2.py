# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileExists_2.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 438)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupbox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.groupbox.setFont(font)
        self.groupbox.setStyleSheet("QGroupBox {\n"
"    color: rgb(32, 74, 135);\n"
"}")
        self.groupbox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupbox.setObjectName("groupbox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupbox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidget = QtWidgets.QListWidget(self.groupbox)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupbox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.groupbox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.groupbox)
        self.pushButton.setStyleSheet("QPushButton {\n"
	"background-color: rgb(245, 121, 0);\n"
	"color: white;\n"
	"font-weight: bold;\n}")
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("orginal")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupbox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupbox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(9)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupbox)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
	"background-color: rgb(155, 64, 191);\n"
	"color: white;\n"
	"font-weight: bold;\n}")
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("new")
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupbox)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(32, 74, 135);\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}")
        self.pushButton_2.setObjectName("skip")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupbox)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(78, 154, 6);\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}")
        self.pushButton_3.setObjectName("replace")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupbox)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(32, 74, 135);\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}")
        self.pushButton_4.setObjectName("skipall")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupbox)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: rgb(78, 154, 6);\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}")
        self.pushButton_5.setObjectName("replaceall")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout.addWidget(self.groupbox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupbox.setTitle(_translate("MainWindow", "File Already Exists"))
        self.label.setText(_translate("MainWindow", "Orginal File"))
        self.pushButton.setText(_translate("MainWindow", "Rename"))
        self.label_2.setText(_translate("MainWindow", "New File"))
        self.pushButton_6.setText(_translate("MainWindow", "Rename"))
        self.pushButton_2.setText(_translate("MainWindow", "Skip"))
        self.pushButton_3.setText(_translate("MainWindow", "Replace"))
        self.pushButton_4.setText(_translate("MainWindow", "SkipAll"))
        self.pushButton_5.setText(_translate("MainWindow", "ReplaceAll"))

# class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
#     def __init__(self, *args, **kwargs):
#         super().__init__()
#         self.setupUi(self)
        
# if __name__ == "__main__":
#    app = QtWidgets.QApplication(sys.argv)
#    window = Ui_MainWindow()
#    window.show()
#    app.exec_()