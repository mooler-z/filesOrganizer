import os, sys, shutil
from PyQt5 import QtCore, QtGui, QtWidgets
from organize_util import Renamer, Organizer
from organize_util import general_extensions
from copy import deepcopy
from fileExists_2 import Ui_MainWindow as fileExist


class Ui_MainWindow():
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 666)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: rgba(224, 224, 224, 222);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(224, 224, 224);\n"
"    color: rgb(115, 210, 22);\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_13.clicked.connect(self.setRenameDirectory)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("QPushButton {\n"
"    background-color: rgb(115, 210, 22);\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/folder-open.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_5.addWidget(self.pushButton_13, 0, 2, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_5.addWidget(self.lineEdit_9, 0, 0, 1, 1)
        styleSheet = """
                QComboBox {
                        border: 1px solid gray;
                        border-radius: 3px;
                        min-width: 2em;
                        color: black;
                }

                QComboBox:editable {
                        background: white;
                }
                QComboBox:!editable, QComboBox::drop-down:editable {
                        background: white;
                }
                QComboBox::down-arrow {
                        background: white;
                        image: url(angleDown.svg);
                }
        """
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["all"])
        self.comboBox.currentTextChanged.connect(self.updateCbValue)
        self.comboBox.setStyleSheet(styleSheet)
        self.gridLayout_5.addWidget(self.comboBox, 0, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_5)
        self.line_5 = QtWidgets.QFrame(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(False)
        font.setWeight(50)
        self.line_5.setFont(font)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_5.addWidget(self.line_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_14.clicked.connect(self.addNameFiles)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("QPushButton {\n"
"    background-color: rgb(78, 154, 6);\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/plus-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon1)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_8.addWidget(self.pushButton_14)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_8.addWidget(self.lineEdit_10)
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_19.clicked.connect(self.renameFiles)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("QPushButton {\n"
"    background-color: rgb(78, 154, 6);\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}")
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_8.addWidget(self.pushButton_19)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.verticalLayout_5.addWidget(self.textEdit)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.progressBar_2 = QtWidgets.QProgressBar(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.progressBar_2.setFont(font)
        self.progressBar_2.setStyleSheet("QProgressBar{\n"
" background-color: rgba(67, 191, 64, 86);\n"
" color: #000000;\n"
" border: 1px solid grey;\n"
" padding: 3px;\n"
" height: 15px;\n"
" text-align: center;\n"
" font-weight: bold;\n"
" }\n"
" QProgressBar::chunk{\n"
" background: rgb(0, 200, 83);\n"
" width: 5px;\n"
" margin: 0.5px\n"
" }")
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.verticalLayout_7.addWidget(self.progressBar_2)
        self.gridLayout_3.addWidget(self.groupBox, 0, 2, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
" background-color: rgb(224, 224, 224);\n"
" color: rgb(114, 159, 207);\n"
"}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    background-color: rgb(252, 175, 62, 152);\n"
"    border: 3px solid rgb(252, 175, 62, 215);\n"
"    border-radius: 9px;\n"
"    font-family: courier;\n"
"    font-weight: 700;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(252, 175, 62, 255);\n"
"}")
        self.pushButton_8.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/video.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QtCore.QSize(90, 90))
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_10.addWidget(self.pushButton_8)
        self.line_3 = QtWidgets.QFrame(self.groupBox_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_10.addWidget(self.line_3)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    background-color: rgb(173, 127, 168, 152);\n"
"    border: 3px solid rgb(173, 127, 168, 215);\n"
"    border-radius: 9px;\n"
"    font-family: courier;\n"
"    font-weight: 700;\n"
"    font-size: 15px;\n"
"    box-shadow: 0 9px #999;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(173, 127, 168, 255);\n"
"}")
        self.pushButton_9.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/docker.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon3)
        self.pushButton_9.setIconSize(QtCore.QSize(99, 99))
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_10.addWidget(self.pushButton_9)
        self.line_6 = QtWidgets.QFrame(self.groupBox_2)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_10.addWidget(self.line_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    background-color: rgb(138, 226, 52, 152);\n"
"    border: 3px solid rgb(138, 226, 52, 215);\n"
"    border-radius: 9px;\n"
"    font-family: courier;\n"
"    font-weight: 700;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(138, 226, 52, 255);\n"
"}")
        self.pushButton_7.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/photo-video.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon4)
        self.pushButton_7.setIconSize(QtCore.QSize(90, 90))
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_10.addWidget(self.pushButton_7)
        self.line_8 = QtWidgets.QFrame(self.groupBox_2)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_10.addWidget(self.line_8)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"    background-color: rgba(64, 158, 191, 153);\n"
"    border: 3px solid rgba(64, 158, 191, 215);\n"
"    border-radius: 9px;\n"
"    font-family: courier;\n"
"    font-weight: 700;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(64, 158, 191, 255);\n"
"}")
        self.pushButton_10.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/toolbox.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon5)
        self.pushButton_10.setIconSize(QtCore.QSize(90, 90))
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_10.addWidget(self.pushButton_10)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox1 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox1.setFont(font)
        self.groupBox1.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(224, 224, 224);\n"
"    color: rgb(114, 159, 207);\n"
"}")
        self.groupBox1.setObjectName("groupBox1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox1)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox1)
        self.pushButton.clicked.connect(self.setSrcOrgDir)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(52, 101, 164);\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}")
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line_2 = QtWidgets.QFrame(self.groupBox1)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(False)
        font.setWeight(50)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox1)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox1)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(32, 74, 135);\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.organize)
        self.gridLayout_2.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox1)
        self.pushButton_2.clicked.connect(self.setDestOrgDir)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(52, 101, 164);\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.textEdit_1 = QtWidgets.QTextEdit(self.groupBox1)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(False)
        font.setWeight(50)
        self.textEdit_1.setFont(font)
        self.textEdit_1.setObjectName("textEdit_1")
        self.textEdit_1.setReadOnly(True)
        self.verticalLayout.addWidget(self.textEdit_1)
        self.line_4 = QtWidgets.QFrame(self.groupBox1)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setBold(False)
        font.setWeight(50)
        self.line_4.setFont(font)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox1)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar{\n"
" background-color: rgba(64, 155, 191, 118);\n"
" color: #000000;\n"
" font-weight: bold;\n"
" border: 1px solid grey;\n"
" padding: 3px;\n"
" height: 15px;\n"
" text-align: center;\n"
" }\n"
" QProgressBar::chunk{\n"
" background: rgb(52, 101, 164);\n"
" width: 5px;\n"
" margin: 0.5px\n"
" }")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_9.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.gridLayout_3.addWidget(self.groupBox1, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuTwo = QtWidgets.QMenu(self.menubar)
        self.menuTwo.setObjectName("menuTwo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionone = QtWidgets.QAction(MainWindow)
        self.actionone.setObjectName("actionone")
        self.actionadsad = QtWidgets.QAction(MainWindow)
        self.actionadsad.setObjectName("actionadsad")
        self.menuMenu.addAction(self.actionone)
        self.menuTwo.addAction(self.actionadsad)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuTwo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Rename"))
        self.pushButton_13.setText(_translate("MainWindow", "..."))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "path to a folder that you want to rename"))
        self.pushButton_14.setText(_translate("MainWindow", "add"))
        self.lineEdit_10.setPlaceholderText(_translate("MainWindow", "new name"))
        self.pushButton_19.setText(_translate("MainWindow", "rename"))
        self.progressBar_2.setFormat(_translate("MainWindow", "progress: %p%"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Utilities"))
        self.groupBox1.setTitle(_translate("MainWindow", "Organize"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "path to a folder you want organized."))
        self.pushButton.setText(_translate("MainWindow", "src"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "path to where it should be organized to"))
        self.pushButton_3.setText(_translate("MainWindow", "Organize"))
        self.pushButton_2.setText(_translate("MainWindow", "dest"))
        self.progressBar.setFormat(_translate("MainWindow", "progress: %p%"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuTwo.setTitle(_translate("MainWindow", "Two"))
        self.actionone.setText(_translate("MainWindow", "one"))
        self.actionadsad.setText(_translate("MainWindow", "adsad"))
        
    def setSrcOrgDir(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        self.srcOrgDir = file_dialog.getExistingDirectory(self, "Open Directory", "", QtWidgets.QFileDialog.ShowDirsOnly)
        self.lineEdit.setText(self.srcOrgDir)
        self.lineEdit_2.setText(self.srcOrgDir)
        
        self.srcOrgDirFiles = [os.path.join(self.srcOrgDir,i) for i in os.listdir(self.srcOrgDir)]
        
        if self.srcOrgDir:
            noOfFiles = len([name for name in os.listdir(self.srcOrgDir) if os.path.isfile(os.path.join(self.srcOrgDir, name))])
            self.progressBar.setRange(0, noOfFiles)
            
        self.checkDuplicates(self.srcOrgDir)

    def setDestOrgDir(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        self.destOrgDir = file_dialog.getExistingDirectory(self, "Open Directory", "", QtWidgets.QFileDialog.ShowDirsOnly)
        self.lineEdit_2.setText(self.destOrgDir)
        
        self.destOrgDirFiles = [os.path.join(self.destOrgDir, i) for i in os.listdir(self.destOrgDir)]
        
        self.checkDuplicates(self.destOrgDir)
        
    def checkDuplicates(self, destOrgDir=""):
        self.deepCopyFile = deepcopy(self.srcOrgDirFiles)
        self.destOrgDirExist = destOrgDir
        
        typesOfFiles = list(
            set([os.path.splitext(i)[1] for i in self.deepCopyFile])
            )
        
        folders = [
                [
                folder for ext in typesOfFiles if ext in exts
                ] for folder, exts in general_extensions.items()
            ]
        folders = [folder for folder in folders if folder]
        folders = [folder[0] for folder in folders]
        
        self.duplicates = []

        for file in self.deepCopyFile:
            for folder in folders:
                if os.path.splitext(file)[1] in general_extensions[folder]:
                    # tuple of the file and where to move it
                    if os.path.exists(os.path.join(self.destOrgDirExist, file)):
                        self.duplicates.append((file, os.path.join(self.destOrgDirExist, folder)))
        
    def organize(self):
        self.checkDuplicates(self.srcOrgDir)
        self.textEdit_1.clear()
        if self.lineEdit.text() != "" and self.lineEdit_2.text() != "":
            self.organizer = Organizer(self.lineEdit.text(), self.lineEdit_2.text())
            self.organizer.updateValueSignal.connect(self.updateOrgProgressBar)
            self.organizer.updateTextEditSignal.connect(self.updateOrgTextEdit)
            self.organizer.start()
        else:
            pass
        self.destOrgDir = ""
        self.srcOrgDir = ""
    
    def updateOrgProgressBar(self, value):
        self.progressBar.setValue(value)

    def updateOrgTextEdit(self, fileExists, old_text, new_text):
        if old_text == "..done..":
            self.textEdit_1.append("{}.".format(new_text))
                # pass
                # find_text, ok = QtWidgets.QInputDialog.getText(self, "File Already Exists", "Find:")
                # app = QtWidgets.QApplication(sys.argv)
                # self.dialog = Ui_Dialog()
                # self.dialog.show()
                # app.exec_()
        #     self.wins = [CreateNewUser("File already exists", i) for i in self.duplicates]
        #     if self.wins:
        #         for i in self.wins:
        #             i.show()
            if self.duplicates:
                self.baseNames = [os.path.basename(i[0]) for i in self.duplicates]
                self.wind = fileExist()
                self.wind.listWidget.addItems(self.baseNames)
                self.wind.listWidget.itemPressed.connect(self.itemIsPressed)
                self.wind.pushButton.clicked.connect(self.renameOriginal)
                self.wind.pushButton_6.clicked.connect(self.renameNew)
                self.wind.pushButton_4.clicked.connect(self.skipAllButt)
                self.wind.pushButton_2.clicked.connect(self.skipButt)
                self.wind.pushButton_3.clicked.connect(self.replaceButt)
                self.wind.pushButton_5.clicked.connect(self.replaceAllButt)
                self.wind.show()
                    
        elif old_text != "..done..":
            if not fileExists:
                if len(old_text) > 26:
                        old_text = old_text[:27] + '...'
                if  len(new_text) > 26:
                        new_text = new_text[:27]+'...'
                self.textEdit_1.append("⚶ {}   ⇛   {}.".format(old_text, new_text))
                
    def itemIsPressed(self, item):
        self.currentlySelected = item
        self.wind.lineEdit.setText(os.path.basename(item.text()))
        self.wind.lineEdit_2.setText(os.path.basename(item.text()))
        
    def updateList(self, file):
        self.duplicates = [i for i in self.duplicates if file not in i[0]]
        self.baseNames = [os.path.basename(i[0]) for i in self.duplicates]
        
        self.wind.lineEdit.setText("")
        self.wind.lineEdit_2.setText("")
        
        self.wind.listWidget.clear()
        self.wind.listWidget.addItems(self.baseNames)
        
    def renameOriginal(self):
        files = [i for i in self.duplicates if self.wind.lineEdit_2.text() in i[0]][0]
        os.rename(
                os.path.join(files[1], os.path.basename(files[0])), 
                os.path.join(files[1], self.wind.lineEdit.text())
                )
        shutil.move(files[0], files[1])
        
        self.updateList(self.wind.lineEdit_2.text())
        
        if not self.duplicates:
            self.wind.close()
        
    def renameNew(self):
        files = [i for i in self.duplicates if self.wind.lineEdit.text() in i[0]][0]
        os.rename(
                files[0],
                os.path.join(os.path.dirname(files[0]), self.wind.lineEdit_2.text())
                )   
        shutil.move(
                os.path.join(os.path.dirname(files[0]), self.wind.lineEdit_2.text()),
                files[1]
                )
        
        self.wind.lineEdit.setText("")
        self.wind.lineEdit_2.setText("")
        
        self.updateList(self.wind.lineEdit_2.text())
        
        self.updateAll()
        if not self.duplicates:
            self.wind.close()
        

    def skipAllButt(self):
        self.wind.close()
        
    def skipButt(self):
        skipedItem = self.wind.listWidget.selectedItems()[0].text()
        self.duplicates = [i for i in self.duplicates if skipedItem not in i[0]]
        
        self.baseNames = [os.path.basename(i[0]) for i in self.duplicates]
        
        self.wind.listWidget.clear()
        self.wind.listWidget.addItems(self.baseNames)
        self.wind.lineEdit.setText("")
        self.wind.lineEdit_2.setText("")
        
    
    def replaceButt(self):
        files = [i for i in self.duplicates if self.wind.lineEdit.text() in i[0]][0]
        print(files[0], os.path.join(files[1], os.path.basename(files[0])))
        os.replace(files[0], os.path.join(files[1], os.path.basename(files[0])))
        self.updateList(os.path.basename(files[0]))
        # self.wind.lineEdit.setText("")
        # self.wind.lineEdit_2.setText("")
        # self.duplicates = [i for i in self.duplicates if os.path.basename(files[0]) not in i[0]]
        # self.baseNames = [os.path.basename(i[0]) for i in self.duplicates]
        # self.updateAll()
    
    def replaceAllButt(self):
        for file in self.duplicates:
            os.replace(file[0], os.path.join(file[1], os.path.basename(file[0])))
        self.wind.close()
        
    def setRenameDirectory(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        self.renameDirectory = file_dialog.getExistingDirectory(self, "Open Directory", "", QtWidgets.QFileDialog.ShowDirsOnly)
    
        if self.renameDirectory:
            self.lineEdit_9.setText(self.renameDirectory)
            num_of_files = len([name for name in os.listdir(self.renameDirectory)])
            self.progressBar_2.setRange(0, num_of_files)
                
            extensions = list(set([os.path.splitext(i)[1] for i in os.listdir(self.renameDirectory) if not os.path.isdir(i)]))
            self.comboBox.clear()
            self.file_exts = ['all']
            self.file_exts += extensions
            self.comboBox.addItems(self.file_exts)
            
    def updateCbValue(self, text):
        self.cbRename_value = text
        
    def renameFiles(self):
        prefix_text = self.lineEdit_10.text()
        self.textEdit.clear()
        
        if self.renameDirectory != "" and prefix_text != "":
            self.renamer = Renamer(self.renameDirectory, self.cbRename_value, prefix_text, 1)
            self.renamer.updateValueSignal.connect(self.updateProgressBar)
            self.renamer.updateTextEditSignal.connect(self.updateTextEdit)
            self.renamer.start()
        else:
            pass
    
    def addNameFiles(self):
        prefix_text = self.lineEdit_10.text()
        self.textEdit.clear()
        
        if self.renameDirectory != "" and prefix_text != "":
            self.renamer = Renamer(self.renameDirectory, self.cbRename_value, prefix_text, 0)
            self.renamer.updateValueSignal.connect(self.updateProgressBar)
            self.renamer.updateTextEditSignal.connect(self.updateTextEdit)
            self.renamer.start()
        else:
            pass
    
    def updateProgressBar(self, value):
        self.progressBar_2.setValue(value)
        
    def updateTextEdit(self, old_text, new_text):
        if old_text == "..done..":
            self.textEdit.append("{}.".format(new_text))
        else:
            self.textEdit.append("⚶ {}   ⇛   {}.".format(old_text, new_text))


class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        # self.src, self.dest = src, dest
        # self.setupUi(self)
        
    def run(self):
        pass
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(498, 177)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "OrginalFile"))
        self.pushButton.setText(_translate("Dialog", "Rename"))
        self.label_2.setText(_translate("Dialog", "NewFile    "))
        self.pushButton_2.setText(_translate("Dialog", "Rename"))
        self.pushButton_3.setText(_translate("Dialog", "Skip"))
        self.pushButton_5.setText(_translate("Dialog", "Replace"))
        self.pushButton_4.setText(_translate("Dialog", "SkipAll"))
        self.pushButton_6.setText(_translate("Dialog", "ReplaceAll"))
        # self.lineEdit.setText(self.src)
        # self.lineEdit_2.setText(self.dest)
        # self.show()

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setupUi(self)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
